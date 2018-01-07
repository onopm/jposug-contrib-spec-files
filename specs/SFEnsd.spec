#
# spec file for package SFEnsd
#

%define _name nsd

%include Solaris.inc
%include packagenamemacros.inc
%include base.inc

Name:			SFEnsd
IPS_Package_Name:	service/network/dns/nsd
Summary:		Fast and lean authoritative DNS Name Server
Version:		4.1.19
License: 		BSD
Source:                 http://www.nlnetlabs.nl/downloads/nsd/nsd-%{version}.tar.gz
Source1:                nsd.xml
Url:			http://www.nlnetlabs.nl/nsd/

BuildRequires: library/libevent
BuildRequires: library/security/openssl
Requires:      libevent

%description
NSD is a complete implementation of an authoritative DNS name server.
For further information about what NSD is and what NSD is not please
consult the REQUIREMENTS document which is a part of this distribution
(thanks to Olaf).

%package munin
IPS_package_name: diagnostic/munin/plugins/nsd
Summary:          Munin plugin for nsd
Requires:         diagnostic/munin/common

%description munin
Munin plugin for nsd

%prep
# %setup -n ruby-%{version}-p%{patchlevel}
%setup -n nsd-%{version}


%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

./configure \
    --prefix=/usr/nsd \
    --enable-bind8-stats \
    --enable-checking \
    --enable-ratelimit \
    --with-ssl \
    --with-libevent \
    --with-user=nsd \
    --with-configdir=/etc/nsd \
    --with-zonesdir=/var/nsd/zones \
    --with-zonelistfile=/var/nsd/zone.list \
    --with-dbfile=/var/nsd/nsd.db \
    --with-pidfile=/var/run/nsd/nsd.pid \
    --with-xfrdfile=/var/nsd/xfrd.state \
    --with-xfrdir=/var/nsd/xfr 

make -j$CPUS
make -j$CPUS nsd-mem


mv contrib/nsd.init contrib/nsd.init.dist
sed -e 's!/usr/sbin!/usr/nsd/sbin!' \
    -e 's!/etc/nsd.conf!/etc/nsd/nsd.conf!' \
    -e 's!/var/run/nsd/nsd.pid!/var/run/nsd.pid!' < contrib/nsd.init.dist > contrib/nsd.init

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -m 0755 nsd-mem %{buildroot}/usr/nsd/sbin/nsd-mem

rmdir %{buildroot}/var/run/nsd
rmdir %{buildroot}/var/run

install -Dp -m0644 contrib/nsd.init %{buildroot}/lib/svc/method/svc-nsd
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_localstatedir}/svc/manifest/network/dns/nsd.xml

# install -Dp -m0644 nsd.conf.sample %{buildroot}/etc/nsd.conf
mkdir %{buildroot}/var/nsd/zones

install -Dp -m0644 contrib/nsd_munin_ %{buildroot}/usr/share/munin/plugins/nsd_munin_

%clean
rm -rf $RPM_BUILD_ROOT

%actions
group groupname="nsd"
user ftpuser=false gcos-field="NSD Reserved UID" username="nsd" password=NP group="nsd"

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /etc
%dir %attr (0755, root, sys) /etc/nsd
/etc/nsd/nsd.conf.sample
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/nsd
/usr/nsd/*
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, nsd, sys) %{_localstatedir}/nsd
%dir %attr (0755, nsd, sys) %{_localstatedir}/nsd/xfr
%dir %attr (0755, nsd, sys) %{_localstatedir}/nsd/zones
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/network
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/network/dns
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/network/dns/nsd.xml
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/svc-nsd

%files munin
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, bin) /usr/share/munin
%dir %attr (0755, root, bin) /usr/share/munin/plugins
%attr (0755, root, bin) /usr/share/munin/plugins/nsd_munin_

%changelog
* Sun Jan 07 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.19
* Mon Jul 24 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.17
* Tue Feb 21 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.15
* Fri Dec 16 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.14
* Fri Sep 30 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.13
* Thu Sep 08 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.12
* Thu Mar 15 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.8
* Mon Dec 14 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.1.7
* Thu Sep 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
