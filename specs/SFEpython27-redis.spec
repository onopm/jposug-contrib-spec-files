#
# spec file for package SFEpython27-imaging
#

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define python_version   2.7
%define execpython      %{_bindir}/%{_arch64}/python%{python_version}

Name:                    SFEpython27-redis
IPS_package_name:        library/python-2/python-redis-27
Summary:                 The Python interface to the Redis key-value store.
URL:                     http://github.com/andymccurdy/redis-py
Version:                 2.4.13
Source:                  http://cloud.github.com/downloads/andymccurdy/redis-py/redis-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          python-redis.copyright
BuildRequires:           SFEpython27-setuptools
Requires:                SFEpython27


%description
The Python interface to the Redis key-value store.


%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
%setup -n redis-%{version}


%build
%{execpython} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{execpython} setup.py install -O1 --skip-build --root="$RPM_BUILD_ROOT" --prefix="%{_prefix}"

# move to vendor-packages
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
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/

%changelog
* Sun May 20 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for openindiana
