#
# spec file for package SFEopenvpn
#
# includes module(s): openvpn
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc
%define srcname openvpn
%define _prefix /usr
%define sysconfdir /etc
%define _sbindir /usr/sbin
%define sampledir .
Name:		SFEopenvpn
IPS_Package_Name:       system/network/openvpn
Summary:	Open source, full-featured SSL VPN package
Group:		System/Security
URL:		http://openvpn.net
License:	GPLv2
Version:	2.2.2
Source:		http://swupdate.openvpn.net/community/releases/%srcname-%version.tar.gz
Source1:        SFEopenvpn-openvpn.xml
Source2:        SFEopenvpn-openvpn 
#Source3:	https://github.com/OpenVPN/easy-rsa/archive/release/2.x.zip
%define easyrsa2_url https://github.com/OpenVPN/easy-rsa/archive/release/2.x.zip
%define easyrsa2_source 2.x.zip
#Patch1:         openvpn231-solaris.patch
# http://comments.gmane.org/gmane.os.solaris.opensolaris.pkg.sfe/28
%define _basedir  /
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %pnm_buildrequires_wget
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif
%include default-depend.inc

BuildRequires: library/lzo
Requires: library/lzo
BuildRequires: driver/network/tuntap
Requires: driver/network/tuntap
BuildRequires: %{pnm_buildrequires_SUNWopenssl}
Requires: %{pnm_requires_SUNWopenssl}

%prep
%setup -q -n %srcname-%version
#%patch1 -p0
wget %easyrsa2_url
unzip %easyrsa2_source

%build
CPUS=$(psrinfo | awk '$2=="on-line"{cpus++}END{print (cpus==0)?1:cpus}')
#export CFLAGS
%if %{cc_is_gcc}
    export CC=gcc
    export CXX=g++
    export CFLAGS="%optflags -fno-strict-aliasing"
%else
    export CFLAGS="%optflags"
%endif
export LDFLAGS="%_ldflags"
./configure --prefix=%{_prefix} --mandir=%{_mandir}  --sysconfdir=%{sysconfdir}

