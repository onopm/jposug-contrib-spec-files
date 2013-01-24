#
# spec file for package: SFEperl-cpan-meta
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 2.120921
%define tarball_name    CPAN-Meta

Name:		SFEperl-cpan-meta
IPS_package_name: library/perl-5/cpan-meta
Version:	2.120921
IPS_component_version: 2.120921
Summary:	the distribution metadata for a CPAN dist 
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~dagolden/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            David Golden <dagolden@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~dagolden/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
the distribution metadata for a CPAN dist 

%package 584
IPS_package_name: library/perl-5/cpan-meta-584
Summary: the distribution metadata for a CPAN dist for perl-584
BuildRequires:	runtime/perl-584
BuildRequires:	library/perl-5/cpan-meta-requirements-584
BuildRequires:	library/perl-5/parse-cpan-meta-584
BuildRequires:	library/perl-5/library/perl-5/extutils-makemaker-584
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/cpan-meta-512
Summary: the distribution metadata for a CPAN dist for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/cpan-meta-requirements-512
BuildRequires:	library/perl-5/library/perl-5/extutils-makemaker-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
# make test

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
#%attr(0755,root,bin) %dir %{_bindir}
#%{_bindir}/*

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Thu Jan 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-584 and perl-512
