%include Solaris.inc
%include default-depend.inc

%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23jposug %( if [ -x /opt/jposug/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24jposug %( if [ -x /opt/jposug/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build25jposug %( if [ -x /opt/jposug/ruby/2.5/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build26jposug %( if [ -x /opt/jposug/ruby/2.6/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 0

%define gemname specinfra
%define sfe_gemname specinfra

# Common layer for serverspec and itamae

Summary:          Common layer for serverspec and itamae
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.76.9
License:          MIT
URL:              https://github.com/mizzy/specinfra
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Common layer for serverspec and itamae

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          Common layer for serverspec and itamae
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# Requires:         library/ruby/%{gemname}-23

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
# net-ssh >= 2.7
Requires:         library/ruby/net-ssh-23
# net-telnet = 0.1.1
Requires:         library/ruby/net-telnet-23
# sfl >= 0
Requires:         library/ruby/sfl-23
# Requires:         library/ruby/%{gemname}

%description 23
Common layer for serverspec and itamae
%endif

%if %{build23jposug}

%package 23jposug
IPS_package_name: jposug/library/ruby/%{gemname}-23jposug
Summary:          Common layer for serverspec and itamae
BuildRequires:    jposug/runtime/ruby-23jposug = *
Requires:         jposug/runtime/ruby-23jposug = *
# net-scp >= 0
Requires:         jposug/library/ruby/net-scp-23jposug
# net-ssh >= 2.7
Requires:         jposug/library/ruby/net-ssh-23jposug
# net-telnet = 0.1.1
Requires:         jposug/library/ruby/net-telnet-23jposug
# sfl >= 0
Requires:         jposug/library/ruby/sfl-23jposug
# Requires:         library/ruby/%{gemname}

%description 23jposug
Common layer for serverspec and itamae
%endif

%if %{build24jposug}

%package 24jposug
IPS_package_name: jposug/library/ruby/%{gemname}-24jposug
Summary:          Common layer for serverspec and itamae
BuildRequires:    jposug/runtime/ruby-24jposug = *
Requires:         jposug/runtime/ruby-24jposug = *
# net-scp >= 0
Requires:         jposug/library/ruby/net-scp-24jposug
# net-ssh >= 2.7
Requires:         jposug/library/ruby/net-ssh-24jposug
# net-telnet = 0.1.1
Requires:         jposug/library/ruby/net-telnet-24jposug
# sfl >= 0
Requires:         jposug/library/ruby/sfl-24jposug
# Requires:         library/ruby/%{gemname}

%description 24jposug
Common layer for serverspec and itamae
%endif

%if %{build25jposug}

%package 25jposug
IPS_package_name: jposug/library/ruby/%{gemname}-25jposug
Summary:          Common layer for serverspec and itamae
BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
# net-scp >= 0
Requires:         jposug/library/ruby/net-scp-25jposug
# net-ssh >= 2.7
Requires:         jposug/library/ruby/net-ssh-25jposug
# net-telnet = 0.1.1
Requires:         jposug/library/ruby/net-telnet-25jposug
# sfl >= 0
Requires:         jposug/library/ruby/sfl-25jposug
# Requires:         library/ruby/%{gemname}

%description 25jposug
Common layer for serverspec and itamae
%endif

%if %{build26jposug}

%package 26jposug
IPS_package_name: jposug/library/ruby/%{gemname}-26jposug
Summary:          Common layer for serverspec and itamae
BuildRequires:    jposug/runtime/ruby-26jposug = *
Requires:         jposug/runtime/ruby-26jposug = *
# net-scp >= 0
Requires:         jposug/library/ruby/net-scp-26jposug
# net-ssh >= 2.7
Requires:         jposug/library/ruby/net-ssh-26jposug
# net-telnet = 0.1.1
Requires:         jposug/library/ruby/net-telnet-26jposug
# sfl >= 0
Requires:         jposug/library/ruby/sfl-26jposug
# Requires:         library/ruby/%{gemname}

%description 26jposug
Common layer for serverspec and itamae
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
        --no-document \
        --install-dir .${gemdir} \
        --bindir .${bindir} \
        -V \
        --force %{SOURCE0}
}

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
* Wed Feb 13 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.76.9 and obsolete packagges for ruby-21 and ruby-22
* Mon Mar 05 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete dependencies to net-telnet because net-telnet is included in ruby packages
* Sun Mar 04 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.73.2 and build packges for ruby-26jposug
* Sat Dec 30 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.73.0 and build packges for ruby-2{3,4,5}jposug
* Wed Sep 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.71.2
* Tue May 23 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.68.0
* Mon Apr 17 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.67.8 and package for ruby24 is added, ruby-19 and ruby-20 are obsolete
* Tue Feb 07 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.66.8
* Tue Oct 11 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.63.3
* Tue Jul 12 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.59.6
* Fri Jun 24 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.59.3
* Thu Jun 23 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.59.2
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
* Mon Mar 05 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete dependencies to net-telnet because net-telnet is included in ruby packages
* Sun Mar 04 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.73.2 and build packges for ruby-26jposug
* Sat Dec 30 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.73.0 and build packges for ruby-2{3,4,5}jposug
* Wed Sep 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.71.2
* Tue May 23 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.68.0
* Mon Apr 17 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.67.8 and package for ruby24 is added, ruby-19 and ruby-20 are obsolete
* Tue Feb 07 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.66.8
* Tue Oct 11 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.63.3
* Tue Jul 12 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.59.6
* Fri Jun 24 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.59.3
* Thu Jun 23 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.59.2
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
