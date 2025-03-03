%include Solaris.inc
%include packagenamemacros.inc
%include base.inc
%define cc_is_gcc 0

%define _bindir /usr/ruby/1.8/bin
%define _sbindir /usr/ruby/1.8/sbin
%define _mandir /usr/ruby/1.8/share/man

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%define confdir conf/solaris

Name:           puppet
IPS_package_name:        system/management/puppet
Version:        2.7.16
#Release:        0.1rc1%{?dist}
Release:        1%{?dist}
Summary:        A network tool for managing many disparate systems
Group:		Applications/System
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        http://puppetlabs.com/downloads/%{name}/%{name}-%{version}.tar.gz
#Source0:        http://puppetlabs.com/downloads/%{name}/%{name}-%{version}rc1.tar.gz
# Source1:        http://puppetlabs.com/downloads/%{name}/%{name}-%{version}.tar.gz.asc
#Source1:        http://puppetlabs.com/downloads/%{name}/%{name}-%{version}rc1.tar.gz.asc
Source2:        svc-puppetd
Source3:        svc-puppetmasterd
Source4:        puppetd.xml
Source5:        puppetmasterd.xml
# Source6:        puppet-pkg.rb

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  runtime/ruby-18
BuildRequires:  runtime/ruby-18/facter
Requires:  runtime/ruby-18
Requires:  runtime/ruby-18/facter

# %if 0%{?fedora} || 0%{?rhel} >= 5
# BuildArch:      noarch
# Requires:       ruby(abi) >= 1.8
# Requires:       ruby-shadow
# %endif

# Requires:       facterzna >= 1.5
# Requires:       ruby >= 1.8.1
# %{!?_without_augeas:Requires: ruby-augeas}

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%package server
IPS_package_name:        system/management/puppet/server
Group:		Applications/System
Summary:        Server for the puppet system management tool
Requires:       puppet = %{version}-%{release}

%description server
Provides the central puppet server daemon which provides manifests to clients.
The server can also function as a certificate authority and file server.

%prep
%setup -q -n %{name}-%{version}
patch -s -p1 < conf/redhat/rundir-perms.patch


%build
# Fix some rpmlint complaints
for f in mac_dscl.pp mac_dscl_revert.pp \
         mac_pkgdmg.pp ; do
  sed -i -e'1d' examples/$f
  chmod a-x examples/$f
done
for f in external/nagios.rb network/http_server/mongrel.rb relationship.rb; do
  sed -i -e '1d' lib/puppet/$f
done
#chmod +x ext/puppetstoredconfigclean.rb

find examples/ -type f -empty | xargs rm
find examples/ -type f | xargs chmod a-x

# puppet-queue.conf is more of an example, used for stompserver
mv conf/puppet-queue.conf examples/etc/puppet/

%install
rm -rf %{buildroot}
ruby install.rb --destdir=%{buildroot} --quick --no-rdoc

install -d -m0755 %{buildroot}%{_sysconfdir}/puppet/manifests
install -d -m0755 %{buildroot}%{_datadir}/%{name}/modules
install -d -m0755 %{buildroot}%{_localstatedir}/lib
# install -d -m0755 %{buildroot}%{_localstatedir}/run/puppet
# install -d -m0755 %{buildroot}%{_localstatedir}/lib/puppet
# install -d -m0750 %{buildroot}%{_localstatedir}/log/puppet

install -Dp -m0644 %{SOURCE2} %{buildroot}/lib/svc/method/svc-puppetd
install -Dp -m0644 %{SOURCE3} %{buildroot}/lib/svc/method/svc-puppetmasterd
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_localstatedir}/svc/manifest/system/management/puppetd.xml
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_localstatedir}/svc/manifest/system/management/puppetmasterd.xml
# install -m0755 %{SOURCE6} %{buildroot}/usr/ruby/1.8/lib/ruby/site_ruby/1.8/puppet/provider/package/pkg.rb

# We need something for these ghosted files, otherwise rpmbuild
# will complain loudly. They won't be included in the binary packages
touch %{buildroot}%{_sysconfdir}/puppet/puppetmasterd.conf
touch %{buildroot}%{_sysconfdir}/puppet/puppetca.conf
touch %{buildroot}%{_sysconfdir}/puppet/puppet.conf

