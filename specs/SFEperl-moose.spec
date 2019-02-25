#
# spec file for package: SFEperl-moose
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 2.0602
%define tarball_name    Moose

Name:		SFEperl-moose
IPS_package_name: library/perl-5/moose
Version:	2.0602
IPS_component_version: 2.602
Summary:	Moose
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~doy/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Moose-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/list-moreutils
BuildRequires:	library/perl-5/class-load
BuildRequires:	library/perl-5/mro-compat
BuildRequires:	library/perl-5/sub-exporter
BuildRequires:	library/perl-5/sub-name
BuildRequires:	library/perl-5/test-fatal
BuildRequires:	library/perl-5/test-requires

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Jesse Luehrs <doy@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~doy/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Moose

%package 512
IPS_package_name: library/perl-5/moose-512
Summary: Moose for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/list-moreutils-512
BuildRequires:	library/perl-5/class-load-512
BuildRequires:	library/perl-5/mro-compat-512
BuildRequires:	library/perl-5/sub-exporter-512
BuildRequires:	library/perl-5/sub-name-512
BuildRequires:	library/perl-5/test-fatal-512
BuildRequires:	library/perl-5/test-requires-512
BuildRequires:	library/perl-5/eval-closure-512
BuildRequires:	library/perl-5/devel-globaldestruction-512
Requires:	runtime/perl-512
Requires:	library/perl-5/moose

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test


%install
rm -rf $RPM_BUILD_ROOT
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

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Mon Feb 11 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
