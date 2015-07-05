%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 1
%define build27 1
%define build34 0

%define tarball_index P
%define tarball_name Pillow
%define tarball_version 2.9.0

Name:                    SFEpython-pillow
IPS_package_name:        library/python/pillow
Summary:                 Python Imaging Library (Fork)
URL:                     http://python-pillow.github.io/
Version:                 %{tarball_version}
License:                 Standard PIL License
SUNW_Copyright:          python-pillow.copyright
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
Python Imaging Library (Fork)

%if %{build26}
%package 26
IPS_package_name: library/python/pillow-26
Summary:          Python Imaging Library (Fork)
BuildRequires:    runtime/python-26
BuildRequires:    %{pnm_buildrequires_SUNWzlib_devel}
BuildRequires:    %{pnm_buildrequires_SUNWjpg_devel}
BuildRequires:    %{pnm_buildrequires_SUNWpng}
BuildRequires:    %{pnm_buildrequires_SUNWTiff}
BuildRequires:    %{pnm_requires_SUNWfreetype2}
Requires:         runtime/python-26
Requires:         library/python-2/setuptools-26
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
BuildRequires:    %{pnm_buildrequires_SUNWzlib_devel}
BuildRequires:    %{pnm_buildrequires_SUNWjpg_devel}
BuildRequires:    %{pnm_buildrequires_SUNWpng}
BuildRequires:    %{pnm_buildrequires_SUNWTiff}
BuildRequires:    %{pnm_requires_SUNWfreetype2}
Requires:         runtime/python-27
Requires:         library/python-2/setuptools-27
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

%description 34
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

}

%if %{build26}
build_for 2.6
mv $RPM_BUILD_ROOT/usr/bin/pildriver.py $RPM_BUILD_ROOT/usr/bin/pildriver2.6.py 
mv $RPM_BUILD_ROOT/usr/bin/pilprint.py $RPM_BUILD_ROOT/usr/bin/pilprint2.6.py
mv $RPM_BUILD_ROOT/usr/bin/pilfile.py $RPM_BUILD_ROOT/usr/bin/pilfile2.6.py
mv $RPM_BUILD_ROOT/usr/bin/pilconvert.py $RPM_BUILD_ROOT/usr/bin/pilconvert2.6.py
mv $RPM_BUILD_ROOT/usr/bin/pilfont.py $RPM_BUILD_ROOT/usr/bin/pilfont2.6.py
%endif

%if %{build27}
build_for 2.7
mv $RPM_BUILD_ROOT/usr/bin/pildriver.py $RPM_BUILD_ROOT/usr/bin/pildriver2.7.py 
mv $RPM_BUILD_ROOT/usr/bin/pilprint.py $RPM_BUILD_ROOT/usr/bin/pilprint2.7.py
mv $RPM_BUILD_ROOT/usr/bin/pilfile.py $RPM_BUILD_ROOT/usr/bin/pilfile2.7.py
mv $RPM_BUILD_ROOT/usr/bin/pilconvert.py $RPM_BUILD_ROOT/usr/bin/pilconvert2.7.py
mv $RPM_BUILD_ROOT/usr/bin/pilfont.py $RPM_BUILD_ROOT/usr/bin/pilfont2.7.py
%endif

%if %{build34}
build_for 3.4
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
%dir %attr (0755, root, bin) %{_bindir}
%attr (0755, root, bin) %{_bindir}/pildriver2.6.py
%attr (0755, root, bin) %{_bindir}/pilfont2.6.py
%attr (0755, root, bin) %{_bindir}/pilprint2.6.py
%attr (0755, root, bin) %{_bindir}/pilfile2.6.py
%attr (0755, root, bin) %{_bindir}/pilconvert2.6.py
%endif

%if %{build27}
%files 27
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.7
%{_libdir}/python2.7/site-packages
%dir %attr (0755, root, bin) %{_bindir}
%attr (0755, root, bin) %{_bindir}/pildriver2.7.py
%attr (0755, root, bin) %{_bindir}/pilfont2.7.py
%attr (0755, root, bin) %{_bindir}/pilprint2.7.py
%attr (0755, root, bin) %{_bindir}/pilfile2.7.py
%attr (0755, root, bin) %{_bindir}/pilconvert2.7.py
%endif

%if %{build34}
%files 34
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python3.4
%{_libdir}/python3.4/site-packages
%endif

%changelog
* Tue Jun 09 2015 - Osamu Tabata <cantimerny.g@gmail.com>
- Support for python 2.7 and bump to 2.9.0
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.2
* Tue May 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.0
* Wed Jan 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
