%include Solaris.inc
%include default-depend.inc

%define build24jposug %( if [ -x /opt/jposug/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build25jposug %( if [ -x /opt/jposug/ruby/2.5/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build26jposug %( if [ -x /opt/jposug/ruby/2.6/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build27jposug %( if [ -x /opt/jposug/ruby/2.7/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 0

%define gemname gratan
%define sfe_gemname gratan

# Gratan is a tool to manage MySQL permissions using Ruby DSL.

Summary:          Gratan is a tool to manage MySQL permissions using Ruby DSL.
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          0.3.2
License:          MIT
URL:              http://gratan.codenize.tools/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Gratan is a tool to manage MySQL permissions using Ruby DSL.

%if %{build24jposug}

%package 24jposug
IPS_package_name: jposug/library/ruby/%{gemname}-24jposug
Summary:          Gratan is a tool to manage MySQL permissions using Ruby DSL.
BuildRequires:    jposug/runtime/ruby-24jposug = *
Requires:         jposug/runtime/ruby-24jposug = *
# deep_merge >= 0
Requires:         jposug/library/ruby/deep_merge-24jposug
# hashie >= 0
Requires:         jposug/library/ruby/hashie-24jposug
# mysql2 >= 0
Requires:         jposug/library/ruby/mysql2-24jposug
# term-ansicolor >= 0
Requires:         jposug/library/ruby/term-ansicolor-24jposug
# Requires:         library/ruby/%{gemname}

%description 24jposug
Gratan is a tool to manage MySQL permissions using Ruby DSL.
%endif

%if %{build25jposug}

%package 25jposug
IPS_package_name: jposug/library/ruby/%{gemname}-25jposug
Summary:          Gratan is a tool to manage MySQL permissions using Ruby DSL.
BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
# deep_merge >= 0
Requires:         jposug/library/ruby/deep_merge-25jposug
# hashie >= 0
Requires:         jposug/library/ruby/hashie-25jposug
# mysql2 >= 0
Requires:         jposug/library/ruby/mysql2-25jposug
# term-ansicolor >= 0
Requires:         jposug/library/ruby/term-ansicolor-25jposug
# Requires:         library/ruby/%{gemname}

%description 25jposug
Gratan is a tool to manage MySQL permissions using Ruby DSL.
%endif

%if %{build26jposug}

%package 26jposug
IPS_package_name: jposug/library/ruby/%{gemname}-26jposug
Summary:          Gratan is a tool to manage MySQL permissions using Ruby DSL.
BuildRequires:    jposug/runtime/ruby-26jposug = *
Requires:         jposug/runtime/ruby-26jposug = *
# deep_merge >= 0
Requires:         jposug/library/ruby/deep_merge-26jposug
# hashie >= 0
Requires:         jposug/library/ruby/hashie-26jposug
# mysql2 >= 0
Requires:         jposug/library/ruby/mysql2-26jposug
# term-ansicolor >= 0
Requires:         jposug/library/ruby/term-ansicolor-26jposug
# Requires:         library/ruby/%{gemname}

%description 26jposug
Gratan is a tool to manage MySQL permissions using Ruby DSL.
%endif

%if %{build27jposug}

%package 27jposug
IPS_package_name: jposug/library/ruby/%{gemname}-27jposug
Summary:          Gratan is a tool to manage MySQL permissions using Ruby DSL.
BuildRequires:    jposug/runtime/ruby-27jposug = *
Requires:         jposug/runtime/ruby-27jposug = *
# deep_merge >= 0
Requires:         jposug/library/ruby/deep_merge-27jposug
# hashie >= 0
Requires:         jposug/library/ruby/hashie-27jposug
# mysql2 >= 0
Requires:         jposug/library/ruby/mysql2-27jposug
# term-ansicolor >= 0
Requires:         jposug/library/ruby/term-ansicolor-27jposug
# Requires:         library/ruby/%{gemname}

%description 27jposug
Gratan is a tool to manage MySQL permissions using Ruby DSL.
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
* Sun Oct 27 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.2
* Sun Mar 04 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
