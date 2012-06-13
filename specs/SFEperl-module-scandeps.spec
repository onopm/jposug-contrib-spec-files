#
# spec file for package: SFEperl-module-scandeps
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 1.08
%define tarball_name    Module-ScanDeps

Name:		SFEperl-module-scandeps
IPS_package_name: library/perl-5/module-scandeps
Version:	1.08
IPS_component_version: 1.8
Summary:	Recursively scan Perl code for dependencies
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~autrijus/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSCHUPP/Module-ScanDeps-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Audrey Tang <cpan@audreyt.org>
Meta(info.upstream_url):        http://search.cpan.org/~autrijus/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Recursively scan Perl code for dependencies

# %package 584
# IPS_package_name: library/perl-5/module-scandeps-584
# Summary: Recursively scan Perl code for dependencies for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/module-build-584 # not builded yet
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/module-scandeps-512
Summary: Recursively scan Perl code for dependencies for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/module-build-512
Requires:	runtime/perl-512


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

export PERL5LIB=/usr/perl5/vendor_perl/5.12
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
mkdir -p $RPM_BUILD_ROOT/usr/perl5/5.12
mv $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT/usr/perl5/5.12

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
%attr(755,root,bin) %dir /usr/perl5/5.12/bin
/usr/perl5/5.12/bin/*

%changelog
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
