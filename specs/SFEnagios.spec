#
# spec file for package SFEnagios
#
# includes module(s): nagios
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc

Name:		SFEnagios
IPS_package_name:        diagnostic/nagios
Version:	3.5.1
Summary:	Host/service/network monitoring program
Group:		Applications/System
License:	GPLv2
URL:		http://www.nagios.org/
Source:		%{sf_download}/nagios/nagios-%{version}.tar.gz
Source1:	nagios.xml
Source2:	svc-nagios
# Patch1:		SFEnagios-3.3.1.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

BuildRequires:	SUNWsndmu
Requires:	SUNWsndmu
BuildRequires:	SUNWjpg-devel
Requires:	SUNWjpg
BuildRequires:	library/gd
Requires:	library/gd
Requires:	diagnostic/nagios/common
Requires:	diagnostic/nagios/plugins

%description
Nagios is a program that will monitor hosts and services on your
network.  It has the ability to send email or page alerts when a
problem arises and when a problem is resolved.  Nagios is written
in C and is designed to run under Linux (and some other *NIX
variants) as a background process, intermittently running checks
on various services that you specify.

The actual service checks are performed by separate "plugin" programs
which return the status of the checks to Nagios. The plugins are
available at http://sourceforge.net/projects/nagiosplug.

This package provides the core program, web interface, and documentation
files for Nagios. Development files are built as a separate package.

%package common
IPS_package_name:        diagnostic/nagios/common
Group:		Applications/System
Summary:	Provides common directories, uid and gid among nagios-related packages
SUNW_BaseDir:	/

%description common
Provides common directories, uid and gid among nagios-related packages.


%package devel
IPS_package_name:        diagnostic/nagios/devel
Group:		Applications/System
Summary:	Provides include files that Nagios-related applications may compile against
Requires:	%{name}
SUNW_BaseDir:	%{_basedir}


%description devel
Nagios is a program that will monitor hosts and services on your
network. It has the ability to email or page you when a problem arises
and when a problem is resolved. Nagios is written in C and is
designed to run under Linux (and some other *NIX variants) as a
background process, intermittently running checks on various services
that you specify.

This package provides include files that Nagios-related applications
may compile against.


%prep
%setup -q -n nagios
# %patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CC=/usr/bin/gcc
# export CFLAGS="%{optflags}"
# export LDFLAGS="%{_ldflags}"

./configure \
	--prefix=%{_datadir}/nagios \
	--exec-prefix=%{_libdir}/nagios \
	--with-httpd-conf=%{_datadir}/nagios/httpd \
	--with-init-dir=%{_initrddir} \
	--with-cgiurl=/nagios/cgi-bin \
	--with-htmlurl=/nagios \
	--with-lockfile=%{_localstatedir}/run/nagios.pid \
	--libdir=%{_libdir}/nagios \
	--with-nagios-user=nagios \
	--with-nagios-grp=nagios \
	--bindir=%{_sbindir} \
	--sbindir=%{_libdir}/nagios/cgi-bin \
	--libexecdir=%{_libdir}/nagios/plugins \
	--sysconfdir=%{_sysconfdir}/nagios \
	--localstatedir=%{_localstatedir}/log/nagios \
	--datadir=%{_datadir}/nagios/html \
	--with-gd-lib=%{_libdir} \
	--with-gd-inc=%{_includedir}/gd2 \
	--with-template-objects \
	--with-template-extinfo
	# --enable-embedded-perl \
	# --with-perlcache \

make -j$CPUS all


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_datadir}/nagios/httpd

make DESTDIR=%{buildroot} INIT_OPTS="" INSTALL_OPTS="" COMMAND_OPTS="" CGIDIR="%{_libdir}/nagios/cgi-bin" CFGDIR="%{_sysconfdir}/nagios" fullinstall

install -d -m 0755 %{buildroot}%{_sysconfdir}/nagios/objects
install -d -m 0755 %{buildroot}%{_sysconfdir}/nagios/private
install -d -m 0755 %{buildroot}%{_libdir}/nagios/plugins/eventhandlers
install -d -m 0775 %{buildroot}%{_includedir}/nagios
install -D -m 0644 include/locations.h %{buildroot}%{_includedir}/nagios/locations.h
install -d -m 0755 %{buildroot}%{_localstatedir}/spool/nagios

install -m 0644 sample-config/cgi.cfg %{buildroot}%{_sysconfdir}/nagios/cgi.cfg
install -m 0644 sample-config/mrtg.cfg %{buildroot}%{_sysconfdir}/nagios/mrtg.cfg
install -m 0644 sample-config/nagios.cfg %{buildroot}%{_sysconfdir}/nagios/nagios.cfg
install -m 0644 sample-config/resource.cfg %{buildroot}%{_sysconfdir}/nagios/resource.cfg
install -m 0644 sample-config/template-object/commands.cfg  %{buildroot}%{_sysconfdir}/nagios/objects/commands.cfg
install -m 0644 sample-config/template-object/contacts.cfg %{buildroot}%{_sysconfdir}/nagios/objects/contacts.cfg
install -m 0644 sample-config/template-object/localhost.cfg %{buildroot}%{_sysconfdir}/nagios/objects/localhost.cfg
install -m 0644 sample-config/template-object/printer.cfg %{buildroot}%{_sysconfdir}/nagios/objects/printer.cfg
install -m 0644 sample-config/template-object/switch.cfg %{buildroot}%{_sysconfdir}/nagios/objects/switch.cfg
install -m 0644 sample-config/template-object/templates.cfg %{buildroot}%{_sysconfdir}/nagios/objects/templates.cfg
install -m 0644 sample-config/template-object/timeperiods.cfg %{buildroot}%{_sysconfdir}/nagios/objects/timeperiods.cfg
install -m 0644 sample-config/template-object/windows.cfg %{buildroot}%{_sysconfdir}/nagios/objects/windows.cfg

install -d -m 0755 %{buildroot}%{_datadir}/nagios/html/includes/rss/extlib
install -d -m 0755 %{buildroot}%{_datadir}/nagios/html/includes/rss/htdocs
install -d -m 0755 %{buildroot}%{_datadir}/nagios/html/includes/rss/scripts

install -d 0755 %{buildroot}%/var/svc/manifest/site
install -m 0644 %{SOURCE1} %{buildroot}%/var/svc/manifest/site
install -d 0755 %{buildroot}%/lib/svc/method
install -m 0555 %{SOURCE2} %{buildroot}%/lib/svc/method
rm -rf %{buildroot}%{_initrddir}

%clean
rm -rf %{buildroot}


%pre common
test -x $BASEDIR/var/lib/postrun/postrun || exit 0
( echo '/usr/sbin/groupadd nagios';
  echo '/usr/sbin/useradd -d %{_localstatedir}/spool/nagios -s /bin/true -g nagios nagios';
) | $BASEDIR/var/lib/postrun/postrun -i -a

%postun common
test -x $BASEDIR/var/lib/postrun/postrun || exit 0
( echo '/usr/sbin/userdel nagios';
  echo '/usr/sbin/groupdel nagios';
) | $BASEDIR/var/lib/postrun/postrun -i -a

%actions common
group groupname="nagios"
user ftpuser=false gcos-field="Nagios Reserved UID" username="nagios" password=NP group="nagios"
# need to add user webservd to nagios group

%files
%defattr(-, root, bin)
%doc Changelog INSTALLING LICENSE README UPGRADING
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/nagios/httpd/nagios.conf
# %{_datadir}/nagios/html/robots.txt
# %{_datadir}/nagios/html/[^i]*
# %{_datadir}/nagios/html/contexthelp
# %{_datadir}/nagios/html/[^d]*
# %{_datadir}/nagios/html/[^m]*
# %{_datadir}/nagios/html/[^s]*
# %attr(0644, root, bin) %config(noreplace) %{_datadir}/nagios/html/config.inc.php
%{_datadir}/nagios/html
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_sbindir}
%{_sbindir}/*
%{_libdir}/nagios/cgi-bin/*cgi
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins/eventhandlers
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/site
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/site/nagios.xml
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/svc-nagios
%dir %attr(0755, root, sys) %{_sysconfdir}
%dir %attr(0755, root, nagios) %{_sysconfdir}/nagios
%config(noreplace) %{_sysconfdir}/nagios/*cfg
%dir %attr(0750, root, nagios) %{_sysconfdir}/nagios/objects
%config(noreplace) %{_sysconfdir}/nagios/objects/*cfg
%dir %attr(0750, root, nagios) %{_sysconfdir}/nagios/private

%files common
%defattr(-, root, bin)
## %{_initrddir}/nagios
%dir %attr(0755, root, sys) %{_sysconfdir}
%dir %attr(0755, root, nagios) %{_sysconfdir}/nagios
%dir %attr(0755, root, sys) %{_localstatedir}
%dir %attr(0755, root, sys) %{_localstatedir}/log
%dir %attr(0755, root, bin) %{_localstatedir}/spool
%dir %attr(0755, nagios, nagios) %{_localstatedir}/spool/nagios
%dir %attr(0750, nagios, webservd) %{_localstatedir}/log/nagios
%dir %attr(0750, nagios, webservd) %{_localstatedir}/log/nagios/archives
%dir %attr(2775, nagios, webservd) %{_localstatedir}/log/nagios/rw
%dir %attr(0750, nagios, nagios) %{_localstatedir}/log/nagios/spool/
%dir %attr(0750, nagios,nagios) %{_localstatedir}/log/nagios/spool/checkresults

%files devel
%defattr(-, root, bin)
%{_includedir}/nagios

%changelog
* Mon Apr 18 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix file list
* Sat Nov 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete apache-22 from Requries and BuildRequires because Oracle Solaris 11.3 provides apache-22 and apache-24
- fix Requires
* Tue Nov 05 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.5.1

* Thu Mar 21 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.5.0

* Sat Dec 15 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix attr

* Wed Dec 12 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.4.3

* Wed Nov 14 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.4.2

* Thu Jul 17 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- set %actions for nagios/common
- move SMF files from nagios/common to nagios

* Thu May 17 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 3.4.1

* Wed May  9 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 3.4.0
- remove patch1

* Tue Mar 27 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify owner, group and permission for Solaris 11

* Tue Aug 23 2011 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update to 3.3.1

* Tue May 17 2011 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add requires. apache-php5 and naios/plugins.
- add "--sbindir=%{_libdir}/nagios/cgi-bin" to configure
- modify attr of %{_sysconfdir}/nagios

* Mon May 16 2011 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify SMF manifest
- modify SMF init file

* Tue May 10 2011 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add IPS_package_name to divide package
- mv init script to /lib/svc/method
- modify init script to adjust some file pathes
- modify owner of %{_localstatedir}/log/nagios


* Sun Mar 06 2011 - Milan Jurik
- fix config issues
* Sat Mar 05 2011 - Milan Jurik
- initial spec based on Fedora
