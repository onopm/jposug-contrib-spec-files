#
# spec file for package: SFEperl-db_file
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 1.829
%define tarball_name    DB_File

Name:		SFEperl-db-file
IPS_package_name: library/perl-5/db-file
Version:	%{tarball_version}
IPS_component_version: %{tarball_version}
Summary:	Tie to DB files
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~pmqs/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: SFEperl-db_file.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/DB_File-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Paul Marquess <pmqs@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~pmqs/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Tie to DB files

%package 584
IPS_package_name: library/perl-5/db-file-584
Summary: Tie to DB files for perl-584
BuildRequires:	runtime/perl-584
BuildRequires:	database/berkeleydb-5
Requires:	runtime/perl-584
Requires:	database/berkeleydb-5

%package 512
IPS_package_name: library/perl-5/db-file-512
Summary: Tie to DB files for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	database/berkeleydb-5
Requires:	runtime/perl-512
Requires:	database/berkeleydb-5

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
make test

rm -rf $RPM_BUILD_ROOT
make pure_install
make realclean

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test

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
* Mon Dec 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequries and Requires
- use %{tarball_version} at Version and IPS_component_version
* Thu Jul 11 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.829
* Thu Sep 27 JST 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
