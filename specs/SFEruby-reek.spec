%include Solaris.inc
%include default-depend.inc

%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23jposug %( if [ -x /opt/jposug/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24jposug %( if [ -x /opt/jposug/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build25jposug %( if [ -x /opt/jposug/ruby/2.5/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build26jposug %( if [ -x /opt/jposug/ruby/2.6/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 0

%define gemname reek
%define sfe_gemname reek

# Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.

Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          4.8.1
License:          MIT
URL:              https://github.com/troessner/reek/wiki
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# Requires:         library/ruby/%{gemname}-21

%description 21-old
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# codeclimate-engine-rb ~> 0.4.0
Requires:         library/ruby/codeclimate-engine-rb-21
# parser < 2.6, >= 2.5.0.0
Requires:         library/ruby/parser-21
# rainbow < 4.0, >= 2.0
Requires:         library/ruby/rainbow-21
# Requires:         library/ruby/%{gemname}

%description 21
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# Requires:         library/ruby/%{gemname}-22

%description 22-old
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# codeclimate-engine-rb ~> 0.4.0
Requires:         library/ruby/codeclimate-engine-rb-22
# parser < 2.6, >= 2.5.0.0
Requires:         library/ruby/parser-22
# rainbow < 4.0, >= 2.0
Requires:         library/ruby/rainbow-22
# Requires:         library/ruby/%{gemname}

%description 22
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# Requires:         library/ruby/%{gemname}-23

%description 23-old
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# codeclimate-engine-rb ~> 0.4.0
Requires:         library/ruby/codeclimate-engine-rb-23
# parser < 2.6, >= 2.5.0.0
Requires:         library/ruby/parser-23
# rainbow < 4.0, >= 2.0
Requires:         library/ruby/rainbow-23
# Requires:         library/ruby/%{gemname}

%description 23
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%if %{build23jposug}

%package 23jposug
IPS_package_name: jposug/library/ruby/%{gemname}-23jposug
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    jposug/runtime/ruby-23jposug = *
Requires:         jposug/runtime/ruby-23jposug = *
# codeclimate-engine-rb ~> 0.4.0
Requires:         jposug/library/ruby/codeclimate-engine-rb-23jposug
# parser < 2.6, >= 2.5.0.0
Requires:         jposug/library/ruby/parser-23jposug
# rainbow < 4.0, >= 2.0
Requires:         jposug/library/ruby/rainbow-23jposug
# Requires:         library/ruby/%{gemname}

%description 23jposug
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%if %{build24jposug}

%package 24jposug
IPS_package_name: jposug/library/ruby/%{gemname}-24jposug
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    jposug/runtime/ruby-24jposug = *
Requires:         jposug/runtime/ruby-24jposug = *
# codeclimate-engine-rb ~> 0.4.0
Requires:         jposug/library/ruby/codeclimate-engine-rb-24jposug
# parser < 2.6, >= 2.5.0.0
Requires:         jposug/library/ruby/parser-24jposug
# rainbow < 4.0, >= 2.0
Requires:         jposug/library/ruby/rainbow-24jposug
# Requires:         library/ruby/%{gemname}

%description 24jposug
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%if %{build25jposug}

%package 25jposug
IPS_package_name: jposug/library/ruby/%{gemname}-25jposug
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
# codeclimate-engine-rb ~> 0.4.0
Requires:         jposug/library/ruby/codeclimate-engine-rb-25jposug
# parser < 2.6, >= 2.5.0.0
Requires:         jposug/library/ruby/parser-25jposug
# rainbow < 4.0, >= 2.0
Requires:         jposug/library/ruby/rainbow-25jposug
# Requires:         library/ruby/%{gemname}

%description 25jposug
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif

%if %{build26jposug}

%package 26jposug
IPS_package_name: jposug/library/ruby/%{gemname}-26jposug
Summary:          Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
BuildRequires:    jposug/runtime/ruby-26jposug = *
Requires:         jposug/runtime/ruby-26jposug = *
# codeclimate-engine-rb ~> 0.4.0
Requires:         jposug/library/ruby/codeclimate-engine-rb-26jposug
# parser < 2.6, >= 2.5.0.0
Requires:         jposug/library/ruby/parser-26jposug
# rainbow < 4.0, >= 2.0
Requires:         jposug/library/ruby/rainbow-26jposug
# Requires:         library/ruby/%{gemname}

%description 26jposug
Reek is a tool that examines Ruby classes, modules and methods and reports any code smells it finds.
%endif


%prep
%setup -q -c -T

%build
build_for() {
    if [ "x${1}" = 'x2.6jposug' -o "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
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
%if %{build23jposug}
# ruby-23jposug
build_for 2.3jposug
%endif
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

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

install_for() {
    if [ "x${1}" = 'x2.6jposug' -o "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
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

%if %{build21}
install_for 2.1
%endif
%if %{build22}
install_for 2.2
%endif
%if %{build23}
install_for 2.3
%endif
%if %{build23jposug}
install_for 2.3jposug
%endif
%if %{build24jposug}
install_for 2.4jposug
%endif
%if %{build25jposug}
install_for 2.5jposug
%endif
%if %{build26jposug}
install_for 2.6jposug
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

%if %{build23jposug}
%files 23jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.3
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*23jposug
%endif
%endif

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


%changelog
* Thu May 10 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
