%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 %( if [ -x /usr/bin/python2.6 ]; then echo '1'; else echo '0'; fi)
%define build27 %( if [ -x /usr/bin/python2.7 ]; then echo '1'; else echo '0'; fi)
%define build34 %( if [ -x /usr/bin/python3.4 ]; then echo '1'; else echo '0'; fi)
%define build35 %( if [ -x /usr/bin/python3.5 ]; then echo '1'; else echo '0'; fi)

%define tarball_index c
%define tarball_name click
%define tarball_version 6.2
%define include_executable 0

Name:                    SFEpython-click
IPS_package_name:        library/python/click
Summary:                 A simple wrapper around optparse for powerful command line utilities.
URL:                     http://github.com/mitsuhiko/click
Version:                 %{tarball_version}
License:                 UNKNOWN
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
A simple wrapper around optparse for powerful command line utilities.

%if %{build26}
%package 26
IPS_package_name: library/python/click-26
Summary:          A simple wrapper around optparse for powerful command line utilities.
BuildRequires:    runtime/python-26
Requires:         runtime/python-26
Requires:         library/python/click

%description 26
A simple wrapper around optparse for powerful command line utilities.
%endif

%if %{build27}
%package 27
IPS_package_name: library/python/click-27
Summary:          A simple wrapper around optparse for powerful command line utilities.
BuildRequires:    runtime/python-27
Requires:         runtime/python-27
Requires:         library/python/click

%description 27
A simple wrapper around optparse for powerful command line utilities.
%endif

%if %{build34}
%package 34
IPS_package_name: library/python/click-34
Summary:          A simple wrapper around optparse for powerful command line utilities.
BuildRequires:    runtime/python-34
Requires:         runtime/python-34
Requires:         library/python/click

%description 34
A simple wrapper around optparse for powerful command line utilities.
%endif

%if %{build35}
%package 35
IPS_package_name: library/python/click-35
Summary:          A simple wrapper around optparse for powerful command line utilities.
BuildRequires:    runtime/python-35
Requires:         runtime/python-35
Requires:         library/python/click

%description 35
A simple wrapper around optparse for powerful command line utilities.
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
* Wed Jan 13 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
