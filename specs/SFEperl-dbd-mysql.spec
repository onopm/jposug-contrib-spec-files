#
# spec file for package: SFEperl-dbd-mysql
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%define cc_is_gcc 1

%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 4.025
%define tarball_name    DBD-mysql

Name:		SFEperl-dbd-mysql
IPS_package_name: library/perl-5/dbd-mysql
Version:	4.025
IPS_component_version: 4.25
Summary:	MySQL driver for DBI
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~capttofu/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/C/CA/CAPTTOFU/DBD-mysql-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584 = *
BuildRequires:	runtime/perl-512 = *

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Patrick Galbraith <patg@patg.net>
Meta(info.upstream_url):        http://search.cpan.org/~capttofu/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
MySQL driver for DBI

%package 584
IPS_package_name: library/perl-5/dbd-mysql-584
Summary: MySQL driver for DBI for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584 = *

%package 512
IPS_package_name: library/perl-5/dbd-mysql-512
Summary: MySQL driver for DBI for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512 = *

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export CC=/usr/bin/gcc
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
    DESTDIR=$RPM_BUILD_ROOT \
    LIB=/usr/perl5/vendor_perl/5.8.4 \
    --mysql_config=/usr/mysql/5.1/bin/mysql_config
make
# make test

rm -rf $RPM_BUILD_ROOT
make pure_install
make clean

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
    DESTDIR=$RPM_BUILD_ROOT \
    LIB=/usr/perl5/vendor_perl/5.12 \
    --mysql_config=/usr/mysql/5.1/bin/mysql_config
    
make
# make test


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
* Sat Dec 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- specify versions of required packages
