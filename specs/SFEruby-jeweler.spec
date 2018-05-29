%include Solaris.inc
%include default-depend.inc

%define build19 %( if [ -x /usr/ruby/1.9/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build20 %( if [ -x /usr/ruby/2.0/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 1

%define gemname jeweler
%define sfe_gemname jeweler

Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.0.1
License:          MIT
URL:              http://github.com/technicalpickles/jeweler
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
Simple and opinionated helper for creating Rubygem projects on GitHub

%if %{build19}
%if %{keep_dependency}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# builder >= 0
Requires:         library/ruby/builder-19
# bundler >= 1.0
Requires:         library/ruby/bundler-19
# git >= 1.2.5
Requires:         library/ruby/git-19
# github_api >= 0
Requires:         library/ruby/github_api-19
# highline >= 1.6.15
Requires:         library/ruby/highline-19
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-19
Requires:         library/ruby/%{gemname}-19

%description 19-old
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# builder >= 0
Requires:         library/ruby/builder-19
# bundler >= 1.0
Requires:         library/ruby/bundler-19
# git >= 1.2.5
Requires:         library/ruby/git-19
# github_api >= 0
Requires:         library/ruby/github_api-19
# highline >= 1.6.15
Requires:         library/ruby/highline-19
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-19

%description 19
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%if %{build20}
%if %{keep_dependency}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# builder >= 0
Requires:         library/ruby/builder-20
# bundler >= 1.0
Requires:         library/ruby/bundler-20
# git >= 1.2.5
Requires:         library/ruby/git-20
# github_api >= 0
Requires:         library/ruby/github_api-20
# highline >= 1.6.15
Requires:         library/ruby/highline-20
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-20
Requires:         library/ruby/%{gemname}-20

%description 20-old
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# builder >= 0
Requires:         library/ruby/builder-20
# bundler >= 1.0
Requires:         library/ruby/bundler-20
# git >= 1.2.5
Requires:         library/ruby/git-20
# github_api >= 0
Requires:         library/ruby/github_api-20
# highline >= 1.6.15
Requires:         library/ruby/highline-20
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-20

%description 20
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# builder >= 0
Requires:         library/ruby/builder-21
# bundler >= 1.0
Requires:         library/ruby/bundler-21
# git >= 1.2.5
Requires:         library/ruby/git-21
# github_api >= 0
Requires:         library/ruby/github_api-21
# highline >= 1.6.15
Requires:         library/ruby/highline-21
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-21
Requires:         library/ruby/%{gemname}-21

%description 21-old
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# builder >= 0
Requires:         library/ruby/builder-21
# bundler >= 1.0
Requires:         library/ruby/bundler-21
# git >= 1.2.5
Requires:         library/ruby/git-21
# github_api >= 0
Requires:         library/ruby/github_api-21
# highline >= 1.6.15
Requires:         library/ruby/highline-21
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-21

%description 21
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# builder >= 0
Requires:         library/ruby/builder-22
# bundler >= 1.0
Requires:         library/ruby/bundler-22
# git >= 1.2.5
Requires:         library/ruby/git-22
# github_api >= 0
Requires:         library/ruby/github_api-22
# highline >= 1.6.15
Requires:         library/ruby/highline-22
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-22
Requires:         library/ruby/%{gemname}-22

%description 22-old
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# builder >= 0
Requires:         library/ruby/builder-22
# bundler >= 1.0
Requires:         library/ruby/bundler-22
# git >= 1.2.5
Requires:         library/ruby/git-22
# github_api >= 0
Requires:         library/ruby/github_api-22
# highline >= 1.6.15
Requires:         library/ruby/highline-22
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-22

%description 22
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# builder >= 0
Requires:         library/ruby/builder-23
# bundler >= 1.0
Requires:         library/ruby/bundler-23
# git >= 1.2.5
Requires:         library/ruby/git-23
# github_api >= 0
Requires:         library/ruby/github_api-23
# highline >= 1.6.15
Requires:         library/ruby/highline-23
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-23
Requires:         library/ruby/%{gemname}-23

%description 23-old
Simple and opinionated helper for creating Rubygem projects on GitHub
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          Simple and opinionated helper for creating Rubygem projects on GitHub
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# builder >= 0
Requires:         library/ruby/builder-23
# bundler >= 1.0
Requires:         library/ruby/bundler-23
# git >= 1.2.5
Requires:         library/ruby/git-23
# github_api >= 0
Requires:         library/ruby/github_api-23
# highline >= 1.6.15
Requires:         library/ruby/highline-23
# nokogiri >= 1.5.10
Requires:         library/ruby/nokogiri-23

%description 23
Simple and opinionated helper for creating Rubygem projects on GitHub
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
- use rake and rdoc included in runtime/ruby-*
* Sun Dec 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.1 and build packages for ruby-22 and ruby-23
* Wed Dec 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not generate package for ruby-18 and generate package for ruby-21 and ruby-20
* Wed Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
