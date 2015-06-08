#
# spec file for package: SFEperl-net-server
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include osdistro.inc

%define tarball_version 2.008
%define tarball_name    Net-Server
%if %( expr %{osbuild} '=' 175 )
# Solaris
%define with_584 1
%define with_510 0
%define with_512 1
%else
# OI
%define with_584 0
%define with_510 1
%define with_512 0
%endif
Name:		SFEperl-net-server
IPS_package_name: library/perl-5/net-server
Version:	2.0.0.8
IPS_component_version: 2.0.0.8
Summary:	Extensible (class) oriented internet server
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~rhandom/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/R/RH/RHANDOM/Net-Server-%{tarball_version}.tar.gz

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Paul Seamons <perl@seamons.com>
Meta(info.upstream_url):        http://search.cpan.org/~rhandom/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Extensible (class) oriented internet server

%if %{with_584} 
%package 584
IPS_package_name: library/perl-5/net-server-584
Summary: Extensible (class) oriented internet server for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584
Requires:	library/perl-5/net-server
%endif

%if %{with_510} 
%package 510 
IPS_package_name: library/perl-5/net-server-510
Summary: Extensible (class) oriented internet server for perl-510
BuildRequires:	runtime/perl-510
Requires:	runtime/perl-510
Requires:	library/perl-5/net-server
%endif

%if %{with_512} 
%package 512
IPS_package_name: library/perl-5/net-server-512
Summary: Extensible (class) oriented internet server for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512
Requires:	library/perl-5/net-server
%endif

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
rm -rf $RPM_BUILD_ROOT
%if %{with_584}
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
make test

make pure_install
make clean
%endif

%if %{with_510}
export PERL5LIB=/usr/perl5/vendor_perl/5.10.0
/usr/perl5/5.10.0/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.10.0
make
make test

make pure_install
make clean
%endif

%if %{with_512}
export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test

make pure_install
make clean
%endif

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
%{_bindir}

%if %{with_584}
%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4
%endif

%if %{with_510}
%files 510
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.10.0
%endif

%if %{with_512}
%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
%endif

%changelog
* Sun Dec 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add '%include osdistro.inc' because %{osbuild} is defined in osdistro.inc
* Jul 21 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Bump up 2.008. Supported oi_151a9
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add %attr
* Sun Jan 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
