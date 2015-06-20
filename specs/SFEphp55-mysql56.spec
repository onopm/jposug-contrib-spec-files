#
# spec file for package SFEphp55-mysql56
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

Name:                    SFEphp55-mysql56
IPS_package_name:	 web/php-55/extension/php-mysql56
Summary:                 PHP 5.5 module for MySQL 5.6
Version:                 %{tarball_version}
License:		 PHP License
Url:                     http://www.php.net/
Source:		 http://jp.php.net/distributions/%{tarball_name}-%{tarball_version}.tar.bz2
Distribution:            OpenSolaris
Vendor:		 OpenSolaris Community
SUNW_Basedir:            /
#SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-55
BuildRequires: text/gnu-sed
BuildRequires: database/mysql-56
BuildRequires: database/mysql-56/library
BuildRequires: database/mysql-56/devel
BuildRequires: developer/lexer/re2c

Requires: database/mysql-56/library >= 5.6.0
Requires: web/php-55 = %{version}

%description
PHP 5.5 module for MySQL 5.6

%prep
%setup -c -n %name-%version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS="-m64 -xO4 -xchip=generic -xregs=no%frameptr -mt"
export LDFLAGS="-L/usr/mysql/5.6/lib/`isainfo -k`/mysql -L/lib/`isainfo -k` -L/usr/lib/`isainfo -k` -R/usr/mysql/5.6/lib/`isainfo -k`/mysql -R/lib/`isainfo -k` -R/usr/lib/`isainfo -k`"
export CC=cc

pwd
cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

pushd ext/mysql
/usr/php/5.5/bin/phpize
./configure \
 --prefix=%{_prefix} \
 --exec-prefix=%{_prefix} \
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --with-php-config=/usr/php/5.5/bin/php-config \
 --with-mysql=/usr/mysql/5.6 \
 --with-zlib-dir=/usr/lib/%{_arch64}
gmake -j$CPUS
# gmake test
popd

mkdir -p ext/mysqli/ext/mysqlnd
cp ext/mysqlnd/mysql_float_to_double.h ext/mysqli/ext/mysqlnd

pushd ext/mysqli
/usr/php/5.5/bin/phpize
./configure \
 --prefix=%{_prefix} \
 --exec-prefix=%{_prefix} \
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --with-php-config=/usr/php/5.5/bin/php-config \
 --with-mysqli=/usr/mysql/5.6/bin/mysql_config
gmake -j$CPUS
# gmake test
popd

pushd ext/pdo_mysql
/usr/php/5.5/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --with-php-config=/usr/php/5.5/bin/php-config \
 --with-pdo-mysql=/usr/mysql/5.6
gmake -j$CPUS
# gmake test
popd


%install

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/etc/php/5.5/conf.d

for mod in mysql mysqli pdo_mysql; do
 pushd ext/${mod}/
 make install INSTALL_ROOT=$RPM_BUILD_ROOT \
     PECL_EXTENSION_DIR=%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/ \
     PECL_INCLUDE_DIR=%{_prefix}/php/5.5/include
 popd
 cat > $RPM_BUILD_ROOT/etc/php/5.5/conf.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
done

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/mysql.so
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/mysqli.so
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/pdo_mysql.so
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/include
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/include/php
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/include/php/ext
%attr(0755, root, bin) %{_prefix}/php/%{php_version}/include/php/ext/mysqli
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/php/5.5/conf.d/*

%changelog
* Sat Jun 20 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.26
* Wed Mar 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.22
* Tue Oct 28 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.18
* Mon Mar 10 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.10
* Mon Feb 17 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.5.9
* Tue Jan 28 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify LDFLAGS
* Fri Jan 17 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
