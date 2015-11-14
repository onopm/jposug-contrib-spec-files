#
#
# spec file for package SFEtun
#
# includes module(s): tun
#
%include Solaris.inc
%include packagenamemacros.inc

%define src_name master
%define src_url http://github.com/kaizawa/tuntap/archive
%define usr_kernel /usr/kernel
%define drv_base %{usr_kernel}/drv

Name:		SFEtun
IPS_Package_Name:	driver/network/tuntap
Summary:	Virtual Point-to-Point network device
URL:		http://www.whiteboard.ne.jp/~admin2/tuntap/
License:        GPLv2
SUNW_Copyright:	tuntap.copyright
Meta(info.upstream): Kazuyoshi Aizawa <admin2@whiteboard.ne.jp>
Version:	1.4.201207
Source:		%{src_url}/%{src_name}.tar.gz
Patch1:		%name-configure.in.patch
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%description
tuntap is a TAP driver for Solaris that can be used for OpenVPN, OpenConnect,
and vpnc.

The code is based on the Universal TUN/TAP driver. Some changes were made and
code added for supporting Ethernet tunneling feature, since the Universal
TUN/TAP driver for Solaris only supports IP tunneling known as TUN.

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires:                %{name}

%prep
%setup -q -n tuntap-%{src_name}
%patch1 -p0 -b .orig

%build
autoconf -f
./configure
make
%ifarch sparcv9 amd64
mv tun tun64
mv tap tap64
make clean
./configure --disable-64bit
make
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -D if_tun.h $RPM_BUILD_ROOT%{_includedir}/net/if_tun.h
install -D tun $RPM_BUILD_ROOT%{drv_base}/tun
install -D tap $RPM_BUILD_ROOT%{drv_base}/tap
%ifarch sparcv9 amd64
install -D tun64 $RPM_BUILD_ROOT%{drv_base}/%{_arch64}/tun
install -D tap64 $RPM_BUILD_ROOT%{drv_base}/%{_arch64}/tap
%endif
install -D tun.conf $RPM_BUILD_ROOT%{drv_base}/tun.conf
install -D tap.conf $RPM_BUILD_ROOT%{drv_base}/tap.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
( PATH=/usr/bin:/usr/sfw/bin; export PATH ;
  retval=0;
  /usr/sbin/add_drv tun || retval=1;
  [ "$retval" = 0 ] && /usr/sbin/add_drv tap || retval=1;
  exit $retval ) 

%preun
( echo PATH=/usr/bin:/usr/sfw/bin; export PATH ;
  /usr/sbin/rem_drv tun || retval=1;
  /usr/sbin/rem_drv tap || retval=1;
  exit 0
)

%actions
driver name=tun
driver name=tap

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%dir %attr (0755, root, bin) %{_includedir}/net
%{_includedir}/net/if_tun.h
%dir %attr (0755, root, sys) %{usr_kernel}
%dir %attr (0755, root, sys) %{drv_base}
%{drv_base}/tun
%{drv_base}/tap
%{drv_base}/tun.conf
%{drv_base}/tap.conf
%ifarch amd64 sparcv9
%dir %attr (0755, root, sys) %{drv_base}/%{_arch64}
%{drv_base}/%{_arch64}/tun
%{drv_base}/%{_arch64}/tap
%endif

%changelog
* Sun Jul 19 2014 - YAMAMOTO Takashi
- Support for oi_151a9
* Sun Apr 28 2013 - YAMAMOTO Takashi
- Bump to 1.4 (2012/7)
* Thu Nov 27 2012 - YAMAMOTO Takashi
- changed package name
* Thu Oct 06 2011 - Milan Jurik
- add IPS package name
* Fri Jul 29 2011 - Alex Viskovatoff
- add SUNW_Copyright
* Wed May 12 2010 - Milan Jurik
- update according the latest upstream
- IPS support added
* Wed Oct  3 2007 - Doug Scott
- Added base spec
- Updated to build tap from latest source
* Wed Apr 07 2007 - Eric Boutilier
- Initial spec
