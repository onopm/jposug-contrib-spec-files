%include Solaris.inc
%include default-depend.inc

%define build19 %( if [ -x /usr/ruby/1.9/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build20 %( if [ -x /usr/ruby/2.0/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 1

%define gemname infrataster
%define sfe_gemname infrataster

Summary:          Infrastructure Behavior Testing Framework
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          0.3.2
License:          MIT
URL:              https://github.com/ryotarai/infrataster
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
Infrastructure Behavior Testing Framework

%if %{build19}
%if %{keep_dependency}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# capybara >= 0
Requires:         library/ruby/capybara-19
# faraday >= 0
Requires:         library/ruby/faraday-19
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-19
# net-ssh >= 0
Requires:         library/ruby/net-ssh-19
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-19
# poltergeist >= 0
Requires:         library/ruby/poltergeist-19
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-19
# thor >= 0
Requires:         library/ruby/thor-19
Requires:         library/ruby/%{gemname}-19

%description 19-old
Infrastructure Behavior Testing Framework
%endif

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# capybara >= 0
Requires:         library/ruby/capybara-19
# faraday >= 0
Requires:         library/ruby/faraday-19
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-19
# net-ssh >= 0
Requires:         library/ruby/net-ssh-19
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-19
# poltergeist >= 0
Requires:         library/ruby/poltergeist-19
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-19
# thor >= 0
Requires:         library/ruby/thor-19

%description 19
Infrastructure Behavior Testing Framework
%endif

%if %{build20}
%if %{keep_dependency}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# capybara >= 0
Requires:         library/ruby/capybara-20
# faraday >= 0
Requires:         library/ruby/faraday-20
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-20
# net-ssh >= 0
Requires:         library/ruby/net-ssh-20
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-20
# poltergeist >= 0
Requires:         library/ruby/poltergeist-20
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-20
# thor >= 0
Requires:         library/ruby/thor-20
Requires:         library/ruby/%{gemname}-20

%description 20-old
Infrastructure Behavior Testing Framework
%endif

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# capybara >= 0
Requires:         library/ruby/capybara-20
# faraday >= 0
Requires:         library/ruby/faraday-20
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-20
# net-ssh >= 0
Requires:         library/ruby/net-ssh-20
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-20
# poltergeist >= 0
Requires:         library/ruby/poltergeist-20
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-20
# thor >= 0
Requires:         library/ruby/thor-20

%description 20
Infrastructure Behavior Testing Framework
%endif

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# capybara >= 0
Requires:         library/ruby/capybara-21
# faraday >= 0
Requires:         library/ruby/faraday-21
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-21
# net-ssh >= 0
Requires:         library/ruby/net-ssh-21
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-21
# poltergeist >= 0
Requires:         library/ruby/poltergeist-21
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-21
# thor >= 0
Requires:         library/ruby/thor-21
Requires:         library/ruby/%{gemname}-21

%description 21-old
Infrastructure Behavior Testing Framework
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# capybara >= 0
Requires:         library/ruby/capybara-21
# faraday >= 0
Requires:         library/ruby/faraday-21
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-21
# net-ssh >= 0
Requires:         library/ruby/net-ssh-21
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-21
# poltergeist >= 0
Requires:         library/ruby/poltergeist-21
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-21
# thor >= 0
Requires:         library/ruby/thor-21

%description 21
Infrastructure Behavior Testing Framework
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# capybara >= 0
Requires:         library/ruby/capybara-22
# faraday >= 0
Requires:         library/ruby/faraday-22
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-22
# net-ssh >= 0
Requires:         library/ruby/net-ssh-22
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-22
# poltergeist >= 0
Requires:         library/ruby/poltergeist-22
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-22
# thor >= 0
Requires:         library/ruby/thor-22
Requires:         library/ruby/%{gemname}-22

%description 22-old
Infrastructure Behavior Testing Framework
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# capybara >= 0
Requires:         library/ruby/capybara-22
# faraday >= 0
Requires:         library/ruby/faraday-22
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-22
# net-ssh >= 0
Requires:         library/ruby/net-ssh-22
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-22
# poltergeist >= 0
Requires:         library/ruby/poltergeist-22
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-22
# thor >= 0
Requires:         library/ruby/thor-22

%description 22
Infrastructure Behavior Testing Framework
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# capybara >= 0
Requires:         library/ruby/capybara-23
# faraday >= 0
Requires:         library/ruby/faraday-23
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-23
# net-ssh >= 0
Requires:         library/ruby/net-ssh-23
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-23
# poltergeist >= 0
Requires:         library/ruby/poltergeist-23
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-23
# thor >= 0
Requires:         library/ruby/thor-23
Requires:         library/ruby/%{gemname}-23

%description 23-old
Infrastructure Behavior Testing Framework
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          Infrastructure Behavior Testing Framework
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# capybara >= 0
Requires:         library/ruby/capybara-23
# faraday >= 0
Requires:         library/ruby/faraday-23
# faraday_middleware >= 0.10.0
Requires:         library/ruby/faraday_middleware-23
# net-ssh >= 0
Requires:         library/ruby/net-ssh-23
# net-ssh-gateway >= 0
Requires:         library/ruby/net-ssh-gateway-23
# poltergeist >= 0
Requires:         library/ruby/poltergeist-23
# rspec < 4.0, >= 2.0
Requires:         library/ruby/rspec-23
# thor >= 0
Requires:         library/ruby/thor-23

%description 23
Infrastructure Behavior Testing Framework
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

%if %{build19}
# ruby-19
build_for 1.9
%endif

%if %{build20}
# ruby-20
build_for 2.0
%endif

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

%if %{build19}
# ruby-19
install_for 1.9
%endif

%if %{build20}
install_for 2.0
%endif

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

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build19}
%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*19
%endif
%endif

%if %{build20}
%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*20
%endif
%endif

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

%changelog
* Sun Dec 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.2 and build package for ruby-23
* Fri Nov 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.1
* Mon Aug 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.0
* Tue Jun 16 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.6
* Fri Mar 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.5
* Sun Jan 18 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.1
* Sat Jan 17 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-22
* Tue Jul 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
