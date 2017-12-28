%include Solaris.inc
%include packagenamemacros.inc

%define perl_version 5.12
%define perl_vendorlib /usr/perl5/vendor_perl/%{perl_version}
%define tarball_name     munin

Name:      munin
IPS_package_name:        diagnostic/munin
Version:   2.0.30
Summary:   Network-wide graphing framework (grapher/gatherer)
License:   GPLv2 and Bitstream Vera
Group:     System Environment/Daemons
URL:       http://munin-monitoring.org/

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source0: http://downloads.sourceforge.net/sourceforge/munin/%{tarball_name}-%{version}.tar.gz
Source1:	munin-asyncd.xml
Source2:	svc-munin-asyncd
Source3:        SFEmunin-Makefile.config
Source4:        munin.logadm.conf
Source5:        munin-node.logadm.conf

Patch1: SFEmunin-SyncDictFile.patch
# Patch2: SFEmunin-2.0.19-makefile.patch
Patch3: munin-plugin-mysql_.patch

BuildRequires: library/perl-5/module-build-512
BuildRequires: library/perl-5/log-log4perl-512
BuildRequires: library/perl-5/net-server-512
BuildRequires: library/perl-5/net-ssleay-512
BuildRequires: library/perl-5/net-snmp-512
BuildRequires: library/perl-5/io-stringy-512
BuildRequires: library/perl-5/test-differences-512
BuildRequires: library/perl-5/test-longstring-512
BuildRequires: library/perl-5/cache-cache-512
BuildRequires: library/perl-5/cache-memcached-512
BuildRequires: library/perl-5/date-manip-512
BuildRequires: library/perl-5/db-file-512
BuildRequires: library/perl-5/file-copy-recursive-512
BuildRequires: library/perl-5/io-socket-inet6-512
BuildRequires: library/perl-5/lwp-512
BuildRequires: library/perl-5/net-cidr-512
BuildRequires: library/perl-5/rrdtool-512
BuildRequires: library/perl-5/uri-512
BuildRequires: library/perl-5/test-deep-512
BuildRequires: library/perl-5/test-mockmodule-512
BuildRequires: library/perl-5/file-slurp-512

# java buildrequires on fedora
# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# BuildRequires: java-1.6.0-devel
# BuildRequires: mx4j
# BuildRequires: jpackage-utils
# %endif

Requires: %{name}-common = %{version}
Requires: library/perl-5/net-server-512
Requires: library/perl-5/net-snmp-512
Requires: library/perl-5/rrdtool-512
Requires: library/perl-5/log-log4perl-512
Requires: library/perl-5/html-template-512
Requires: library/perl-5/io-socket-inet6-512
Requires: library/perl-5/uri-512
Requires: library/perl-5/file-copy-recursive-512
Requires: library/perl-5/date-manip-512
Requires: system/font/truetype/dejavu

# Requires: logrotate
# Requires: /bin/mail
# Requires(pre): shadow-utils
# Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# %if 0%{?rhel} > 5 || 0%{?fedora} > 6
# Requires: dejavu-sans-mono-fonts
# %else
# Requires: bitstream-vera-fonts
# %endif

%description
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains the grapher/gatherer. You will only need one instance of
it in your network. It will periodically poll all the nodes in your network
it's aware of for data, which it in turn will use to create graphs and HTML
pages, suitable for viewing with your graphical web browser of choice.

Munin is written in Perl, and relies heavily on Tobi Oetiker's excellent
RRDtool.

%package node
IPS_package_name:        diagnostic/munin/node
Group: System Environment/Daemons
Summary: Network-wide graphing framework (node)
BuildArchitectures: noarch
Requires: %{name}-common = %{version}
Requires: library/perl-5/net-server-512
Requires: library/perl-5/lwp-512
Requires: library/perl-5/net-cidr-512
# memcache plugin requires library/perl-5/cache-memcached-512
Requires: library/perl-5/cache-memcached-512
# Requires: procps >= 2.0.7
# Requires: sysstat, /usr/bin/which, hdparm
# Requires(pre): shadow-utils
# Requires(post): /sbin/chkconfig
# Requires(preun): /sbin/chkconfig
# Requires(preun): /sbin/service
# Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# mysql plugin requires Cache::Cache
Requires: library/perl-5/cache-cache-512

