# spec file for package fribidi
#
# Copyright (c) 2007 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%define src_name fribidi
Name:        SFEfribidi 
Version:     0.19.2
Summary:     Library implementing the Unicode Bidirectional Algorithm
Group:       System/Libraries
License:     LGPLv2
URL:         http://fribidi.org/
Source:      http://fribidi.org/download/%{src_name}-%{version}.tar.gz
BuildRoot:   %{_tmppath}/%{name}-%{version}-root

%prep
%setup -q -n %{src_name}-%{version}

%build
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export CFLAGS="%optflags"
export RPM_OPT_FLAGS="$CFLAGS"
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

./configure --prefix=%{_prefix}		\
	    --libdir=%{_libdir}		\
	    --bindir=%{_bindir}		\
	    --includedir=%{_includedir}	\
	    --sysconfdir=%{_sysconfdir}	\
	    --datadir=%{_datadir}       \
	    --mandir=%{_mandir}

make -j $CPUS
 
%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf ${RPM_BUILD_ROOT}

%changelog
* Sun Apr 11 2010 - Milan Jurik
- cleanup for the latest pkgtool
* Sun Aug 17 2008 - nonsea@users.sourceofrge.net
- Bump to 0.19.1
* Fri Oct 19 2007 - nonsea@users.sourceforge.net
- Initial spec
