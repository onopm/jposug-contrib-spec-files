#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name:                SFElibast
IPS_Package_Name:	 library/desktop/libast 
Summary:             Library of Assorted Spiffy Things
Version:             0.7
Source:              http://eterm.org/download/libast-%{version}.tar.gz
License:             MIT
Group:		Desktop (GNOME)/Libraries
SUNW_Copyright:      libast.copyright
URL:                 http://www.eterm.org/download/

SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n libast-%version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

# This source is gcc-centric, therefore...
export CC=gcc
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
#export CFLAGS="-O4 -fPIC -DPIC -Xlinker -i -fno-omit-frame-pointer"
%if %option_with_fox
export CFLAGS="$CFLAGS -I/usr/X11/include"
%endif
export LDFLAGS="%_ldflags"
%configure --enable-static=no
make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm ${RPM_BUILD_ROOT}%{_libdir}/libast.la

%changelog
* Mon Jun 10 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- Added 64bit build
* Wed Jul 20 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Sun Jul 10 2011 - Alex Viskovatoff
- Build with SFEgcc
* Fri Mar 21 2008 - nonsea@users.sourceforge.net
- Fix Source error.
* Thu Nov 15 2007 - daymobrew@users.sourceforge.net
- Add support for Indiana builds.
* Mon Mar 19 2007 - dougs@truemail.co.th
- Fixed -fno-omit-frame-pointer flag
* Tue Nov 07 2006 - Eric Boutilier
- Initial spec
