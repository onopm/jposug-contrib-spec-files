#
# spec file for package SFEamanda
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

%define src_name	amanda

%define amanda_user	amandabackup
%define amanda_userid	36
%define amanda_indexserver	amandahost
%define amanda_tapeserver	%{indexserver}
%define defconfig DailySet1
%define svcdir /lib/svc/manifest/network

Name:		SFEamanda
IPS_package_name:	backup/amanda
SUNW_Copyright: %{name}.copyright
Summary:	A network-capable tape backup solution
Version:	3.3.5
Source:		%{sf_download}/%{src_name}/%{src_name}-%{version}.tar.gz
Source1: SFEamanda_crontab
Source4: SFEamanda_disklist
Source8: SFEamanda_hosts
#Source9: amanda.socket
#Source10: amanda@.service
#Source11: activate-devpay.1.gz
Source12: SFEamanda_killpgrp.8
#Source13: amanda-udp.socket
#Source14: amanda-udp.service
Source100: SFEamanda_server.xml.in
Source101: SFEamanda_client.xml.in
Patch2: amanda-3.1.1-xattrs.patch
Patch3: amanda-3.1.1-tcpport.patch
Patch6: amanda-3.2.0-config-dir.patch
Patch11: amanda-3.3.2-autogen.patch
License:	BSD and GPLv3+ and GPLv2+ and GPLv2
Group:		Applications/System
URL:		http://www.amanda.org
SUNW_BaseDir:	/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

BuildRequires:  SUNWgnome-common-devel
Buildrequires:  SUNWgnu-readline
BuildRequires:  %pnm_buildrequires_perl_default
Requires:       SUNWgnuplot
Requires:       SUNWgnu-readline
Requires:       %pnm_requires_perl_default
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc
Requires:      system/library/gcc-runtime
%endif

%description 
AMANDA, the Advanced Maryland Automatic Network Disk Archiver, is a
backup system that allows the administrator of a LAN to set up a
single master backup server to back up multiple hosts to one or more
tape drives or disk files.  AMANDA uses native dump and/or GNU tar
facilities and can back up a large number of workstations running
multiple versions of Unix.  Newer versions of AMANDA (including this
version) can use SAMBA to back up Microsoft(TM) Windows95/NT hosts.
The amanda package contains the core AMANDA programs and will need to
be installed on both AMANDA clients and AMANDA servers.  Note that you
will have to install the amanda-client and/or amanda-server packages as
well.

%package libs
IPS_package_name:       backup/amanda/libs
Summary: Amanda libraries
Group: Applications/System
Requires:     backup/amanda 

%description libs
This package contains basic Amanda libraries, which are used by all
Amanda programs.

%package client
IPS_package_name:       backup/amanda/client
Summary: The client component of the AMANDA tape backup system
Group: Applications/System
#Requires: fileutils grep
#Requires(pre): amanda = %{version}-%{release}
#Requires: amanda-libs%{?_isa} = %{version}-%{release}
Requires:	backup/amanda
Requires:	backup/amanda/libs 
Requires:	%pnm_requires_SUNWpostrun
Requires:	%pnm_requires_text_gnu_grep

%description client
The Amanda-client package should be installed on any machine that will
be backed up by AMANDA (including the server if it also needs to be
backed up).  You will also need to install the amanda package on each
AMANDA client machine.

%package server
IPS_package_name:       backup/amanda/server
Summary: The server side of the AMANDA tape backup system
Group: Applications/System
#Requires: fileutils grep
#Requires(pre): amanda = %{version}-%{release}
#Requires: amanda-libs%{?_isa} = %{version}-%{release}
Requires:	backup/amanda
Requires:	backup/amanda/libs
Requires:	%pnm_requires_SUNWpostrun
Requires:	%pnm_requires_text_gnu_grep