# Install the ext/ directory to %%{_datadir}/%%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a ext/ %{buildroot}%{_datadir}/%{name}
# emacs and vim bits are installed elsewhere
rm -rf %{buildroot}%{_datadir}/%{name}/ext/{emacs,vim}

# Install emacs mode files
emacsdir=%{buildroot}%{_datadir}/emacs/site-lisp
install -Dp -m0644 ext/emacs/puppet-mode.el $emacsdir/puppet-mode.el
install -Dp -m0644 ext/emacs/puppet-mode-init.el \
    $emacsdir/site-start.d/puppet-mode-init.el

# Install vim syntax files
vimdir=%{buildroot}%{_datadir}/vim/vimfiles
install -Dp -m0644 ext/vim/ftdetect/puppet.vim $vimdir/ftdetect/puppet.vim
install -Dp -m0644 ext/vim/syntax/puppet.vim $vimdir/syntax/puppet.vim

# %if 0%{?fedora} >= 15
# # Setup tmpfiles.d config
# mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d
# echo "D /var/run/%{name} 0755 %{name} %{name} -" > \
#     %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf
# %endif

%files
%defattr(-, root, bin, 0755)
%doc CHANGELOG LICENSE README.md README_DEVELOPER.md CONTRIBUTING.md
%{_bindir}/pi
%{_bindir}/puppet
%{_bindir}/ralsh
%{_bindir}/filebucket
%{_bindir}/puppetdoc
%{_sbindir}/puppetca
%{_sbindir}/puppetd
%dir %attr (0755, root, sys) /usr
# %dir %attr (0755, root, bin) /usr/ruby/1.8
# %dir %attr (0755, root, bin) /usr/ruby/1.8/bin
# %dir %attr (0755, root, bin) /usr/ruby/1.8/lib
# %dir %attr (0755, root, bin) /usr/ruby/1.8/lib/ruby
# %dir %attr (0755, root, bin) /usr/ruby/1.8/share
# %dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, sys) %{_localstatedir}
# %dir %attr (0755, root, sys) %{_localstatedir}/log
# %dir %attr (0755, root, other) %{_localstatedir}/lib
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/system
%attr (0755, root, bin) %{ruby_sitelibdir}/
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, sys) %{_sysconfdir}/puppet
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, other) /usr/share/doc
# %if 0%{?fedora} >= 15
# %config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf
# %endif
# %config(noreplace) %{_sysconfdir}/sysconfig/puppet
# %config(noreplace) %{_sysconfdir}/puppet/puppet.conf
%config(noreplace) %{_sysconfdir}/puppet/auth.conf
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetca.conf
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppet.conf
# We don't want to require emacs or vim, so we need to own these dirs
%attr (0755, root, bin) %{_datadir}/emacs
%attr (0755, root, bin) %{_datadir}/vim
%{_datadir}/%{name}
# These need to be owned by puppet so the server can
# write to them
# %dir %attr(-, puppet, puppet) %{_localstatedir}/run/puppet
# %dir %attr(0755, root, sys) %{_localstatedir}/log
# %dir %attr(0755, puppet, puppet) %{_localstatedir}/log/puppet
%dir %attr(0755, root, other) %{_localstatedir}/lib
# %dir %attr(0755, puppet, puppet) %{_localstatedir}/lib/puppet
%{_mandir}/man5/puppet.conf.5.gz
%{_mandir}/man8/pi.8.gz
%{_mandir}/man8/puppet.8.gz
%{_mandir}/man8/puppetca.8.gz
%{_mandir}/man8/puppetd.8.gz
%{_mandir}/man8/ralsh.8.gz
%{_mandir}/man8/puppetdoc.8.gz
%{_mandir}/man8/puppet-agent.8.gz
%{_mandir}/man8/puppet-apply.8.gz
%{_mandir}/man8/puppet-catalog.8.gz
%{_mandir}/man8/puppet-describe.8.gz
%{_mandir}/man8/puppet-cert.8.gz
%{_mandir}/man8/puppet-certificate.8.gz
%{_mandir}/man8/puppet-certificate_request.8.gz
%{_mandir}/man8/puppet-certificate_revocation_list.8.gz
%{_mandir}/man8/puppet-config.8.gz
%{_mandir}/man8/puppet-device.8.gz
%{_mandir}/man8/puppet-doc.8.gz
%{_mandir}/man8/puppet-facts.8.gz
%{_mandir}/man8/puppet-file.8.gz
%{_mandir}/man8/puppet-filebucket.8.gz
%{_mandir}/man8/puppet-help.8.gz
%{_mandir}/man8/puppet-inspect.8.gz
%{_mandir}/man8/puppet-key.8.gz
%{_mandir}/man8/puppet-kick.8.gz
%{_mandir}/man8/puppet-man.8.gz
%{_mandir}/man8/puppet-node.8.gz
%{_mandir}/man8/puppet-parser.8.gz
%{_mandir}/man8/puppet-plugin.8.gz
%{_mandir}/man8/puppet-queue.8.gz
%{_mandir}/man8/puppet-report.8.gz
%{_mandir}/man8/puppet-resource.8.gz
%{_mandir}/man8/puppet-resource_type.8.gz
%{_mandir}/man8/puppet-secret_agent.8.gz
%{_mandir}/man8/puppet-status.8.gz
%{_mandir}/man8/puppet-module.8.gz
%{_mandir}/man8/puppet-instrumentation_probe.8.gz
%{_mandir}/man8/puppet-instrumentation_listener.8.gz
%{_mandir}/man8/puppet-instrumentation_data.8.gz
%{_mandir}/man8/puppet-ca.8.gz

