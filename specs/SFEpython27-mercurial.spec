#
# spec file for package SFEpython27-mercurial
#
# includes module(s): SFEpython27-mercurial
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_url         http://mercurial.selenic.com/release
%define src_name        mercurial
%define pyprefix        /usr/python
%define pyver           2.7
%define hgver           2.1
%define pkg_hgver       2.1.2
%define execpython      %{pyprefix}/bin/python%{pyver}
%define execpython64    %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32          lib
%define _lib64          lib64

Name:                   SFEpython27-mercurial
IPS_package_name:       developer/versioning/SFEmercurial-%{pkg_hgver}
Summary:                The Mercurial Source Control Management System
URL:                    http://www.sqlalchemy.org
Version:                %{pkg_hgver}
Source:                 %{src_url}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
License:                GPLv2
SUNW_Copyright:	        SFEpython27-mercurial.copyright
Requires:               SFEpython27

%prep
%setup -c -n %{src_name}-%{version}

%ifarch amd64 sparcv9
rm -rf %{src_name}-%{version}-64
cp -rp %{src_name}-%{version} %{src_name}-%{version}-64
#rm -rf %{_name}-%{unmangled_version}
%endif

%build
cd %{src_name}-%{version}
%{execpython} setup.py build

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py build
%endif


%install
cd %{src_name}-%{version}
%{execpython} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}
mv $RPM_BUILD_ROOT%{pyprefix}/bin/hg $RPM_BUILD_ROOT%{pyprefix}/bin/hg%{hgver}

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}
mv $RPM_BUILD_ROOT%{pyprefix}/bin/hg  $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/hg%{hgver}
%endif


# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/vendor-packages
mv $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/site-packages/* \
   $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/site-packages


%ifarch amd64 sparcv9
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/vendor-packages
mv $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/site-packages/* \
   $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/site-packages
%endif


%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{pyprefix}/bin
%{pyprefix}/bin/hg%{hgver}

%dir %attr (0755, root, bin) %{pyprefix}/%{_lib32}
%{pyprefix}/%{_lib32}/python%{pyver}/*

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{pyprefix}/bin/%{_arch64}
%{pyprefix}/bin/%{_arch64}/hg%{hgver}

%dir %attr (0755, root, bin) %{pyprefix}/%{_lib64}
%{pyprefix}/%{_lib64}/python%{pyver}/*
%endif

%changelog
* Sun Sep 21 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- version 2.1.2 set
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Python 2.7 amd64 arch support
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
