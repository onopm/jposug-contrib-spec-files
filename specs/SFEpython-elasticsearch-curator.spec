%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 %( if [ -x /usr/bin/python2.6 ]; then echo '1'; else echo '0'; fi)
%define build27 %( if [ -x /usr/bin/python2.7 ]; then echo '1'; else echo '0'; fi)
%define build34 %( if [ -x /usr/bin/python3.4 ]; then echo '1'; else echo '0'; fi)
%define build35 %( if [ -x /usr/bin/python3.5 ]; then echo '1'; else echo '0'; fi)

%define tarball_index e
%define tarball_name elasticsearch-curator
%define tarball_version 3.4.0
%define include_executable 1

Name:                    python-elasticsearch-curator
IPS_package_name:        library/python/elasticsearch-curator
Summary:                 Tending your Elasticsearch indices
URL:                     http://github.com/elastic/curator
Version:                 %{tarball_version}
License:                 Apache License, Version 2.0
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
Tending your Elasticsearch indices

%if %{build26}
%package 26
IPS_package_name: library/python/elasticsearch-curator-26
Summary:          Tending your Elasticsearch indices
BuildRequires:    runtime/python-26
Requires:         runtime/python-26
Requires:         library/python/elasticsearch-curator
Requires:         library/python/click-26
Requires:         library/python/elasticsearch-26
Requires:         library/python/urllib3-26

%description 26
Tending your Elasticsearch indices
%endif

%if %{build27}
%package 27
IPS_package_name: library/python/elasticsearch-curator-27
Summary:          Tending your Elasticsearch indices
BuildRequires:    runtime/python-27
Requires:         runtime/python-27
Requires:         library/python/elasticsearch-curator
Requires:         library/python/click-27
Requires:         library/python/elasticsearch-27
Requires:         library/python/urllib3-27

%description 27
Tending your Elasticsearch indices
%endif

%if %{build34}
%package 34
IPS_package_name: library/python/elasticsearch-curator-34
Summary:          Tending your Elasticsearch indices
BuildRequires:    runtime/python-34
Requires:         runtime/python-34
Requires:         library/python/elasticsearch-curator
Requires:         library/python/click-34
Requires:         library/python/elasticsearch-34
Requires:         library/python/urllib3-34

%description 34
Tending your Elasticsearch indices
%endif

%if %{build35}
%package 35
IPS_package_name: library/python/elasticsearch-curator-35
Summary:          Tending your Elasticsearch indices
BuildRequires:    runtime/python-35
Requires:         runtime/python-35
Requires:         library/python/elasticsearch-curator
Requires:         library/python/click-35
Requires:         library/python/elasticsearch-35
Requires:         library/python/urllib3-35

%description 35
Tending your Elasticsearch indices
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
- add Requires
* Tue Jan 12 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