make -j$CPUS

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/var/svc/manifest/network/
cp %{SOURCE1} %{buildroot}/var/svc/manifest/network/openvpn.xml
mkdir -p %{buildroot}/lib/svc/method/
cp %{SOURCE2} %{buildroot}/lib/svc/method/openvpn
chmod +x %{buildroot}/lib/svc/method/openvpn
mkdir -p %{buildroot}/var/run/openvpn
mkdir -p %{buildroot}/var/openvpn
mkdir -p %{buildroot}/%{sysconfdir}/openvpn/ccd
mkdir -p %{buildroot}/%{sysconfdir}/openvpn/easy-rsa
mkdir -p %{buildroot}/%{sysconfdir}/openvpn/easy-rsa/keys
touch %{buildroot}/%{sysconfdir}/openvpn/easy-rsa/keys/index.txt
install -m 0644 easy-rsa-release-2.x/easy-rsa/2.0/* %{buildroot}/%{sysconfdir}/openvpn/easy-rsa
install -m 0644 %{sampledir}/sample-scripts/bridge-start %{buildroot}/%{sysconfdir}/openvpn
install -m 0644 %{sampledir}/sample-scripts/bridge-stop %{buildroot}/%{sysconfdir}/openvpn
# for V2.3
#install -m 0644 distro/rpm/openvpn.init.d.rhel %{buildroot}/%{sysconfdir}/openvpn
#install -m 0644 distro/rpm/openvpn.init.d.suse %{buildroot}/%{sysconfdir}/openvpn
install -m 0644 sample-scripts/openvpn.init %{buildroot}/%{sysconfdir}/openvpn
install -m 0644 %{sampledir}/sample-config-files/static-home.conf %{buildroot}/%{sysconfdir}/openvpn/static-home.conf.sample
install -m 0644 %{sampledir}/sample-config-files/static-office.conf %{buildroot}/%{sysconfdir}/openvpn/static-office.conf.sample
install -m 0644 %{sampledir}/sample-config-files/tls-office.conf %{buildroot}/%{sysconfdir}/openvpn/tls-office.conf.sample
install -m 0644 %{sampledir}/sample-config-files/tls-home.conf %{buildroot}/%{sysconfdir}/openvpn/tls-home.conf.sample
install -m 0644 %{sampledir}/sample-config-files/client.conf %{buildroot}/%{sysconfdir}/openvpn/client.conf.sample
install -m 0644 %{sampledir}/sample-config-files/server.conf %{buildroot}/%{sysconfdir}/openvpn
install -m 0644 %{sampledir}/sample-config-files/README %{buildroot}/%{sysconfdir}/openvpn

%clean
rm -rf %{buildroot}
# Attention!
# master.tar.gz often appears on github.
rm -rf %{SOURCE3}

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_prefix}
%dir %{_sbindir}
%{_sbindir}/openvpn
%dir %attr (0755, root, sys) %{sysconfdir}
%dir %attr (0755, root, sys) %{sysconfdir}/openvpn
%dir %attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa
%dir %attr (0700, root, root) %config(noreplace) %{sysconfdir}/openvpn/easy-rsa/keys
%dir %attr (0755, root, sys) %{sysconfdir}/openvpn/ccd
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/build*
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/clean-all
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/inherit-inter
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/list-crl
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/pkitool
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/revoke-full
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/sign-req
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/sign-server-req
%attr (0755, root, sys) %{sysconfdir}/openvpn/easy-rsa/whichopensslcnf
%attr (0664, root, sys) %{sysconfdir}/openvpn/easy-rsa/openssl*
%attr (0664, root, sys) %config(noreplace) %{sysconfdir}/openvpn/easy-rsa/vars
%attr (0644, root, root) %config(noreplace) %{sysconfdir}/openvpn/easy-rsa/keys/*
%attr (0664, root, sys) %config(noreplace) %{sysconfdir}/openvpn/*.conf*
%attr (0664, root, sys) %{sysconfdir}/openvpn/README
%attr (0664, root, sys) %{sysconfdir}/openvpn/bridge-*
%attr (0664, root, sys) %{sysconfdir}/openvpn/openvpn.init*
# for V2.3
#%dir %{_prefix}/lib
#%dir %{_prefix}/lib/openvpn
#%{_prefix}/lib/openvpn/*
#%dir %attr (0755, root, bin) %{_prefix}/include
#%{_prefix}/include/openvpn-plugin.h
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man8
%{_mandir}/man8/openvpn.8
%dir %attr (0755, root, other) %dir %_docdir
%_docdir/%srcname
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/openvpn
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/network
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/network/openvpn.xml
%dir %attr (0555, root, root) /var/openvpn
%dir %attr (0755, root, sys) /var/run
%dir %attr (0555, root, root) /var/run/openvpn

%changelog
* Sat Jul 19 2014 - YAMAMOTO Takashi
- Bumped to final easy-rsa version 2.final
* Sun Apr 28 2013 - YAMAMOTO Takashi
- Bumped to 2.2.2
* Wed Mar 20 2013 - YAMAMOTO Takashi
- degrade the version to 2.1.14
- build with gcc by default
* Tue Dec 10 2012 - YAMAMOTO Takashi
- Corrected dependency.
* Tue Nov 20 2012 - YAMAMOTO Takashi
- Bump to 2.2.2. Fix some problems.
* Fri Nov 16 2012 - YAMAMOTO Takashi
- Added a manifest file
* Tue Mar 20 2012 - YAMAMOTO Takashi
- Initial, fix dependency using for pnm.
* Wed Sep 28 2011 - Alex Viskovatoff
- Update to 2.2.1, fixing %files; add SUNW_copyright
- openssl is not in /usr/sfw
* Tue Jun 7 2011 - Ken Mays <kmays2000@gmail.com>
- Bumped to 2.2.0, comes with integrated tun.c
* Wed Oct  3 2007 - Doug Scott <dougs@truemail.co.th>
- Added modified tun.c
* Wed Apr 07 2007 - Eric Boutilier
- Initial spec
