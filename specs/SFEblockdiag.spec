%include Solaris.inc
%include packagenamemacros.inc

%define tarball_name blockdiag
%define tarball_version 1.5.0

Name:                    SFEblockdiag
IPS_package_name:        image/blockdiag
Summary:                 blockdiag generate block-diagram image file from spec-text file.
URL:                     http://pypi.python.org/pypi/blockdiag/
Version:                 %{tarball_version}
License:                 Apache License 2.0
Source:                  http://pypi.python.org/packages/source/b/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-26
BuildRequires:           library/python-2/setuptools-26
Requires:                runtime/python-26
Requires:                library/python-2/funcparserlib-26 >= 0.3.6
Requires:                library/python-2/ordereddict-26
Requires:                library/python-2/pillow-26 >= 2.2.1
Requires:                library/python-2/webcolors-26

%description
blockdiag generate block-diagram image file from spec-text file.

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

# cp -r src/* $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages/

# move to vendor-packages
# mkdir -p $RPM_BUILD_ROOT%{_libdir}/python2.6/vendor-packages
# mv $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages/* \
#    $RPM_BUILD_ROOT%{_libdir}/python2.6/vendor-packages/
# rmdir $RPM_BUILD_ROOT%{_libdir}/python2.6/site-packages

# %{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/blockdiag
%dir %attr (0755, root, bin) %{_libdir}
# %{_libdir}/python2.6/vendor-packages
%{_libdir}/python2.6/site-packages

%changelog
* Fri Jan 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.0
* Wed Jan 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- blockdiag 1.3.2 requires Pillow instead of PIL
* Tue Jan 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.2
* Sat Feb 09 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
