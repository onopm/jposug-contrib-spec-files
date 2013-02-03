#
# spec file for package SFEpython27-sqlalchemy
#
# includes module(s): sqlalchemy
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_index f
%define tarball_name funcparserlib
%define tarball_version 0.3.5

Name:                    SFEpython-funcparserlib
IPS_package_name:        library/python-2/funcparserlib-26
Summary:                 Recursive descent parsing library based on functional combinators
URL:                     http://pypi.python.org/pypi/funcparserlib/
Version:                 0.3.5
License:                 MIT License
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26

%description
Recursive descent parsing library based on functional combinators

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
# /usr/bin/python2.6 bootstrap.py
# bin/buildout
/usr/bin/python2.6 setup.py build

%install
rm -rf $RPM_BUILD_ROOT

/usr/bin/python2.6 setup.py install \
    --skip-build \
    --root=$RPM_BUILD_ROOT

# cp -r src/* $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages/

# move to vendor-packages
# mkdir -p $RPM_BUILD_ROOT%{_libdir}/python2.6/vendor-packages
# mv $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages/* \
#    $RPM_BUILD_ROOT%{_libdir}/python2.6/vendor-packages/
# rmdir $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages

# %{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
# %{_libdir}/python2.6/vendor-packages
%{_libdir}/python2.6/site-packages

%changelog
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
