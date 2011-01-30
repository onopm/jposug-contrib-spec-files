#!/usr/bin/perl

use strict;

use Getopt::Std;

my %opt;
getopts('sin:' => \%opt);

my $svr4=defined($opt{s})?1:0;	# default is ips mode.
$svr4=0 if(defined($opt{i}));
my $metapkgname=defined($opt{n})?$opt{n}:'';

my %pkgdb;
open(PKGDB,"pkg list -av|") or die "cannot get pkg list -a\n";
while(<PKGDB>){
  /^pkg:\/(.+?)@(.+?):/;
  my $pkgname=$1;
  $pkgdb{$pkgname}=$2;
#  print "$pkgname=$pkgdb{$pkgname}\n";
}
close(PKGDB);

if($svr4){
    print "Requires:\t";
} else {
  print <<_END
# JUSTPLAYER PKGLABO Environment.
# http://pkglabo.justplayer.com/
set name=info.maintainer_url value=pkglabo\@justplayer.com
set name=info.upstream_url value=http://pkglabo.justplayer.com/
set name=pkg.summary value="JUSTPLAYER PKGLABO ."
set name=description value="JUSTPLAYER PKGLABO ."
set name=pkg.name value=$metapkgname
_END
}

my $comma='';
while(<>){
  chomp;
  my $pkgname=$_;
  if($pkgdb{$pkgname}){
    if($svr4){
      foreach my $pkg (&get_svr4pkgname($pkgname)){
	print $comma.$pkg;
	$comma=',';
      }
    } else {
      print "depend fmri=$pkgname\@$pkgdb{$pkgname} type=require\n";
    }
  }
}

print "\n";

sub get_svr4pkgname{
  my ($pkg)=@_;
  my @result;

  open(DEPEND,"pkg contents -rm $pkg|") or die("cannot launch pkg contents -rm $pkg");
  while(<DEPEND>){
    if(/^legacy arch=i386 .+? pkg=([^ ]+) /){
      push(@result,$1);
    }
  }
  close(DEPEND);
  return @result;
}
