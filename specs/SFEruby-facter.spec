%include Solaris.inc

%define gemname facter
%define generate_executable 1

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}


%define has_ruby_noarch %has_ruby_abi

Summary: Ruby module for collecting simple facts about a host operating system
Name: facter
IPS_package_name:        library/ruby-19/%{gemname}
Version: 2.0.1
License: ASL 2.0
Group: System Environment/Base
URL: http://www.puppetlabs.com/puppet/related-projects/%{name}/
# Source0: http://puppetlabs.com/downloads/facter/facter-%{version}.tar.gz
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: runtime/ruby-19
Requires: runtime/ruby-19

%description
Ruby module for collecting simple facts about a host Operating
lsystem. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%package 20
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Ruby module for collecting simple facts about a host operating system
BuildRequires:	  runtime/ruby-20
Requires:	  runtime/ruby-20

%description 20
Ruby module for collecting simple facts about a host operating system

%package 21
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Ruby module for collecting simple facts about a host operating system
BuildRequires:	  runtime/ruby-21
Requires:	  runtime/ruby-21

%description 21
Ruby module for collecting simple facts about a host operating system

%prep
%setup -q -c -T

%build
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}


%install
rm -rf %{buildroot}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
   %{buildroot}%{bindir19}/
%endif

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
   %{buildroot}%{bindir20}/
%endif

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
   %{buildroot}%{bindir21}/
%endif

mkdir -p %{buildroot}/usr/bin
cat %{buildroot}%{gemdir19}/gems/%{gemname}-%{version}/bin/facter | \
    sed -e 's!/usr/bin/env ruby!/usr/ruby/1.9/bin/ruby!' > %{buildroot}/usr/bin/facter-19
cat %{buildroot}%{gemdir20}/gems/%{gemname}-%{version}/bin/facter | \
    sed -e 's!/usr/bin/env ruby!/usr/ruby/2.0/bin/ruby!' > %{buildroot}/usr/bin/facter-20
cat %{buildroot}%{gemdir21}/gems/%{gemname}-%{version}/bin/facter | \
    sed -e 's!/usr/bin/env ruby!/usr/ruby/2.1/bin/ruby!' > %{buildroot}/usr/bin/facter-21
cd %{buildroot}/usr/bin
ln -s facter-21 facter

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
/usr/bin/facter-19
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
/usr/bin/facter-20
/usr/ruby/2.0

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
/usr/bin/facter
/usr/bin/facter-21
/usr/ruby/2.1

%changelog
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
