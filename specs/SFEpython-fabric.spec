%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_index F
%define tarball_name Fabric
%define tarball_version 1.6.0

Name:                    SFEpython-fabric
IPS_package_name:        library/python-2/fabric-26
Summary:                 Fabric is a simple, Pythonic tool for remote execution and deployment.
URL:                     http://pypi.python.org/pypi/%{tarball_name}/
Version:                 1.6.0
License:                 BSD License
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26
Requires:                library/python-2/paramiko-26


%description
Fabric is a syntax highlighting package written in Python.

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
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
%dir %attr (0755, root, bin) %{_bindir}
/usr/bin/fab
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.6/site-packages

%changelog
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
