#
# spec file for package: SFEperl-io-multiplex
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 1.13
%define tarball_name    IO-Multiplex
Name:		SFEperl-io-multiplex
IPS_package_name: library/perl-5/io-multiplex
Version:	1.13
IPS_component_version: 1.13
Summary:	IO::Multiplex - Manage IO on many file handles
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~rhandom/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:        http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{tarball_name}-%{tarball_version}.tar.gz

%include default-depend.inc
%include perl-depend.inc

%description
It is object oriented in design, and will notify you of significant events by
calling methods on an object that you supply. If you are not using objects,
you can simply supply __PACKAGE__ instead of an object reference.
You may have one callback object registered for each file handle, or one global
one. Possibly both -- the per-file handle callback object will be used instead
of the global one. Each file handle may also have a timer associated with it.
A callback function is called when the timer expires.

%package 510 
IPS_package_name: library/perl-5/io-multiplex-510
Summary: IO::Multiplex - Manage IO on many file handles for perl-510
BuildRequires:	runtime/perl-510
Requires:	runtime/perl-510
Requires:	library/perl-5/io-multiplex

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
rm -rf $RPM_BUILD_ROOT

export PERL5LIB=/usr/perl5/vendor_perl/5.10.0
/usr/perl5/5.10.0/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.10.0
make
make test

make pure_install
make clean

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}

%files 510
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.10.0

%changelog
* Jul 21 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial commit
