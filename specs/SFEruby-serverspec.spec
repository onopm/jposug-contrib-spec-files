%include Solaris.inc
%include default-depend.inc

%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23jposug %( if [ -x /opt/jposug/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24jposug %( if [ -x /opt/jposug/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build25jposug %( if [ -x /opt/jposug/ruby/2.5/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 1
%define keep_dependency 0

%define gemname serverspec
%define sfe_gemname serverspec

Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.41.3
License:          MIT
URL:              http://serverspec.org/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# multi_json >= 0
Requires:         library/ruby/multi_json-21
# rspec ~> 3.0
Requires:         library/ruby/rspec-21
# rspec-its >= 0
Requires:         library/ruby/rspec-its-21
# specinfra ~> 2.72
Requires:         library/ruby/specinfra-21 >= 2.72.0
Requires:         library/ruby/%{gemname}

%description 21
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# multi_json >= 0
Requires:         library/ruby/multi_json-22
# rspec ~> 3.0
Requires:         library/ruby/rspec-22
# rspec-its >= 0
Requires:         library/ruby/rspec-its-22
# specinfra ~> 2.72
Requires:         library/ruby/specinfra-22 >= 2.72.0
Requires:         library/ruby/%{gemname}

%description 22
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}-23

%description 23-old
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# multi_json >= 0
Requires:         library/ruby/multi_json-23
# rspec ~> 3.0
Requires:         library/ruby/rspec-23
# rspec-its >= 0
Requires:         library/ruby/rspec-its-23
# specinfra ~> 2.72
Requires:         library/ruby/specinfra-23 >= 2.72.0
Requires:         library/ruby/%{gemname}

%description 23
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%if %{build23jposug}

%package 23jposug
IPS_package_name: jposug/library/ruby/%{gemname}-23jposug
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    jposug/runtime/ruby-23jposug = *
Requires:         jposug/runtime/ruby-23jposug = *
# multi_json >= 0
Requires:         jposug/library/ruby/multi_json-23jposug
# rspec ~> 3.0
Requires:         jposug/library/ruby/rspec-23jposug
# rspec-its >= 0
Requires:         jposug/library/ruby/rspec-its-23jposug
# specinfra ~> 2.72
Requires:         jposug/library/ruby/specinfra-23jposug >= 2.72.0
Requires:         jposug/library/ruby/%{gemname}

%description 23jposug
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%if %{build24jposug}

%package 24jposug
IPS_package_name: jposug/library/ruby/%{gemname}-24jposug
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    jposug/runtime/ruby-24jposug = *
Requires:         jposug/runtime/ruby-24jposug = *
# multi_json >= 0
Requires:         jposug/library/ruby/multi_json-24jposug
# rspec ~> 3.0
Requires:         jposug/library/ruby/rspec-24jposug
# rspec-its >= 0
Requires:         jposug/library/ruby/rspec-its-24jposug
# specinfra ~> 2.72
Requires:         jposug/library/ruby/specinfra-24jposug >= 2.72.0
Requires:         jposug/library/ruby/%{gemname}

%description 24jposug
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%if %{build25jposug}

%package 25jposug
IPS_package_name: jposug/library/ruby/%{gemname}-25jposug
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
# multi_json >= 0
Requires:         jposug/library/ruby/multi_json-25jposug
# rspec ~> 3.0
Requires:         jposug/library/ruby/rspec-25jposug
# rspec-its >= 0
Requires:         jposug/library/ruby/rspec-its-25jposug
# specinfra ~> 2.72
Requires:         jposug/library/ruby/specinfra-25jposug >= 2.72.0
Requires:         jposug/library/ruby/%{gemname}

%description 25jposug
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif


%prep
%setup -q -c -T

%build
build_for() {
    if [ "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
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

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

install_for() {
    if [ "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
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
   
%if %{generate_executable}
    [ -d %{buildroot}/usr/bin ] || mkdir -p %{buildroot}/usr/bin
    pushd %{buildroot}/usr/bin
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


%changelog
* Sun Dec 31 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.41.3 and build packages for ruby-2{3,4,5}jposug
* Wed Sep 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.40.0
* Tue May 23 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.39.1
* Mon Apr 17 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- package for ruby-24 is added, ruby-19 and ruby-20 are obsolete
* Tue Feb 07 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.38.0
* Mon Oct 24 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.37.2
* Tue Oct 11 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.37.0
* Mon May 23 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.36.0
* Fri Apr 22 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.32.0
* Mon Mar 07 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.30.0
- bump to 2.30.1
* Tue Feb 09 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.29.2
* Sun Dec 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build package for ruby-23
* Tue Dec 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.24.3
* Sun Nov 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.24.2
* Tue Oct 27 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.24.1
* Sat Aug 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.21.0
* Thu Jul 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.20.0
* Mon Jun 22 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.19.0
* Fri Jun 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Requires according to changes of IPS packagenames
* Thu Jun 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.18.0
* Mon Jun 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.17.1
- change IPS_package_names and keep old IPS_package_names to keep dependency
* Sun May 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.17.0
* Tue May 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.16.0
* Tue Mar 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.12.0
- bump to 2.13.0
* Sun Mar 22 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.11.0
* Sat Feb 28 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.0
* Sat Feb 28 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.9.1
* Wed Feb 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.2
* Sun Feb 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.1
* Fri Jan 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.7.2
- generate package for ruby-22
* Sun Dec 14 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix symbolic links
* Mon Dec 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.7.0
* Fri Dec 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.6.0
* Thu Dec 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.5.0
* Wed Nov 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.0
* Sun Sep 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.0
* Mon Sep 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.15.0
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.10.0
* Tue Jul 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.1
* Thu Jun 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.0
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.1
* Fri May 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.0
* Wed May 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4.2
* Tue Apr 15 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Mon Apr 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18
- bump to 1.1.0
* Fri Mar 28 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.0
* Tue Feb 25 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build package for ruby-21
* Mon Feb 17 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.15.3
* Wed Jan 29 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.15.0
* Sun Jan 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.14.3
* Sun Dec 29 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.14.2
* Thu Dec 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.6
- bump to 0.13.7
* Tue Dec 17 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.4
- bump to 0.13.5
* Mon Dec 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.3
* Thu Dec 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.2
* Wed Dec 04 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.1
* Mon Dec 02 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.12.0
* Wed Nov 27 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.11.5 and modify shebang
* Mon Nov 18 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.11.4
* Thu Oct 31 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.13
* Fri Oct 18 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.8
* Thu Oct 17 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.6
* Wed Oct 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.5
* Tue Oct 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.4
* Tue Oct 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.8
* Thu Oct 03 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.7
* Wed Sep 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.6
* Thu Aug 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.6
* Tue Jul 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.0
* Mon Jul 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.28
* Fri Jul 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.22
* Wed Jun 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.10
* Tue Jun 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.7
* Wed Jun 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.4
- bump to 0.6.5
* Fri Jun 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.2
* Mon Jun 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.5
- bump to 0.5.6
* Thu Jun 06 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.0
* Tue May 28 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.12
* Sat May 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.10
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.9
- generate package for ruby-20
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.7
* Fri May 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.0
* Tue May 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.1
* Fri May 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.26
* Wed May 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.24
* Tue May 07 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.23
* Mon May 06 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.22
* Wed May 01 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.17
* Wed Apr 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.16
* Wed Apr 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.13
* Mon Apr 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.9
* Fri Apr 12 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.7 and add Requires
* Thu Apr  9 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.3
* Thu Apr  4 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.1.6
* Sat Mar 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.17
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
