#
# spec file for package SFEpython27-redis
#

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_name         redis
%define pyprefix         /usr/python
%define pyver            2.7
%define rdver            2.7.2
%define execpython       %{pyprefix}/bin/python%{pyver}
%define execpython64     %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32           lib
%define _lib64           lib64

Name:                    SFEpython27-redis
IPS_package_name:        library/python-2/SFEpython27-redis-%{rdver}
Summary:                 The Python interface to the Redis key-value store.
URL:                     http://github.com/andymccurdy/redis-py
Version:                 %{rdver}
Source:                  http://cloud.github.com/downloads/andymccurdy/redis-py/redis-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          python-redis.copyright
Requires:                runtime/SFEpython-273
Requires:                library/python-2/SFEsetuptools-27

%description
The Python interface to the Redis key-value store.


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
%{execpython} setup.py install install -O1 --skip-build --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py install install -O1 --skip-build --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}
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
* Tue Sep 23 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris11
* Sun May 20 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for openindiana
