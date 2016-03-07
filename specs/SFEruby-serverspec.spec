%include Solaris.inc
%include default-depend.inc

%define build19 %( if [ -x /usr/ruby/1.9/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build20 %( if [ -x /usr/ruby/2.0/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 1
%define keep_dependency 1

%define gemname serverspec
%define sfe_gemname serverspec
%define specinfra_ver 2.48.0

Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.30.1
License:          MIT
URL:              http://serverspec.org/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else

%if %{build19}
%if %{keep_dependency}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19-old
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# multi_json >= 0
Requires:         library/ruby/multi_json-19
# rspec ~> 3.0
Requires:         library/ruby/rspec-19
# rspec-its >= 0
Requires:         library/ruby/rspec-its-19
# specinfra ~> 2.43
Requires:         library/ruby/specinfra-19 >= %{specinfra_ver}
Requires:         library/ruby/%{gemname}

%description 19
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%if %{build20}
%if %{keep_dependency}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20-old
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# multi_json >= 0
Requires:         library/ruby/multi_json-20
# rspec ~> 3.0
Requires:         library/ruby/rspec-20
# rspec-its >= 0
Requires:         library/ruby/rspec-its-20
# specinfra ~> 2.43
Requires:         library/ruby/specinfra-20 >= %{specinfra_ver}
Requires:         library/ruby/%{gemname}

%description 20
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
%endif

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
# specinfra ~> 2.43
Requires:         library/ruby/specinfra-21 >= %{specinfra_ver}
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
# specinfra ~> 2.43
Requires:         library/ruby/specinfra-22 >= %{specinfra_ver}
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
# specinfra ~> 2.43
Requires:         library/ruby/specinfra-23 >= %{specinfra_ver}

%description 23
RSpec tests for your servers configured by Puppet, Chef, Itamae or anything else
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
