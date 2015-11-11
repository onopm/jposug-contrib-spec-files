#
# spec file for package: SFEperl-class-load
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.19
%define tarball_name    Class-Load

Name:		SFEperl-class-load
IPS_package_name: library/perl-5/class-load
Version:	0.19
IPS_component_version: 0.19
Summary:	Class:Load
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~drolsky/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Class-Load-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/test-fatal
BuildRequires:	library/perl-5/test-requires
BuildRequires:	library/perl-5/module-implementation
BuildRequires:	library/perl-5/module-runtime
BuildRequires:	library/perl-5/package-stash

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Dave Rolsky <autarch@urth.org>
Meta(info.upstream_url):        http://search.cpan.org/~drolsky/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description


%package 512
IPS_package_name: library/perl-5/class-load-512
Summary: Class:Load for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/test-fatal-512
BuildRequires:	library/perl-5/test-requires-512
BuildRequires:	library/perl-5/module-implementation-512
BuildRequires:	library/perl-5/module-runtime-512
BuildRequires:	library/perl-5/package-stash-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
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
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(755,root,sys) %dir %{_bindir}
#%{_bindir}/*

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Sat 09 Jun 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit.