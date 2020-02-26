%include Solaris.inc
%include packagenamemacros.inc

%define perl_version 5.26jposug
%define perl_vendorlib /opt/jposug/perl5/vendor_perl/5.26
%define tarball_name     munin
%define _prefix /opt/jposug

Name:      munin
IPS_package_name:        jposug/diagnostic/munin
Version:   2.0.56
Summary:   Network-wide graphing framework (grapher/gatherer)
License:   GPLv2 and Bitstream Vera
Group:     System Environment/Daemons
URL:       http://munin-monitoring.org/

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Source0: http://downloads.sourceforge.net/sourceforge/munin/%{tarball_name}-%{version}.tar.gz
Source0:        http://downloads.munin-monitoring.org/munin/stable/%{version}/%{tarball_name}-%{version}.tar.gz
Source1:        munin-asyncd.xml
Source2:        svc-munin-asyncd
Source3:        SFEmunin-Makefile-jposug.config
Source4:        munin.logadm.conf
Source5:        munin-node.logadm.conf

Patch1: SFEmunin-SyncDictFile.patch
# Patch2: SFEmunin-2.0.19-makefile.patch
# Patch3: munin-plugin-mysql_.patch

BuildRequires: library/perl-5/module-build-526jposug
BuildRequires: library/perl-5/log-log4perl-526jposug
BuildRequires: library/perl-5/net-server-526jposug
BuildRequires: library/perl-5/net-ssleay-526jposug
BuildRequires: library/perl-5/net-snmp-526jposug
BuildRequires: library/perl-5/io-stringy-526jposug
BuildRequires: library/perl-5/test-differences-526jposug
BuildRequires: library/perl-5/test-longstring-526jposug
BuildRequires: library/perl-5/cache-cache-526jposug
BuildRequires: library/perl-5/cache-memcached-526jposug
BuildRequires: library/perl-5/date-manip-526jposug
BuildRequires: library/perl-5/db_file-526jposug
BuildRequires: library/perl-5/file-copy-recursive-526jposug
BuildRequires: library/perl-5/io-socket-inet6-526jposug
BuildRequires: library/perl-5/lwp-526jposug
BuildRequires: library/perl-5/net-cidr-526jposug
BuildRequires: library/perl-5/rrdtool-526jposug
BuildRequires: library/perl-5/uri-526jposug
BuildRequires: library/perl-5/test-deep-526jposug
BuildRequires: library/perl-5/test-mockmodule-526jposug
BuildRequires: library/perl-5/file-slurp-526jposug

# java buildrequires on fedora
# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# BuildRequires: java-1.6.0-devel
# BuildRequires: mx4j
# BuildRequires: jpackage-utils
# %endif

Requires: %{name}-common = %{version}
Requires: library/perl-5/net-server-526jposug
Requires: library/perl-5/net-snmp-526jposug
Requires: library/perl-5/rrdtool-526jposug
Requires: library/perl-5/log-log4perl-526jposug
Requires: library/perl-5/html-template-526jposug
Requires: library/perl-5/io-socket-inet6-526jposug
Requires: library/perl-5/uri-526jposug
Requires: library/perl-5/file-copy-recursive-526jposug
Requires: library/perl-5/date-manip-526jposug
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
IPS_package_name:        jposug/diagnostic/munin/node
Group: System Environment/Daemons
Summary: Network-wide graphing framework (node)
BuildArchitectures: noarch
Requires: %{name}-common = %{version}
Requires: library/perl-5/net-server-526jposug
Requires: library/perl-5/lwp-526jposug
Requires: library/perl-5/net-cidr-526jposug
# memcache plugin requires library/perl-5/cache-memcached-526jposug
Requires: library/perl-5/cache-memcached-526jposug
# Requires: procps >= 2.0.7
# Requires: sysstat, /usr/bin/which, hdparm
# Requires(pre): shadow-utils
# Requires(post): /sbin/chkconfig
# Requires(preun): /sbin/chkconfig
# Requires(preun): /sbin/service
# Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# mysql plugin requires Cache::Cache
Requires: library/perl-5/cache-cache-526jposug

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
IPS_package_name:        jposug/diagnostic/munin/common
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
IPS_package_name:        jposug/diagnostic/munin/async
Group: System Environment/Daemons
Summary: Network-wide graphing framework (async)
BuildArchitectures: noarch
Requires: %{name}-common = %{version}
Requires: library/perl-5/db-file-526jposug
Requires: library/perl-5/net-server-526jposug

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
# %patch3 -p1

%build
export PATH=/opt/jposug/perl5/5.26/bin:$PATH
# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# export  CLASSPATH=plugins/javalib/org/munin/plugin/jmx:$(build-classpath mx4j):$CLASSPATH
# %endif
#make 	CONFIG=dists/redhat/Makefile.config
# make -f dists/sunos/Makefile

cp %{SOURCE3} .
make    CONFIG=SFEmunin-Makefile-jposug.config \
        PREFIX=%{_prefix} \
 	DOCDIR=%{_docdir}/%{name}-%{version} \
	MANDIR=%{_mandir} \
	LOGDIR=/var/log/munin \
	SPOOLDIR=/var/lib/munin/spool \
	CONFDIR=/etc/munin \
        PERL='/opt/jposug/perl5/5.26/bin/perl -I./'

# make test

%install
rm -rf %{buildroot}


## Node
# %if 0%{?rhel} > 4 || 0%{?fedora} > 6
# 	JAVALIBDIR=%{buildroot}%{_datadir}/java \
# %endif
make    CONFIG=SFEmunin-Makefile-jposug.config \
	PREFIX=%{buildroot}%{_prefix} \
 	DOCDIR=%{buildroot}%{_docdir}/%{name}-%{version} \
	MANDIR=%{buildroot}%{_mandir} \
    	CONFDIR=%{buildroot}/etc/munin \
	LOGDIR=%{buildroot}/var/log/munin \
	SPOOLDIR=%{buildroot}/var/lib/munin/spool \
	DESTDIR=%{buildroot} \
        PERL=/opt/jposug/perl5/5.26/bin/perl \
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
rm -f $RPM_BUILD_ROOT/opt/jposug/lib/munin-jmx-plugins.jar
rm -f $RPM_BUILD_ROOT/opt/jposug/share/munin/munin-jmx-plugins.jar

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

sed -i.bak -e 's!/usr/bin/perl!/opt/jposug/perl5/5.26/bin/perl!' %{buildroot}%{_prefix}/{bin,sbin}/*
rm -f %{buildroot}%{_prefix}/{bin,sbin}/*.bak

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
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) /opt/jposug
%dir %attr(0755, root, bin) %{_bindir}
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
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) /opt/jposug
%dir %attr(0755, root, bin) %{_sbindir}
%{_bindir}/munin-get
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
%dir %attr(0755, root, sys) %{_datadir}
/opt/jposug/share/munin/munin-storable2datafile
/opt/jposug/share/munin/munin-datafile2storable
%dir %attr(0755, root, other) %{_docdir}
%dir %{perl_vendorlib}/Munin
%{perl_vendorlib}/Munin/Common
%dir %attr (0755, root, sys) /var
%dir %attr(0755, root, other) /var/lib
%dir %attr(-, munin, munin) /var/lib/munin
/var/lib/munin/spool
/var/lib/munin/cgi-tmp
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) /opt/jposug
%dir %attr(0755, root, bin) %{_sbindir}
# /opt/jposug/sbin/munin-sched

%files async
%defattr(-, root, bin)
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) /opt/jposug
%dir %attr(0755, root, sys) %{_datadir}
/opt/jposug/share/munin/munin-async
/opt/jposug/share/munin/munin-asyncd
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
* Wed Feb 26 2020 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.56
* Mon Oct 28 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.50
* Tue Feb 26 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.45
* Fri Feb 08 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
