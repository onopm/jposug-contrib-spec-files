#!/usr/bin/perl
use strict;
use warnings;

my $VERSION=`uname -v`;
$VERSION=~s/[^0-9]//g;

exit unless $ARGV[0];

my %depend_rule;

foreach my $spec (@ARGV){
  print STDERR "search dependency ... $spec\n";
  my $info=$spec;
  open(IN,"$spec");
  while(<IN>){
    if(/(Build)?Requires:\s*(SUNW.*)/){
      my $name=$2;
      if ($name){
	$depend_rule{$name}++;
      }
    }
  }
  close(IN);
}

if(%depend_rule){
  foreach my $depend (keys %depend_rule) {
    my $result=get_ipspkgname($depend);
    print $result.' ' if ($result);
  }
}

sub get_ipspkgname{
  my ($pkg)=@_;

  open(DEPEND,"pkg search -p -s http://pkg.opensolaris.org/release $pkg|") or die("cannot launch pkg contents -rm $pkg");
  while(<DEPEND>){
    if(/^pkg:\/(.+?)\@[0-9.]+?-0.([0-9]+) \((.+)\)$/){
      my $pkgname=$1;
      my $pkgver=$2;
      my $repository=$3;
      print "$&\n$1,$2,$3\n";

      if ($repository eq 'opensolaris.org' && $pkgver eq $VERSION){
	print STDERR "Find ... $pkgname\n";
	return $pkgname;
      }
    }
  }
  close(DEPEND);
  return 0;
}
