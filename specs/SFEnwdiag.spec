%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_index n
%define tarball_name nwdiag
%define tarball_version 1.0.0

Name:                    SFEnwdiag
IPS_package_name:        image/nwdiag
Summary:                 nwdiag generate network-diagram image file from spec-text file.
URL:                     http://pypi.python.org/pypi/nwdiag/
Version:                 1.0.0
License:                 Apache License 2.0
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
BuildRequires:           library/python-2/setuptools-26
Requires:                runtime/python-26
Requires:                image/blockdiag >= 1.3.0

%description
nwdiag generate network-diagram image file from spec-text file.

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
%{_bindir}/nwdiag
%{_bindir}/rackdiag
%{_bindir}/packetdiag
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.6/site-packages

%changelog
* Thu Jan 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix required blockdiag version
* Tue Jan 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.0
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
