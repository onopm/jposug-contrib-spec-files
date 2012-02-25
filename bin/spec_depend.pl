#!/usr/bin/perl

use strict;
use warnings;
use Pod::Usage;

#exit unless $ARGV[0];
my $build_list = shift || 'build.list';
die "$build_list not found." if ! -r $build_list;

open my $list_fh, "<", $build_list or die "open error $!\n";

while(my $spec_file = <$list_fh>){
    $spec_file =~ s/#.*//g;
    $spec_file =~ s/^s+//g;
    $spec_file =~ s/s+$//g;
    $spec_file =~ s/\r?\n//g;
    next if $spec_file !~ /\.spec$/;

    my $build_requires = search_build_require($spec_file);
    next if(!$build_requires);

    (my $sfe_name = $spec_file) =~ s/\.spec$//g;

    print "${sfe_name}.info : $build_requires\n";
}
exit;

sub search_build_require {
    my $file_name = shift;
    return if ! -r $file_name;

    my @requires;

    open my $fh, "<", $file_name;
    if(!$fh){
        warn "SKIP: spec-file open error [$file_name]: $!";
        return;
    }

    while(my $line = <$fh>){
        $line =~ s/\r?\n//g;

        #if($line =~ s/^%include\s+//g){
        #    warn "(include) $line\n";
        #}

        next if $line !~ s/^BuildRequires:\s+//g;
        if(-f "${line}.spec"){
            #warn "(debug) require: $line\n";
            push @requires, $line."info";
        }
    }
    close $fh;
    return join " ",@requires;
}

__END__

=head1 NAME

amon2-setup.pl - setup script for amon2

=head1 SYNOPSIS

    % amon2-setup.pl MyApp

            --flavor=Basic   basic flavour(default)
            --flavor=Lite    Amon2::Lite flavour
            --flavor=Minimum minimalistic flavour for benchmarking

                                    --help   Show this help

=head1 AUTHOR

Takafumi Ono

=cut

