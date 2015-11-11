#
# spec file for package SFEpython27-django
#
# includes module(s): Django
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_name        Django
%define pyprefix        /usr/python
%define pyver           2.7
%define djver           1.4
%define fdjver          1.4.3
%define execpython      %{pyprefix}/bin/python%{pyver}
%define execpython64    %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32          lib
%define _lib64          lib64

Name:		        SFEpython27-django
IPS_Package_Name:	web/python/SFEpython27-django-%{fdjver}
Version:	        %{fdjver}
Summary:	        A high-level Python Web framework that enables Rapid Development
License:                BSD
Group:                  Development/Languages/Python
URL:                    http://www.djangoproject.com/
Source:                 http://www.djangoproject.com/m/releases/%{djver}/Django-%{version}.tar.gz
SUNW_Copyright:	        SFEpython27-django.copyright
BuildRoot:	        %{_tmppath}/%{name}-%{version}-build
Requires:               runtime/SFEpython-273
Requires:               library/python-2/SFEsetuptools-27

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
mv $RPM_BUILD_ROOT%{pyprefix}/bin/django-admin.py $RPM_BUILD_ROOT%{pyprefix}/bin/django-admin%{djver}.py

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py install --root="$RPM_BUILD_ROOT" --prefix=%{pyprefix}
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}
mv $RPM_BUILD_ROOT%{pyprefix}/bin/django-admin.py  $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/django-admin%{djver}.py
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
%dir %attr (0755, root, sys) /usr
%{pyprefix}/bin/django-admin%{djver}.py
%{pyprefix}/%{_lib32}/python%{pyver}/*

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%{pyprefix}/bin/%{_arch64}/django-admin%{djver}.py
%{pyprefix}/%{_lib64}/python%{pyver}/*
%endif


%changelog
* Mon Sep 22 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Supprt for Solaris11
* Sun Apr 4 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Supprt for amd64 arch
* Sun Apr 4 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
