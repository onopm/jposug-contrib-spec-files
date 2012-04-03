#
# spec file for package SFEpython27-mercurial-21
#
# includes module(s): SFEpython27-mercurial-21
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_url     http://mercurial.selenic.com/release
%define src_name    mercurial

Name:                    SFEpython27-mercurial-21
IPS_package_name:        developer/versioning/mercurial-21
Summary:                 The Mercurial Source Control Management System
URL:                     http://www.sqlalchemy.org
Version:                 2.1.2
Source:                  %{src_url}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
License:                 GPLv2
SUNW_Copyright:	         SFEpython27-mercurial-21.copyright
Requires:                SFEpython27
Requires:                SFEpython27-setuptools

%define python_version 2.7

%prep
%setup -q -n %{src_name}-%{version}

%build
python%{python_version} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python%{python_version} setup.py install --root=$RPM_BUILD_ROOT/% --prefix=%{_prefix} --no-compile

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
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
