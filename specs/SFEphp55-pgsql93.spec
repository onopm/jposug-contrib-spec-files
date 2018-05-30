#
# spec file for package SFEphp55-pgsql93
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#
%include Solaris.inc

%define _prefix /usr
%define php_version 5.5
%define tarball_version  5.5.26
%define tarball_name     php

Name:                    SFEphp55-pgsql93
IPS_package_name:	 web/php-55/extension/php-pgsql93
Summary:                 PHP 5.5 module for PostgreSQL 93
Version:                 %{tarball_version}
License:		 PHP License
Url:                     http://www.php.net/
Source:			 http://jp.php.net/distributions/%{tarball_name}-%{tarball_version}.tar.bz2
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
#SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-55 >= %{version}
BuildRequires: text/gnu-sed
BuildRequires: database/postgres-93/library
BuildRequires: database/postgres-93/developer
BuildRequires: developer/lexer/re2c

Requires: database/postgres-93/library
Requires: web/php-55 >= %{version}

%description
The SFEphp55-pgsql93 package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL-9.3 database
support to PHP. PostgreSQL-9.3 is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL-9.3, you should install this package in addition to the main
php package.

%prep
%setup -c -n %name-%version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="-m64 -xO4 -xchip=pentium -xregs=no%frameptr -mt"
export CPPFLAGS="-m64 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
export LDFLAGS="-L/usr/postgres/9.3/lib/`isainfo -k` -L/lib/`isainfo -k` -L/usr/lib/`isainfo -k` -R/lib/`isainfo -k` -R/usr/lib/`isainfo -k`"
export CC=cc

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

pushd ext/pgsql/
/usr/php/5.5/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir}/`isainfo -k` \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --with-php-config=/usr/php/5.5/bin/php-config \
 --with-pgsql=/usr/postgres/9.3/bin/amd64
gmake -j$CPUS
popd

pushd ext/pdo_pgsql/
/usr/php/5.5/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --with-php-config=/usr/php/5.5/bin/php-config \
 --with-pdo-pgsql=/usr/postgres/9.3/bin/amd64
gmake -j$CPUS
popd


%install

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/etc/php/5.5/conf.d

for mod in pgsql pdo_pgsql; do
 pushd ext/${mod}/
 make install INSTALL_ROOT=$RPM_BUILD_ROOT \
     PECL_EXTENSION_DIR=%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20100525/ \
     PECL_INCLUDE_DIR=%{_prefix}/php/5.5/include
 popd
 cat > $RPM_BUILD_ROOT/etc/php/5.5/conf.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
done

#mkdir -p $RPM_BUILD_ROOT/%{_prefix}/php/5.5/modules/
#mkdir -p  $RPM_BUILD_ROOT/etc/php/5.5/conf.d

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/pgsql.so
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/pdo_pgsql.so
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/php/5.5/conf.d/*

%changelog
* Sat Jun 20 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.26
* Tue Mar 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.22
* Tue Oct 28 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.18
* Mon Jul 07 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.14
* Mon Mar 10 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.10
* Fri Jan 17 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.8
- build 64bit binary instead of 32bit binary
* Thu Jan 16 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
