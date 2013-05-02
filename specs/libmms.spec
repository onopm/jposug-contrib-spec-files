#
# spec file for package libmms
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner:halton
# bugdb: http://bugs.launchpad.net/libmms/+bug/
#

Name:           libmms
Summary:        mms stream protocol library
Group:          Libraries/Multimedia
Version:        0.6.2
Release:        1
Distribution:   Java Desktop System
Vendor:         Sun Microsystems, Inc.
URL:            http://sourceforge.net/projects/libmms/
License:      	LGPL
Source:         %{sf_download}/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

%description
libmms is a library implementing the mms streaming protocol

%package devel
Summary: Libraries and includefiles for developing with libmms
Group:	 Development/Libraries

%description devel
This paackage provides the necessary development headers and libraries
to allow you to devel with libmms

%prep
%setup -q
cd ..
%ifarch amd64 sparcv9
rm -rf %{name}-%{version}-64
cp -rp %{name}-%{version} %{name}-%{version}-64
%endif

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi
export CFLAGS="%optflags"
libtoolize --force
aclocal $ACLOCAL_FLAGS -I .
autoheader
automake -a -c -f
autoconf

./configure --prefix=%{_prefix} \
            --bindir=%{_bindir} \
            --mandir=%{_mandir} \
            --libdir=%{_libdir} \
            --datadir=%{_datadir} \
            --includedir=%{_includedir} \
            --sysconfdir=%{_sysconfdir}
make -j $CPUS

%ifarch amd64 sparcv9
cd ../%{name}-%{version}-64
export CFLAGS="%optflags64"
export RPM_OPT_FLAGS="$CFLAGS"
export CFLAGS="$CFLAGS -m64"
libtoolize --force
aclocal $ACLOCAL_FLAGS -I .
autoheader
automake -a -c -f
autoconf

./configure --prefix=%{_prefix} \
            --bindir=%{_bindir}/%{_arch64} \
            --mandir=%{_mandir} \
            --libdir=%{_libdir}/%{_arch64} \
            --datadir=%{_datadir} \
            --includedir=%{_includedir} \
            --sysconfdir=%{_sysconfdir}
make -j $CPUS
%endif

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make -i install DESTDIR=$RPM_BUILD_ROOT
%ifarch amd64 sparcv9
cd ../%{name}-%{version}-64
make -i install DESTDIR=$RPM_BUILD_ROOT
%endif
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%changelog
* Thr May 01 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- 64 bit ready
* Sun Oct 23 2011 - Milan Jurik
- bump to 0.6.2
* Thu Jun 10 2010 - Albert Lee <trisk@opensolaris.org>
- Bump to 0.6
- Update URLs
* Tue Sep 02 2008 - halton.huo@sun.com
- Initial version
