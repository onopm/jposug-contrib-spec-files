%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 %( if [ -x /usr/bin/python2.6 ]; then echo '1'; else echo '0'; fi)
%define build27 %( if [ -x /usr/bin/python2.7 ]; then echo '1'; else echo '0'; fi)
%define build34 %( if [ -x /usr/bin/python3.4 ]; then echo '1'; else echo '0'; fi)
%define build35 %( if [ -x /usr/bin/python3.5 ]; then echo '1'; else echo '0'; fi)

%define tarball_index f
%define tarball_name funcparserlib
%define tarball_version 0.3.6

Name:                    SFEpython-funcparserlib
IPS_package_name:        library/python/funcparserlib
Summary:                 Recursive descent parsing library based on functional combinators
URL:                     https://github.com/vlasovskikh/funcparserlib
Version:                 %{tarball_version}
License:                 MIT
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
Recursive descent parsing library based on functional combinators

%if %{build26}
%package 26
IPS_package_name: library/python/funcparserlib-26
Summary:          Recursive descent parsing library based on functional combinators
BuildRequires:    runtime/python-26
Requires:         runtime/python-26
Requires:         library/python/funcparserlib

%description 26
Recursive descent parsing library based on functional combinators
%endif

%if %{build27}
%package 27
IPS_package_name: library/python/funcparserlib-27
Summary:          Recursive descent parsing library based on functional combinators
BuildRequires:    runtime/python-27
Requires:         runtime/python-27
Requires:         library/python/funcparserlib

%description 27
Recursive descent parsing library based on functional combinators
%endif

%if %{build34}
%package 34
IPS_package_name: library/python/funcparserlib-34
Summary:          Recursive descent parsing library based on functional combinators
BuildRequires:    runtime/python-34
Requires:         runtime/python-34
Requires:         library/python/funcparserlib

%description 34
Recursive descent parsing library based on functional combinators
%endif

%if %{build35}
%package 35
IPS_package_name: library/python/funcparserlib-35
Summary:          Recursive descent parsing library based on functional combinators
BuildRequires:    runtime/python-35
Requires:         runtime/python-35
Requires:         library/python/funcparserlib

%description 35
Recursive descent parsing library based on functional combinators
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
* Tue Dec 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packages for python-27, python-34 and python-35
* Fri Jan 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.6
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
