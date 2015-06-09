%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_index P
%define tarball_name Pillow
%define tarball_version 2.8.2

Name:                    SFEpython-pillow
IPS_package_name:        library/python-2/pillow-26
Summary:                 Python Imaging Library (Fork)
URL:                     http://python-imaging.github.io/
Version:                 %{tarball_version}
License:                 Standard PIL License
Source:                  http://pypi.python.org/packages/source/P/Pillow/%{tarball_name}-%{tarball_version}.zip
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
Requires:                runtime/python-26

%description
Python Imaging Library (Fork)

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
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.2
* Tue May 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.0
* Wed Jan 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
