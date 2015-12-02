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
%define pyprefix        /usr/python
%define pyver           2.7
%define execpython      %{pyprefix}/bin/python%{pyver}
%define execpython64    %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32          lib
%define _lib64          lib64

Name:                   SFEpython27-setuptools
IPS_package_name:       library/python-2/SFEsetuptools-27
Summary:                Distribute (fork of Setuptools) is a collection of extensions to Distutils
URL:                    http://pypi.python.org/pypi/distribute
Version:                0.6.21
Source:                 %{src_url}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
License:                PSF-2 license
SUNW_Copyright:         SFEpython27-setuptools.copyright

BuildRequires:          SFEpython27
Requires:               SFEpython27

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
rm -rf $RPM_BUILD_ROOT%{pyprefix}/bin

%ifarch amd64 sparcv9
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/vendor-packages
mv $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/site-packages/* \
   $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/site-packages
rm -rf $RPM_BUILD_ROOT%{pyprefix}/bin
%endif


%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{pyprefix}/%{_lib32}
%{pyprefix}/%{_lib32}/python%{pyver}/*

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{pyprefix}/%{_lib64}
%{pyprefix}/%{_lib64}/python%{pyver}/*
%endif


%changelog
* Sun Sep 21 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris11
* Sun May 11 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- delete --no-compile option
* Sun May 11 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Python 2.7 amd64 arch support
* Sun Apr 2 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
* Sun Apr 30 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Buildrequire append
