#
# spec file for package: python-kanjifilter
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
%define tarball_name pykf
%define tarball_version 0.4

Name:                    SFEpython-kanjifilter
IPS_package_name:        library/python-2/kanjifilter
Summary:                 Japanese Kanji filter module 
SUNW_Copyright:          %{name}.copyright
URL:                     http://pypi.python.org/pypi/%{tarball_name}/
Version:                 0.4
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26

%description
Japanese Kanji filter module

%prep
%setup -q -n %{tarball_name}-%{tarball_version}
pushd .
cd src
for f in `/bin/ls -1`; do
  dos2unix $f > $f.unix
  /bin/mv -f $f.unix $f
done
popd

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
* Sun Apr 27 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- initial commit
