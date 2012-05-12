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
%define python_version 2.7
%define execpython      %{_bindir}/%{_arch64}/python%{python_version}

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
BuildRequires:           SFEpython27
Requires:                SFEpython27

%prep
%setup -q -n %{src_name}-%{version}

%build
%{execpython} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{execpython} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
cp $RPM_BUILD_ROOT%{_bindir}/hg $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/hg
rm $RPM_BUILD_ROOT%{_bindir}/hg
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/hg
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages

%changelog
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Python 2.7 amd64 arch support
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
