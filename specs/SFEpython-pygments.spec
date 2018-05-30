%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_index P
%define tarball_name Pygments
%define tarball_version 1.5

Name:                    SFEpython-pygments
IPS_package_name:        library/python-2/pygments-26
Summary:                 Pygments is a syntax highlighting package written in Python.
URL:                     http://pypi.python.org/pypi/%{tarball_name}/
Version:                 1.5
License:                 BSD License
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26
Requires:                library/python-2/markupsafe-26

%description
Pygments is a syntax highlighting package written in Python.

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
/usr/bin/pygmentize
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.6/site-packages

%changelog
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
