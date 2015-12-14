%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define tarball_name blockdiag
%define tarball_version 1.5.3

Name:                    SFEblockdiag
IPS_package_name:        image/blockdiag
Summary:                 blockdiag generate block-diagram image file from spec-text file.
URL:                     http://pypi.python.org/pypi/blockdiag/
Version:                 1.5.3
License:                 Apache License 2.0
Source:                  http://pypi.python.org/packages/source/b/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:           runtime/python-27
BuildRequires:           library/python/setuptools-27
Requires:                runtime/python-27
Requires:                library/python/funcparserlib-27
Requires:                library/python/ordereddict-27
Requires:                library/python/pillow-27
Requires:                library/python/webcolors-27

%description
blockdiag generate block-diagram image file from spec-text file.

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
# /usr/bin/python2.7 bootstrap.py
# bin/buildout
/usr/bin/python2.7 setup.py build

%install
rm -rf $RPM_BUILD_ROOT

/usr/bin/python2.7 setup.py install \
    --skip-build \
    --root=$RPM_BUILD_ROOT

# cp -r src/* $RPM_BUILD_ROOT%{_libdir}/python2.7/site-packages/

# move to vendor-packages
# mkdir -p $RPM_BUILD_ROOT%{_libdir}/python2.7/vendor-packages
# mv $RPM_BUILD_ROOT%{_libdir}/python2.7/site-packages/* \
#    $RPM_BUILD_ROOT%{_libdir}/python2.7/vendor-packages/
# rmdir $RPM_BUILD_ROOT%{_libdir}/python2.7/site-packages

# %{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/blockdiag
%dir %attr (0755, root, bin) %{_libdir}
# %{_libdir}/python2.7/vendor-packages
%{_libdir}/python2.7/site-packages

%changelog
* Mon Dec 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.3 and use python-27
* Fri Jan 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.0
- add Requires
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