%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/system/management/puppetd.xml
# /var/svc/manifest/system/management/puppetd.xml
%attr (0555, root, bin) /lib/svc/method/svc-puppetd



%files server
%defattr(-, root, bin, 0755)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/system
%{_sbindir}/puppetmasterd
%{_sbindir}/puppetrun
%{_sbindir}/puppetqd
# %config(noreplace) %{_sysconfdir}/puppet/fileserver.conf
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, sys) %{_sysconfdir}/puppet
%dir %attr (0755, root, sys) %{_sysconfdir}/puppet/manifests
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppetmasterd.conf
%{_mandir}/man8/filebucket.8.gz
%{_mandir}/man8/puppetmasterd.8.gz
%{_mandir}/man8/puppetrun.8.gz
%{_mandir}/man8/puppetqd.8.gz
%{_mandir}/man8/puppet-master.8.gz
%dir %attr(0755, root, other) %{_localstatedir}/lib
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/system/management/puppetmasterd.xml
%attr (0555, root, bin) /lib/svc/method/svc-puppetmasterd

%clean
rm -rf %{buildroot}

%changelog
* Fri Jun 15 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.7.16

* Wed May 16 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.7.14

* Fri May 11 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- include /var/lib to %files because it is needed at first time.
- rename /etc/puppet/puppetd.conf to /etc/puppet/puppet.conf

* Thu May 10 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Source6 for Solaris 11

* Wed Apr 25 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- adjust %files and init scripts to Oracle Solaris 11

* Fri Apr 13 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 2.7.13

* Sat Mar 24 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- import to solaris

* Mon Mar 12 2012 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.12-1
- Update for 2.7.12

* Fri Feb 24 2012 Matthaus Litteken <matthaus@puppetlabs.com> - 2.7.11-2
- Update 2.7.11 from proper tag, including #12572

* Wed Feb 22 2012 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.11-1
- Update for 2.7.11

* Wed Jan 25 2012 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.10-1
- Update for 2.7.10

* Fri Dec 9 2011 Matthaus Litteken <matthaus@puppetlabs.com> - 2.7.9-1
- Update for 2.7.9

* Thu Dec 8 2011 Matthaus Litteken <matthaus@puppetlabs.com> - 2.7.8-1
- Update for 2.7.8

* Wed Nov 30 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.8-0.1rc1
- Update for 2.7.8rc1

* Mon Nov 21 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.7-1
- Relaese 2.7.7

* Tue Nov 01 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.7-0.1rc1
- Update for 2.7.7rc1

* Fri Oct 21 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.6-1
- 2.7.6 final

* Thu Oct 13 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.6-.1rc3
- New RC

* Fri Oct 07 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.6-0.1rc2
- New RC

* Mon Oct 03 2011 Michael Stahnke <stahnma@puppetlabs.com> -  2.7.6-0.1rc1
- New RC

