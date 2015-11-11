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

# specファイル名からips_package_name群を返す変換テーブル表を作る
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
open my $s2ifh, ">./spec2ipsname.list" or die("file write error");
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
    my %definelist;
    search_depend_files($spec_file,\%requires,\%definelist);

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
	if(defined($requires{'patch'})){
            my $sources='';
            foreach (@{$requires{'patch'}}){
                if(! /^(http|https|ftp):\/\//){
                    $sources.='patches/'.$_.' ';
                }
            }
	    my $sfe_name = $spec_file;
	    $depend_sources.=' '.${sources} if(${sources});
	}
	# いままでなかった問題が顕在化してくるのでコメントアウト
	#if(defined($requires{'source'})){
	#    my $sources='';
	#    foreach (@{$requires{'source'}}){
	#	if(! /^(http|https|ftp):\/\//){
	#	    $sources.='ext-sources/'.$_.' ';
	#	}
	#    }
	#    $depend_sources.=' '.${sources} if(${sources});
	#}
    }
    my $sfe_name = $spec_file;
    $sfe_name=~ s/\.spec$/.proto/g;
    print "${sfe_name} : ${spec_file} ${depend_sources} ${build_requires}\n";
}

exit;

sub search_depend_files {
    my ($file_name,$requires,$definelist) = @_;
    return if ! -r $file_name;

    open my $fh, "<", $file_name;
    if(!$fh){
        warn "SKIP: spec-file open error [$file_name]: $!";
        return;
    }

#   print STDERR "--- ${file_name}  ----\n";

    while(my $line = <$fh>){
        $line =~ s/\r?\n//g;

        if($line =~ s/^\%include\s+(.+)//g){
	    my $file=$1;
#	    print "$file\n";
	    if ( -r $file ){
		search_depend_files($file,$requires,$definelist);
	    } elsif ( -r 'include/'.$file ){
		search_depend_files('include/'.$file,$requires,$definelist);
	    }
        } elsif( $line =~ /^(buildrequires):\s*([\/\w-]+)/i ||
	    $line =~ /^(source)[\d]*:\s*(.+)/i ||
	    $line =~ /^(patch)[\d]*:\s*(.+)/i
	    ){
	    my $key=lc($1);
	    my $val=replace_define($2,%$definelist);
#	    print "line=$line\n";
#	    print "KEY:VAL=$key:$val\n";
	    push @{$requires->{$key}}, $val;
	} elsif( $line =~ /\%package\s+(-n)?\s*(.+)/i ){
	    my $opt=$1 || '';
	    my $package=$2;
	    my $sfe_pkg;
	    if($opt){
		$sfe_pkg=replace_define($package,%$definelist);
	    } else {
		$sfe_pkg=replace_define("%{name}-".$package,%$definelist);
	    }
	    # get_build_requires で SFEhoge-devel の元 spec ファイルを拾っているにもかかわらず、
	    # SFEhoge-devel.spec ファイルを要求してしまう。なので、comment out した
	    # $sfe_pkg_list{$sfe_pkg}=1;
	    print STDERR "Add sfe_pkg_list $sfe_pkg\n";
	} elsif( $line =~ /\%define\s+(.+?)\s+(.+)/i ||
		 $line =~ /^([A-Za-z_][A-Za-z0-9_]+):\s*(.+)/i
	    ){
	    my $key=lc($1);
	    my $val=$2;
#	    print STDERR "define KEY:VAL=$key:$val\n";
	    $definelist->{$key}=$val;
	}
    }
    close $fh;
#    print Dumper $requires;
#    print "------------\n";
    return $requires;
}

sub replace_define {
    my ($line,%definelist)=@_;
#    p \%definelist;
    $definelist{'sf_download'}='http://downloads.sourceforge.net';
    $line =~ s{\%\{([A-Za-z][0-9a-zA-Z_]*)\}}{$definelist{$1} // "%{$1}"}emg; 
    return $line;
}


#
# 与えられたspecファイルから、ips_nameの羅列を返す
#
sub get_build_requires {
    my ($file_name) = @_;
    return if ! -r $file_name;

    open my $fh, "<", $file_name;
    if(!$fh){
        warn "SKIP: spec-file open error [$file_name]: $!";
        return;
    }
    my %definelist;
    my %result;

    my $spec=$file_name;
    $spec=~s/.spec$//;

    while(my $line = <$fh>){
        $line =~ s/\r?\n//g;

	if( $line =~ /^IPS_package_name:\s*([\/\w-]+)/i 
	    ){
	    my $val=replace_define($1,%definelist);
	    print STDERR "IPS PACKAGE NAME $val is in $file_name.\n";
	    $result{$val}=$spec;
	} elsif( $line =~ /\%package\s+(-n)?\s*(.+)/i ){
	    my $opt=$1 || '';
	    my $package=$2;
	    my $sfe_pkg;
	    if($opt){
		$sfe_pkg=replace_define($package,%definelist);
	    } else {
		$sfe_pkg=replace_define("%{name}-".$package,%definelist);
	    }
	    $result{$sfe_pkg}=$spec;
	    print STDERR "Extend Package NAME $sfe_pkg is in $file_name\n";
	} elsif( $line =~ /\%define\s+(.+?)\s+(.+)/i ||
		 $line =~ /^([A-Za-z_][A-Za-z0-9_]+):\s*(.+)/i
	    ){
	    my $key=lc($1);
	    my $val=$2;
#	    print STDERR "define KEY:VAL=$key:$val\n";
	    $definelist{$key}=$val;
	}
    }
    close $fh;
    return %result;
}


__END__

=head1 NAME

spec_build.pl - search depend local-spec-files.

=head1 SYNOPSIS

    % spec_build.pl [build.list]

=head1 AUTHOR

Takafumi Ono

=cut

