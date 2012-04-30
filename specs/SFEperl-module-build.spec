#
# spec file for package: SFEperl-module-build
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.40
%define tarball_name    Module-Build

Name:		SFEperl-module-build
IPS_package_name: library/perl-5/module-build
Version:	0.40
IPS_component_version: 0.40
Summary:	Build, test, and install Perl modules
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/Module-Build-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-512
BuildRequires:  library/perl-5/module-metadata
BuildRequires:  library/perl-5/perl-ostype
BuildRequires:  library/perl-5/version
BuildRequires:  library/perl-5/parse-cpan-meta
Requires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Ken Williams <kwilliams@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Build, test, and install Perl modules
%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.12
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl
mkdir -p $RPM_BUILD_ROOT/usr/perl5/vendor_perl
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/perl5/vendor_perl


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}
# %attr(755,root,sys) %dir %{_bindir}
%{_bindir}/*

%changelog
