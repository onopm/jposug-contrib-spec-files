%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 %( if [ -x /usr/bin/python2.6 ]; then echo '1'; else echo '0'; fi)
%define build27 %( if [ -x /usr/bin/python2.7 ]; then echo '1'; else echo '0'; fi)
%define build34 %( if [ -x /usr/bin/python3.4 ]; then echo '1'; else echo '0'; fi)
%define build35 %( if [ -x /usr/bin/python3.5 ]; then echo '1'; else echo '0'; fi)

%define tarball_index w
%define tarball_name webcolors
%define tarball_version 1.5

Name:                    SFEpython-webcolors
IPS_package_name:        library/python/webcolors
Summary:                 A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
URL:                     https://github.com/ubernostrum/webcolors
Version:                 %{tarball_version}
License:                 BSD License
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.

%if %{build26}
%package 26
IPS_package_name: library/python/webcolors-26
Summary:          A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
BuildRequires:    runtime/python-26
Requires:         runtime/python-26
Requires:         library/python/webcolors

%description 26
A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
%endif

%if %{build27}
%package 27
IPS_package_name: library/python/webcolors-27
Summary:          A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
BuildRequires:    runtime/python-27
Requires:         runtime/python-27
Requires:         library/python/webcolors

%description 27
A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
%endif

%if %{build34}
%package 34
IPS_package_name: library/python/webcolors-34
Summary:          A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
BuildRequires:    runtime/python-34
Requires:         runtime/python-34
Requires:         library/python/webcolors

%description 34
A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
%endif

%if %{build35}
%package 35
IPS_package_name: library/python/webcolors-35
Summary:          A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
BuildRequires:    runtime/python-35
Requires:         runtime/python-35
Requires:         library/python/webcolors

%description 35
A library for working with color names and color value formats defined by the HTML and CSS specifications for use in documents on the Web.
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
%endif

%if %{build27}
%files 27
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.7
%{_libdir}/python2.7/site-packages
%endif

%if %{build34}
%files 34
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python3.4
%{_libdir}/python3.4/site-packages
%endif

%if %{build35}
%files 35
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python3.5
%{_libdir}/python3.5/site-packages
%endif

%changelog
* Mon Dec 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5 and build packages for python-27, python-34 and python-35
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
