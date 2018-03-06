#
# spec file for package SFEnagios-plugins
#
# includes module(s): nagios-plugins
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc

Name:		SFEnagios-plugins
IPS_package_name:        diagnostic/nagios/plugins
Version:	2.2.1
Summary:	Nagios plugins
Group:		Applications/System
License:	GPLv2
URL:		http://www.nagios.org/
# Source:		%{sf_download}/nagiosplug/nagios-plugins-%{version}.tar.gz
# Source:	http://assets.nagios.com/downloads/nagiosplugins/nagios-plugins-%{version}.tar.gz
Source:         https://nagios-plugins.org/download/nagios-plugins-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_BaseDir:   %{_basedir}
%include default-depend.inc

BuildRequires:	diagnostic/nagios/devel
Requires:	diagnostic/nagios/common

%description
Provides Nagios plugins

%package dig
IPS_package_name:        diagnostic/nagios/plugins/dig
Group:		Applications/System
Summary:	Provides check_dig plugin.
SUNW_BaseDir:	/
# BuildRequires:  pkg:/network/dns/bind
Requires:       pkg:/network/dns/bind

%description dig
Provides check_dig plugin.

%package dns
IPS_package_name:        diagnostic/nagios/plugins/dns
Group:		Applications/System
Summary:	Provides check_dns plugin.
SUNW_BaseDir:	/
# BuildRequires:  pkg:/network/dns/bind
Requires:       pkg:/network/dns/bind

%description dns
Provides check_dns plugin.

%package fping
IPS_package_name:        diagnostic/nagios/plugins/fping
Group:		Applications/System
Summary:	Provides check_fpings plugin.
SUNW_BaseDir:	/
BuildRequires:  diagnostic/fping
Requires:       diagnostic/fping

%description fping
Provides check_fping plugin.

%prep
%setup -q -n nagios-plugins-%{version}

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
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/nagios
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_dig

%files dns
%defattr(-, root, sys)
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/nagios
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_dns

%files fping
%defattr(-, root, sys)
%dir %attr(0755, root, bin) %{_libdir}
%dir %attr(0755, root, bin) %{_libdir}/nagios
%dir %attr(0755, root, bin) %{_libdir}/nagios/plugins
%attr (0555, root, bin) %{_libdir}/nagios/plugins/check_fping

%changelog
* Wed Feb 14 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.1
* Thu Feb 02 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.0
* Fri Dec 16 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.4
* Sat Nov 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.1
* Wed Dec 17 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump  to 2.0.3
* Tue May 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.2
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.1
* Wed Mar 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0
* Mon Feb 17 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %defattr
* Tue Jan 21 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Sun Dec 23 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Requires and BuildRequires
* Tue Jul 17 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4.16

* Fri Apr 13 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add utils.sh and utils.pm to %files

* Tue Mar 27 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add check_ldap to %files

* Fri May 20 2011 - Fumihisa Tonaka <fumi.ftnk@gmail.com>
- modify install section.
- add make check_swap
- list files in %files section
- add dig, dns and fping package

* Sun Mar 06 2011 - Milan Jurik
- fix Solaris build
* Sat Mar 05 2011 - Milan Jurik
- initial spec
