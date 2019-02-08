#
# spec file for package SFEnagios-plugins
#
# includes module(s): nagios-plugins
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc

%define _basedir /opt/jposug
%define _sysconfdir /etc
%define _localstatedir /var

Name:		SFEnagios-plugins
IPS_package_name:        jposug/diagnostic/nagios/plugins
Version:	2.2.1
Summary:	Nagios plugins
Group:		Applications/System
License:	GPLv3
URL:		http://www.nagios.org/
# Source:		%{sf_download}/nagiosplug/nagios-plugins-%{version}.tar.gz
# Source:	http://assets.nagios.com/downloads/nagiosplugins/nagios-plugins-%{version}.tar.gz
Source:         https://nagios-plugins.org/download/nagios-plugins-%{version}.tar.gz
# patch1 is based on https://blog.jasonantman.com/2009/10/nagios-check_by_ssh-and-nat/
Patch1:         nagios-plugins-check_by_ssh.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir:   /
%include default-depend.inc

BuildRequires:	jposug/diagnostic/nagios/devel
Requires:	jposug/diagnostic/nagios/common

%description
Provides Nagios plugins

%package dig
IPS_package_name:        jposug/diagnostic/nagios/plugins/dig
Group:		Applications/System
Summary:	Provides check_dig plugin.
SUNW_BaseDir:	/
# BuildRequires:  pkg:/network/dns/bind
Requires:       pkg:/network/dns/bind

%description dig
Provides check_dig plugin.

%package dns
IPS_package_name:        jposug/diagnostic/nagios/plugins/dns
Group:		Applications/System
Summary:	Provides check_dns plugin.
SUNW_BaseDir:	/
# BuildRequires:  pkg:/network/dns/bind
Requires:       pkg:/network/dns/bind

%description dns
Provides check_dns plugin.

%package fping
IPS_package_name:        jposug/diagnostic/nagios/plugins/fping
Group:		Applications/System
Summary:	Provides check_fpings plugin.
SUNW_BaseDir:	/
BuildRequires:  diagnostic/fping
Requires:       diagnostic/fping

%description fping
Provides check_fping plugin.

%prep
%setup -q -n nagios-plugins-%{version}
%patch1 -p0

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

%ifarch sparcv9
export CFLAGS="-I/usr/include/kerberosv5"
%else
# export CFLAGS="%{optflags} -I/usr/include/kerberosv5"
export CFLAGS="-I/usr/include/kerberosv5"
export LDFLAGS="%{_ldflags}"
%endif

./configure \
	--prefix=%{_datadir}/nagios \
	--exec-prefix=%{_libdir}/nagios \
        --with-httpd-conf=%{_sysconfdir}/apache2/2.2/conf.d \
	--with-init-dir=%{_initrddir} \
	--with-cgiurl=/nagios/cgi-bin \
	--with-htmlurl=/nagios \
	--with-lockfile=%{_localstatedir}/run/nagios.pid \
	--libdir=%{_libdir}/nagios \
	--with-nagios-user=nagios \
	--with-nagios-grp=nagios \
	--bindir=%{_sbindir} \
	--libexecdir=%{_libdir}/nagios/plugins \
	--disable-static \
	--enable-extra-opts \
	--sysconfdir=%{_sysconfdir}/nagios \
	--localstatedir=%{_localstatedir}/log/nagios \
	--datadir=%{_datadir}/nagios/html \
	--with-gd-lib=%{_libdir} \
	--with-gd-inc=%{_includedir}/gd2 \
	--enable-embedded-perl \
	--with-perlcache \
	--with-template-objects \
	--with-template-extinfo

# 	--with-libiconv-prefix=/usr/gnu \

make -j$CPUS all
cd plugins
make -j$CPUS check_swap
cd ../

%install
rm -rf %{buildroot}

#make DESTDIR=%{buildroot} install

install -d -m 0755 %{buildroot}%{_libdir}/nagios/plugins

cd plugins
for i in check_* urlize negate
do
    [ -x $i ] && \
    install -m 0755 $i %{buildroot}%{_libdir}/nagios/plugins
done

# check_uptime works on Linux only and it is not builded on Solaris.
# But check_uptime.c is installed because mode of check_uptime.c is 0755.
# Then delete installed check_uptime.c
# rm %{buildroot}%{_libdir}/nagios/plugins/check_uptime.c

cd ../plugins-root
for i in check_* pst3
do
    [ -x $i ] && \
    install -m 0755 $i %{buildroot}%{_libdir}/nagios/plugins
done

cd ../plugins-scripts
for i in check_* utils.sh utils.pm
do
    if [ -x $i ]
    then
	install -m 0755 $i %{buildroot}%{_libdir}/nagios/plugins
    else
	install -m 0644 $i %{buildroot}%{_libdir}/nagios/plugins
    fi
done


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, sys)
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/nagios
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_apt
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_breeze
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_breeze.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_by_ssh
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_clamd
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_cluster
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_dhcp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_disk
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_disk_smb
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_disk_smb.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_dummy
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_file_age
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_file_age.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_flexlm
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_flexlm.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ftp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_hpjd
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_http
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_icmp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ifoperstatus
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ifoperstatus.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ifstatus
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ifstatus.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_imap
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ircd
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ircd.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_jabber
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ldap
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_load
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_log
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_log.sh
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_mailq
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_mailq.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_mrtg
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_mrtgtraf
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_nagios
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_nntp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_nntps
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_nt
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ntp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ntp.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ntp_peer
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ntp_time
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_nwstat
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_oracle
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_oracle.sh
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_overcr
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ping
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_pop
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_procs
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_real
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_rpc
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_rpc.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_sensors
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_sensors.sh
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_simap
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_smtp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_snmp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_spop
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ssh
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ssmtp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_swap
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_tcp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_time
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_udp
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_ups
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_users
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_wave
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_wave.pl
%attr (0555, root, bin) %{_libdir}/nagios/plugins/negate
%attr (4555, root, bin) %{_libdir}/nagios/plugins/pst3
%attr (0555, root, bin) %{_libdir}/nagios/plugins/urlize
%attr (0644, root, bin) %{_libdir}/nagios/plugins/utils.sh
%attr (0644, root, bin) %{_libdir}/nagios/plugins/utils.pm


%files dig
%defattr(-, root, sys)
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/nagios
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_dig

%files dns
%defattr(-, root, sys)
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/nagios
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_dns

%files fping
%defattr(-, root, sys)
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/nagios
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_fping

%changelog
* Fri Feb 08 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
