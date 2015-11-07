#
# spec file for package: SFEperl-scalar-util
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define build584 1
%define build512 1

%define tarball_version 1.42
%define tarball_name    Scalar-Util

Name:		SFEperl-scalar-util
IPS_package_name: library/perl-5/scalar-util
Version:	%{tarball_version}
IPS_component_version: %{tarball_version}
Summary:	Scalar utilities (dualvar reftype etc)
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~gbarr/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/Scalar-List-Utils-%{tarball_version}.tar.gz

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Graham Barr <gbarr@pobox.com>
Meta(info.upstream_url):        http://search.cpan.org/~gbarr/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Scalar utilities (dualvar reftype etc)

%if %{build584}
%package 584
IPS_package_name: library/perl-5/scalar-util-584
Summary: Scalar utilities (dualvar reftype etc) for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/scalar-util-512
Summary: Scalar utilities (dualvar reftype etc) for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512
%endif

%prep
if [ -d $RPM_BUILD_ROOT ]
then
    rm -rf $RPM_BUILD_ROOT
fi

%setup -q -n Scalar-List-Utils-%{tarball_version}

%build

%if %{build584}
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
make test
make pure_install
%endif

%if %{build512}
export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test
make pure_install
%endif

%install
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

%if %{build584}
%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4
%endif

%if %{build512}
%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
%endif

%changelog
* Tue May 26 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.42
* Tue Nov 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.35
* Mon Sep 09 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.32
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
