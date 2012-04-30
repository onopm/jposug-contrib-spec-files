#
# spec file for package SFEperl-version
#
# includes module(s): version
#

%include Solaris.inc
%include packagenamemacros.inc

%define version_version 0.99

Name:                    SFEperl-version
IPS_package_name:        library/perl-5/version
Summary:                 version-%{version_version} PERL module
Version:                 %{perl_version}.%{version_version}
Source:                  http://www.cpan.org/modules/by-module/version/version-%{version_version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:  %{pnm_buildrequires_perl_default}
Requires:  	%{pnm_requires_perl_default}

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
perl Makefile.PL \
    PREFIX=%{_prefix}\
    DESTDIR=$RPM_BUILD_ROOT \
    LIB=/usr/perl5/vendor_perl/%{perl_version}

make CC=$CC CCCDLFLAGS="%picflags" OPTIMIZE="%optflags" LD=$CC

%install
rm -rf $RPM_BUILD_ROOT
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
%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}


%changelog
* Sun Apr 29 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.99
* Thr Apr 30 2009 - Thomas Wagner
- bump to 0.76
* Wed Jun 18 2008 - daymobrew@users.sourceforge.net
- Bump to 0.7501.
* Tue Nov 13 2007 - trisk@acm.jhu.edu
- Initial spec
