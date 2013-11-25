#
# spec file for package: SFEperl-any-moose
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.18
%define tarball_name    Any-Moose

Name:		SFEperl-any-moose
IPS_package_name: library/perl-5/any-moose
Version:	0.18
IPS_component_version: 0.18
Summary:	Any::Moose
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~sartak/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/Any-Moose-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Shawn M Moore <cpan@sartak.org>
Meta(info.upstream_url):        http://search.cpan.org/~sartak/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Any::Moose

# %package 584
# IPS_package_name: library/perl-5/any-moose-584
# Summary:  Any::Moose for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/extutils-makemaker-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/any-moose-512
Summary: Any::Moose for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/extutils-makemaker-512
BuildRequires:	library/perl-5/moose-512
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
* Mon Nov 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for perl-584
* Sun Jun 17 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-584
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
