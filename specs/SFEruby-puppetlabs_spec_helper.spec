%include Solaris.inc
%include default-depend.inc

%define build19 %( if [ -x /usr/ruby/1.9/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build20 %( if [ -x /usr/ruby/2.0/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 1

%define gemname puppetlabs_spec_helper
%define sfe_gemname puppet-spec-helper

Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
Name:             ruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          1.0.1
License:          Apache-2.0
URL:              http://github.com/puppetlabs/puppetlabs_spec_helper
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules

%if %{build19}
%if %{keep_dependency}
%package 19old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19old
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# mocha >= 0
Requires:         library/ruby/mocha-19
# puppet-lint >= 0
Requires:         library/ruby/puppet-lint-19
# puppet-syntax >= 0
Requires:         library/ruby/puppet-syntax-19
# rspec-puppet >= 0
Requires:         library/ruby/rspec-puppet-19
Requires:         library/ruby/%{gemname}

%description 19
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%if %{build20}
%if %{keep_dependency}
%package 20old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20old
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# mocha >= 0
Requires:         library/ruby/mocha-20
# puppet-lint >= 0
Requires:         library/ruby/puppet-lint-20
# puppet-syntax >= 0
Requires:         library/ruby/puppet-syntax-20
# rspec-puppet >= 0
Requires:         library/ruby/rspec-puppet-20
Requires:         library/ruby/%{gemname}

%description 20
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%if %{build21}
%if %{keep_dependency}
%package 21old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21old
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# mocha >= 0
Requires:         library/ruby/mocha-21
# puppet-lint >= 0
Requires:         library/ruby/puppet-lint-21
# puppet-syntax >= 0
Requires:         library/ruby/puppet-syntax-21
# rspec-puppet >= 0
Requires:         library/ruby/rspec-puppet-21
Requires:         library/ruby/%{gemname}

%description 21
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%if %{build22}
%if %{keep_dependency}
%package 22old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22old
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# mocha >= 0
Requires:         library/ruby/mocha-22
# puppet-lint >= 0
Requires:         library/ruby/puppet-lint-22
# puppet-syntax >= 0
Requires:         library/ruby/puppet-syntax-22
# rspec-puppet >= 0
Requires:         library/ruby/rspec-puppet-22
Requires:         library/ruby/%{gemname}

%description 22
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%if %{build23}
%if %{keep_dependency}
%package 23old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# mocha >= 0
Requires:         library/ruby/mocha-23
# puppet-lint >= 0
Requires:         library/ruby/puppet-lint-23
# puppet-syntax >= 0
Requires:         library/ruby/puppet-syntax-23
# rspec-puppet >= 0
Requires:         library/ruby/rspec-puppet-23
Requires:         library/ruby/%{gemname}-23

%description 23old
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# mocha >= 0
Requires:         library/ruby/mocha-23
# puppet-lint >= 0
Requires:         library/ruby/puppet-lint-23
# puppet-syntax >= 0
Requires:         library/ruby/puppet-syntax-23
# rspec-puppet >= 0
Requires:         library/ruby/rspec-puppet-23

%description 23
Contains rake tasks and a standard spec_helper for running spec tests on puppet modules
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
* Tue Dec 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build package for ruby-23
* Sun Nov 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.1
* Mon Sep 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
