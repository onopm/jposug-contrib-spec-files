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
sub p { print Dumper shift }


sub spectool($$)
{
    my ($command, $spec) = @_;
    split("\n", `spectool --specdirs=\`pwd\`:\`pwd\`/include --ips $command $spec`);
}

sub search_depend_files($$) {
    my ($spec, $requires) = @_;
    my (@files, $key);
    return if ! -r $spec;

    for $key ('buildrequires', 'patches', 'sources') {
	@files = spectool("get_$key", $spec);
	@{$requires->{$key}} = @files if ($#files >= 0);
    }
}

sub get_build_requires($)
{
    my ($spec) = @_;
    my (%result, @package_names, $package_name, @ips_package_names);

    @package_names = spectool('get_packages', $spec);
    @ips_package_names = spectool('get_package_names', $spec);
    $spec =~ s/\.spec$//;
    for $package_name (@package_names) {
        $result{$package_name} = $spec if ($package_name !~ /^$spec$/);
    }
    $result{shift(@ips_package_names)} = $spec;
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

