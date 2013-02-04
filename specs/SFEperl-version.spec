#
# spec file for package SFEperl-version
#
# includes module(s): version
#

%include Solaris.inc
%include packagenamemacros.inc

%define version_version 0.9901

Name:                    SFEperl-version
IPS_package_name:        library/perl-5/version
Summary:                 version-%{version_version} PERL module
Version:                 %{version_version}
Source:                  http://www.cpan.org/modules/by-module/version/version-%{version_version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:  runtime/perl-584
BuildRequires:  runtime/perl-512

%package version-584
IPS_package_name: library/perl-5/version-584
Summary: version-%{version_version} PERL module for perl-584
Requires: perl-584
Requires: library/perl-5/version

%package version-512
IPS_package_name: library/perl-5/version-512
Summary: version-%{version_version} PERL module for perl-512
Requires: perl-512
Requires: library/perl-5/version


%ifarch sparc
%define perl_dir sun4-solaris-64int
%else
%define perl_dir i86pc-solaris-64int 
%endif
%include default-depend.inc

%prep
%setup -q            -c -n %name-%version

%build
cd version-%{version_version}
/usr/perl5/5.12/bin/perl Makefile.PL \
    PREFIX=%{_prefix}\
    DESTDIR=$RPM_BUILD_ROOT \
    LIB=/usr/perl5/vendor_perl/5.12

make CC=$CC CCCDLFLAGS="%picflags" OPTIMIZE="%optflags" LD=$CC

rm -rf $RPM_BUILD_ROOT
make install
make clean

/usr/perl5/5.8.4/bin/perl Makefile.PL \
    PREFIX=%{_prefix}\
    DESTDIR=$RPM_BUILD_ROOT \
    LIB=/usr/perl5/vendor_perl/5.8.4

make CC=$CC CCCDLFLAGS="%picflags" OPTIMIZE="%optflags" LD=$CC

%install
cd version-%{version_version}
make install

# Workaround , not work INSTALLSITEMAN3DIR.
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3/
# mv $RPM_BUILD_ROOT/usr/man/man3/version.3 $RPM_BUILD_ROOT%{_mandir}/man3/
mv $RPM_BUILD_ROOT/usr/man/man3/* $RPM_BUILD_ROOT%{_mandir}/man3/
rmdir $RPM_BUILD_ROOT/usr/man/man3
rmdir $RPM_BUILD_ROOT/usr/man

rm -rf $RPM_BUILD_ROOT%{_prefix}/lib

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%defattr(-,root,bin)
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}

%files version-584
%defattr (-, root, bin)
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files version-512
%defattr (-, root, bin)
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.12


%changelog
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Mon Jun 04 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9901
* Mon Jun 04 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
* Sun Apr 29 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.99
* Thr Apr 30 2009 - Thomas Wagner
- bump to 0.76
* Wed Jun 18 2008 - daymobrew@users.sourceforge.net
- Bump to 0.7501.
* Tue Nov 13 2007 - trisk@acm.jhu.edu
- Initial spec