* Fri Sep 30 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.5-1
- Fixes for CVE-2011-3869, 3870, 3871

* Wed Sep 28 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.4-1
- Fix for CVE-2011-3484

* Wed Jul 06 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.2-0.2.rc1
- Clean up rpmlint errors
- Put man pages in correct package

* Wed Jul 06 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.7.2-0.1.rc1
- Update to 2.7.2rc1

* Wed Jun 15 2011 Todd Zullinger <tmz@pobox.com> - 2.6.9-0.1.rc1
- Update rc versioning to ensure 2.6.9 final is newer to rpm
- sync changes with Fedora/EPEL

* Tue Jun 14 2011 Michael Stahnke <stahnma@puppetlabs.com> - 2.6.9rc1-1
- Update to 2.6.9rc1

* Thu Apr 14 2011 Todd Zullinger <tmz@pobox.com> - 2.6.8-1
- Update to 2.6.8

* Thu Mar 24 2011 Todd Zullinger <tmz@pobox.com> - 2.6.7-1
- Update to 2.6.7

* Wed Mar 16 2011 Todd Zullinger <tmz@pobox.com> - 2.6.6-1
- Update to 2.6.6
- Ensure %%pre exits cleanly
- Fix License tag, puppet is now GPLv2 only
- Create and own /usr/share/puppet/modules (#615432)
- Properly restart puppet agent/master daemons on upgrades from 0.25.x
- Require libselinux-utils when selinux support is enabled
- Support tmpfiles.d for Fedora >= 15 (#656677)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 17 2010 Todd Zullinger <tmz@pobox.com> - 0.25.5-1
- Update to 0.25.5
- Adjust selinux conditional for EL-6
- Apply rundir-perms patch from tarball rather than including it separately
- Update URL's to reflect the new puppetlabs.com domain

* Fri Jan 29 2010 Todd Zullinger <tmz@pobox.com> - 0.25.4-1
- Update to 0.25.4

* Tue Jan 19 2010 Todd Zullinger <tmz@pobox.com> - 0.25.3-2
- Apply upstream patch to fix cron resources (upstream #2845)

* Mon Jan 11 2010 Todd Zullinger <tmz@pobox.com> - 0.25.3-1
- Update to 0.25.3

* Tue Jan 05 2010 Todd Zullinger <tmz@pobox.com> - 0.25.2-1.1
- Replace %%define with %%global for macros

* Tue Jan 05 2010 Todd Zullinger <tmz@pobox.com> - 0.25.2-1
- Update to 0.25.2
- Fixes CVE-2010-0156, tmpfile security issue (#502881)
- Install auth.conf, puppetqd manpage, and queuing examples/docs

* Wed Nov 25 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.25.1-1
- New upstream version

* Tue Oct 27 2009 Todd Zullinger <tmz@pobox.com> - 0.25.1-0.3
- Update to 0.25.1
- Include the pi program and man page (R.I.Pienaar)

* Sat Oct 17 2009 Todd Zullinger <tmz@pobox.com> - 0.25.1-0.2.rc2
- Update to 0.25.1rc2

* Tue Sep 22 2009 Todd Zullinger <tmz@pobox.com> - 0.25.1-0.1.rc1
- Update to 0.25.1rc1
- Move puppetca to puppet package, it has uses on client systems
- Drop redundant %%doc from manpage %%file listings

* Fri Sep 04 2009 Todd Zullinger <tmz@pobox.com> - 0.25.0-1
- Update to 0.25.0
- Fix permissions on /var/log/puppet (#495096)
- Install emacs mode and vim syntax files (#491437)
- Install ext/ directory in %%{_datadir}/%%{name} (/usr/share/puppet)

* Mon May 04 2009 Todd Zullinger <tmz@pobox.com> - 0.25.0-0.1.beta1
- Update to 0.25.0beta1
- Make Augeas and SELinux requirements build time options

* Mon Mar 23 2009 Todd Zullinger <tmz@pobox.com> - 0.24.8-1
- Update to 0.24.8
- Quiet output from %%pre
- Use upstream install script
- Increase required facter version to >= 1.5

* Tue Dec 16 2008 Todd Zullinger <tmz@pobox.com> - 0.24.7-4
- Remove redundant useradd from %%pre

* Tue Dec 16 2008 Jeroen van Meeuwen <kanarip@kanarip.com> - 0.24.7-3
- New upstream version
- Set a static uid and gid (#472073, #471918, #471919)
- Add a conditional requirement on libselinux-ruby for Fedora >= 9
- Add a dependency on ruby-augeas

* Wed Oct 22 2008 Todd Zullinger <tmz@pobox.com> - 0.24.6-1
- Update to 0.24.6
- Require ruby-shadow on Fedora and RHEL >= 5
- Simplify Fedora/RHEL version checks for ruby(abi) and BuildArch
- Require chkconfig and initstripts for preun, post, and postun scripts
- Conditionally restart puppet in %%postun
- Ensure %%preun, %%post, and %%postun scripts exit cleanly
- Create puppet user/group according to Fedora packaging guidelines
- Quiet a few rpmlint complaints
- Remove useless %%pbuild macro
- Make specfile more like the Fedora/EPEL template

* Mon Jul 28 2008 David Lutterkort <dlutter@redhat.com> - 0.24.5-1
- Add /usr/bin/puppetdoc

* Thu Jul 24 2008 Brenton Leanhardt <bleanhar@redhat.com>
- New version
- man pages now ship with tarball
- examples/code moved to root examples dir in upstream tarball

* Tue Mar 25 2008 David Lutterkort <dlutter@redhat.com> - 0.24.4-1
- Add man pages (from separate tarball, upstream will fix to
  include in main tarball)

* Mon Mar 24 2008 David Lutterkort <dlutter@redhat.com> - 0.24.3-1
- New version

* Wed Mar  5 2008 David Lutterkort <dlutter@redhat.com> - 0.24.2-1
- New version

* Sat Dec 22 2007 David Lutterkort <dlutter@redhat.com> - 0.24.1-1
- New version

* Mon Dec 17 2007 David Lutterkort <dlutter@redhat.com> - 0.24.0-2
- Use updated upstream tarball that contains yumhelper.py

* Fri Dec 14 2007 David Lutterkort <dlutter@redhat.com> - 0.24.0-1
- Fixed license
- Munge examples/ to make rpmlint happier

* Wed Aug 22 2007 David Lutterkort <dlutter@redhat.com> - 0.23.2-1
- New version

* Thu Jul 26 2007 David Lutterkort <dlutter@redhat.com> - 0.23.1-1
- Remove old config files

* Wed Jun 20 2007 David Lutterkort <dlutter@redhat.com> - 0.23.0-1
- Install one puppet.conf instead of old config files, keep old configs
  around to ease update
- Use plain shell commands in install instead of macros

* Wed May  2 2007 David Lutterkort <dlutter@redhat.com> - 0.22.4-1
- New version

* Thu Mar 29 2007 David Lutterkort <dlutter@redhat.com> - 0.22.3-1
- Claim ownership of _sysconfdir/puppet (bz 233908)

* Mon Mar 19 2007 David Lutterkort <dlutter@redhat.com> - 0.22.2-1
- Set puppet's homedir to /var/lib/puppet, not /var/puppet
- Remove no-lockdir patch, not needed anymore

* Mon Feb 12 2007 David Lutterkort <dlutter@redhat.com> - 0.22.1-2
- Fix bogus config parameter in puppetd.conf

* Sat Feb  3 2007 David Lutterkort <dlutter@redhat.com> - 0.22.1-1
- New version

* Fri Jan  5 2007 David Lutterkort <dlutter@redhat.com> - 0.22.0-1
- New version

* Mon Nov 20 2006 David Lutterkort <dlutter@redhat.com> - 0.20.1-2
- Make require ruby(abi) and buildarch: noarch conditional for fedora 5 or
  later to allow building on older fedora releases

* Mon Nov 13 2006 David Lutterkort <dlutter@redhat.com> - 0.20.1-1
- New version

* Mon Oct 23 2006 David Lutterkort <dlutter@redhat.com> - 0.20.0-1
- New version

* Tue Sep 26 2006 David Lutterkort <dlutter@redhat.com> - 0.19.3-1
- New version

* Mon Sep 18 2006 David Lutterkort <dlutter@redhat.com> - 0.19.1-1
- New version

* Thu Sep  7 2006 David Lutterkort <dlutter@redhat.com> - 0.19.0-1
- New version

* Tue Aug  1 2006 David Lutterkort <dlutter@redhat.com> - 0.18.4-2
- Use /usr/bin/ruby directly instead of /usr/bin/env ruby in
  executables. Otherwise, initscripts break since pidof can't find the
  right process

* Tue Aug  1 2006 David Lutterkort <dlutter@redhat.com> - 0.18.4-1
- New version

* Fri Jul 14 2006 David Lutterkort <dlutter@redhat.com> - 0.18.3-1
- New version

* Wed Jul  5 2006 David Lutterkort <dlutter@redhat.com> - 0.18.2-1
- New version

* Wed Jun 28 2006 David Lutterkort <dlutter@redhat.com> - 0.18.1-1
- Removed lsb-config.patch and yumrepo.patch since they are upstream now

* Mon Jun 19 2006 David Lutterkort <dlutter@redhat.com> - 0.18.0-1
- Patch config for LSB compliance (lsb-config.patch)
- Changed config moves /var/puppet to /var/lib/puppet, /etc/puppet/ssl
  to /var/lib/puppet, /etc/puppet/clases.txt to /var/lib/puppet/classes.txt,
  /etc/puppet/localconfig.yaml to /var/lib/puppet/localconfig.yaml

* Fri May 19 2006 David Lutterkort <dlutter@redhat.com> - 0.17.2-1
- Added /usr/bin/puppetrun to server subpackage
- Backported patch for yumrepo type (yumrepo.patch)

* Wed May  3 2006 David Lutterkort <dlutter@redhat.com> - 0.16.4-1
- Rebuilt

* Fri Apr 21 2006 David Lutterkort <dlutter@redhat.com> - 0.16.0-1
- Fix default file permissions in server subpackage
- Run puppetmaster as user puppet
- rebuilt for 0.16.0

* Mon Apr 17 2006 David Lutterkort <dlutter@redhat.com> - 0.15.3-2
- Don't create empty log files in post-install scriptlet

* Fri Apr  7 2006 David Lutterkort <dlutter@redhat.com> - 0.15.3-1
- Rebuilt for new version

* Wed Mar 22 2006 David Lutterkort <dlutter@redhat.com> - 0.15.1-1
- Patch0: Run puppetmaster as root; running as puppet is not ready
  for primetime

* Mon Mar 13 2006 David Lutterkort <dlutter@redhat.com> - 0.15.0-1
- Commented out noarch; requires fix for bz184199

* Mon Mar  6 2006 David Lutterkort <dlutter@redhat.com> - 0.14.0-1
- Added BuildRequires for ruby

* Wed Mar  1 2006 David Lutterkort <dlutter@redhat.com> - 0.13.5-1
- Removed use of fedora-usermgmt. It is not required for Fedora Extras and
  makes it unnecessarily hard to use this rpm outside of Fedora. Just
  allocate the puppet uid/gid dynamically

* Sun Feb 19 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-4
- Use fedora-usermgmt to create puppet user/group. Use uid/gid 24. Fixed
problem with listing fileserver.conf and puppetmaster.conf twice

* Wed Feb  8 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-3
- Fix puppetd.conf

* Wed Feb  8 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-2
- Changes to run puppetmaster as user puppet

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 0.13.0-1
- Don't mark initscripts as config files

* Mon Feb  6 2006 David Lutterkort <dlutter@redhat.com> - 0.12.0-2
- Fix BuildRoot. Add dist to release

* Tue Jan 17 2006 David Lutterkort <dlutter@redhat.com> - 0.11.0-1
- Rebuild

* Thu Jan 12 2006 David Lutterkort <dlutter@redhat.com> - 0.10.2-1
- Updated for 0.10.2 Fixed minor kink in how Source is given

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 0.10.1-3
- Added basic fileserver.conf

* Wed Jan 11 2006 David Lutterkort <dlutter@redhat.com> - 0.10.1-1
- Updated. Moved installation of library files to sitelibdir. Pulled
initscripts into separate files. Folded tools rpm into server

* Thu Nov 24 2005 Duane Griffin <d.griffin@psenterprise.com>
- Added init scripts for the client

* Wed Nov 23 2005 Duane Griffin <d.griffin@psenterprise.com>
- First packaging
