%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 %( if [ -x /usr/bin/python2.6 ]; then echo '1'; else echo '0'; fi)
%define build27 %( if [ -x /usr/bin/python2.7 ]; then echo '1'; else echo '0'; fi)
%define build34 %( if [ -x /usr/bin/python3.4 ]; then echo '1'; else echo '0'; fi)
%define build35 %( if [ -x /usr/bin/python3.5 ]; then echo '1'; else echo '0'; fi)

%define tarball_index c
%define tarball_name certifi
%define tarball_version 2018.4.16
%define include_executable 0

Name:                    SFEpython-certifi
IPS_package_name:        library/python/certifi
Summary:                 Python package for providing Mozilla's CA Bundle.
URL:                     http://certifi.io/
Version:                 %{tarball_version}
License:                 ISC
Source:                  https://pypi.io/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
Python package for providing Mozilla's CA Bundle.

%if %{build26}
%package 26
IPS_package_name: library/python/certifi-26
Summary:          Python package for providing Mozilla's CA Bundle.
BuildRequires:    runtime/python-26
Requires:         runtime/python-26
Requires:         library/python/certifi

%description 26
Python package for providing Mozilla's CA Bundle.
%endif

%if %{build27}
%package 27
IPS_package_name: library/python/certifi-27
Summary:          Python package for providing Mozilla's CA Bundle.
BuildRequires:    runtime/python-27
Requires:         runtime/python-27
Requires:         library/python/certifi

%description 27
Python package for providing Mozilla's CA Bundle.
%endif

%if %{build34}
%package 34
IPS_package_name: library/python/certifi-34
Summary:          Python package for providing Mozilla's CA Bundle.
BuildRequires:    runtime/python-34
Requires:         runtime/python-34
Requires:         library/python/certifi

%description 34
Python package for providing Mozilla's CA Bundle.
%endif

%if %{build35}
%package 35
IPS_package_name: library/python/certifi-35
Summary:          Python package for providing Mozilla's CA Bundle.
BuildRequires:    runtime/python-35
Requires:         runtime/python-35
Requires:         library/python/certifi

%description 35
Python package for providing Mozilla's CA Bundle.
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

    if [ -d $RPM_BUILD_ROOT/usr/bin ]
    then
        for i in $(ls $RPM_BUILD_ROOT/usr/bin/*|egrep -v '[0-9]$')
        do
            mv ${i} ${i}-${python_version}
        done
    fi
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
%if %{build34}
# fix libdir path for 3.4
if [ -d $RPM_BUILD_ROOT/usr/lib/lib/python3.4 -a ! -e $RPM_BUILD_ROOT/usr/lib/python3.4 ]
then
    mv $RPM_BUILD_ROOT/usr/lib/lib/python3.4 $RPM_BUILD_ROOT/usr/lib/
    rmdir $RPM_BUILD_ROOT/usr/lib/lib
fi
%endif

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
* Wed Jun 13 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2018.4.16
* Tue Feb 14 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
