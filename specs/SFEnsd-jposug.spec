#
# spec file for package SFEnsd
#

%define _name nsd

%include Solaris.inc
%include packagenamemacros.inc
%include base.inc

Name:			SFEnsd-jposug
IPS_Package_Name:	jposug/service/network/dns/nsd
Summary:		Fast and lean authoritative DNS Name Server
Version:		4.3.0
License: 		BSD
Source:                 http://www.nlnetlabs.nl/downloads/nsd/nsd-%{version}.tar.gz
Source1:                nsd.xml
Url:			http://www.nlnetlabs.nl/nsd/

BuildRequires: jposug/library/libevent
BuildRequires: jposug/library/security/libressl
Requires:      jposug/library/libevent

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

export CC=/usr/bin/gcc
export CFLAGS='-m64'
export LDFLAGS="-L/opt/jposug/lib -L/lib/%{_arch64} -L/usr/lib/%{_arch64} -R/opt/jposug/lib -R/lib/%{_arch64} -R/usr/lib/%{_arch64}"
export PKG_CONFIG_PATH=/opt/jposug/lib/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig

./configure \
    --prefix=/opt/jposug/nsd \
    --enable-bind8-stats \
    --enable-checking \
    --enable-ratelimit \
    --with-ssl=/opt/jposug \
    --with-libevent=/opt/jposug \
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
sed -e 's!/usr/sbin!/opt/jposug/nsd/sbin!' \
    -e 's!/etc/nsd.conf!/etc/nsd/nsd.conf!' \
    -e 's!/var/run/nsd/nsd.pid!/var/run/nsd.pid!' < contrib/nsd.init.dist > contrib/nsd.init

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -m 0755 nsd-mem %{buildroot}/opt/jposug/nsd/sbin/nsd-mem

rmdir %{buildroot}/var/run/nsd
rmdir %{buildroot}/var/run

install -Dp -m0644 contrib/nsd.init %{buildroot}/lib/svc/method/svc-nsd
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_localstatedir}/svc/manifest/network/dns/nsd.xml

# install -Dp -m0644 nsd.conf.sample %{buildroot}/etc/nsd.conf
mkdir %{buildroot}/var/nsd/zones

install -Dp -m0644 contrib/nsd_munin_ %{buildroot}/opt/jposug/share/munin/plugins/nsd_munin_

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
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
%dir %attr (0755, root, bin) /opt/jposug/nsd
/opt/jposug/nsd/*
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
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
%dir %attr (0755, root, sys) /opt/jposug/share
%dir %attr (0755, root, bin) /opt/jposug/share/munin
%dir %attr (0755, root, bin) /opt/jposug/share/munin/plugins
%attr (0755, root, bin) /opt/jposug/share/munin/plugins/nsd_munin_

%changelog
* Wed Mar 18 2020 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
