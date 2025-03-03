#
# spec file for package SFEOpenIPMI
#
# TODO: uses private copy of libedit, should be modified to use system one
%include Solaris.inc
%define cc_is_gcc 1
%include packagenamemacros.inc
%include base.inc
#%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Summary: IPMI (Intelligent Platform Management Interface) library and tools
Name: SFEOpenIPMI
IPS_Package_Name: system/management/openipmi
SUNW_Copyright:         %{name}.copyright
#rc
#Version: 2.0.20-rc3
Version: 2.0.19
#Release: 14%{?dist}
License: LGPLv2+ and GPLv2+ or BSD
Group: System Environment/Base
URL: http://sourceforge.net/projects/openipmi/
#rc
#Source: http://ftp.jaist.ac.jp/pub/sourceforge/o/project/op/openipmi/OpenIPMI\ 2.0\ Library/OpenIPMI-%{version}.tar.gz
Source: http://ftp.jaist.ac.jp/pub/Linux/Momonga/development/source/SOURCES/OpenIPMI-%{version}.tar.gz
Source1: SFEOpenIPMI-openipmi.sysconf
Source2: SFEOpenIPMI-openipmi.initscript
Source4: SFEOpenIPMI-openipmi.README.initscript
%include default-depend.inc
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: %pnm_buildrequires_library_database_gdbm %pnm_buildrequires_developer_swig %pnm_buildrequires_library_glib2 %pnm_buildrequires_system_management_snmp_net %pnm_buildrequires_library_ncurses
BuildRequires: %pnm_buildrequires_openssl
BuildRequires: %pnm_buildrequires_gnome_preferences_control_center
Requires: system/management/openipmi/libs
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif

Patch0: OpenIPMI-2.0.19.solaris.patch

%description
The Open IPMI project aims to develop an open code base to allow access to
platform information using Intelligent Platform Management Interface (IPMI).
This package contains the tools of the OpenIPMI project.

%package libs
IPS_Package_Name: system/management/openipmi/libs
Group: Development/Libraries
Summary: The OpenIPMI runtime libraries

%description libs
The OpenIPMI-libs package contains the runtime libraries for shared binaries
and applications.

#%package perl
#Group: Development/Libraries
#Summary: IPMI Perl language bindings
#Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
#Requires: OpenIPMI-libs = %{version}-%{release}

#%description perl
#The OpenIPMI-perl package contains the Perl language bindings for OpenIPMI.

#%package python
#Group: Development/Libraries
#Summary: IPMI Python language bindings
#Requires: OpenIPMI-libs = %{version}-%{release} 

#%description python
#The OpenIPMI-python package contains the Python language bindings for OpenIPMI.

%package developer
IPS_Package_Name: system/management/openipmi/developer
Group: Development/Libraries
Summary: The development environment for the OpenIPMI project
#Requires: pkgconfig
#Requires: %{name} = %{version}-%{release}
Requires: system/management/openipmi

%description developer
The OpenIPMI-devel package contains the development libraries and header files
of the OpenIPMI project.

%prep
%setup -q -n OpenIPMI-%{version}
%patch0 -p1

%build
#export CFLAGS="-fPIC $RPM_OPT_FLAGS -fno-strict-aliasing"
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi
export CC=gcc
export CXX=g++
export CFLAGS="%optflags -fno-strict-aliasing -Wno-pointer-sign"
export CPPFLAGS="-D_POSIX_PTHREAD_SEMANTICS"
export LDFLAGS="%{_ldflags} -lncurses -lsocket -lnsl -luuid"
export LD_OPTIONS="%gnu_lib_path"

#%configure --with-pythoninstall=%{python_sitearch} --disable-dependency-tracking --with-tcl=no --disable-static --with-tkinter=no
%configure --disable-dependency-tracking --with-tcl=no --disable-static --with-tkinter=no
# get rid of rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make -j$CPUS  # not %{?_smp_mflags} safe

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/openipmigui.1*

#install -d ${RPM_BUILD_ROOT}%{_sysconfdir}
#install -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_sysconfdir}/ipmi.conf
install -m 644 %SOURCE1 ./ipmi_pending.conf
#install -d ${RPM_BUILD_ROOT}%{_initrddir}
#install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}%{_initrddir}/ipmi
#install -d ${RPM_BUILD_ROOT}/lib/svc/method
#install -m 755 %{SOURCE2} ${RPM_BUILD_ROOT}/lib/svc/method/ipmi
install -m 755 %{SOURCE2} ./ipmi_pending.initscript
install -m 644 %SOURCE4 ./README.initscript

#%post
#/sbin/chkconfig --add ipmi

#%preun
#if [ $1 = 0 ]; then
#   service ipmi stop >/dev/null 2>&1
#   /sbin/chkconfig --del ipmi
#fi

#%postun
#if [ "$1" -ge "1" ]; then
#    service ipmi condrestart >/dev/null 2>&1 || :
#fi

#%post libs -p /sbin/ldconfig

#%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%doc CONFIGURING_FOR_LAN COPYING COPYING.BSD COPYING.LIB FAQ README README.Force README.MotorolaMXP README.initscript *_pending.*
#%dir %attr (0755, root, sys) %{_sysconfdir}
#%config(noreplace) %{_sysconfdir}/ipmi.conf
#%{_initrddir}/ipmi
#%dir %attr (0755, root, bin) /lib
#%dir %attr (0755, root, bin) /lib/svc
#%dir %attr (0755, root, bin) /lib/svc/method
#%attr (0755, root, bin) /lib/svc/method/ipmi
%{_bindir}/ipmicmd
%{_bindir}/ipmilan
%{_bindir}/ipmish
%{_bindir}/ipmi_ui
%{_bindir}/openipmicmd
%{_bindir}/openipmish
%{_bindir}/rmcp_ping
%{_bindir}/solterm
%{_mandir}/man1/ipmi_ui*
%{_mandir}/man1/openipmicmd*
%{_mandir}/man1/openipmish*
%{_mandir}/man1/rmcp_ping*
%{_mandir}/man1/solterm*
%{_mandir}/man7/ipmi_cmdlang*
%{_mandir}/man7/openipmi_conparms*
%{_mandir}/man8/ipmilan*

#%files perl
#%defattr(-,root,root)
#%attr(644,root,root) %{perl_vendorarch}/OpenIPMI.pm
#%{perl_vendorarch}/auto/OpenIPMI/

#%files python
#%defattr(-,root,root)
#%{python_sitearch}/*OpenIPMI*

%files libs
%defattr(-,root,bin)
%{_libdir}/*.so.*

%files developer
%defattr(-,root,bin)
%{_includedir}/OpenIPMI
%{_libdir}/*.so
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Dec 06 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- changed the download url
- appended a file dependency of gcc.

* Wed Dec 04 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- disable perl and python

* Tue Dec 11 2012 Ales Ledvinka <aledvink@redhat.com> - 2.0.16-14
- fixed rpmdiff tests

* Tue Dec 11 2012 Ales Ledvinka <aledvink@redhat.com> - 2.0.16-13
- init script modified for in-kernel ipmi (#881450)

* Fri May 28 2010 Jan Safranek <jsafrane@redhat.com> - 2.0.16-12
- compiled with -fno-strict-aliasing (#596148)

* Wed May 26 2010 Jan Safranek <jsafrane@redhat.com> - 2.0.16-11
- fixed pkgconfig configuration file (#594072)

* Mon May  3 2010 Jan Safranek <jsafrane@redhat.com> - 2.0.16-10
- removed OpenIPMI-gui subpackage, because TCL is compile without
  multithreading support and the gui relies on it (#588332)

* Thu Mar 18 2010 Jan Safranek <jsafrane@redhat.com> - 2.0.16-9
- implemented mandatory 'force-reload' command in ipmi service (#562151)

* Wed Mar  3 2010 Jan Safranek <jsafrane@redhat.com> - 2.0.16-8
- add README.initscript describing /etc/init.d/ipmi initscript exit codes
  (#562151)

* Mon Feb 22 2010 Jan Safranek <jsafrane@redhat.com> - 2.0.16-7
- fix package License: field, there *are* sources with BSD header
- distribute README files and COPYING in package

* Tue Jan  5 2010 Jan Safranek <jsafrane@redhat.com> - 2.0.16-6
- fix package License: field, there is no source with BSD header

* Tue Dec  1 2009 Jan Safranek <jsafrane@redhat.com> - 2.0.16-5
- fix rpmlint errors

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.0.16-4
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 15 2009 Jan Safranek <jsafrane@redhat.com> - 2.0.16-2
- fix compilation flags, debuginfo package is correctly generated now

* Thu Mar 19 2009 Jan Safranek <jsafrane@redhat.com> - 2.0.16-1
- new upstream release

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 2.0.14-10
- rebuild with new openssl

* Thu Dec 11 2008 Jan Safranek <jsafrane@redhat.com> - 2.0.14-9
- fix linking without rpath, prelink won't screw up the libraries
  anymore (#475265)

* Wed Dec 10 2008 Jan Safranek <jsafrane@redhat.com> - 2.0.14-8
- shorter probe interval is used in init script, making the service startup
  quicker in most situations (#475101)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.14-7
- Rebuild for Python 2.6

* Thu Oct 30 2008 Jan Safranek <jsafrane@redhat.com> - 2.0.14-6
- removed static libraries from the -devel subpackage
- fixed openipmigui.desktop file

* Thu Oct 23 2008 Jan Safranek <jsafrane@redhat.com> - 2.0.14-5
- fixed typos in the descriptions
- added .desktop file for openipmigui tool

* Mon Oct 20 2008 Jan Safranek <jsafrane@redhat.com> - 2.0.14-4
- fixed description of the package

* Thu Oct 16 2008 Jan Safranek <jsafrane@redhat.com> - 2.0.14-3
- split ipmitool to separate package
- added 'reload' functionality to init script
- added seraparate -gui subpackage

* Wed Jul 30 2008 Phil Knirsch <pknirsch@redhat.com> - 2.0.14-2
- Fixed rpath problem in libOpenIPMIposix.so.0.0.1

* Tue Jul 29 2008 Phil Knirsch <pknirsch@redhat.com> - 2.0.14-1
- Fixed several specfile problems (#453751)
- Update to OpenIPMI-2.0.14

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.13-2
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Phil Knirsch <pknirsch@redhat.com> - 2.0.13-1
- Updated to OpenIPMI-2.0.13
- Rebuild due to new openssl

* Wed Oct 10 2007 Phil Knirsch <pknirsch@redhat.com> - 2.0.11-3
- Added missing perl-devel buildrequires

* Mon Sep 24 2007 Phil Knirsch <pknirsch@redhat.com> - 2.0.11-2
- Added missing popt-devel buildrequires

* Fri Aug 17 2007 Phil Knirsch <pknirsch@redhat.com> - 2.0.11-2
- Fix rebuild problems due to glibc change
- License review and fixes

* Tue Apr 24 2007 Phil Knirsch <pknirsch@redhat.com> - 2.0.11-1
- Update to OpenIPMI-2.0.11

* Tue Feb 27 2007 Phil Knirsch <pknirsch@redhat.com> - 2.0.6-8
- Update for ipmitool-1.8.9

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.0.6-7
- rebuild for python 2.5

* Tue Nov 28 2006 Phil Knirsch <pknirsch@redhat.com> - 2.0.6-6.fc7
- Update due to new net-snmp-5.4
- Some specfile updates

* Tue Jul 18 2006 Phil Knirsch <pknirsch@redhat.com> - 2.0.6-5
- Fixed check for udev in initscript (#197956)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.6-4.1
- rebuild

* Fri Jun 16 2006 Bill Nottingham <notting@redhat.com> 2.0.6-4
- don't include <linux/compiler.h>

* Fri Jun 16 2006 Jon Masters <jcm@redhat.com> 2.0.6-3
- Fix a build requires (needs glibc-kernheaders)

* Thu Jun 15 2006 Jesse Keating <jkeating@redhat.com> 2.0.6-2
- Bump for new glib2

* Tue May 16 2006 Phil Knirsch <pknirsch@redhat.com> 2.0.6-1
- Fixed bug with type conversion in ipmitool (#191091)
- Added python bindings 
- Split off perl and python bindings in separate subpackages
- Dropped obsolete patches
- Added missing buildprereq on readline-devel
- Made it install the python bindings properly on 64bit archs

* Mon May 15 2006 Phil Knirsch <pknirsch@redhat.com>
- Updated ipmitool to 1.8.8
- Updated OpenIPMI to 2.0.6

* Fri Feb 17 2006 Phil Knirsch <pknirsch@redhat.com> 1.4.14-19
- Added missing PreReq for chkconfig

* Mon Feb 13 2006 Jesse Keating <jkeating@redhat.com> - 1.4.14-18.2.1
- rebump for build order issues during double-long bump

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.4.14-18.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.4.14-18.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Feb 06 2006 Phil Knirsch <pknirsch@redhat.com> 1.4.14-18
- Updated ipmitool to latest upstream version.
- Removed 3 patches for already fixed bugs in latest ipmitool.
- Adapted warning message fix for ipmitool for latest version.

* Tue Jan 24 2006 Phil Knirsch <pknirsch@redhat.com> 1.4.14-17
- Fixed some minor things in initscripts.

* Mon Jan 09 2006 Phil Knirsch <pknirsch@redhat.com> 1.4.14-16
- Included FRU fix for displaying FRUs with ipmitool
- Included patch for new option to specify a BMC password for IPMI 2.0 sessions

* Tue Jan 03 2006 Radek Vokal <rvokal@redhat.com> 1.4.14-15
- Rebuilt against new libnetsnmp

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 23 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-14
- Some more initscript and sysconfig updates from Dell.

* Wed Nov 09 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-13
- Rebuilt to link against latest openssl libs.
- Fixed ipmitool not setting session privilege level (#172312)

* Wed Nov 02 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-11
- Rebuild to link against new net-snmp libs.

* Tue Oct 11 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-10
- Updated initscript to fix missing redhat-lsb bug (#169901)

* Thu Sep 08 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-9
- Another update to latest initscripts from Dell
- Fixed some missing return statements for non-void functions (#164138)

* Thu Sep 01 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-8
- Updated initscript to latest version from Dell

* Fri Aug 12 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-7
- Fixed the unwanted output of failed module loading of the initscript. Behaves
  now like all our other initscripts (#165476)

* Fri Aug 05 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-6
- Fixed build problem on 64bit machines

* Fri Jul 15 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-5
- Fixed missing change to not autostart in the initscript

* Wed Jul 06 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-4
- Made the initscript a replacing configfile

* Mon Jul 04 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-3
- Updated versions of the initscripts and sysconf files
- Fixed typo in preun script and changelog

* Mon Jun 27 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.14-2
- Updated to OpenIPMI-1.4.14
- Split the main package into normal and libs package for multilib support
- Added ipmitool-1.8.2 to OpenIPMI and put it in tools package
- Added sysconf and initscript (#158270)
- Fixed oob subscripts (#149142)

* Wed Mar 30 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.11-5
- Correctly put libs in the proper packages

* Thu Mar 17 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.11-4
- gcc4 rebuild fixes
- Added missing gdbm-devel buildprereq

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 1.4.11-3
- bump release and rebuild with gcc 4

* Tue Feb 08 2005 Karsten Hopp <karsten@redhat.de> 1.4.11-2 
- update

* Tue Oct 26 2004 Phil Knirsch <pknirsch@redhat.com>
- Initial version
