#
# spec file for package SFEpython27-setuptools
#
# includes module(s): SFEpython27-setuptools
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_url         http://pypi.python.org/packages/source/d/distribute/
%define src_name        distribute

Name:                   SFEpython27-setuptools
IPS_package_name:       library/python-2/setuptools-27
Summary:                Distribute (fork of Setuptools) is a collection of extensions to Distutils
URL:                    http://pypi.python.org/pypi/distribute
Version:                0.6.21
Source:                 %{src_url}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
License:                PSF-2 license
SUNW_Copyright:         SFEpython27-setuptools.copyright

BuildRequires: SFEpython27
Requires:      SFEpython27

%define python_version 2.7

%prep
%setup -q -n %{src_name}-%{version}

%build
python%{python_version} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{python_version} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix} --no-compile


# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/python%{python_version}/site-packages

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python%{python_version}/vendor-packages/

%changelog
* Sun Apr 2 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
* Sun Apr 30 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Buildrequire append
