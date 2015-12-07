%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 %( if [ -x /usr/bin/python2.6 ]; then echo '1'; else echo '0'; fi)
%define build27 %( if [ -x /usr/bin/python2.7 ]; then echo '1'; else echo '0'; fi)
%define build34 %( if [ -x /usr/bin/python3.4 ]; then echo '1'; else echo '0'; fi)
%define build35 %( if [ -x /usr/bin/python3.5 ]; then echo '1'; else echo '0'; fi)

%define tarball_index P
%define tarball_name Pillow
%define tarball_version 3.0.0
%define include_executable 1

Name:                    SFEpython-pillow
IPS_package_name:        library/python/pillow
Summary:                 Python Imaging Library (Fork)
URL:                     http://python-pillow.github.io/
Version:                 %{tarball_version}
License:                 Standard PIL License
SUNW_Copyright:          python-pillow.copyright
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:    %{pnm_buildrequires_SUNWzlib_devel}
BuildRequires:    %{pnm_buildrequires_SUNWjpg_devel}
BuildRequires:    %{pnm_buildrequires_SUNWpng}
BuildRequires:    %{pnm_buildrequires_SUNWTiff}
BuildRequires:    %{pnm_requires_SUNWfreetype2}

%description
Python Imaging Library (Fork)

%if %{build26}
%package 26
IPS_package_name: library/python/pillow-26
Summary:          Python Imaging Library (Fork)
BuildRequires:    runtime/python-26
Requires:         runtime/python-26
Requires:         library/python/pillow
Requires:         %{pnm_requires_SUNWfreetype2}
Requires:         %{pnm_buildrequires_SUNWTiff}
Requires:         %{pnm_requires_SUNWzlib}
Requires:         %{pnm_requires_SUNWjpg}
Requires:         %{pnm_requires_SUNWpng}

%description 26
Python Imaging Library (Fork)
%endif

%if %{build27}
%package 27
IPS_package_name: library/python/pillow-27
Summary:          Python Imaging Library (Fork)
BuildRequires:    runtime/python-27
Requires:         runtime/python-27
Requires:         library/python/pillow
Requires:         %{pnm_requires_SUNWfreetype2}
Requires:         %{pnm_buildrequires_SUNWTiff}
Requires:         %{pnm_requires_SUNWzlib}
Requires:         %{pnm_requires_SUNWjpg}
Requires:         %{pnm_requires_SUNWpng}


%description 27
Python Imaging Library (Fork)
%endif

%if %{build34}
%package 34
IPS_package_name: library/python/pillow-34
Summary:          Python Imaging Library (Fork)
BuildRequires:    runtime/python-34
Requires:         runtime/python-34
Requires:         library/python/pillow
Requires:         %{pnm_requires_SUNWfreetype2}
Requires:         %{pnm_buildrequires_SUNWTiff}
Requires:         %{pnm_requires_SUNWzlib}
Requires:         %{pnm_requires_SUNWjpg}
Requires:         %{pnm_requires_SUNWpng}

%description 34
Python Imaging Library (Fork)
%endif

%if %{build35}
%package 35
IPS_package_name: library/python/pillow-35
Summary:          Python Imaging Library (Fork)
BuildRequires:    runtime/python-35
Requires:         runtime/python-35
Requires:         library/python/pillow
Requires:         %{pnm_requires_SUNWfreetype2}
Requires:         %{pnm_buildrequires_SUNWTiff}
Requires:         %{pnm_requires_SUNWzlib}
Requires:         %{pnm_requires_SUNWjpg}
Requires:         %{pnm_requires_SUNWpng}

%description 35
Python Imaging Library (Fork)
%endif


%prep
%setup -q -n %{tarball_name}-%{tarball_version}
if [ -d $RPM_BUILD_ROOT ]
then
    rm -rf $RPM_BUILD_ROOT
fi

%build
build_for () {
    python_version=$1

    /usr/bin/python${python_version} setup.py build
    /usr/bin/python${python_version} setup.py install \
        --skip-build \
        --root=$RPM_BUILD_ROOT
    for i in $(ls $RPM_BUILD_ROOT/usr/bin/*|egrep -v '[0-9]$')
    do
	mv ${i} ${i}-${python_version}
    done
}

%if %{build26}
build_for 2.6
%endif

%if %{build27}
build_for 2.7
%endif

%if %{build34}
build_for 3.4
%endif

%if %{build35}
build_for 3.5
%endif

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
# %doc 

%if %{build26}
%files 26
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.6
%{_libdir}/python2.6/site-packages
%if %{include_executable}
/usr/bin/*2.6
%endif
%endif

%if %{build27}
%files 27
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.7
%{_libdir}/python2.7/site-packages
%if %{include_executable}
/usr/bin/*2.7
%endif
%endif

%if %{build34}
%files 34
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python3.4
%{_libdir}/python3.4/site-packages
%if %{include_executable}
/usr/bin/*3.4
%endif
%endif

%if %{build35}
%files 35
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python3.5
%{_libdir}/python3.5/site-packages
%if %{include_executable}
/usr/bin/*3.5
%endif
%endif

%changelog
* Tue Dec 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.0.0 and build package for  python-35
* Tue Jun 09 2015 - Osamu Tabata <cantimerny.g@gmail.com>
- Support for python 2.7 and bump to 2.9.0
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.2
* Tue May 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.0
* Wed Jan 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
