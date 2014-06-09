#
# spec file for package: SFEperl-storable
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 2.45
%define tarball_name    Storable

Name:		SFEperl-storable
IPS_package_name: library/perl-5/storable
Version:	%{tarball_version}
IPS_component_version: %{tarball_version}
Summary:	Persistent data structure mechanism
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~ams/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
# Source0:	http://search.cpan.org/CPAN/authors/id/A/AM/AMS/Storable-%{tarball_version}.tar.gz
Source0:	http://cpan.metacpan.org/authors/id/A/AM/AMS/Storable-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Abhijit Menon-Sen <ams@toroid.org>
Meta(info.upstream_url):        http://search.cpan.org/~ams/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Persistent data structure mechanism

%package 584
IPS_package_name: library/perl-5/storable-584
Summary: Persistent data structure mechanism for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584
Requires:	library/perl-5/xsloader-584

%package 512
IPS_package_name: library/perl-5/storable-512
Summary: Persistent data structure mechanism for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512
Requires:	library/perl-5/xsloader-512


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
make clean

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
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- change Source0 URL
* Mon Jun 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.45
* Tue Jun 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
