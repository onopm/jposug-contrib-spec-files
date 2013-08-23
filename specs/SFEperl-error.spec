#
# spec file for package: SFEperl-error
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.17020
%define tarball_name    Error

Name:		SFEperl-error
IPS_package_name: library/perl-5/error
Version:	0.17016
IPS_component_version: 0.17016
Summary:	Error/exception handling in an 00-ish way
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/dist/Error/
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/%{tarball_name}-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Tim Bunce <Tim.Bunce@pobox.com>
Meta(info.upstream_url):        http://search.cpan.org/~timb/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
The Error package provides two interfaces. Firstly Error provides
a procedural interface to exception handling. Secondly Error is a
base class for errors/exceptions that can either be thrown, for
subsequent catch, or can simply be recorded.
Errors in the class Error should not be thrown directly, but the
user should throw errors from a sub-class of Error


%package 584
IPS_package_name: library/perl-5/error-584
Summary: Error/exception handling in an 00-ish way for perl-584
BuildRequires:	library/perl-5/module-build-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/error-512
Summary: Error/exception handling in an 00-ish way for perl-512
BuildRequires:	 library/perl-5/module-build-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/site_perl/5.8.4
make
# make test

rm -rf $RPM_BUILD_ROOT
make pure_install

# mkdir -p $RPM_BUILD_ROOT/usr/perl5/5.8.4
# mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/5.8.4

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/site_perl/5.12
make
# make test

%install
# rm -rf $RPM_BUILD_ROOT
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

# mkdir -p $RPM_BUILD_ROOT/usr/perl5/5.12
# mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/5.12

rm -rf $RPM_BUILD_ROOT/usr/bin

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
%{_prefix}/perl5/site_perl/5.8.4
# /usr/perl5/5.8.4/*

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/site_perl/5.12
# /usr/perl5/5.12/*

%changelog
* Fri Aug 23 2013 - Osamu Tabata <cantimerny.g@gmail.com>
- initial commit
