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

Name:		SFEperl-dbd-pg90
IPS_package_name: library/perl-5/dbd-pg90
Version:	2.19.3
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
BuildRequires:	database/postgres-90/library
BuildRequires:	database/postgres-90/developer

Requires:	%{pnm_requires_SUNWpmdbi}
Requires:	database/postgres-90/library

Meta(info.maintainer):          taki@justplayer.com
Meta(info.upstream):            Greg Sabino Mullane <greg@turnstep.com>
Meta(info.upstream_url):        http://search.cpan.org/~turnstep/DBD-Pg-%{version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Postgres Driver for DBI

# %package 584
# IPS_package_name: library/perl-5/dbd-pg90-584
# Summary: Postgres Driver for DBI for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/version-584
# BuildRequires:	library/perl-5/test-simple-584
# BuildRequires:	library/perl-5/json-pp-584 # not builded yet
# BuildRequires:	%{pnm_buildrequires_SUNWpmdbi}
# BuildRequires:	SFEpostgres-90-libs
# BuildRequires:	SFEpostgres-90-devel
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/dbd-pg90-512
Summary: Postgres Driver for DBI for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/version-512
BuildRequires:	library/perl-5/test-simple-512
BuildRequires:	library/perl-5/json-pp-512
BuildRequires:	%{pnm_buildrequires_SUNWpmdbi}
BuildRequires:	database/postgres-90/library
BuildRequires:	database/postgres-90/developer
Requires:	runtime/perl-512


%prep
%setup -q -n DBD-Pg-%{version}

%build
POSTGRES_LIB="/usr/postgres/9.0/lib/"; export POSTGRES_LIB

# export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
# /usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
#   DESTDIR=$RPM_BUILD_ROOT \
#   LIB=/usr/perl5/vendor_perl/5.8.4
# make
# # make test

# rm -rf $RPM_BUILD_ROOT
# make pure_install DESTDIR=$RPM_BUILD_ROOT

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL  PREFIX=%{_prefix} \
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
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}

# %files 584
# %defattr (-, root, bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Thu Nov 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.19.3
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Sun Jan 06 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modifyl %files section because dbd-pg90 and dbd-pg90-512 included same file and conflicted
* Fri Jun 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.19.2
- generate packages for perl-512
