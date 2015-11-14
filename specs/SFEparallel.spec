%include Solaris.inc
%include packagenamemacros.inc

%define         date 20130922

Summary:        executing jobs in parallel using one or more computers.
Name:           parallel
IPS_package_name:        text/gnu-parallel
Version:        0.%{date}
License:        GPLv3+
URL:            http://www.gnu.org/software/parallel/
Source0:        http://ftp.gnu.org/gnu/parallel/parallel-%{date}.tar.bz2

BuildRequires:  runtime/perl-512

%description
GNU parallel is a shell tool for executing jobs in parallel using one or more computers.
A job is can be a single command or a small script that has to be run for each of 
the lines in the input. The typical input is a list of files, a list of hosts, 
a list of users, a list of URLs, or a list of tables. A job can also be a command that 
reads from a pipe. GNU parallel can then split the input and pipe it into commands in parallel. 

%prep
%setup -q -n parallel-%{date}

%configure

%build
PATH=$PATH:/usr/perl5/5.12/bin
export PATH
make 

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, bin, 0755)
# %doc COPYING NEWS README
%dir %attr (0755, root, sys) /usr
%{_bindir}/*
%{_mandir}/*/*
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, other) /usr/share/doc
/usr/share/doc/parallel/*

%changelog
* Fri Sep 27 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 20130922
* Fri Jun 01 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial
