#
# spec file for package SFEopenvpn
#
# includes module(s): openvpn
#
%include Solaris.inc
%include packagenamemacros.inc
%define srcname openvpn

Name:		SFEopenvpn
Summary:	Open source, full-featured SSL VPN package
Group:		System/Security
URL:		http://openvpn.net
License:	GPLv2
Version:	2.2.1
Source:		http://swupdate.openvpn.net/community/releases/%srcname-%version.tar.gz
Source1:        SFEopenvpn-openvpn.xml
Source2:        SFEopenvpn-openvpn 
# http://comments.gmane.org/gmane.os.solaris.opensolaris.pkg.sfe/28
%define _basedir  /
SUNW_BaseDir:   %{_basedir}
SUNW_Copyright: %{name}.copyright
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

BuildRequires: library/lzo
Requires: library/lzo
BuildRequires: system/network/tuntap
Requires: system/network/tuntap
BuildRequires: %{pnm_buildrequires_SUNWopenssl}
Requires: %{pnm_requires_SUNWopenssl}

%prep
%setup -q -n %srcname-%version

%build
CPUS=$(psrinfo | awk '$2=="on-line"{cpus++}END{print (cpus==0)?1:cpus}')

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

./configure --prefix=%{_prefix}  \
            --mandir=%{_mandir}

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/network/
cp %{SOURCE1} $RPM_BUILD_ROOT/var/svc/manifest/network/openvpn.xml
mkdir -p $RPM_BUILD_ROOT/lib/svc/method/
cp %{SOURCE2} $RPM_BUILD_ROOT/lib/svc/method/openvpn
chmod +x $RPM_BUILD_ROOT/lib/svc/method/openvpn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_sbindir}
%{_sbindir}/openvpn
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man8
%{_mandir}/man8/openvpn.8
%dir %attr (0755, root, other) %dir %_docdir
%_docdir/%srcname
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/network/openvpn.xml
%attr (0555, root, bin) /lib/svc/method/openvpn

%changelog
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