%description node
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains node software. You should install it on all the nodes
in your network. It will know how to extract all sorts of data from the
node it runs on, and will wait for the gatherer to request this data for
further processing.

It includes a range of plugins capable of extracting common values such as
cpu usage, network usage, load average, and so on. Creating your own plugins
which are capable of extracting other system-specific values is very easy,
and is often done in a matter of minutes. You can also create plugins which
relay information from other devices in your network that can't run Munin,
such as a switch or a server running another operating system, by using
SNMP or similar technology.

Munin is written in Perl, and relies heavily on Tobi Oetiker's excellent
RRDtool.

%package common
IPS_package_name:        diagnostic/munin/common
Group: System Environment/Daemons
Summary: Network-wide graphing framework (common files)
BuildArchitectures: noarch
# Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description common
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains common files that are used by both the server (munin)
and node (munin-node) packages.


%package async
IPS_package_name:        diagnostic/munin/async
Group: System Environment/Daemons
Summary: Network-wide graphing framework (async)
BuildArchitectures: noarch
Requires: %{name}-common = %{version}
Requires: library/perl-5/db-file-512
Requires: library/perl-5/net-server-512

%description async
munin-async

# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# %package java-plugins
# Group: System Environment/Daemons
# Summary: java-plugins for munin
# Requires: %{name}-node = %{version}
# BuildArchitectures: noarch

# %description java-plugins
# java-plugins for munin-node.
# %endif

%prep
%setup -q
%patch1
# %patch2
# %if 0%{?rhel} < 6 && 0%{?fedora} < 11
# %patch2 -p0
# %endif
%patch3 -p1

%build
export PATH=/usr/perl5/5.12/bin:$PATH
# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# export  CLASSPATH=plugins/javalib/org/munin/plugin/jmx:$(build-classpath mx4j):$CLASSPATH
# %endif
#make 	CONFIG=dists/redhat/Makefile.config
# make -f dists/sunos/Makefile

cp %{SOURCE3} .
make    CONFIG=SFEmunin-Makefile.config \
        PREFIX=%{_prefix} \
 	DOCDIR=%{_docdir}/%{name}-%{version} \
	MANDIR=%{_mandir} \
	LOGDIR=/var/log/munin \
	SPOOLDIR=/var/lib/munin/spool \
	CONFDIR=/etc/munin

make test

%install

## Node
# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# 	JAVALIBDIR=%{buildroot}%{_datadir}/java \
# %endif
make    CONFIG=SFEmunin-Makefile.config \
	PREFIX=%{buildroot}%{_prefix} \
 	DOCDIR=%{buildroot}%{_docdir}/%{name}-%{version} \
	MANDIR=%{buildroot}%{_mandir} \
    	CONFDIR=%{buildroot}/etc/munin \
	LOGDIR=%{buildroot}/var/log/munin \
	SPOOLDIR=%{buildroot}/var/lib/munin/spool \
	DESTDIR=%{buildroot} \
	install

# mkdir -p %{buildroot}/etc/rc.d/init.d
mkdir -p %{buildroot}/etc/munin/plugins
mkdir -p %{buildroot}/etc/munin/node.d
mkdir -p %{buildroot}/etc/munin/plugin-conf.d
mkdir -p %{buildroot}/etc/munin/conf.d
mkdir -p %{buildroot}/var/lib/munin
mkdir -p %{buildroot}/var/log/munin
mkdir -p %{buildroot}/var/svc/manifest/site
mkdir -p %{buildroot}/lib/svc/method

install -m0644 dists/tarball/plugins.conf %{buildroot}/etc/munin/plugin-conf.d/munin-node
install -m0444 build/resources/solaris-smf/munin-node.xml %{buildroot}/var/svc/manifest/site
install -m0555 build/resources/solaris-smf/munin-node %{buildroot}/lib/svc/method

#
# remove the Sybase plugin for now, as they need perl modules
# that are not in extras. We can readd them when/if those modules are added.
#
rm -f %{buildroot}/usr/share/munin/plugins/sybase_space

## Server

mkdir -p %{buildroot}/var/www/html/munin
# mkdir -p %{buildroot}/var/log/munin
mkdir -p %{buildroot}/var/spool/cron/crontabs
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

