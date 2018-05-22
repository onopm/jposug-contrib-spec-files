#!/usr/bin/perl
#
#
# SFE*.specどおしの依存関係を作成するプログラム
#

use strict;
use warnings;
use Pod::Usage;
# Debug (dumper
use Data::Dumper;
use Digest::MD5 qw/md5_hex/;
use Storable;
use File::Basename;
use constant CACHEDIR => "./cache_spec_depend";
use constant SPEC2IPSNAME => "spec2ipsname.list";

sub p { print Dumper shift }

sub spectool($$)
{
    my ($command, $spec) = @_;
    my (@retval, $res, $line, @lines, $md5, $md5_cached, @cache, $cache_ar, $fh, $spec_base, $ext);
    $spec_base = basename($spec, ('.spec'));
    @retval = ();
    $res = open $fh, "<", "$spec";
    if(!$res){
        die "ERROR: spec-file open error [$spec]: $!";
    } else {
        @lines = <$fh>;
        close $fh;
    }
    $md5 = md5_hex(@lines);
    $res = open $fh, "<", CACHEDIR."/$spec_base.$command";
    if($res) {
        $cache_ar = Storable::fd_retrieve($fh);
        close $fh;
        @cache = @$cache_ar;   
        $md5_cached = shift(@cache);
        if ($md5 eq $md5_cached) {
            print STDERR "$spec_base.$command (cached)\n";
            return @cache; 
        }
    }
    if ($command =~ /get_copyright/) {
        for $line (@lines) { 
            $line =~ s/\r?\n//g;
            if( $line =~ /^SUNW_Copyright\s*:\s*([\/\w\-%\.{}\(\)]+)/i ){
                @retval = (@retval, split("\n", `spectool --specdirs=\`pwd\`:\`pwd\`/include:\`pwd\`/base-specs --ips eval '$1' $spec`));
                #print STDERR "found: SUNW_Copyright\n";
            }
        } 
        if ($#retval < 0) {
            @retval = split("\n", `spectool --specdirs=\`pwd\`:\`pwd\`/include:\`pwd\`/base-specs --ips eval '%{name}.copyright' $spec`);
            #print STDERR "not found: SUNW_Copyright\n";
        } 
    } else {
        @retval = split("\n", `spectool --specdirs=\`pwd\`:\`pwd\`/include:\`pwd\`/base-specs --ips $command $spec`);
    }
    mkdir CACHEDIR if (! -d CACHEDIR);
    $res = open $fh, ">", CACHEDIR."/$spec_base.$command";
    if(!$res){
        die "ERROR: cache-file open error [$spec_base.$command]: $!";
    } else {
        @cache = ($md5, @retval);
        Storable::store_fd \@cache, $fh;
        close $fh;
        for $ext ('info', 'proto') {
            if (-f "$spec_base.$ext") {
	        print STDERR "/bin/rm -rf $spec_base.$ext\n";
	        `/bin/rm -rf $spec_base.$ext`;
            }
        }
    }
    @retval; 
}

