#
# spec file for package SFEpython27-sqlalchemy
#
# includes module(s): sqlalchemy
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_index o
%define tarball_name ordereddict
%define tarball_version 1.1

Name:                    SFEpython-ordereddict
IPS_package_name:        library/python-2/ordereddict-26
Summary:                 A drop-in substitute for Py2.7's new collections.OrderedDict that works in Python 2.4-2.6.
URL:                     http://pypi.python.org/pypi/%{tarball_name}
Version:                 0.3.5
License:                 MIT License
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26

%description
A drop-in substitute for Py2.7's new collections.OrderedDict that works in Python 2.4-2.6.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.6/site-packages

%changelog
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
