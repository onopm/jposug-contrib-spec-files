#
# spec file for package: python-worldtimezone
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc
%define cc_is_gcc 0
%define _gpp g++
%include base.inc

%define tarball_index p
%define tarball_name pytz
%define tarball_version 2014.2

Name:                    SFEpython-worldtimezone
IPS_package_name:        library/python-2/worldtimezone
Summary:                 World Timezone Definitions for Python
SUNW_Copyright:          %{name}.copyright
URL:                     http://pypi.python.org/pypi/%{tarball_name}/
Version:                 %tarball_version
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26

%description
pytz - World Timezone Definitions for Python

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags"
export PYCC_CC="$CC"
export PYCC_CXX="$CXX"
/usr/bin/python2.6 setup.py build

%install
rm -rf $RPM_BUILD_ROOT

/usr/bin/python2.6 setup.py install \
    --skip-build \
    --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.6/site-packages

%changelog
* Tue May 20 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- change summary

* Tue May 20 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- initial commit
