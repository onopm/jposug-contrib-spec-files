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

%define gemname virtus
%define sfe_gemname virtus

# Attributes on Steroids for Plain Old Ruby Objects

Summary:          Attributes on Steroids for Plain Old Ruby Objects
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          1.0.5
License:          MIT
URL:              https://github.com/solnic/virtus
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Attributes on Steroids for Plain Old Ruby Objects

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# Requires:         library/ruby/%{gemname}-21

%description 21-old
Attributes on Steroids for Plain Old Ruby Objects
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# axiom-types ~> 0.1
Requires:         library/ruby/axiom-types-21
# coercible ~> 1.0
Requires:         library/ruby/coercible-21
# descendants_tracker >= 0.0.3, ~> 0.0
Requires:         library/ruby/descendants_tracker-21
# equalizer >= 0.0.9, ~> 0.0
Requires:         library/ruby/equalizer-21
# Requires:         library/ruby/%{gemname}

%description 21
Attributes on Steroids for Plain Old Ruby Objects
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# Requires:         library/ruby/%{gemname}-22

%description 22-old
Attributes on Steroids for Plain Old Ruby Objects
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# axiom-types ~> 0.1
Requires:         library/ruby/axiom-types-22
# coercible ~> 1.0
Requires:         library/ruby/coercible-22
# descendants_tracker >= 0.0.3, ~> 0.0
Requires:         library/ruby/descendants_tracker-22
# equalizer >= 0.0.9, ~> 0.0
Requires:         library/ruby/equalizer-22
# Requires:         library/ruby/%{gemname}

%description 22
Attributes on Steroids for Plain Old Ruby Objects
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# Requires:         library/ruby/%{gemname}-23

%description 23-old
Attributes on Steroids for Plain Old Ruby Objects
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# axiom-types ~> 0.1
Requires:         library/ruby/axiom-types-23
# coercible ~> 1.0
Requires:         library/ruby/coercible-23
# descendants_tracker >= 0.0.3, ~> 0.0
Requires:         library/ruby/descendants_tracker-23
# equalizer >= 0.0.9, ~> 0.0
Requires:         library/ruby/equalizer-23
# Requires:         library/ruby/%{gemname}

%description 23
Attributes on Steroids for Plain Old Ruby Objects
%endif

%if %{build23jposug}

%package 23jposug
IPS_package_name: jposug/library/ruby/%{gemname}-23jposug
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    jposug/runtime/ruby-23jposug = *
Requires:         jposug/runtime/ruby-23jposug = *
# axiom-types ~> 0.1
Requires:         jposug/library/ruby/axiom-types-23jposug
# coercible ~> 1.0
Requires:         jposug/library/ruby/coercible-23jposug
# descendants_tracker >= 0.0.3, ~> 0.0
Requires:         jposug/library/ruby/descendants_tracker-23jposug
# equalizer >= 0.0.9, ~> 0.0
Requires:         jposug/library/ruby/equalizer-23jposug
# Requires:         library/ruby/%{gemname}

%description 23jposug
Attributes on Steroids for Plain Old Ruby Objects
%endif

%if %{build24jposug}

%package 24jposug
IPS_package_name: jposug/library/ruby/%{gemname}-24jposug
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    jposug/runtime/ruby-24jposug = *
Requires:         jposug/runtime/ruby-24jposug = *
# axiom-types ~> 0.1
Requires:         jposug/library/ruby/axiom-types-24jposug
# coercible ~> 1.0
Requires:         jposug/library/ruby/coercible-24jposug
# descendants_tracker >= 0.0.3, ~> 0.0
Requires:         jposug/library/ruby/descendants_tracker-24jposug
# equalizer >= 0.0.9, ~> 0.0
Requires:         jposug/library/ruby/equalizer-24jposug
# Requires:         library/ruby/%{gemname}

%description 24jposug
Attributes on Steroids for Plain Old Ruby Objects
%endif

%if %{build25jposug}

%package 25jposug
IPS_package_name: jposug/library/ruby/%{gemname}-25jposug
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
# axiom-types ~> 0.1
Requires:         jposug/library/ruby/axiom-types-25jposug
# coercible ~> 1.0
Requires:         jposug/library/ruby/coercible-25jposug
# descendants_tracker >= 0.0.3, ~> 0.0
Requires:         jposug/library/ruby/descendants_tracker-25jposug
# equalizer >= 0.0.9, ~> 0.0
Requires:         jposug/library/ruby/equalizer-25jposug
# Requires:         library/ruby/%{gemname}

%description 25jposug
Attributes on Steroids for Plain Old Ruby Objects
%endif

%if %{build26jposug}

%package 26jposug
IPS_package_name: jposug/library/ruby/%{gemname}-26jposug
Summary:          Attributes on Steroids for Plain Old Ruby Objects
BuildRequires:    jposug/runtime/ruby-26jposug = *
Requires:         jposug/runtime/ruby-26jposug = *
# axiom-types ~> 0.1
Requires:         jposug/library/ruby/axiom-types-26jposug
# coercible ~> 1.0
Requires:         jposug/library/ruby/coercible-26jposug
# descendants_tracker >= 0.0.3, ~> 0.0
Requires:         jposug/library/ruby/descendants_tracker-26jposug
# equalizer >= 0.0.9, ~> 0.0
Requires:         jposug/library/ruby/equalizer-26jposug
# Requires:         library/ruby/%{gemname}

%description 26jposug
Attributes on Steroids for Plain Old Ruby Objects
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
