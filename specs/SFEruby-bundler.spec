%include Solaris.inc
%include default-depend.inc

%define build24jposug %( if [ -x /opt/jposug/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build25jposug %( if [ -x /opt/jposug/ruby/2.5/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build26jposug %( if [ -x /opt/jposug/ruby/2.6/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build27jposug %( if [ -x /opt/jposug/ruby/2.7/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 0

%define gemname bundler
%define sfe_gemname bundler

# Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably

Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.0.2
License:          MIT
URL:              https://bundler.io/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably

%if %{build24jposug}

%package 24jposug
IPS_package_name: jposug/library/ruby/%{gemname}-24jposug
Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
BuildRequires:    jposug/runtime/ruby-24jposug = *
Requires:         jposug/runtime/ruby-24jposug = *
# Requires:         library/ruby/%{gemname}

%description 24jposug
Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
%endif

%if %{build25jposug}

%package 25jposug
IPS_package_name: jposug/library/ruby/%{gemname}-25jposug
Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
# Requires:         library/ruby/%{gemname}

%description 25jposug
Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
%endif

%if %{build26jposug}

%package 26jposug
IPS_package_name: jposug/library/ruby/%{gemname}-26jposug
Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
BuildRequires:    jposug/runtime/ruby-26jposug = *
Requires:         jposug/runtime/ruby-26jposug = *
# Requires:         library/ruby/%{gemname}

%description 26jposug
Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
%endif

%if %{build27jposug}

%package 27jposug
IPS_package_name: jposug/library/ruby/%{gemname}-27jposug
Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
BuildRequires:    jposug/runtime/ruby-27jposug = *
Requires:         jposug/runtime/ruby-27jposug = *
# Requires:         library/ruby/%{gemname}

%description 27jposug
Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
%endif


%prep
%setup -q -c -T

%build
build_for() {
    if [ "x${1}" = 'x2.7jposug' -o "x${1}" = 'x2.6jposug' -o "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
    then
        ruby_ver=$(echo $1 | sed -e 's/jposug//')
        bindir="/opt/jposug/ruby/${ruby_ver}/bin"
    else
        ruby_ver=$1
        bindir="/usr/ruby/${ruby_ver}/bin"
    fi
    gemdir="$(${bindir}/ruby -r rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    ${bindir}/gem install --local \
        --no-env-shebang \
        --no-document \
        --install-dir .${gemdir} \
        --bindir .${bindir} \
        -V \
        --force %{SOURCE0}
}

%if %{build24jposug}
# ruby-24jposug
build_for 2.4jposug
%endif
%if %{build25jposug}
# ruby-25jposug
build_for 2.5jposug
%endif
%if %{build26jposug}
# ruby-26jposug
build_for 2.6jposug
%endif
%if %{build27jposug}
# ruby-27jposug
build_for 2.7jposug
%endif

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

install_for() {
    if [ "x${1}" = 'x2.7jposug' -o "x${1}" = 'x2.6jposug' -o "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
    then
        ruby_ver=$(echo $1 | sed -e 's/jposug//')
        dir_prefix="/opt/jposug/ruby/${ruby_ver}"
        dir_prefix_relative="../../opt/jposug/ruby/${ruby_ver}"
        jposug='jposug'
    else
        ruby_ver=$1
        dir_prefix="/usr/ruby/${ruby_ver}"
        dir_prefix_relative="../ruby/${ruby_ver}"
        jposug=''
    fi
    bindir="${dir_prefix}/bin"
    gemdir="$(${bindir}/ruby -r rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    mkdir -p %{buildroot}${dir_prefix}
    cp -a .${dir_prefix}/* \
        %{buildroot}/${dir_prefix}/

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
		    sed -e "s!^\#\!/usr/bin/env ruby\$!\#\!${bindir}/ruby!" \
			-e "s!^\#\!/usr/bin/ruby\$!\#\!${bindir}/ruby!" \
			-e "s!^\#\!ruby\$!\#\!${bindir}/ruby!" \
			${i}.bak > ${i}
		    rm ${i}.bak
		fi
	    done
	    popd
	fi
    done

    [ -d %{buildroot}${geminstdir}/test ] && rm -rf %{buildroot}${geminstdir}/test || true

%if %{generate_executable}
    pushd %{buildroot}%{_bindir}
    for i in $(ls ${dir_prefix_relative}/bin/*)
    do
	[ -f ${i} ] && ln -s ${i} $(basename ${i})$(echo ${ruby_ver}|sed -e 's/\.//')${jposug}
    done
    popd
%endif

}

%if %{build24jposug}
install_for 2.4jposug
%endif
%if %{build25jposug}
install_for 2.5jposug
%endif
%if %{build26jposug}
install_for 2.6jposug
%endif
%if %{build27jposug}
install_for 2.7jposug
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build24jposug}
%files 24jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.4
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*24jposug
%endif
%endif

%if %{build25jposug}
%files 25jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.5
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*25jposug
%endif
%endif

%if %{build26jposug}
%files 26jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.6
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*26jposug
%endif
%endif

%if %{build27jposug}
%files 27jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.7
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*27jposug
%endif
%endif


%changelog
* Thu Nov 07 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.2 and obsolete Ruby 2.3
* Tue Feb 12 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.1 and obsolete Ruby 2.1 and Ruby 2.2
* Mon Mar 05 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packages for ruby-26jposug
* Fri Dec 29 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.16.1 and build packages for ruby-2{3,4,5}jposug
* Fri May 06 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.12.2
* Wed Dec 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not generate package for ruby-18
- bump to 1.7.9
* Tue Feb 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21
* Wed Feb 19 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.3
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.5
* Sat Mar 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.4
* Mon Feb 04 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify to success building packages
* Thu Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