%description server
The amanda-server package should be installed on the AMANDA server,
the machine attached to the device(s) (such as a tape drive) where backups
will be written. You will also need to install the amanda package on
the AMANDA server machine.  And, if the server is also to be backed up, the
server also needs to have the amanda-client package installed.

%prep
%setup -q -n %{src_name}-%{version}
%patch2 -p1 -b .xattrs
%patch3 -p1 -b .tcpport
%patch6 -p1 -b .config
%patch11 -p1 -b .autogen
cp -f %SOURCE100 example/amandaserver.xml.in
cp -f %SOURCE101 example/amandaclient.xml.in
./autogen

%build
export CC=gcc
export CXX=g++
export CFLAGS="%optflags -fno-strict-aliasing -Wno-pointer-sign"
export CPPFLAGS=""
export LDFLAGS="%{_ldflags}"
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
#   Get default settings for various configuration and command-line options:
#	--with-index-server
#	    define and substitute DEFAULT_SERVER
#	--with-config
#	    define and substitute DEFAULT_CONFIG
#	--with-tape-server
#	    define and substitute DEFAULT_TAPE_SERVER
#	--with-tape-device
#	    define and substitute DEFAULT_TAPE_DEVICE; substitue EXAMPLE_TAPEDEV
#	--with-amandates
#	    define ascend substitute DEFAULT_AMANDATES_FILE

#	--with-krb5-security		\
./configure --prefix=%{_prefix}	\
	--enable-shared			\
	--disable-static		\
	--disable-dependency-tracking	\
	--disable-installperms		\
	--with-amdatadir=%{_localstatedir}/lib/amanda	\
	--with-amperldir=%{perl_vendorarch}	\
	--with-index-server=%{amanda_indexserver}	\
	--with-tape-server=%{amanda_tapeserver}	\
	--with-config=%{defconfig}      \
	--with-gnutar-listdir=%{_localstatedir}/lib/amanda/gnutar-lists	\
	--with-gnutar=/usr/bin/gtar	\
	--with-smbclient=%{_bindir}/smbclient	\
	--with-amandates=%{_localstatedir}/lib/amanda/amandates \
	--with-amandahosts		\
	--with-user=%amanda_user	\
	--with-group=sys		\
	--with-tmpdir=/var/log/amanda	\
	--sysconfdir=%{_sysconfdir}	\
	--with-ssh-security		\
	--with-rsh-security		\
	--with-bsdtcp-security		\
	--with-bsdudp-security		\
	--libdir=%{_libdir}		\
	--libexecdir=%{_libexecdir}	\
	--enable-threads=solaris	\
	--disable-s3-device		\
	--with-fqdn			\
	--with-gnuplot=/usr/bin/gnuplot	\
	--with-amperldir=%{_prefix}/%{perl_path_vendor_perl_version} \
	--with-amandahosts		\
	--with-readline
	
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

#make install BINARY_OWNER=%(id -un) SETUID_GROUP=%(id -gn) DESTDIR=$RPM_BUILD_ROOT
#
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/amanda
#mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log/amanda
#mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/amanda
#

make install BINARY_OWNER=%(id -un) SETUID_GROUP=%(id -gn) DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/amanda
mkdir -p $RPM_BUILD_ROOT/var/log/amanda
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/amanda
install -m 600 %SOURCE8 $RPM_BUILD_ROOT%{_localstatedir}/lib/amanda/.amandahosts
#install -p -m 644 -D %{SOURCE9} %{buildroot}%{_unitdir}/amanda.socket
#install -p -m 644 -D %{SOURCE10} %{buildroot}%{_unitdir}/amanda@.service
#install -p -m 644 -D %{SOURCE13} %{buildroot}%{_unitdir}/amanda-udp.socket
#install -p -m 644 -D %{SOURCE14} %{buildroot}%{_unitdir}/amanda-udp.service
#install -D %{SOURCE11}  $RPM_BUILD_ROOT/%{_mandir}/man1/activate-devpay.1.gz
install -D %{SOURCE12}  $RPM_BUILD_ROOT/%{_mandir}/man8/killpgrp.8

