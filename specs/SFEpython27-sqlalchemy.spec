#
# spec file for package SFEpython27-sqlalchemy
#
# includes module(s): sqlalchemy
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_name        SQLAlchemy
%define pyprefix        /usr/python
%define pyver           2.7
%define sqlver          0.7.9
%define src_url         http://nchc.dl.sourceforge.net/sourceforge/sqlalchemy
%define execpython      %{pyprefix}/bin/python%{pyver}
%define execpython64    %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32          lib
%define _lib64          lib64


Name:                   SFEpython27-sqlalchemy
IPS_package_name:       library/python-2/SFEpython27-sqlalchemy-%{sqlver}
Summary:                SQL-Alchemy is a Python SQL toolkit and Object Relational Mapper
URL:                    http://www.sqlalchemy.org
Version:                %{sqlver}
Source:                 %{src_url}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
Requires:               runtime/SFEpython-273
Requires:               library/python-2/SFEsetuptools-27
SUNW_Copyright:	        SFEpython27-sqlalchemy.copyright


%prep
%setup -c -n %{src_name}-%{version}

%ifarch amd64 sparcv9
rm -rf %{src_name}-%{version}-64
cp -rp %{src_name}-%{version} %{src_name}-%{version}-64
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


%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}
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

echo deleting pyo files
find $RPM_BUILD_ROOT -name '*.pyo' -exec rm {} \;

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{pyprefix}/%{_lib32}/python%{pyver}/*

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%{pyprefix}/%{_lib64}/python%{pyver}/*
%endif

%changelog
* Mon Sep 22 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris11
* Sun Apr 5 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for amd64 arch
* Sun Apr 5 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
