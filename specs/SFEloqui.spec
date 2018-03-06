#
# spec file for package Loqui
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#
%include Solaris.inc
%define cc_is_gcc 1
%include packagenamemacros.inc
%include base.inc

%define _prefix	         /usr
%define _var_prefix      /var
%define tarball_name     loqui
%define tarball_version  0.5.5
%define major_version    0.5

%define _basedir         %{_prefix}

Name:                    SFEloqui
IPS_package_name:        desktop/irc/loqui
Summary:	         Loqui IRC Client for Gtk2
Version:                 0.5.5
License:		 GPL
Url:                     https://launchpad.net/%{tarball_name}
Source:			 http://launchpad.net/%{tarball_name}/%{major_version}/%{tarball_version}/+download/%{tarball_name}-%{tarball_version}.tar.gz

Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif
BuildRequires: SFEgob
Requires: SFEgob

# OpenSolaris IPS Package Manifest Fields
Meta(info.upstream):	 	Loqui Developer Team
Meta(info.maintainer):	 	TAKI, Yasushi <taki@justplayer.com>
# Meta(info.repository_url):	[open source code repository]
Meta(info.classification):	Applications/Internet

%description
Loqui is a IRC Client that has following features:
 - Connect to multiple servers
 - The view that outputs all messages on other channels (call "Common Buffer")
 - Window has 4-views (Message of the current channel, nick list, channel list, "Common Buffer")
 - Multi-protocols (beta)

%prep
%setup -c -n %{tarball_name}-%{tarball_version}
#%patch1 -p0

%ifarch amd64 sparcv9
rm -rf %{tarball_name}-%{tarball_version}-64
cp -rp %{tarball_name}-%{tarball_version} %{tarball_name}-%{tarball_version}-64
%endif

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

export CC=gcc
export CXX=g++
export LDFLAGS="%_ldflags %gnu_lib_path -lsocket"

./configure --prefix=%{_prefix} \
            --exec-prefix=%{_prefix} \
            --bindir=%{_prefix}/bin \
            --libexecdir=%{_prefix}/bin \
            --sbindir=%{_prefix}/bin \
            --datadir=%{_prefix}/share \
            --sysconfdir=%{_prefix}/etc \
            --mandir=%{_prefix}/man \
            --libdir=%{_prefix}/lib \
            --includedir=%{_prefix}/include \
            --localedir=%{_prefix}/share/locale/ \
            --docdir=%{_prefix}/doc \
            --with-includes=/usr/include:/usr/sfw/include:/usr/sfw/include:/usr/gnu/include \
            --with-libs=/usr/lib:/usr/sfw/lib:/usr/gnu/lib

gmake -j$CPUS 

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{tarball_version}-64

export CFLAGS="-m64"
export LDFLAGS="-lsocket"

./configure --prefix=%{_prefix} \
            --exec-prefix=%{_prefix} \
            --bindir=%{_prefix}/bin/%{_arch64} \
            --libexecdir=%{_prefix}/bin/%{_arch64} \
            --sbindir=%{_prefix}/bin/%{_arch64} \
            --datadir=%{_prefix}/share \
            --sysconfdir=%{_prefix}/etc \
            --mandir=%{_prefix}/man \
            --libdir=%{_prefix}/lib/%{_arch64} \
            --includedir=%{_prefix}/include \
            --sharedstatedir=%{_var_prefix} \
            --localstatedir=%{_var_prefix} \
            --localedir=%{_prefix}/share/locale/ \
            --docdir=%{_prefix}/doc \
            --with-includes=/usr/include:/usr/sfw/include:/usr/sfw/include:/usr/gnu/include \
            --with-libs=/usr/lib/%{_arch64}:/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64}

gmake -j$CPUS

%endif
%install
cd %{tarball_name}-%{tarball_version}

gmake install DESTDIR=$RPM_BUILD_ROOT

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{tarball_version}-64
gmake install DESTDIR=$RPM_BUILD_ROOT
%endif

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_prefix}/share
%attr (0755, root, other) %{_prefix}/share/*

%changelog
* Tue Mar 19 2013 - TAKI <taki@justplayer.com>
- bump to 0.5.5
* Tue Feb 05 2013 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- change BuildRequires that refer to gcc at OI
* Tue Jan 19 JST 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Support for OpenIndiana
* Sat Jan  5 JST 2013 TAKI, Yasushi <taki@justplayer.com>
- bump to 0.5.3
- add build requires gcc-45
* Sun Jun  5 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- fix dependency using for pnm.
* Tue Feb  1 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- Fix some problems.
* Tue Jan 25 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- Initial Revision
