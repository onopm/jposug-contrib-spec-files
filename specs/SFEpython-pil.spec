%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_index p
%define tarball_name Imaging
%define tarball_version 1.1.7

Name:                    SFEpython-pil
IPS_package_name:        library/python-2/pil-26
Summary:                 Python Imaging Library
URL:                     http://pypi.python.org/pypi/PIL
Version:                 1.1.7
License:                 Python (MIT style)
Source:                  http://effbot.org/media/downloads/Imaging-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26

%description
Python Imaging Library

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
/usr/bin/pilfont.py
/usr/bin/pilprint.py
/usr/bin/pilfile.py
/usr/bin/pildriver.py
/usr/bin/pilconvert.py
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.6/site-packages

%changelog
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
