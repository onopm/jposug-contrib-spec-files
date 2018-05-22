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
%define tarball_version  2.3.1
%define tarball_name     xdebug

Name:                    SFEphp55-xdebug
IPS_package_name:	 web/php-55/extension/php-xdebug
Summary:                 Xdebug module for PHP 5.5
Version:                 %{tarball_version}
License:		 Xdebug License
Url:                     http://xdebug.org/
Source:                  http://xdebug.org/files/%{tarball_name}-%{tarball_version}.tgz
Source1:                 %{name}.ini
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-55
Requires: web/php-55 >= *

%prep
%setup -c -n %tarball_name-%tarball_version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="-m64 -xO4 -xchip=pentium -xregs=no%frameptr -mt"
export CPPFLAGS="-m64 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
export LDFLAGS="-L/lib/`isainfo -k` -L/usr/lib/`isainfo -k` -R/lib/`isainfo -k` -R/usr/lib/`isainfo -k`"

#export CFLAGS="$RPM_OPT_FLAGS"
#export LDFLAGS="%_ldflags"
#export CC=cc

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

/usr/php/5.5/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir} \
 --with-php-config=/usr/php/5.5/bin/php-config

gmake -j$CPUS CFLAGS="$CFLAGS"
echo no | gmake test

%install

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/usr/php/5.5/lib/extensions/no-debug-non-zts-20121212
cp modules/xdebug.so $RPM_BUILD_ROOT/usr/php/5.5/lib/extensions/no-debug-non-zts-20121212
mkdir -p  $RPM_BUILD_ROOT/etc/php/5.5/conf.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/php/5.5/conf.d/%{tarball_name}.ini

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
# %dir %attr(0755, root, bin) %{_prefix}/php/5.5/modules
# %{_prefix}/php/5.5/modules/*
/usr/php/5.5/lib/extensions/no-debug-non-zts-20121212/*
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/php/5.5/conf.d/*

%changelog
* Wed Mar 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.1
* Tue Apr 15 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- require any version of php-55
- Initial Revision
