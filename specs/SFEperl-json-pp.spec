#
# spec file for package: SFEperl-json-pp
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 2.27202
%define tarball_name    JSON-PP

Name:		SFEperl-json-pp
IPS_package_name: library/perl-5/json-pp
Version:	2.27202
IPS_component_version: 2.27202
Summary:	JSON-PP
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~makamaka/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MAKAMAKA/JSON-PP-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Makamaka Hannyaharamitu <makamaka@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~makamaka/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
JSON-PP

%package 584
IPS_package_name: library/perl-5/json-pp-584
Summary: JSON-PP for perl-584
BuildRequires:	runtime/perl-584
BuildRequires:	library/perl-5/cpan-meta-yaml
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/json-pp-512
Summary: JSON-PP for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/cpan-meta-yaml
Requires:	runtime/perl-512
Requires:       library/perl-5/json-pp


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
# rm -rf $RPM_BUILD_ROOT
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
%attr(0755,root,bin) %dir %{_bindir}
%{_bindir}/*

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Mon Sep 09 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.27202
* Fri Jun 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