install -m 0600 build/resources/crontab-generic-munin %{buildroot}/var/spool/cron/crontabs/munin
cp -a master/www/* %{buildroot}/var/www/html/munin/

# install config for sendmail under fedora
# install -m 0644 %{SOURCE1} %{buildroot}/etc/munin/plugin-conf.d/sendmail
# install config for hddtemp_smartctl
# install -m 0644 %{SOURCE2} %{buildroot}/etc/munin/plugin-conf.d/hddtemp_smartctl
# install config for postfix under fedora
# install -m 0644 %{SOURCE6} %{buildroot}/etc/munin/plugin-conf.d/postfix
rm -f $RPM_BUILD_ROOT/usr/lib/munin-jmx-plugins.jar
rm -f $RPM_BUILD_ROOT/usr/share/munin/munin-jmx-plugins.jar
# rm -r $RPM_BUILD_ROOT/usr/lib
rm -rf $RPM_BUILD_ROOT/etc/rc.d
rm -rf $RPM_BUILD_ROOT/var/run
# rm -rf $RPM_BUILD_ROOT/var/lib

# Use system font
rm -f $RPM_BUILD_ROOT/%{_datadir}/munin/DejaVuSansMono.ttf
rm -f $RPM_BUILD_ROOT/%{_datadir}/munin/DejaVuSans.ttf

install -d 0755 %{buildroot}%/var/svc/manifest/site
install -m 0644 %{SOURCE1} %{buildroot}%/var/svc/manifest/site
install -d 0755 %{buildroot}%/lib/svc/method
install -m 0555 %{SOURCE2} %{buildroot}%/lib/svc/method

# install logadm config files
mkdir -p $RPM_BUILD_ROOT/etc/logadm.d
install -m 0444 %{SOURCE4} $RPM_BUILD_ROOT/etc/logadm.d
install -m 0444 %{SOURCE5} $RPM_BUILD_ROOT/etc/logadm.d

%clean
rm -rf $RPM_BUILD_ROOT

# #
# # node package scripts
# #
# %pre node
# getent group munin >/dev/null || groupadd -r munin
# getent passwd munin >/dev/null || \
# useradd -r -g munin -d /var/lib/munin -s /sbin/nologin \
#     -c "Munin user" munin
# exit 0

# %post node
# /sbin/chkconfig --add munin-node
# # Only run configure on a new install, not an upgrade.
# if [ "$1" = "1" ]; then
#      /usr/sbin/munin-node-configure --shell 2> /dev/null | sh >& /dev/null || :
# fi

# %preun node
# test "$1" != 0 || %{_initrddir}/munin-node stop &>/dev/null || :
# test "$1" != 0 || /sbin/chkconfig --del munin-node

# #
# # main package scripts
# #
# %pre
# getent group munin >/dev/null || groupadd -r munin
# getent passwd munin >/dev/null || \
# useradd -r -g munin -d /var/lib/munin -s /sbin/nologin \
#     -c "Munin user" munin
# exit 0

%actions common
group groupname="munin"
user ftpuser=false gcos-field="munin Reserved UID" username="munin" password=NP group="munin"

%files
%defattr(-, root, bin)
%dir %attr(0755, root, other) %{_docdir}
%doc %{_docdir}/%{name}-%{version}/
%{_bindir}/munin-cron
%{_bindir}/munindoc
%{_bindir}/munin-check
%dir %attr(0755, root, sys) %{_datadir}
%dir %{_datadir}/munin
%{_datadir}/munin/munin-graph
%{_datadir}/munin/munin-html
%{_datadir}/munin/munin-limits
%{_datadir}/munin/munin-update
%{perl_vendorlib}/Munin/Master
%dir %attr(0755, root, sys) /etc
%dir %attr(0755, root, sys) /etc/logadm.d
%attr(0444, root, sys) /etc/logadm.d/munin.logadm.conf
%dir %attr(0755, root, sys) /etc/munin
%dir %attr(0755, root, sys) /etc/munin/conf.d
%dir %attr(0755, root, sys) /etc/munin/munin-conf.d
%dir %attr(0755, root, sys) /etc/munin/templates
%attr(0755, root, sys) /etc/munin/static
%config(noreplace) /etc/munin/templates/*
# %config(noreplace) /etc/cron.d/munin
%dir %attr(0755, root, sys) /var
%dir %attr(0755, root, sys) /var/spool/cron
%dir %attr(0755, root, sys) /var/spool/cron/crontabs
%config(noreplace) %attr(0600, root, sys) /var/spool/cron/crontabs/munin
%config(noreplace) /etc/munin/munin.conf
# %config(noreplace) /etc/logrotate.d/munin
%attr(0755, root, other) %dir /var/lib
%attr(-, munin, munin) %dir /var/lib/munin
%attr(-, munin, munin) %dir /var/lib/munin/plugin-state
# %attr(-, munin, munin) %dir /var/run/munin
%dir %attr(0755, root, sys) /var/log
%attr(-, munin, munin) %dir /var/log/munin
%attr(-, munin, munin) /var/www/html/munin
%dir %attr(0755, root, sys) /usr
%doc %{_mandir}/man8/munin*
%doc %{_mandir}/man5/munin.conf*

%files node
%defattr(-, root, bin)
%dir %attr(0755, root, sys) /etc
%dir %attr(0755, root, sys) /etc/logadm.d
%attr(0444, root, sys) /etc/logadm.d/munin-node.logadm.conf
%dir %attr(0755, root, sys) /etc/munin
%dir %attr(0755, root, sys) /etc/munin/plugin-conf.d
%dir %attr(0755, root, sys) /etc/munin/node.d
%config(noreplace) /etc/munin/munin-node.conf
%config(noreplace) /etc/munin/plugin-conf.d/munin-node
# %config(noreplace) /etc/munin/plugin-conf.d/munin-node
# %config(noreplace) /etc/munin/plugin-conf.d/sendmail
# %config(noreplace) /etc/munin/plugin-conf.d/hddtemp_smartctl
# %config(noreplace) /etc/munin/plugin-conf.d/postfix
# %config(noreplace) /etc/logrotate.d/munin-node
# /etc/rc.d/init.d/munin-node
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/munin-node
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/site
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/site/munin-node.xml
%{_sbindir}/munin-run
%{_sbindir}/munin-node
%{_sbindir}/munin-node-configure
%dir %attr(0755, root, sys) /var/log
%attr(-, munin, munin) %dir /var/log/munin
%dir %attr(0755, root, sys) %{_datadir}
%dir %{_datadir}/munin
%dir /etc/munin/plugins
%attr(0755, root, other) %dir /var/lib
%attr(-, munin, munin) %dir /var/lib/munin
%dir %attr(-, munin, munin) /var/lib/munin/plugin-state
%{_datadir}/munin/plugins/
%dir %attr(0755, root, other) %{_docdir}
%doc %{_docdir}/%{name}-%{version}/
%attr(0755, root, sys) %dir /usr
%attr(0755, root, bin) %dir %{_mandir}
%attr(0755, root, bin) %dir %{_mandir}/man1
%attr(0755, root, bin) %dir %{_mandir}/man3
%attr(0755, root, bin) %dir %{_mandir}/man5
%doc %{_mandir}/man5/munin-node*
%doc %{_mandir}/man3/Munin*
%doc %{_mandir}/man1/munin*
%{perl_vendorlib}/Munin/Node
%{perl_vendorlib}/Munin/Plugin*

%files common
%defattr(-, root, bin)
%doc Announce-2.0 ChangeLog COPYING HACKING.pod INSTALL README UPGRADING UPGRADING-1.4 perltidyrc
%attr(0755, root, sys) %dir /usr
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_docdir}
%dir %{perl_vendorlib}/Munin
%{perl_vendorlib}/Munin/Common
%dir %attr (0755, root, sys) /var
%dir %attr(0755, root, other) /var/lib
%dir %attr(-, munin, munin) /var/lib/munin
/var/lib/munin/spool
/var/lib/munin/cgi-tmp
/usr/share/munin/munin-storable2datafile
/usr/share/munin/munin-datafile2storable
/usr/sbin/munin-sched

%files async
%defattr(-, root, bin)
%dir %attr(0755, root, sys) /usr
%dir %attr(0755, root, sys) %{_datadir}
/usr/share/munin/munin-async
/usr/share/munin/munin-asyncd
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/site
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/site/munin-asyncd.xml
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/svc-munin-asyncd


# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# %files java-plugins
# %defattr(-, root, root)
# %{_datadir}/java/%{name}-jmx-plugins.jar
# %endif

%changelog
* Thu Apr 27 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.30
- Fri Dec 19 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add patch3 to make mysql_innodb_insert_buf to work
* Sun Dec 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Thu Dec 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.25
* Tue Jun 10 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.21
* Wed Mar 05 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.19
* Sat Jan 25 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.17
* Thu Jun 06 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add logadm config files
* Mon May 13 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.14
- add Requires
* Sat Mar 23 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.12
* Wed Feb 20 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires

* Tue Feb 19 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix & add BuildRequires

* Wed Jan 16 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.0.11.1

* Wed Jan 16 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.0.10

* Sat Dec 15 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix attr

* Mon Dec 10 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.0.9

* Wed Nov 07 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
- modify for 11.1

* Fri Oct 12 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.7
- modify some attr 755 to 0755

* Tue Oct 02 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add async subpackage for munin-aync
- add SMF manifest and script for munin-asyncd

* Wed Sat 29 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add patch1 to avoid flock error

* Wed Sep 26 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires to munin

* Tue Sep 25 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires to munin

* Mon Sep 24 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires to munin and munin-node

* Mon Sep 10 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.0.6

* Sun Aug 26 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify make options

* Fri Aug 24 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.0.4

* Fri Jun  29 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.0.1

* Thu May  3 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- import to jposug
- update to 1.4.7

* Tue Feb 08 2011 Kevin Fenzi <kevin@tummy.com> - 1.4.5-5
- Add patch for uppercase nodes (fixes 673263)

* Wed Jul 07 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-4
- Move docs to common subpackage to make sure COPYING is installed.

* Sat Jul 03 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-3
- Add /etc/munin/node.d dir

* Sat Jun 12 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-2
- Add /etc/munin/conf.d/ dir

* Sat Jun 05 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.5-1
- Update to 1.4.5

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.4.4-2
- Mass rebuild with perl-5.12.0

* Mon Mar 01 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.4-1
- Update to 1.4.4
- Add more doc files. Fixes bug #563824
- fw_forwarded_local fixed upstream in 1.4.4. Fixes bug #568500

* Sun Jan 17 2010 Kevin Fenzi <kevin@tummy.com> - 1.4.3-2
- Fix owner on state files.
- Add some BuildRequires.
- Make munin-node-configure only run on install, not upgrade. bug 540687

* Thu Dec 31 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.3-1
- Update to 1.4.3

* Thu Dec 17 2009 Ingvar Hagelund <ingvar@linpro.no> - 1.4.2-1
- New upstream release
- Removed upstream packaged fonts
- Added a patch that makes rrdtool use the system bitstream vera fonts on
  rhel < 6 and fedora < 11

* Fri Dec 11 2009 Ingvar Hagelund <ingvar@linpro.no> - 1.4.1-3
- More correct fedora and el versions for previous font path fix
- Added a patch that fixes a quoting bug in GraphOld.pm, fixing fonts on el4

* Wed Dec 09 2009 Ingvar Hagelund <ingvar@linpro.no> - 1.4.1-2
- Remove jmx plugins when not supported (like on el4 and older fedora)
- Correct font path on older distros like el5, el4 and fedora<11

* Fri Dec 04 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.1-1
- Update to 1.4.1

* Sat Nov 28 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.0-1
- Update to final 1.4.0 version

* Sat Nov 21 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.0-0.1.beta
- Update to beta 1.4.0 version.
- Add common subpackage for common files.

* Sun Nov 08 2009 Kevin Fenzi <kevin@tummy.com> - 1.4.0-0.1.alpha
- Initial alpha version of 1.4.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Andreas Thienemann <andreas@bawue.net> - 1.2.6-8
- Updated dependencies to better reflect plugin requirements
- Added hddtemp_smartctl patch to only scan for standby state on /dev/[sh]d? devices.

* Sat Jan 17 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-7
- Adjust font requires for new dejavu-sans-mono-fonts name (fixes #480463)

* Mon Jan 12 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-6
- Fix to require the correct font

* Sun Jan 11 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-5
- Switch to using dejavu-fonts instead of bitstream-vera

* Sun Jan 04 2009 Kevin Fenzi <kevin@tummy.com> - 1.2.6-4
- Require bitstream-vera-fonts-sans-mono for Font (fixes #477428)

* Mon Aug 11 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.6-3
- Move Munin/Plugin.pm to the node subpackage (fixes #457403)

* Sat Jul 12 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.6-2
- Apply postfix patch (fixes #454159)
- Add perl version dep and remove unneeded perl-HTML-Template (fixes #453923)

* Fri Jun 20 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.6-1
- Upgrade to 1.2.6

* Tue May 20 2008 Kevin Fenzi <kevin@tummy.com> - 1.2.5-5
- Rebuild for new perl

* Wed Dec 26 2007 Kevin Fenzi <kevin@tummy.com> - 1.2.5-4
- Add patch to fix ampersand and degrees in plugins (fixes #376441)

* Fri Nov 30 2007 Kevin Fenzi <kevin@tummy.com> - 1.2.5-3
- Removed unnneeded plugins.conf file (fixes #288541)
- Fix license tag.
- Fix ip_conntrack monitoring (fixes #253192)
- Switch to new useradd guidelines.

* Tue Mar 27 2007 Kevin Fenzi <kevin@tummy.com> - 1.2.5-2
- Fix directory ownership (fixes #233886)

* Tue Oct 17 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.5-1
- Update to 1.2.5
- Fix HD stats (fixes #205042)
- Add in logrotate scripts that seem to have been dropped upstream

* Sun Aug 27 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-10
- Rebuild for fc6

* Tue Jun 27 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-9
- Re-enable snmp plugins now that perl-Net-SNMP is available (fixes 196588)
- Thanks to Herbert Straub <herbert@linuxhacker.at> for patch.
- Fix sendmail plugins to look in the right place for the queue

* Sat Apr 22 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-8
- add patch to remove unneeded munin-nagios in cron.
- add patch to remove buildhostname in munin.conf (fixes #188928)
- clean up prep section of spec.

* Fri Feb 24 2006 Kevin Fenzi <kevin@scrye.com> - 1.2.4-7
- Remove bogus Provides for perl RRDs (fixes #182702)

* Thu Feb 16 2006 Kevin Fenzi <kevin@tummy.com> - 1.2.4-6
- Readded old changelog entries per request
- Rebuilt for fc5

* Sat Dec 24 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-5
- Fixed ownership for /var/log/munin in node subpackage (fixes 176529)

* Wed Dec 14 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-4
- Fixed ownership for /var/lib/munin in node subpackage

* Wed Dec 14 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-3
- Fixed libdir messup to allow builds on x86_64

* Mon Dec 12 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-2
- Removed plugins that require Net-SNMP and Sybase

* Tue Dec  6 2005 Kevin Fenzi <kevin@tummy.com> - 1.2.4-1
- Inital cleanup for fedora-extras

* Thu Apr 21 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-4
- Fixed a bug in the iostat plugin

* Wed Apr 20 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-3
- Added the missing /var/run/munin

* Tue Apr 19 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-2
- Removed a lot of unecessary perl dependencies

* Mon Apr 18 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.3-1
- Sync with svn

* Tue Mar 22 2005 Ingvar Hagelund <ingvar@linpro.no> - 1.2.2-5
- Sync with release of 1.2.2
- Add some nice text from the suse specfile
- Minimal changes in the header
- Some cosmetic changes
- Added logrotate scripts (stolen from debian package)

* Sun Feb 01 2004 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS. Version 1.0.0pre2

* Sun Jan 18 2004 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS. Change names to munin.

* Fri Oct 31 2003 Ingvar Hagelund <ingvar@linpro.no>
- Lot of small fixes. Now builds on more RPM distros

* Wed May 21 2003 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS
- 0.9.5-1

* Tue Apr  1 2003 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS
- Makefile-based install of core files
- Build doc (only pod2man)

* Thu Jan  9 2003 Ingvar Hagelund <ingvar@linpro.no>
- Sync with CVS, auto rpmbuild

* Thu Jan  2 2003 Ingvar Hagelund <ingvar@linpro.no>
- Fix spec file for RedHat 8.0 and new version of lrrd

* Wed Sep  4 2002 Ingvar Hagelund <ingvar@linpro.no>
- Small bugfixes in the rpm package

* Tue Jun 18 2002 Kjetil Torgrim Homme <kjetilho@linpro.no>
- new package
