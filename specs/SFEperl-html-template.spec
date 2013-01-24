#
# spec file for package: SFEperl-html-template
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 2.91
%define tarball_name    HTML-Template
%define perl_version 5.12

Name:		SFEperl-html-template
IPS_package_name: library/perl-5/html-template
Version:	2.91
IPS_component_version: 2.91
Summary:	a simple HTML templating system
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~samtregar/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/W/WO/WONKO/HTML-Template-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Sam Tregar <sam@tregar.com>
Meta(info.upstream_url):        http://search.cpan.org/~samtregar/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
a simple HTML templating system

%package 584
IPS_package_name: library/perl-5/html-template-584
Summary: a simple HTML templating system for perl-584
BuildRequires:	runtime/perl-584
BuildRequires:	library/perl-5/file-temp-584
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/html-template-512
Summary: a simple HTML templating system for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/file-temp-512
Requires:	runtime/perl-512

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
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Wed Jan 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files to avoid conflict
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sun Dec 23 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
- fix IPS_package_name
* Thu May  3 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- define perl_version and use %{perl_version}
* Sun Apr 29 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial
