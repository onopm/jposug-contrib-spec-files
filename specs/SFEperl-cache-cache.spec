#
# spec file for package: SFEperl-cache-cache
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 1.06
%define tarball_name    Cache-Cache

Name:		SFEperl-cache-cache
IPS_package_name: library/perl-5/cache-cache
Version:	1.06
IPS_component_version: 1.6
Summary:	Generic cache interface and implementations
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~jswartz/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/J/JS/JSWARTZ/Cache-Cache-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Jonathan Swartz <swartz@pobox.com>
Meta(info.upstream_url):        http://search.cpan.org/~jswartz/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Generic cache interface and implementations

# %package 584
# IPS_package_name: library/perl-5/cache-cache-584
# Summary: Generic cache interface and implementations for perl-584
# BuildRequires:	runtime/perl-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/cache-cache-512
Summary: Generic cache interface and implementations for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512
Requires:	library/perl-5/ipc-sharelite-512

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
# export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
# /usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
#   DESTDIR=$RPM_BUILD_ROOT \
#   LIB=/usr/perl5/vendor_perl/5.8.4
# make
# make test

# rm -rf $RPM_BUILD_ROOT
# make pure_install
# make clean

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

# %files 584
# %defattr (-, root, bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Sun Sep 09 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Mon May 13 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
