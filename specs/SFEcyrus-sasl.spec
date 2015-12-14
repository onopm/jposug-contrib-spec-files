#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

Name:		SFEcyrus-sasl
SUNW_Copyright: %{name}.copyright
IPS_Package_Name:	library/security/cyrus-sasl
Summary:	Simple Authentication and Security Layer library
Version:	2.1.26
Source:		ftp://ftp.cyrusimap.org/cyrus-sasl/cyrus-sasl-%{version}.tar.gz
Patch0:		saslutil.c.patch
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

Requires: %{pnm_requires_SUNWsqlite3} 
BuildRequires: %{pnm_buildrequires_SUNWsqlite3}
#Requires: %{pnm_buildrequires_SUNWopenssl_libraries}
Requires: %{pnm_requires_library_security_openssl}
#BuildRequires: %{pnm_buildrequires_SUNWopenssl_libraries}
BuildRequires: %{pnm_buildrequires_library_security_openssl}
Requires: library/security/libntlm
BuildRequires: library/security/libntlm
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: SFEgcc
Requires:      SFEgccruntime
%endif

%description
SASL is the Simple Authentication and Security Layer, a method for adding authentication support to connection-based protocols.
To use SASL, a protocol includes a command for identifying and authenticating a  user to a server and for optionally negotiating protection of subsequent protocol interactions.
If its use is negotiated, a security layer is inserted between the protocol and the connection.

%prep
%setup -q -n cyrus-sasl-%{version}
%patch0 -p0

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

# needed to prevent an error during configure - strip whitespace
export CC=gcc
export CXX=g++
#CFLAGS="%optflags -I/usr/gnu/include -I/usr/include/gssapi"
#export CFLAGS="`echo $CFLAGS`"
export CFLAGS="%optflags -I/usr/include/gssapi -fPIC"
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags"

./configure --prefix %{_prefix} \
           --enable-shared=yes \
           --enable-static=no \
           --with-dbpath=%{_sysconfdir}/sasldb2 \
           --with-plugindir=%{_libdir}/sasl2 \
           --includedir=%{_includedir}/sasl2 \
           --sysconfdir %{_sysconfdir} \
           --mandir %{_mandir} \
           --with-ipctype=doors

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/sasl2/*.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/sbin
%{_prefix}/sbin/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, other) %{_libdir}/sasl2
%{_libdir}/sasl2/lib*.so*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, bin) %{_includedir}
%dir %attr (0755, root, other) %{_includedir}/sasl2
%{_includedir}/sasl2/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*
%dir %attr (0755, root, bin) %{_mandir}/man8
%{_mandir}/man8/*

%changelog
* Wed Jan 09 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- add --includedir
* Tue Jan 08 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Bump to 2.1.26 (by TAKI,Yasushi <taki@justplayer.com>)
- changed %_prefix
- Fix error "identifier redeclared: gethostname" for Solaris11
- Fix configure option problem
* Tue Jan 08 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- fix linker option problem
* Mon Jan 07 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- build with gcc by default
* Sat Dec 08 2012 - YAMAMOTO Takashi
- use pnm macros
* Mon Dec 12 2011 - Milan Jurik
- bump to 2.1.25
* Sun Feb 13 2011 - Milan Jurik
- bump to 2.1.23
* Fri Oct 24 2008 - jedy.wang@sun.com
- Fixes plugindir problem.
* Fri Jun 06 2008 - river@wikimedia.org
- strip whitespace from $CFLAGS otherwise autoconf gets upset
* Sun Feb 03 2008 - moinak.ghosh@sun.com
- Add dependency on SFElibntlm.
* Tue Jan 15 2008 - moinak.ghosh@sun.com
- Initial spec.
