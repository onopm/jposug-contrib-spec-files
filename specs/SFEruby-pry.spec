%include Solaris.inc
%include default-depend.inc

%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24 %( if [ -x /usr/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 1
%define keep_dependency 0

%define gemname pry
%define sfe_gemname pry

Summary:          An IRB alternative and runtime developer console
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          0.10.4
License:          MIT
URL:              http://pryrepl.org
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
An IRB alternative and runtime developer console

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          An IRB alternative and runtime developer console
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
An IRB alternative and runtime developer console
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          An IRB alternative and runtime developer console
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# coderay ~> 1.1.0
Requires:         library/ruby/coderay-21
# method_source ~> 0.8.1
Requires:         library/ruby/method_source-21
# slop ~> 3.4
Requires:         library/ruby/slop-21
Requires:         library/ruby/%{gemname}

%description 21
An IRB alternative and runtime developer console
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          An IRB alternative and runtime developer console
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
An IRB alternative and runtime developer console
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          An IRB alternative and runtime developer console
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# coderay ~> 1.1.0
Requires:         library/ruby/coderay-22
# method_source ~> 0.8.1
Requires:         library/ruby/method_source-22
# slop ~> 3.4
Requires:         library/ruby/slop-22
Requires:         library/ruby/%{gemname}

%description 22
An IRB alternative and runtime developer console
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          An IRB alternative and runtime developer console
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}-23

%description 23-old
An IRB alternative and runtime developer console
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          An IRB alternative and runtime developer console
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# coderay ~> 1.1.0
Requires:         library/ruby/coderay-23
# method_source ~> 0.8.1
Requires:         library/ruby/method_source-23
# slop ~> 3.4
Requires:         library/ruby/slop-23
Requires:         library/ruby/%{gemname}

%description 23
An IRB alternative and runtime developer console
%endif

%if %{build24}

%package 24
IPS_package_name: library/ruby/%{gemname}-24
Summary:          An IRB alternative and runtime developer console
BuildRequires:    runtime/ruby-24 = *
Requires:         runtime/ruby-24 = *
# coderay ~> 1.1.0
Requires:         library/ruby/coderay-24
# method_source ~> 0.8.1
Requires:         library/ruby/method_source-24
# slop ~> 3.4
Requires:         library/ruby/slop-24
Requires:         library/ruby/%{gemname}

%description 24
An IRB alternative and runtime developer console
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
* Mon Dec 05 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.4 and build packge for ruby-24
* Tue Dec 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.3 and build packge for ruby-23
* Sat Jun 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update specfile based on bin/make_rubygem_spec.rb
- require slop-3 instead of slop which version is over 4.0
* Wed Dec 24 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21 instead of ruby-18
- add symbolic links
- bump to 0.10.1
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.12.2
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
