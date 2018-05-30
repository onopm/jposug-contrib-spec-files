#
# spec file for package SFEnagios
#
# includes module(s): nagios
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc
%include packagenamemacros.inc
#%define cc_is_gcc 1

%define tarball_name    nrpe
%define tarball_version 3.2.1

Name:		SFEnagios-nrpe
IPS_package_name:        diagnostic/nagios/nrpe
Version:	%{tarball_version}
Summary:	NRPE - Nagios Remote Plugin Executor
Group:		Applications/System
License:	GPL
URL:		http://www.nagios.org/
Source:         https://github.com/NagiosEnterprises/nrpe/archive/nrpe-%{tarball_version}.tar.gz
Source1:	nagios-nrpe.xml
Source2:	svc-nagios-nrpe
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       diagnostic/nagios/common

%description
NRPE allows you to remotely execute Nagios plugins on other Linux/Unix machines. This allows you to monitor remote machine metrics (disk usage, CPU load, etc.). NRPE can also communicate with some of the Windows agent addons, so you can execute scripts and check metrics on remote Windows machines as well.

%prep
%setup -q -n %{tarball_name}-%{tarball_name}-%{tarball_version}

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CC='/usr/bin/gcc -m64'
# export CFLAGS="%{optflags}"
# export LDFLAGS="%{_ldflags}"

./configure \
	--prefix=%{_datadir}/nagios \
	--exec-prefix=%{_libdir}/nagios \
	--with-init-dir=%{_initrddir} \
	--with-lockfile=%{_localstatedir}/run/nagios-nrpe.pid \
	--libdir=%{_libdir}/nagios \
	--bindir=%{_sbindir} \
	--sbindir=%{_libdir}/nagios/cgi-bin \
	--libexecdir=%{_libdir}/nagios/plugins \
	--sysconfdir=%{_sysconfdir}/nagios \
	--localstatedir=%{_localstatedir}/log/nagios \
	--datadir=%{_datadir}/nagios/html \
        --enable-command-args

make -j$CPUS all


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} NAGIOS_INSTALL_OPTS="" NRPE_INSTALL_OPTS="" install
mkdir -p %{buildroot}/%{_sysconfdir}/nagios
install -m 0644 sample-config/nrpe.cfg %{buildroot}%{_sysconfdir}/nagios/nrpe.cfg

install -d 0755 %{buildroot}%/var/svc/manifest/site
install -m 0644 %{SOURCE1} %{buildroot}%/var/svc/manifest/site
install -d 0755 %{buildroot}%/lib/svc/method
install -m 0555 %{SOURCE2} %{buildroot}%/lib/svc/method

rm %{buildroot}/usr/sbin/nrpe-uninstall

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, bin)
%doc CHANGELOG.md LEGAL LICENSE.md README.SSL.md README.md SECURITY.md THANKS
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, nagios) %{_sysconfdir}/nagios
%config(noreplace) %{_sysconfdir}/nagios/nrpe.cfg
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/sbin
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_docdir}
/usr/sbin/nrpe
%dir %attr (0755, root, bin) /usr/lib/nagios/plugins
/usr/lib/nagios/plugins/check_nrpe
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/log
%dir %attr (0750, nagios, webservd) %{_localstatedir}/log/nagios
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/site
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/site/nagios-nrpe.xml
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/svc-nagios-nrpe


%changelog
* Thu Mar 15 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.2.1
* Wed Apr 19 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.1.0
* Tue May 13 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add configure option '--enable-command-args'
* Tue Jan 21 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.15
* Wed Mar 13 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.14
* Thu Jun 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
