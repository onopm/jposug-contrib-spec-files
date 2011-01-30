#!/usr/bin/perl

sub get_fileattr {
  my @line=split(/ /,$_[0]);
  my %result;
  foreach my $param (@line){
    my ($key,$val)=split(/=/,$param);
#    print "$key:$val\n";
    $result{$key}=$val;
  }
  return %result;
}


my $pkgname=$ARGV[0];
print stderr "get $pkgname manifest\n";
my $fh=open(IN,"pkg contents -rm $pkgname|") or die "$pkgname is not found";

while(<IN>){
  if (/^set name=(.+)$/){
    my $line=$1;
    if($line=~/^pkg\.fmri value=pkg:\/\/.+?\/(.+?)@.+?$/){
      print "%package -n $1\n";
      print "IPS_package_name: $1\n";
      print "%files -n $1\n";
    } elsif($line=~/^pkg\.summary value=(.+)/){
      print "Summary: $1\n";
    }
  } elsif (/^depend fmri=([^ @]+)@?(.+)? +type=require/) {
    print "Requires: $1\n";
  } elsif (/^depend fmri=([^ @]+)@?(.+)? +type=(.+?)/) {
    print "Warninng: $2: $1\n";
  } elsif (/^dir (.+)$/){
    my %param=get_fileattr($1);
    unless ($param{"variant.arch"}=~/sparc/){
      print "\%dir \%attr ($param{mode}, $param{owner}, $param{group}) /$param{path}\n";
    }
  } elsif (/^file (.+)$/){
    my %param=get_fileattr($1);
    unless ($param{"variant.arch"}=~/sparc/){
      print "\%attr ($param{mode}, $param{owner}, $param{group}) /$param{path}\n";
    }
  } elsif (/^link (.+)$/){
    my %param=get_fileattr($1);
    unless ($param{"variant.arch"}=~/sparc/){
      my $prefix=$param{"path"};
      $prefix=~s/\/.*?$//;
      $param{"target"};
      print '/'.$prefix.'/'.$param{path}."\n";
    }
  } elsif (/^legacy /){

  } elsif (/^license /){

  } else {
    print $_;
  }
}


close($fh);
