#
# spec file for package SFEpython27-MySQL-python
#

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define python_version   2.7
%define execpython      %{_bindir}/%{_arch64}/python%{python_version}

Name:                    SFEpython27-MySQL-python
IPS_package_name:        library/python-2/mysql-python
Summary:                 Python interface to MySQL
URL:                     http://sourceforge.net/projects/mysql-python
Version:                 1.2.3
Source:                  http://download.sourceforge.net/sourceforge/mysql-python/MySQL-python-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          mysql-python.copyright
BuildRequires:           SFEpython27-setuptools
BuildRequires:           database/mysql-51
BuildRequires:           library/zlib
BuildRequires:           library/security/openssl
BuildRequires:           database/mysql-51/library
Requires:                SFEpython27
Requires:                database/mysql-51/library
Requires:                library/zlib
Requires:                library/security/openssl

%description
MySQL support for Python. MySQL versions 3.23-5.1; and Python versions 2.3-2.6 are supported.
MySQLdb is the Python DB API-2.0 interface. 
_mysql is a low-level API similiar to the MySQL C API. ZMySQLDA is a Database Adapter for Zope2.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
%setup -n MySQL-python-%{version}

%build
export LDFLAGS="-R/usr/lib/%{_arch64} -R/usr/mysql/5.1/lib/%{_arch64}/mysql"
export PATH=/usr/mysql/5.1/bin/%{_arch64}:$PATH
%{execpython} setup.py build

%install
export PATH=/usr/mysql/5.1/bin/%{_arch64}:$PATH
rm -rf $RPM_BUILD_ROOT
%{execpython} setup.py install -O1 --skip-build --root="$RPM_BUILD_ROOT" --prefix="%{_prefix}"

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages

echo deleting pyo files
find $RPM_BUILD_ROOT -name '*.pyo' -exec rm {} \;

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/*

%changelog
* Sun May 18 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for openindiana
