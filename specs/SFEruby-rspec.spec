%include Solaris.inc
%include default-depend.inc

%define build19 %( if [ -x /usr/ruby/1.9/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build20 %( if [ -x /usr/ruby/2.0/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 1

%define gemname rspec
%define sfe_gemname rspec

Summary:          BDD for Ruby
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          3.4.0
License:          MIT
URL:              http://github.com/rspec
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
BDD for Ruby

%if %{build19}
%if %{keep_dependency}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19-old
BDD for Ruby
%endif

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# rspec-core ~> 3.4.0
Requires:         library/ruby/rspec-core-19
# rspec-expectations ~> 3.4.0
Requires:         library/ruby/rspec-expectations-19
# rspec-mocks ~> 3.4.0
Requires:         library/ruby/rspec-mocks-19
Requires:         library/ruby/%{gemname}

%description 19
BDD for Ruby
%endif

%if %{build20}
%if %{keep_dependency}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20-old
BDD for Ruby
%endif

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# rspec-core ~> 3.4.0
Requires:         library/ruby/rspec-core-20
# rspec-expectations ~> 3.4.0
Requires:         library/ruby/rspec-expectations-20
# rspec-mocks ~> 3.4.0
Requires:         library/ruby/rspec-mocks-20
Requires:         library/ruby/%{gemname}

%description 20
BDD for Ruby
%endif

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
BDD for Ruby
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# rspec-core ~> 3.4.0
Requires:         library/ruby/rspec-core-21
# rspec-expectations ~> 3.4.0
Requires:         library/ruby/rspec-expectations-21
# rspec-mocks ~> 3.4.0
Requires:         library/ruby/rspec-mocks-21
Requires:         library/ruby/%{gemname}

%description 21
BDD for Ruby
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
BDD for Ruby
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# rspec-core ~> 3.4.0
Requires:         library/ruby/rspec-core-22
# rspec-expectations ~> 3.4.0
Requires:         library/ruby/rspec-expectations-22
# rspec-mocks ~> 3.4.0
Requires:         library/ruby/rspec-mocks-22
Requires:         library/ruby/%{gemname}

%description 22
BDD for Ruby
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}-23

%description 23-old
BDD for Ruby
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          BDD for Ruby
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# rspec-core ~> 3.4.0
Requires:         library/ruby/rspec-core-23
# rspec-expectations ~> 3.4.0
Requires:         library/ruby/rspec-expectations-23
# rspec-mocks ~> 3.4.0
Requires:         library/ruby/rspec-mocks-23

%description 23
BDD for Ruby
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
* Sun Dec 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.4.0
* Fri Jun 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.2.0
* Mon Oct 06 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.1.0
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.99.0
* Mon Jun 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18
* Wed Feb 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21
* Mon Sep 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.14.1
* Sun Mar 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.13.0
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
