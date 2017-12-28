%include Solaris.inc
%include default-depend.inc

%define build21 %( if [ -x /usr/ruby/2.1/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build22 %( if [ -x /usr/ruby/2.2/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24 %( if [ -x /usr/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 1
%define keep_dependency 0

%define gemname facter
%define sfe_gemname facter

Summary:          You can prove anything with facts!
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.4.6
License:          Apache License 2.0
URL:              https://github.com/puppetlabs/facter
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
You can prove anything with facts!

%if %{build21}
%if %{keep_dependency}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          You can prove anything with facts!
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
You can prove anything with facts!
%endif

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          You can prove anything with facts!
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}

%description 21
You can prove anything with facts!
%endif

%if %{build22}
%if %{keep_dependency}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          You can prove anything with facts!
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
You can prove anything with facts!
%endif

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          You can prove anything with facts!
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}

%description 22
You can prove anything with facts!
%endif

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          You can prove anything with facts!
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
Requires:         library/ruby/%{gemname}-23

%description 23-old
You can prove anything with facts!
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          You can prove anything with facts!
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *

%description 23
You can prove anything with facts!
%endif

%if %{build24}
%package 24
IPS_package_name: library/ruby/%{gemname}-24
Summary:          You can prove anything with facts!
BuildRequires:    runtime/ruby-24 = *
Requires:         runtime/ruby-24 = *

%description 24
You can prove anything with facts!
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
* Wed Nov 30 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.6
* Tue Aug 25 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.4 and update spec file
* Thu May 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.3
* Fri Feb 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.1
* Wed Dec 03 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.0
* Mon Sep 01 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.0
* Wed Jun 11 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.2
* Fri May 30 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.1
* Fri Feb 14 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.5
* Wed Jan 08 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use ruby-18 instead of ruby-19
- bump to 1.7.4
- fix to work with ruby-18 correctly
* Fri Nov 15 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use ruby-19 instead of ruby-18
* Tue Sep 24 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.3

* Thu Jul 11 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.2

* Tue Apr 16 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.7.0

* Thu Mar 14 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.6.18

* Mon Dec 10 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.6.16

* Sun Oct 07 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.6.13

* Sun Sep 23 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.6.12

* Wed Aug 22 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.6.11

* Fri Jun 15 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.6.10

* Wed Apr 29 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 1.6.8

* Tue Mar 27 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify %file for Solaris 11

* Mon Oct  3 2011 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- import to solaris

* Thu Sep 29 2011 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.1-1
- Updated to version 1.6.1

* Wed Jul 13 2011 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.0-2
- Update to not be architecture dependant

* Wed Jul 13 2011 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.0-1
- Update to 1.6.0

* Sat Aug 28 2010 Todd Zullinger <tmz@pobox.com> - 1.5.8-1
- Update to 1.5.8

* Fri Sep 25 2009 Todd Zullinger <tmz@pobox.com> - 1.5.7-1
- Update to 1.5.7
- Update #508037 patch from upstream ticket

* Wed Aug 12 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.5.5-3
- Fix #508037 or upstream #2355

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Todd Zullinger <tmz@pobox.com> - 1.5.5-1
- Update to 1.5.5
- Drop upstreamed libperms patch

* Sat Feb 28 2009 Todd Zullinger <tmz@pobox.com> - 1.5.4-1
- New version
- Use upstream install script

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 09 2008 Todd Zullinger <tmz@pobox.com> - 1.5.2-1
- New version
- Simplify spec file checking for Fedora and RHEL versions

* Mon Sep  8 2008 David Lutterkort <dlutter@redhat.com> - 1.5.1-1
- New version

* Thu Jul 17 2008 David Lutterkort <dlutter@redhat.com> - 1.5.0-3
- Change 'mkdir' in install to 'mkdir -p'

* Thu Jul 17 2008 David Lutterkort <dlutter@redhat.com> - 1.5.0-2
- Remove files that were listed twice in files section

* Mon May 19 2008 James Turnbull <james@lovedthanlosty.net> - 1.5.0-1
- New version
- Added util and plist files

* Mon Sep 24 2007 David Lutterkort <dlutter@redhat.com> - 1.3.8-1
- Update license tag
- Copy all of lib/ into ruby_sitelibdir

* Thu Mar 29 2007 David Lutterkort <dlutter@redhat.com> - 1.3.7-1
- New version

* Fri Jan 19 2007 David Lutterkort <dlutter@redhat.com> - 1.3.6-1
- New version

* Thu Jan 18 2007 David Lutterkort <dlutter@redhat.com> - 1.3.5-3
- require which; facter is very unhappy without it

* Mon Nov 20 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-2
- Make require ruby(abi) and buildarch: noarch conditional for fedora 5 or
  later to allow building on older fedora releases

* Tue Oct 10 2006 David Lutterkort <dlutter@redhat.com> - 1.3.5-1
- New version

* Tue Sep 26 2006 David Lutterkort <dlutter@redhat.com> - 1.3.4-1
- New version

* Wed Sep 13 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-2
- Rebuilt for FC6

* Wed Jun 28 2006 David Lutterkort <dlutter@redhat.com> - 1.3.3-1
- Rebuilt

* Fri Jun 19 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Fixed spec file to work again with the extra memory and processor files.
- Require ruby(abi). Build as noarch

* Fri Jun 9 2006 Luke Kanies <luke@madstop.com> - 1.3.0-1
- Added memory.rb and processor.rb

* Mon Apr 17 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-4
- Rebuilt with changed upstream tarball

* Tue Mar 21 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-3
- Do not rely on install.rb, it will be deleted upstream

* Mon Mar 13 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-2
- Commented out noarch; requires fix for bz184199

* Mon Mar  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.4-1
- Removed unused macros

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-2
- Fix BuildRoot. Add dist to release tag

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 1.1.1-1
- Initial build.
