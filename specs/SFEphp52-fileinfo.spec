#
# spec file for package eblib
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#
%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  1.0.4
%define tarball_name     Fileinfo

Name:                    SFEphp52-fileinfo
IPS_package_name:	 web/php-52/extension/php-fileinfo
Summary:                 PHP 5.2 module for Fileinfo
Version:                 1.0.4
License:		 PHP License
Url:                     http://pecl.php.net/package/%{tarball_name}
Source:                  http://pecl.php.net/get/%{tarball_name}-%{tarball_version}.tgz
Source1:                 %{name}.ini
Patch1:			 %{name}-01-ramsy.diff
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: %{pnm_buildrequires_SUNWphp52}
BuildRequires: %{pnm_buildrequires_SUNWgsed_devel}
BuildRequires: SFEfile
BuildRequires: SFEre2c

Requires: %{pnm_requires_SUNWphp52}
Requires: SFEfile

# OpenSolaris IPS Package Manifest Fields
Meta(info.upstream):	 	Ilia Alshanetsky <ilia@prohost.org>
Meta(info.maintainer):	 	taki@justplayer.com
Meta(info.repository_url):	http://cvs.php.net/viewvc.cgi/php-src/ext/fileinfo/
Meta(info.classification):	Development/PHP

%description
Allows retrieval of information regarding a vast majority of file types. This information may include dimensions, quality, length etc. Additionally it can also be used to retrieve the mime type for a particular
file and for text files proper language encoding.

%prep
%setup -c -n %name-%version
%patch1 -p0

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="%_ldflags"
export CC=cc
pwd
cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

/usr/php/5.2/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir} \
 --with-fileinfo=/usr/gnu \
 --with-php-config=/usr/php/5.2/bin/php-config

gmake -j$CPUS
gmake test

%install
cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/php/5.2/modules/
cp modules/fileinfo.so $RPM_BUILD_ROOT/%{_prefix}/php/5.2/modules/
mkdir -p  $RPM_BUILD_ROOT/etc/php/5.2/conf.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/php/5.2/conf.d/%{tarball_name}.ini

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/5.2/modules
%{_prefix}/php/5.2/modules/*
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/php/5.2/conf.d/*

%changelog
* Sun Mar 27 2011 TAKI, Yasushi <taki@justplayer.com>
- Change Permission at /etc
* Tue Jun 30 2011 TAKI, Yasushi <taki@justplayer.com>
- Initial Revision
