#
# spec file for package SFEpython27-MySQL-python
#

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_name        MySQL-python
%define mysqlver        5.1
%define pyprefix        /usr/python
%define pyver           2.7
%define mypver          1.2.3
%define execpython      %{pyprefix}/bin/python%{pyver}
%define execpython64    %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32          lib
%define _lib64          lib64

Name:                    SFEpython27-MySQL-python
IPS_package_name:        library/python-2/SFEMySQL-python-%{mypver}
Summary:                 Python interface to MySQL
URL:                     http://sourceforge.net/projects/mysql-python
Version:                 %{mypver}
Source:                  http://download.sourceforge.net/sourceforge/mysql-python/MySQL-python-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          mysql-python.copyright
BuildRequires:           runtime/SFEpython-273
BuildRequires:           library/zlib
BuildRequires:           library/security/openssl
BuildRequires:           database/mysql-51/library
Requires:                runtime/SFEpython-273
Requires:                database/mysql-51/library
Requires:                library/zlib
Requires:                library/security/openssl

%description
MySQL support for Python. MySQL versions 3.23-5.1; and Python versions 2.3-2.6 are supported.
MySQLdb is the Python DB API-2.0 interface. 
_mysql is a low-level API similiar to the MySQL C API. ZMySQLDA is a Database Adapter for Zope2.


%prep
%setup -c -n %{src_name}-%{version}

%ifarch amd64 sparcv9
rm -rf %{src_name}-%{version}-64
cp -rp %{src_name}-%{version} %{src_name}-%{version}-64
%endif


%build
cd %{src_name}-%{version}
export PATH=/usr/mysql/5.1/bin:$PATH
export LDFLAGS=`mysql_config --libs`
%{execpython} setup.py build

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
export PATH=/usr/mysql/%{mysqlver}/bin/%{_arch64}:$PATH
export LDFLAGS=`mysql_config --libs`
%{execpython64} setup.py build
%endif


%install
cd %{src_name}-%{version}
export PATH=/usr/mysql/5.1/bin:$PATH
export LDFLAGS=`mysql_config --libs`
%{execpython} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
export PATH=/usr/mysql/%{mysqlver}/bin/%{_arch64}:$PATH
export LDFLAGS=`mysql_config --libs`
%{execpython64} setup.py install -O1 --skip-build --root="$RPM_BUILD_ROOT" --prefix=%{pyprefix}
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
%dir %attr (0755, root, bin) %{pyprefix}
%{pyprefix}/%{_lib32}/python%{pyver}/vendor-packages/*
%{pyprefix}/%{_lib64}/python%{pyver}/vendor-packages/*

%changelog
* Sun Sep 21 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris11
* Sun May 18 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for openindiana
