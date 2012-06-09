#
# spec file for package: SFEperl-try-tiny
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.11
%define tarball_name    Try-Tiny

Name:		SFEperl-try-tiny
IPS_package_name: library/perl-5/try-tiny
Version:	0.11
IPS_component_version: 0.11
Summary:	Try::Tiny
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~doy/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Try-Tiny-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Jesse Luehrs <doy@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~doy/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description


%package 512
IPS_package_name: library/perl-5/try-tiny-512
Summary: Try::Tiny for perl-512
BuildRequires:	runtime/perl-512
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