sub search_depend_files($$) {
    my ($spec, $requires) = @_;
    my (@files, $key);
    return if ! -r $spec;

    for $key ('buildrequires', 'patches', 'sources', 'copyright', 'used_spec_files') {
	@files = spectool("get_$key", $spec);
	@{$requires->{$key}} = @files if ($#files >= 0);
    }
}

sub get_build_requires($)
{
    my ($spec) = @_;
    my (%result, @package_names, $package_name, $ips_package_name, @ips_package_names);

    @package_names = spectool('get_packages', $spec);
    @ips_package_names = spectool('get_package_names', $spec);
    $spec =~ s/\.spec$//;
    for $package_name (@package_names) {
        $result{$package_name} = $spec if ($package_name !~ /^$spec$/);
    }
    for $ips_package_name (@ips_package_names) {
    	$result{$ips_package_name} = $spec;
    }
    %result;
}

my $build_list = shift || 'build.list';
pod2usage("$build_list not found.") if ! -f $build_list;

open my $list_fh, "<", $build_list or pod2usage("$build_list open error. :$!");
my @spec_file_lines=<$list_fh>;
close $list_fh;
#chomp foreach @spec_file_lines;

# SFE package list の作成
# spec_file_linesからわざわざ詰め直して作る理由は、あとから追加される可能性があるため
my %sfe_pkg_list; # specファイルの一覧が入るハッシュ。存在したら1。
my %ips_spec_name; # IPS_package_nameから、specファイルを得るハッシュテーブル。
foreach (@spec_file_lines){
    s/#.*//g;
    s/^s+//g;
    s/s+$//g;
    s/\r?\n//g;
    next unless /\.spec$/;

    my $spec=$_;
    %ips_spec_name=(%ips_spec_name,get_build_requires($spec));

    $spec=~s/.spec$//;
    $sfe_pkg_list{$spec}=1;
}
# このファイルは、install_spec.shでspecファイルからipsの名前でインストールするのに使う。
open my $s2ifh, ">./".SPEC2IPSNAME or die("file write error");
for my $key (keys(%ips_spec_name)) {
    print $s2ifh "$ips_spec_name{$key}.spec:$key\n" if ($key !~ /^SFE/);
}
close $s2ifh;

foreach my $spec_file (@spec_file_lines){
    $spec_file =~ s/#.*//g;
    $spec_file =~ s/^s+//g;
    $spec_file =~ s/s+$//g;
    $spec_file =~ s/\r?\n//g;
    next if $spec_file !~ /\.spec$/;

    my %requires;
    search_depend_files($spec_file,\%requires);

    my $depend_sources='';
    my $build_requires='';
 
    if(%requires){
	if(defined($requires{'buildrequires'})){
	    # TODO: ここはjikkou 
	    foreach my $depend (@{$requires{'buildrequires'}}){
		print STDERR "depend check:$depend\n";
		if( $sfe_pkg_list{$depend} ){
		    # SFEのパッケージにあるのならば、buildの順を調整する。
		    print STDERR "add build requires:$depend.info\n";
		    $build_requires.=$depend.'.info ' ;
		} elsif( $ips_spec_name{$depend} ) {
		    print STDERR "add build requires:$ips_spec_name{$depend}.info for $depend\n";
		    $build_requires.=$ips_spec_name{$depend}.'.info ' ;
		} else {
		    # そうでないものは、IPSからインストールにする。
		    print "PRE_INSTALL+=$depend\n";
		}
	    }
	    my $sfe_name = $spec_file;
	    $sfe_name=~ s/\.spec$/.info/g;
	    print "${sfe_name} : ${build_requires}\n" if(${build_requires});
	} 
	if(defined($requires{'patches'})){
 	    my $sources='';
            foreach (@{$requires{'patches'}}){
                if(! /^(http|https|ftp):\/\//){
                    $sources.='patches/'.$_.' ';
                }
            }
	    my $sfe_name = $spec_file;
	    $depend_sources.=' '.${sources} if(${sources});
	}
        if(defined($requires{'sources'})){
	    my $sources='';
	    foreach (@{$requires{'sources'}}){
		if(! /^(http|https|ftp):\/\//){
		    $sources.='ext-sources/'.$_.' ';
		}
	    }
	    $depend_sources.=' '.${sources} if(${sources});
	}
        if(defined($requires{'copyright'})){
	    my $sources='';
	    foreach (@{$requires{'copyright'}}){
		if(! /^(http|https|ftp):\/\//){
		    $sources.='copyright/'.$_.' ';
		}
	    }
	    $depend_sources.=' '.${sources} if(${sources});
	}
        if(defined($requires{'used_spec_files'})){
	    my $sources='';
	    foreach (@{$requires{'used_spec_files'}}){
		my ($pwd) = `pwd`;
		$pwd =~ s/\r?\n//g;
		s/^${pwd}\///;
	        $sources.= $_.' ';
	    }
	    $depend_sources.=' '.${sources} if(${sources});
	}
    }
    my $sfe_name = $spec_file;
    $sfe_name=~ s/\.spec$/.proto/g;
    print "${sfe_name} : ${spec_file} ${depend_sources} ${build_requires}\n";
}

exit;

__END__

=head1 NAME

spec_depend_spectool.pl - search depend local-spec-files.

=head1 SYNOPSIS

    % spec_depend_spectool.pl [build.list]

=head1 AUTHOR

Takafumi Ono

=cut

