%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0
%define keep_dependency 1

%define gemname hiera
%define sfe_gemname hiera

%if %{build19}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%endif

%if %{build20}
%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%endif

%if %{build21}
%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}
%endif

%if %{build22}
%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}
%endif

Summary:          A pluggable data store for hierarcical data
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          3.0.1
License:          Apache License 2.0
URL:              https://github.com/puppetlabs/hiera
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
A pluggable data store for hierarcical data

%if %{build19}
%if %{keep_dependency}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# json_pure >= 0
Requires:         library/ruby/%{gemname}-19

%description 19-old
A pluggable data store for hierarcical data
%endif

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# json_pure >= 0
Requires:         library/ruby/json_pure-19

%description 19
A pluggable data store for hierarcical data
%endif

%if %{build20}
%if %{keep_dependency}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# json_pure >= 0
Requires:         library/ruby/%{gemname}-20

%description 20-old
A pluggable data store for hierarcical data
%endif

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# json_pure >= 0
Requires:         library/ruby/json_pure-20

%description 20
A pluggable data store for hierarcical data
%endif

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# json_pure >= 0
Requires:         library/ruby/%{gemname}-21

%description 21-old
A pluggable data store for hierarcical data
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# json_pure >= 0
Requires:         library/ruby/json_pure-21

%description 21
A pluggable data store for hierarcical data
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# json_pure >= 0
Requires:         library/ruby/%{gemname}-22

%description 22-old
A pluggable data store for hierarcical data
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          A pluggable data store for hierarcical data
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# json_pure >= 0
Requires:         library/ruby/json_pure-22

%description 22
A pluggable data store for hierarcical data
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
install_for 2.2
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

%changelog
* Sat Nov 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.0.1
* Thu May 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.0
* Fri Mar 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-22
* Wed Jun 11 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.4
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18
* Thu May 29 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.3
* Thu Feb 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.2 and generate package for ruby-21
* Wed Jan 29 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.1
* Wed Jan 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Thu Sep 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1
* Thu Jan 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix path in %define gemdir18 and gemdir19
* Thu Dec 20 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use full path in %define gemdir18 and gemdir19
- add BuildRequires
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
