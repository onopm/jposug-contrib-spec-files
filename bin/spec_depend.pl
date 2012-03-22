#!/usr/bin/perl


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
chomp foreach @spec_file_lines;
#p \@spec_file_lines;

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

    if(%requires){
	if(defined($requires{'buildrequires'})){
	    my $build_requires='';
	    foreach my $depend (@{$requires{'buildrequires'}}){
#		print "[${depend}.spec]\n";
		if(grep(($_ eq $depend.'.spec'),@spec_file_lines)) {
		    $build_requires.=$depend.'.info ' ;
		} else {
		    print "PRE_INSTALL+=$depend\n";
		}
	    }
	    my $sfe_name = $spec_file;
	    $sfe_name=~ s/\.spec$/.info/g;
	    print "${sfe_name} : ${build_requires}\n" if(${build_requires});
	} elsif(defined($requires{'patch'})){
	    my $sources='patches/'.join ' patches/',@{$requires{'patch'}};
	    my $sfe_name = $spec_file;
	    $depend_sources.=' '.${sources} if(${sources});
	} elsif(defined($requires{'source'})){
	    my $sources='';
	    foreach (@{$requires{'source'}}){
		if(! /^(http|https|ftp):\/\//){
		    $sources.='ext-sources/'.$_.' ';
		}
	    }
	    $depend_sources.=' '.${sources} if(${sources});
	}
    }
    my $sfe_name = $spec_file;
    $sfe_name=~ s/\.spec$/.proto/g;
    print "${sfe_name} : ${spec_file} ${depend_sources}\n";
}

exit;

sub search_depend_files {
    my ($file_name,$requires,$definelist) = @_;
#    my %requires = $r;
#    my %definelist = $d;
    return if ! -r $file_name;

#    my %requires;
#    my %definelist;

    open my $fh, "<", $file_name;
    if(!$fh){
        warn "SKIP: spec-file open error [$file_name]: $!";
        return;
    }

#   print "--- ${file_name}  ----\n";

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
	} elsif( $line =~ /\%define\s+(.+?)\s+(.+)/i ||
		 $line =~ /^([A-Za-z_][A-Za-z0-9_]+):\s*(.+)/i
	    ){
	    my $key=lc($1);
	    my $val=$2;
#	    print "define KEY:VAL=$key:$val\n";
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

__END__

=head1 NAME

spec_build.pl - search depend local-spec-files.

=head1 SYNOPSIS

    % spec_build.pl [build.list]

=head1 AUTHOR

Takafumi Ono

=cut

