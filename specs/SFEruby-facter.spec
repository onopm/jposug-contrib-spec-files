%include Solaris.inc

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}

%define has_ruby_noarch %has_ruby_abi

Summary: Ruby module for collecting simple facts about a host operating system
Name: facter
IPS_package_name:        runtime/ruby-18/facter
Version: 1.6.16
License: ASL 2.0
Group: System Environment/Base
URL: http://www.puppetlabs.com/puppet/related-projects/%{name}/
Source0: http://puppetlabs.com/downloads/facter/facter-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc
# Source1: http://puppetlabs.com/downloads/%{name}/%{name}-%{version}.tar.gz.asc

Requires: runtime/ruby-18
# Requires: which

BuildRequires: runtime/ruby-18

%description
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
ruby install.rb --destdir=%{buildroot} --quick --no-rdoc
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}%{_bindir}
ln -s ../ruby/1.8/bin/facter .

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%doc LICENSE README.md CONTRIBUTING.md
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, other) /usr/share/doc
%{_bindir}/facter
%{ruby_sitelibdir}/facter.rb
%{ruby_sitelibdir}/facter
# /usr/ruby/1.8/sbin
/usr/ruby/1.8/share
/usr/ruby/1.8/bin


%changelog
* Thu Dec 20 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- make symbolic link from /usr/ruby/1.8/bin/facter to /usr/bin/facter
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
