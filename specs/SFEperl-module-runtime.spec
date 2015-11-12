#
# spec file for package: SFEperl-module-runtime
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.013
%define tarball_name    Module-Runtime

Name:		SFEperl-module-runtime
IPS_package_name: library/perl-5/module-runtime
Version:	0.013
IPS_component_version: 0.13
Summary:	Module::Runtime
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~zefram/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/Z/ZE/ZEFRAM/Module-Runtime-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/module-build

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Andrew Main (Zefram
Meta(info.upstream_url):        http://search.cpan.org/~zefram/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Module::Runtime

# %package 584
# IPS_package_name: library/perl-5/module-runtime-584
# Summary: Module::Runtime for perl-584
# BuildRequires:	runtime/perl-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/module-runtime-512
Summary: Module::Runtime for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
# PERL5LIB=/usr/perl5/vendor_perl/5.8.4 \
# /usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
#   DESTDIR=$RPM_BUILD_ROOT \
#   LIB=/usr/perl5/vendor_perl/5.8.4
# make
# make test

# rm -rf $RPM_BUILD_ROOT
# make pure_install

# /usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
#   DESTDIR=$RPM_BUILD_ROOT \
#   LIB=/usr/perl5/vendor_perl/5.12
# make
# make test

/usr/perl5/5.12/bin/perl Build.PL \
  --installdirs vendor \
  --destdir $RPM_BUILD_ROOT
/usr/perl5/5.12/bin/perl ./Build
/usr/perl5/5.12/bin/perl ./Build test

%install
rm -rf $RPM_BUILD_ROOT
#make pure_install
/usr/perl5/5.12/bin/perl ./Build install --destdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT/usr/perl5/5.12/man $RPM_BUILD_ROOT%{_datadir}
rm -rf $RPM_BUILD_ROOT/usr/perl5/5.12
# mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
#%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(755,root,sys) %dir %{_bindir}
#%{_bindir}/*

# %files 584
# %defattr (-, root, bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit.