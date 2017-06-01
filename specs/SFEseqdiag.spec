%include Solaris.inc
%include packagenamemacros.inc

%define tarball_index s
%define tarball_name seqdiag
%define tarball_version 0.9.5

Name:                    SFEseqdiag
IPS_package_name:        image/seqdiag
Summary:                 seqdiag generate sequence-diagram image file from spec-text file.
URL:                     http://pypi.python.org/pypi/seqdiag/
Version:                 %{tarball_version}
License:                 Apache License 2.0
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-27
BuildRequires:           library/python/setuptools-27
Requires:                runtime/python-27
Requires:                library/python/funcparserlib-27
Requires:                library/python/ordereddict-27
Requires:                library/python/pillow-27
Requires:                library/python/webcolors-27
Requires:                image/blockdiag

%description
seqdiag generate sequence-diagram image file from spec-text file.

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
/usr/bin/python2.7 setup.py build

%install
rm -rf $RPM_BUILD_ROOT

/usr/bin/python2.7 setup.py install \
    --skip-build \
    --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/seqdiag
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.7/site-packages

%changelog
* Tue Dec 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use python-27 instead of python-27
* Fri Jan 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.5
- add Requires
* Wed Jan 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.0
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
