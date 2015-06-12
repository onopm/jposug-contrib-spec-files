#
# spec file for package: SFEperl-compress-raw-zlib
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 2.068
%define tarball_name    Compress-Raw-Zlib

Name:		SFEperl-compress-raw-zlib
IPS_package_name: library/perl-5/compress-raw-zlib
Version:	%{tarball_version}
IPS_component_version: 2.68
Summary:	Compress-Raw-Zlib
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~pmqs/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/Compress-Raw-Zlib-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.upstream):            Paul Marquess <pmqs@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~pmqs/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Compress-Raw-Zlib

%package 584
IPS_package_name: library/perl-5/compress-raw-zlib-584
Summary:  Compress-Raw-Zlib for perl-584
BuildRequires:  runtime/perl-584
Requires:       runtime/perl-584

%package 512
IPS_package_name: library/perl-5/compress-raw-zlib-512
Summary:  Compress-Raw-Zlib for perl-512
BuildRequires:  runtime/perl-512
Requires:       runtime/perl-512

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
make
make test
rm -rf $RPM_BUILD_ROOT
make pure_install

/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.12
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
#%attr(755,root,sys) %dir %{_bindir}
#%{_bindir}/*

%files 584
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.12



%changelog
* Mon May 25 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.068
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Tue Jun 05 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
