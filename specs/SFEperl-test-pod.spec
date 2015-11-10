#
# spec file for package: SFEperl-test-pod
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 1.48
%define tarball_name    Test-Pod

Name:		SFEperl-test-pod
IPS_package_name: library/perl-5/test-pod
Version:	%{tarball_version}
IPS_component_version: %{tarball_version}
Summary:	Tests POD files for correctness
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~dwheeler/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/Test-Pod-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            David E. Wheeler <david@justatheory.com>
Meta(info.upstream_url):        http://search.cpan.org/~dwheeler/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Tests POD files for correctness

%package 584
IPS_package_name: library/perl-5/test-pod-584
Summary: Tests POD files for correctness for perl-584
BuildRequires:	runtime/perl-584
BuildRequires:	library/perl-5/pod-simple-584
BuildRequires:	library/perl-5/test-simple-584
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/test-pod-512
Summary: Tests POD files for correctness for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/pod-simple-512
BuildRequires:	library/perl-5/test-simple-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
make test

rm -rf $RPM_BUILD_ROOT
make pure_install

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test

%install
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(0755,root,bin) %dir %{_bindir}
#%{_bindir}/*

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Tue Dec 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.48
* Mon Nov 18 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
