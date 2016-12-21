%include Solaris.inc
%include default-depend.inc

%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24 %( if [ -x /usr/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 0

%define gemname elasticsearch-transport
%define sfe_gemname es-transport

Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          1.0.18
License:          Apache 2
URL:              https://github.com/elasticsearch/elasticsearch-ruby/tree/master/elasticsearch-transport
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.


%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.

%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# faraday >= 0
Requires:         library/ruby/faraday-21
# multi_json >= 0
Requires:         library/ruby/multi_json-21
Requires:         library/ruby/%{gemname}

%description 21
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.

%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.

%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# faraday >= 0
Requires:         library/ruby/faraday-22
# multi_json >= 0
Requires:         library/ruby/multi_json-22
Requires:         library/ruby/%{gemname}

%description 22
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.

%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}-23

%description 23-old
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.

%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# faraday >= 0
Requires:         library/ruby/faraday-23
# multi_json >= 0
Requires:         library/ruby/multi_json-23
Requires:         library/ruby/%{gemname}

%description 23
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.

%endif

%if %{build24}

%package 24
IPS_package_name: library/ruby/%{gemname}-24
Summary:          Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.
BuildRequires:    runtime/ruby-24 = *
Requires:         runtime/ruby-24 = *
# faraday >= 0
Requires:         library/ruby/faraday-24
# multi_json >= 0
Requires:         library/ruby/multi_json-24
Requires:         library/ruby/%{gemname}

%description 24
Ruby client for Elasticsearch. See the `elasticsearch` gem for full integration.

%endif


%prep
%setup -q -c -T

%build
build_for() {
    ruby_ver=$1
    bindir="/usr/ruby/${ruby_ver}/bin"
    gemdir="$(${bindir}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    ${bindir}/gem install --local \
        --no-env-shebang \
        --install-dir .${gemdir} \
        --bindir .${bindir} \
        --no-ri \
        --no-rdoc \
        -V \
        --force %{SOURCE0}
}

%if %{build21}
# ruby-21
build_for 2.1
%endif
%if %{build22}
# ruby-22
build_for 2.2
%endif
%if %{build23}
# ruby-23
build_for 2.3
%endif
%if %{build24}
# ruby-24
build_for 2.4
%endif

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

install_for() {
    ruby_ver=$1
    bindir="/usr/ruby/${ruby_ver}/bin"
    gemdir="$(${bindir}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    mkdir -p %{buildroot}/usr/ruby/${ruby_ver}
    cp -a ./usr/ruby/${ruby_ver}/* \
        %{buildroot}/usr/ruby/${ruby_ver}/

    for dir in %{buildroot}${geminstdir}/bin %{buildroot}%{_bindir}
    do
	if [ -d ${dir} ]
	then
	    pushd ${dir}
	    for i in ./*
	    do
		if [ -f ${i} ]
		then
		    mv ${i} ${i}.bak
		    sed -e "s!^\#\!/usr/bin/env ruby\$!\#\!/usr/ruby/${ruby_ver}/bin/ruby!" \
			-e "s!^\#\!/usr/bin/ruby\$!\#\!/usr/ruby/${ruby_ver}/bin/ruby!" \
			-e "s!^\#\!ruby\$!\#\!/usr/ruby/${ruby_ver}/bin/ruby!" \
			${i}.bak > ${i}
		    rm ${i}.bak
		fi
	    done
	    popd
	fi
    done
   
%if %{generate_executable}
    pushd %{buildroot}%{_bindir}
    for i in $(ls ../ruby/${ruby_ver}/bin/*)
    do
	[ -f ${i} ] && ln -s ${i} $(basename ${i})$(echo ${ruby_ver}|sed -e 's/\.//')
    done
    popd
%endif

}

%if %{build21}
# ruby-21
install_for 2.1
%endif
%if %{build22}
# ruby-22
install_for 2.2
%endif
%if %{build23}
# ruby-23
install_for 2.3
%endif
%if %{build24}
# ruby-24
install_for 2.4
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build21}
%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*21
%endif
%endif
%if %{build22}
%files 22
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*22
%endif
%endif
%if %{build23}
%files 23
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.3
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*23
%endif
%endif
%if %{build24}
%files 24
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.4
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*24
%endif
%endif

%changelog
* Wed Dec 21 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.18
- obsolete ruby-19 and ruby-20
- generate package for ruby-24
* Mon Apr 18 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.17
* Sun Dec 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.15 and build package for ruby-23
* Sun Nov 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.14
* Tue Mar 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.7 and generate package for ruby-22
* Mon Apr 21 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
