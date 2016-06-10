%include Solaris.inc
%include default-depend.inc

%define build19 %( if [ -x /usr/ruby/1.9/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build20 %( if [ -x /usr/ruby/2.0/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 1

%define gemname specinfra
%define sfe_gemname specinfra

Summary:          Common layer for serverspec and itamae
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.59.0
License:          MIT
URL:              https://rubygems.org/gems/specinfra
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Common layer for serverspec and itamae

%if %{build19}
%if %{keep_dependency}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19-old
Common layer for serverspec and itamae
%endif

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# net-scp >= 0
Requires:         library/ruby/net-scp-19
# net-ssh < 3.1, >= 2.7
Requires:         library/ruby/net-ssh-19
# net-telnet >= 0
Requires:         library/ruby/net-telnet-19
# sfl >= 0
Requires:         library/ruby/sfl-19
Requires:         library/ruby/%{gemname}

%description 19
Common layer for serverspec and itamae
%endif

%if %{build20}
%if %{keep_dependency}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20-old
Common layer for serverspec and itamae
%endif

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# net-scp >= 0
Requires:         library/ruby/net-scp-20
# net-ssh < 3.1, >= 2.7
Requires:         library/ruby/net-ssh-20
# net-telnet >= 0
Requires:         library/ruby/net-telnet-20
# sfl >= 0
Requires:         library/ruby/sfl-20
Requires:         library/ruby/%{gemname}

%description 20
Common layer for serverspec and itamae
%endif

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
Common layer for serverspec and itamae
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# net-scp >= 0
Requires:         library/ruby/net-scp-21
# net-ssh < 3.1, >= 2.7
Requires:         library/ruby/net-ssh-21
# net-telnet >= 0
Requires:         library/ruby/net-telnet-21
# sfl >= 0
Requires:         library/ruby/sfl-21
Requires:         library/ruby/%{gemname}

%description 21
Common layer for serverspec and itamae
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
Common layer for serverspec and itamae
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# net-scp >= 0
Requires:         library/ruby/net-scp-22
# net-ssh < 3.1, >= 2.7
Requires:         library/ruby/net-ssh-22
# net-telnet >= 0
Requires:         library/ruby/net-telnet-22
# sfl >= 0
Requires:         library/ruby/sfl-22
Requires:         library/ruby/%{gemname}

%description 22
Common layer for serverspec and itamae
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}-23

%description 23-old
Common layer for serverspec and itamae
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# net-scp >= 0
Requires:         library/ruby/net-scp-23
# net-ssh < 3.1, >= 2.7
Requires:         library/ruby/net-ssh-23
# net-telnet >= 0
# Ruby 2.3.0 includes net-telnet 0.1.1
# Requires:         library/ruby/net-telnet-23
# sfl >= 0
Requires:         library/ruby/sfl-23

%description 23
Common layer for serverspec and itamae
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
* Fri Jun 10 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.59.0
* Mon May 23 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.57.4
* Fri Apr 22 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.56.1
* Mon Mar 07 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.52.0
- bump to 2.53.0
* Tue Feb 09 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.51.0
* Tue Feb 09 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.51.0
- remove net-telnet from Requires of ruby-23, because ruby-23 includes net-telnet 0.1.1
* Sun Dec 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.45.0 and build package for ruby-23
* Tue Dec 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.44.3
* Tue Oct 27 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.44.1
* Tue Aug 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.40.1
* Thu Aug 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.40.0
* Thu Jul 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.38.1
* Sat Jul 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.37.2
* Wed Jun 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.36.4
* Tue Jun 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.36.3
* Mon Jun 22 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.36.1
* Fri Jun 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Requires according to changes of IPS packagename
* Thu Jun 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.35.1
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.34.8
* Mon Jun 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.34.7
- rename IPS_package_names and keep old name packages to resolve dependency
* Sun May 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.34.2
* Tue May 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.31.1
* Tue Mar 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.24.2
- bump to 2.25.0
* Sun Mar 22 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.21.0
* Fri Mar 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.18.2
* Tue Mar 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.18.0
* Sat Feb 28 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.15.2
* Wed Feb 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.12.6
* Sun Feb 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.12.3
* Fri Jan 23 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.11.8
- generate package for ruby-22
* Wed Dec 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.2
* Mon Dec 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.1
* Fri Dec 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.0
* Wed Dec 03 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.9.2
* Wed Nov 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.0
* Thu Nov 02 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.2
* Thu Sep 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.2
- bump to 2.2.1
* Sun Sep 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.0
* Mon Sep 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.26.0
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.20.0
* Mon Jul 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.19.0
* Tue Jul 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.18.3
* Fri Jun 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.18.2
* The Jun 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.18.0
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.16.0
* Fri May 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.15.0
* Wed May 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.0
* Sun Apr 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1
* Tue Apr 15 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.0
* Mon Apr 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.4
- stop to generate package for ruby-18
* Fri Mar 28 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
* Thu Mar 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.8.0
* Wed Mar 19 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.2
* Sat Feb 22 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.0 and build package for ruby-21
* Sat Feb 22 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.1
* Mon Feb 17 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.8
* Sun Jan 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.1
* Sun Jan 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.1
* Thu Jan 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.0
* Sun Dec 29 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.1.1
* Sat Dec 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.17
* Thu Dec 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.16
* Tue Dec 17 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.14
- bump to 0.0.15
* Mon Dec 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.12
- bump to 0.0.13
* Thu Dec 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.8
* Wed Dec 04 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.7
- bump to 0.0.6
* Mon Dec 02 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
