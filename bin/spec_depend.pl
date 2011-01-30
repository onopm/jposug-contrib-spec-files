#!/usr/bin/perl

exit unless $ARGV[0];

foreach my $spec (@ARGV){
  print stderr "search dependency ... $spec\n";
  my $info=$spec;
  $info=~s/\.spec$/\.info/;
  my $depend_rule='';
  open(IN,"$spec");
  while(<IN>){
    if(/(Build)?Requires:\s*(SUNW.*|.*?-root|(.+))/){
      my $name=$3;
      if ($name){
	unless ($name=~/\%/){
	  $depend_rule.=$name.".info ";
	}
      }
    }
  }
  if($depend_rule){
    print "$info : $depend_rule\n";
  }
  close(IN);
}