ln -s %{_libexecdir}/amanda/amandad $RPM_BUILD_ROOT%{_sbindir}/amandad
ln -s amrecover.8.gz $RPM_BUILD_ROOT%{_mandir}/man8/amoldrecover.8

mkdir -p "${RPM_BUILD_ROOT}%{svcdir}"
for f in amandaclient.xml amandaserver.xml; do
  cp example/$f "${RPM_BUILD_ROOT}%{svcdir}"
done
pushd ${RPM_BUILD_ROOT}
  mv .%{_localstatedir}/lib/amanda/example .%{_sysconfdir}/amanda/%defconfig
  cp ${RPM_SOURCE_DIR}/SFEamanda_crontab .%{_sysconfdir}/amanda/crontab.sample
  cp ${RPM_SOURCE_DIR}/SFEamanda_disklist .%{_sysconfdir}/amanda/%defconfig/disklist
  rm -f .%{_sysconfdir}/amanda/%defconfig/xinetd*
  rm -f .%{_sysconfdir}/amanda/%defconfig/inetd*

  mkdir -p .%{_localstatedir}/lib/amanda/gnutar-lists
  mkdir -p .%{_localstatedir}/lib/amanda/%defconfig/index
  touch .%{_localstatedir}/lib/amanda/amandates
popd
rm -rf $RPM_BUILD_ROOT/usr/share/amanda
find $RPM_BUILD_ROOT -name \*.la | xargs rm
rm -rf $RPM_BUILD_ROOT%{_libdir}/charset.alias
rm -rf $RPM_BUILD_ROOT/usr/include

%clean 
rm -rf ${RPM_BUILD_ROOT}

#to prevent execute both amanda server and client.
%post -n SFEamanda-client
test -x /usr/lib/postrun || exit 0
(
  echo 'svcadm clear network/amandaclient/tcp';
  echo 'svcadm disable network/amandaclient/tcp';
  echo "if [ `egrep 'amanda[[:space:]]+' /etc/services | wc -l` -lt 1 ]; then echo 'amanda		10080/tcp' >> /etc/services; fi";
) | /usr/lib/postrun -b

%post -n SFEamanda-server
test -x /usr/lib/postrun || exit 0
(
  echo 'svcadm clear network/amandaserver/tcp';
  echo 'svcadm disable network/amandaserver/tcp';
  echo "if [ `egrep 'amanda[[:space:]]+' /etc/services | wc -l` -lt 1 ]; then echo 'amanda		10080/tcp' >> /etc/services; fi";
) | /usr/lib/postrun -b

%actions
user ftpuser=false gcos-field="Amanda Reserved UID" username="%{amanda_user}" uid="%{amanda_userid}" password=NP group="sys"

%files
%doc COPYRIGHT NEWS README ChangeLog ReleaseNotes
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_prefix}
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/amandad
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/amanda-sh-lib.sh
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/amcat.awk
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/amndmjob
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/amplot.awk
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/amplot.g
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/amplot.gp
%attr(-,%amanda_user, sys) %{_libexecdir}/amanda/ndmjob

%attr(-,%amanda_user, sys) %{_sbindir}/amandad
%attr(-,%amanda_user, sys) %{_sbindir}/amaespipe
%attr(-,%amanda_user, sys) %{_sbindir}/amarchiver
%attr(-,%amanda_user, sys) %{_sbindir}/amcrypt
%attr(-,%amanda_user, sys) %{_sbindir}/amcrypt-ossl
%attr(-,%amanda_user, sys) %{_sbindir}/amcrypt-ossl-asym
%attr(-,%amanda_user, sys) %{_sbindir}/amcryptsimple
%attr(-,%amanda_user, sys) %{_sbindir}/amgetconf
%attr(-,%amanda_user, sys) %{_sbindir}/amgpgcrypt
%attr(-,%amanda_user, sys) %{_sbindir}/amplot

