#
# spec file for package: SFEperl-dbd-pg90
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#

%include Solaris.inc
%include packagenamemacros.inc

Name:		SFEperl-dbd-pg91
IPS_package_name: library/perl-5/dbd-pg91
Version:	2.19.2
Summary:	Postgres Driver for DBI
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~turnstep/DBD-Pg-%{version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/T/TU/TURNSTEP/DBD-Pg-%{version}.tar.gz

BuildRequires:  %{pnm_buildrequires_perl_default}
Requires:  	%{pnm_requires_perl_default}
BuildRequires:	SFEperl-version
BuildRequires:	SFEperl-test-simple
BuildRequires:	%{pnm_buildrequires_SUNWpmdbi}
BuildRequires:	database/postgres-91/library
BuildRequires:	database/postgres-91/developer

Meta(info.maintainer):          taki@justplayer.com
Meta(info.upstream):            Greg Sabino Mullane <greg@turnstep.com>
Meta(info.upstream_url):        http://search.cpan.org/~turnstep/DBD-Pg-%{version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Postgres Driver for DBI

%package 512
IPS_package_name: library/perl-5/dbd-pg91-512
Summary: Postgres Driver for DBI
Requires: perl-512
Requires:	%{pnm_requires_SUNWpmdbi}
Requires:	database/postgres-91/library

%prep
%setup -q -n DBD-Pg-%{version}

%build
POSTGRES_LIB="/usr/postgres/9.1/lib/"; export POSTGRES_LIB
perl Makefile.PL PREFIX=%{_prefix} \
    DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/%{perl_version} 
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
# %{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(755,root,sys) %dir %{_bindir}
#%{_bindir}/*

%files 512
%defattr (-, root, bin)
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Mon Jun 04 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify IPS_package_name for package 512.

* Mon Jun 04 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit