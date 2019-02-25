#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

# TODO: write SMF manifest for rtmpsrv

Name:                SFErtmpdump
Summary:             RTMPdump -- a toolkit for RTMP streams
IPS_package_name:    video/rtmpdump
Group:               Applications/Sound and Video
License:             GPLv2+, LGPLv2+
SUNW_copyright:      rtmpdump.copyright
URL:                 http://rtmpdump.mplayerhq.hu/
Version:             2.4
Source:		http://rtmpdump.mplayerhq.hu/download/rtmpdump-%{version}.tar.gz
Patch1:		SFErtmpdump-make.patch
Patch2:		SFErtmpdump-librtmp-make.patch
SUNW_BaseDir:        %{_basedir}

%prep
%setup -q -n rtmpdump
%patch1 -p0 -b .orig
%patch2 -p0 -b .orig

%build
export CC=gcc
export CXX=g++
export XCFLAGS="%optflags"
%if %opt_arch64
export XLDFLAGS="-m64"
%else
unset XLDFLAGS
%endif
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

# Rtmpdump has no configure. We'll make do.
XLIBS="-lnsl -lsocket" gmake -j$CPUS

%install
%if %opt_arch64
export SUFFIX=/%{_arch64}
%else
unset SUFFIX
%endif
make install DESTDIR=$RPM_BUILD_ROOT
rm ${RPM_BUILD_ROOT}%{_libdir}/librtmp.a
mv ${RPM_BUILD_ROOT}%{_prefix}/sbin/* ${RPM_BUILD_ROOT}%{_bindir}
rm -r ${RPM_BUILD_ROOT}%{_prefix}/sbin

# move mandirs to a more sensible home
if [ -d ${RPM_BUILD_ROOT}%{_mandir} ]
then
  rm -r ${RPM_BUILD_ROOT}%{_mandir}
fi
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}
mv ${RPM_BUILD_ROOT}%{_prefix}/man/* ${RPM_BUILD_ROOT}%{_mandir}
rm -r ${RPM_BUILD_ROOT}%{_prefix}/man

cd %buildroot%_libdir/pkgconfig
sed 's/libssl,libcrypto/openssl/' librtmp.pc > librtmp.pc.new
mv librtmp.pc.new librtmp.pc

%changelog
* Tue May 14 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- Added 64bit build
* Sat Feb 09 2013 - Milan Jurik
- bump to 2.4
* Oct 12 2011 - Alex Viskovatoff
- Fix librtmp.pc; add SUNW_copyright and IPS_package_name
* Dec 28 2010 - jchoi42@pha.jhu.edu
- Initial spec
