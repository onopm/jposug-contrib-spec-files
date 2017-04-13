%include Solaris.inc
%include default-depend.inc

%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24 %( if [ -x /usr/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 0

%define gemname i18n
%define sfe_gemname i18n

Summary:          New wave Internationalization support for Ruby.
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          0.8.1
License:          MIT
URL:              http://github.com/svenfuchs/i18n
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
New wave Internationalization support for Ruby.

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          New wave Internationalization support for Ruby.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
New wave Internationalization support for Ruby.
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          New wave Internationalization support for Ruby.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}

%description 21
New wave Internationalization support for Ruby.
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          New wave Internationalization support for Ruby.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
New wave Internationalization support for Ruby.
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          New wave Internationalization support for Ruby.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}

%description 22
New wave Internationalization support for Ruby.
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          New wave Internationalization support for Ruby.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}-23

%description 23-old
New wave Internationalization support for Ruby.
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          New wave Internationalization support for Ruby.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}

%description 23
New wave Internationalization support for Ruby.
%endif

%if %{build24}

%package 24
IPS_package_name: library/ruby/%{gemname}-24
Summary:          New wave Internationalization support for Ruby.
BuildRequires:    runtime/ruby-24 = *
Requires:         runtime/ruby-24 = *
Requires:         library/ruby/%{gemname}

%description 24
New wave Internationalization support for Ruby.
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

    rm -r .${gemdir}/cache
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
* Thu Apr 13 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.8.1 and package for ruby-24 is added, for ruby-19 and ruby-20 are obsolete
* Thu May 05 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.0
* Tue May 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