%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Archive.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/BigIntCompat.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/ClientService.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Config.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Config/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Constants.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Debug.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Feature.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Header.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/IPC
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/MainLoop.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/NDMP.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Paths.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Process.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Script_App.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Script.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Tests.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Util.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Xfer.pm

%{_mandir}/man5/amanda-archive-format.5*
%{_mandir}/man7/amanda-compatibility.7*
%{_mandir}/man5/amanda.conf*
%{_mandir}/man7/amanda-auth.7*
%{_mandir}/man7/amanda-match.7*
%{_mandir}/man7/amanda-scripts.7*
%{_mandir}/man8/amanda.8*
%{_mandir}/man8/amarchiver.8*
%{_mandir}/man8/amplot.8*
%{_mandir}/man8/script-email.8*
%{_mandir}/man8/amaespipe.8*
%{_mandir}/man8/amcrypt-ossl-asym.8*
%{_mandir}/man8/amcrypt-ossl.8*
%{_mandir}/man8/amcryptsimple.8*
%{_mandir}/man8/amcrypt.8*
%{_mandir}/man8/amgpgcrypt.8*
%{_mandir}/man8/amgetconf.8*
%{_mandir}/man8/amcleanupdisk.8*
%dir %attr(2775,%amanda_user, sys) %{_sysconfdir}/amanda/
%dir %attr(2775,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig

%dir %attr (0755, root, sys)  %{_localstatedir}
%dir %attr (0755, root, other)  %{_localstatedir}/lib
%attr(0755,%amanda_user,sys)     %dir %{_localstatedir}/lib/amanda/
%attr(600,%amanda_user,sys)   %config(noreplace) %{_localstatedir}/lib/amanda/.amandahosts
%dir %attr (0755, root, sys)  %{_localstatedir}/log
%attr(0755,%amanda_user,sys) %dir %{_localstatedir}/log/amanda

%files libs
%defattr(-,root,bin)
%{_libdir}/amanda/libamdevice*.so
%{_libdir}/amanda/libamserver*.so
%{_libdir}/amanda/libamclient*.so
%{_libdir}/amanda/libamanda-*.so
%{_libdir}/amanda/libamanda.so
%{_libdir}/amanda/libamandad*.so
%{_libdir}/amanda/libamar*.so
%{_libdir}/amanda/libamglue*.so
%{_libdir}/amanda/libamxfer*.so
%{_libdir}/amanda/libndmjob*.so
%{_libdir}/amanda/libndmlib*.so
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Application/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Archive/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Config/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Debug/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Feature/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Header/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/IPC/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/MainLoop/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/NDMP/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Tests/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Util/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Xfer/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Cmdline/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Device/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Disklist/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Logfile/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/Tapelist/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/auto/Amanda/XferServer/

%files server
%defattr(-,root,sys)
%{_libexecdir}/amanda/amdumpd
%{_libexecdir}/amanda/amcheck-device
%{_libexecdir}/amanda/amidxtaped
%{_libexecdir}/amanda/amindexd
%{_libexecdir}/amanda/amlogroll
%{_libexecdir}/amanda/amtrmidx
%{_libexecdir}/amanda/amtrmlog
%{_libexecdir}/amanda/driver
%attr(4750,root,sys) %{_libexecdir}/amanda/dumper
%{_libexecdir}/amanda/chg-disk
%{_libexecdir}/amanda/chg-lib.sh
%{_libexecdir}/amanda/chg-manual
%{_libexecdir}/amanda/chg-multi
%{_libexecdir}/amanda/chg-zd-mtx
%{_libexecdir}/amanda/chunker
%attr(4750,root,sys) %{_libexecdir}/amanda/planner
%{_libexecdir}/amanda/taper
#%{_sbindir}/activate-devpay
%{_sbindir}/amaddclient
%{_sbindir}/amadmin
%{_sbindir}/amcleanup
%{_sbindir}/amcleanupdisk
%{_sbindir}/amdevcheck
%{_sbindir}/amdump
%{_sbindir}/amfetchdump
%{_sbindir}/amflush
%attr(4750,root,sys) %{_sbindir}/amcheck
%{_sbindir}/amcheckdb
%{_sbindir}/amcheckdump
%{_sbindir}/amlabel
%{_sbindir}/amoverview
%{_sbindir}/amreport
%{_sbindir}/amrestore
%{_sbindir}/amrmtape
%{_sbindir}/amserverconfig
%attr(4750,root,sys) %{_sbindir}/amservice
%{_sbindir}/amstatus
%{_sbindir}/amtape
%{_sbindir}/amtapetype
%{_sbindir}/amtoc
%{_sbindir}/amvault

%defattr(-,root,bin)
%{_mandir}/man5/disklist.5*
%{_mandir}/man5/tapelist.5*
%{_mandir}/man7/amanda-devices.7*
%{_mandir}/man7/amanda-changers.7*
%{_mandir}/man7/amanda-interactivity.7*
%{_mandir}/man7/amanda-taperscan.7*
%{_mandir}/man8/amaddclient.8*
%{_mandir}/man8/amadmin.8*
%{_mandir}/man8/amcleanup.8*
%{_mandir}/man8/amdevcheck.8*
%{_mandir}/man8/amdump.8*
%{_mandir}/man8/amfetchdump.8*
%{_mandir}/man8/amflush.8*
%{_mandir}/man8/amcheckdb.8*
%{_mandir}/man8/amcheckdump.8*
%{_mandir}/man8/amcheck.8*
%{_mandir}/man8/amlabel.8*
%{_mandir}/man8/amoverview.8*
%{_mandir}/man8/amreport.8*
%{_mandir}/man8/amrestore.8*
%{_mandir}/man8/amrmtape.8*
%{_mandir}/man8/amserverconfig.8*
%{_mandir}/man8/amservice.8*
%{_mandir}/man8/amstatus.8*
%{_mandir}/man8/amtapetype.8*
%{_mandir}/man8/amtape.8*
%{_mandir}/man8/amtoc.8*
%{_mandir}/man8/amvault.8*
#%{_mandir}/man1/activate-devpay.1*

%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Cmdline.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Curinfo/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Curinfo.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/DB/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Device.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Disklist.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Extract.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Holding.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Changer/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Changer.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Interactivity/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Interactivity.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Logfile.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Recovery/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Report/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Report.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/ScanInventory.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Tapelist.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Taper/
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/XferServer.pm

%dir %attr(2775,%amanda_user, sys) %{_sysconfdir}/amanda/
%dir %attr(2775,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig
%dir %attr(2775,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/label-templates
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/crontab.sample
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/amanda.conf
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/amandaclient.xml
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/amandaserver.xml
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/chg-multi.conf
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/chg-scsi.conf
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/disklist
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/label-templates/*

%dir %attr (0755, root, sys)  %{_localstatedir}
%dir %attr (0755, root, other)  %{_localstatedir}/lib
%attr(0755,%amanda_user,sys)     %dir %{_localstatedir}/lib/amanda/
%attr(-,%amanda_user,sys) %dir %{_localstatedir}/lib/amanda/%defconfig/
%attr(-,%amanda_user,sys) %dir %{_localstatedir}/lib/amanda/%defconfig/index
%attr(-,%amanda_user,sys) %dir %{_localstatedir}/lib/amanda/template.d
%attr(-,%amanda_user,sys) %config(noreplace) %{_localstatedir}/lib/amanda/template.d/*

%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, sys) /lib/svc/manifest
%dir %attr (0755, root, sys) %{svcdir}
%class(manifest) %attr (0444, root, sys) %{svcdir}/amandaserver.xml

%files client
%defattr(-, root, bin)
%defattr(-,root,root)
%dir %{_libexecdir}/amanda/application/
%attr(4750,root,sys) %{_libexecdir}/amanda/application/amgtar
%attr(4750,root,sys) %{_libexecdir}/amanda/application/amstar
%defattr(-,root,sys)
%{_libexecdir}/amanda/application/amlog-script
%{_libexecdir}/amanda/application/ampgsql
%{_libexecdir}/amanda/application/amraw
%{_libexecdir}/amanda/application/amsamba
%{_libexecdir}/amanda/application/amsuntar
%{_libexecdir}/amanda/application/amzfs-sendrecv
%{_libexecdir}/amanda/application/amzfs-snapshot
%{_libexecdir}/amanda/application/script-email

%attr(4750,root,sys) %{_libexecdir}/amanda/calcsize
%attr(4750,root,sys) %{_libexecdir}/amanda/killpgrp
%{_libexecdir}/amanda/noop
%{_libexecdir}/amanda/patch-system
%attr(4750,root,sys) %{_libexecdir}/amanda/rundump
%attr(4750,root,sys) %{_libexecdir}/amanda/runtar
%{_libexecdir}/amanda/selfcheck
%{_libexecdir}/amanda/sendbackup
%{_libexecdir}/amanda/sendsize
%{_libexecdir}/amanda/teecount
%{_sbindir}/amdump_client
%{_sbindir}/amoldrecover
%{_sbindir}/amrecover

%defattr(-,root,bin)
%{_mandir}/man7/amanda-applications.7*
%{_mandir}/man8/amdump_client.8*
%{_mandir}/man5/amanda-client.conf.5*
%{_mandir}/man8/amgtar.8*
%{_mandir}/man8/ampgsql.8*
%{_mandir}/man8/amraw.8*
%{_mandir}/man8/amrecover.8*
%{_mandir}/man8/amoldrecover.8*
%{_mandir}/man8/amsamba.8*
%{_mandir}/man8/amstar.8*
%{_mandir}/man8/amsuntar.8*
%{_mandir}/man8/amzfs-sendrecv.8*
%{_mandir}/man8/amzfs-snapshot.8*
%{_mandir}/man8/killpgrp.8*

%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Application.pm
%attr(-,%amanda_user, sys) %{_prefix}/%{perl_path_vendor_perl_version}/Amanda/Application/

%dir %attr(2775,%amanda_user, sys) %{_sysconfdir}/amanda/
%dir %attr(2775,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/amanda-client.conf
%config(noreplace) %attr(664,%amanda_user, sys) %{_sysconfdir}/amanda/%defconfig/amanda-client-postgresql.conf

%dir %attr (0755, root, sys)  %{_localstatedir}
%dir %attr (0755, root, other)  %{_localstatedir}/lib
%attr(0755,%amanda_user,sys)     %dir %{_localstatedir}/lib/amanda/
%attr(-,%amanda_user,sys) %config(noreplace) %{_localstatedir}/lib/amanda/amandates
%attr(-,%amanda_user,sys) %{_localstatedir}/lib/amanda/gnutar-lists

%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, sys) /lib/svc/manifest
%dir %attr (0755, root, sys) %{svcdir}
%class(manifest) %attr (0444, root, sys) %{svcdir}/amandaclient.xml

%changelog
* Thr May 08 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- You can use amanda immediately.
- added manifests.
- rewrite category like linux.
- bump to 3.3.5
* Sun Jan 27 2013 - Ken Mays <kmays2000@gmail.com>
- bump to 3.3.3
* Sat Jan 26 2013 - Ken Mays <kmays2000@gmail.com>
- bump to 3.2.3, migrated to pnm_macros usage for Perl
* Sat Dec 25 2010 - Milan Jurik
- bump to 3.2.1
* Sat Nov 27 2010 - Milan Jurik
- bump to 3.2.0
* Sun Jul 11 2010 - Milan Jurik
- Initial spec based on Fedora
