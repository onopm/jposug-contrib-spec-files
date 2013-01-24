#
# spec file for package: SFEperl-yaml
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.81
%define tarball_name    YAML

Name:		SFEperl-yaml
IPS_package_name: library/perl-5/yaml
Version:	0.81
IPS_component_version: 0.81
Summary:	YAML Ain't Markup Language (tm)
License:	Artistic
Url:		http://search.cpan.org/~ingy/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

%description
YAML Ain't Markup Language (tm)

%package 584
IPS_package_name: library/perl-5/yaml-584
Summary: YAML Ain't Markup Language (tm) for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584
Requires:	%{name}

%package 512
IPS_package_name: library/perl-5/yaml-512
Summary: YAML Ain't Markup Language (tm) for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512
Requires:	%{name}


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
* Tue Jan 20 2013 - TAKI,Yasushi <taki@justplayer.com>
* Sun Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.81
- generate packages for perl-584 and perl-512
* Wed Oct 17 2007 - laca@sun.com
- bump to 0.66
* Sun Jan 28 2007 - mike kiedrowski (lakeside-AT-cybrzn-DOT-com)
- Updated how version is defined.
* Tue Jul  4 2006 - laca@sun.com
- rename to SFEperl-yaml
- delete -devel-share subpkg
* Thu May 11 2006 - damien.carbery@sun.com
- Change owner of 'auto' dir to root:bin to match SUNWperl-xml-parser.
* Mon Jan 02 2006 - glynn.foster@sun.com
- Initial spec file
