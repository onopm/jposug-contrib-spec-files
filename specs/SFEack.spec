#
# spec file for package: SFEperl-app-ack
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 2.22
%define tarball_name    App-Ack

Name:		SFEack
IPS_package_name: text/ack
Version:	2.22
IPS_component_version: 2.22
Summary:	grep-like text finder
License:	Artistic
Url:		http://search.cpan.org/~petdance/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/ack-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/file-next-512
Requires:	runtime/perl-512
Requires:	library/perl-5/file-next-512

%description
grep-like text finder

%prep
%setup -q -n ack-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test


%install
make install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}/man

find $RPM_BUILD_ROOT/usr/perl5 -type f -name perllocal.pod -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
%{_bindir}/ack
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Thu May 10 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.22
* Sun Nov 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires because 'make test' requires library/perl-5/file-next-512.
* Mon Nov 24 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not include perllocal.pod
* Sun Nov 23 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.14
* Mon Sep 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
