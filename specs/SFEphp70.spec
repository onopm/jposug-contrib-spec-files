%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr/php
%define tarball_name     php
%define tarball_version  7.0.30
%define major_version	 7.0
%define prefix_name      SFEphp70
%define _basedir         %{_prefix}/%{major_version}

%define oracle_solaris_11_2 %(egrep 'Oracle Solaris (11.[23]|12.0)' /etc/release > /dev/null ; if [ $? -eq 0 ]; then echo '1'; else echo '0'; fi)

Name:                    %{prefix_name}
IPS_package_name:        web/php-70
Summary:	         php
Version:                 %{tarball_version}
License:		 PHP
Url:                     http://php.net/
Source:                  http://jp2.php.net/distributions/php-%{version}.tar.bz2
Source1:                 php-fpm70.xml
Source2:                 php70-opcache.ini
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Copyright:          %{prefix_name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:  library/spell-checking/enchant
BuildRequires:  text/nkf
%if %{oracle_solaris_11_2}
BuildRequires: library/libedit
%else
BuildRequires: SFEeditline
%endif
BuildRequires: developer/icu

Requires:       system/management/snmp/net-snmp >= 5.4.1
Requires:       text/tidy
Requires:       library/libtool/libltdl
Requires:       web/php-common
%if %{oracle_solaris_11_2}
Requires:       library/libedit
%else
Requires:       SFEeditline
%endif
Requires:       library/icu


%description
PHP


%prep
%setup -n %{tarball_name}-%{tarball_version}

# fix opcache build problem with SolarisStudio
# see https://bugs.php.net/bug.php?id=65207
for i in ext/opcache/Optimizer/zend_optimizer{.c,.h,_internal.h}
do
nkf -Lu --overwrite=.bak ${i}
done

echo "
#if defined(__sun) && defined(__SVR4) //Solaris
#include <ieeefp.h>
#define isfinite finite
#endif" >>  main/php_config.h.in

%build
mkdir build-cgi build-apache build-embedded build-zts build-ztscli build-fpm
# use GCC To avoid error with Solaris Studio,
export CC=/usr/bin/gcc
export CXX=/usr/bin/g++
# export CFLAGS="-m64 -xO4 -xchip=pentium -xregs=no%frameptr -mt"
# export CPPFLAGS="-m64 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
export CFLAGS="-std=gnu99 -m64 -O2"
export CPPFLAGS="-std=gnu99 -m64 -O2 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
export LDFLAGS="-L/lib/`isainfo -k` -L/usr/lib/`isainfo -k` -R/lib/`isainfo -k` -R/usr/lib/`isainfo -k`"

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
build() {
    # bison-1.875-2 seems to produce a broken parser; workaround.
    # mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
    ln -sf ../configure
CC=${CC} CXX=${CXX} ./configure --prefix=/usr \
    --bindir=/usr/php/7.0/bin \
    --datadir=/usr/php/7.0/share \
    --exec-prefix=/usr/php/7.0 \
    --includedir=/usr/php/7.0/include \
    --libdir=/usr/php/7.0/lib \
    --libexecdir=/usr/php/7.0/modules \
    --mandir=/usr/php/7.0/man \
    --oldincludedir=/usr/php/7.0/share \
    --prefix=/usr/php/7.0 \
    --sbindir=/usr/php/7.0/sbin \
    --sysconfdir=/etc/php/7.0 \
    --with-config-file-path=/etc/php/7.0 \
    --with-config-file-scan-dir=/etc/php/7.0/conf.d \
    --with-pear=/var/php/7.0/pear \
    --cache-file=../config.cache \
    --disable-debug \
    --disable-libgcc \
    --disable-dmalloc \
    --disable-inline-optimization \
    --disable-libtool-lock \
    --disable-static \
    --with-pic \
    --disable-rpath \
    --with-bz2 \
    --enable-gd-native-ttf \
    --with-jpeg-dir=/usr/lib \
    --with-png-dir=/usr/lib \
    --without-gdbm \
    --with-gettext \
    --with-iconv \
    --with-openssl \
    --with-zlib \
    --with-layout=PHP \
    --enable-exif \
    --enable-ftp \
    --with-kerberos \
    --enable-shmop \
    --enable-calendar \
    --enable-xml \
    --with-mhash \
    --enable-opcache=yes \
    --enable-dtrace \
    --disable-intl \
    $*
    if test $? != 0; then
	tail -500 config.log
	: configure failed
	exit 1
    fi

    if [ ${CC} = '/usr/bin/gcc' ]
    then
	mv Makefile Makefile.bak
	sed -e 's/ \-mt / /' < Makefile.bak > Makefile
    fi
    make -j$CPUS
}

# php fails to build on Solaris with --enable-sockets
# https://bugs.php.net/bug.php?id=65427
#     --enable-sockets \


# Build /usr/bin/php-cgi with the CGI SAPI, and all the shared extensions
pushd build-cgi
build --enable-force-cgi-redirect \
    --enable-pcntl \
    --enable-mbstring=shared \
    --enable-mbregex \
    --with-gd=shared \
    --enable-bcmath=shared \
    --enable-dba=shared --with-db4=%{_prefix} \
    --with-xmlrpc=shared \
    --enable-dom=shared \
    --enable-wddx=shared \
    --with-snmp=shared \
    --enable-soap=shared \
    --with-xsl=shared \
    --enable-xmlreader=shared --enable-xmlwriter=shared \
    --with-curl=shared \
    --enable-fastcgi \
    --with-sqlite3=shared \
    --enable-mysqlnd=shared \
    --with-mysqli=shared,mysqlnd \
    --enable-pdo=shared \
    --with-pdo-mysql=shared,mysqlnd \
    --with-pdo-sqlite=shared \
    --enable-json=shared \
    --enable-zip=shared \
    --without-readline \
    --with-libedit \
    --enable-phar=shared \
    --disable-mcrypt \
    --with-tidy=shared \
    --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
    --enable-posix=shared \
    --enable-fileinfo=shared \
    --with-enchant=shared
popd

without_shared="--without-gd \
    --disable-dom --disable-dba --without-unixODBC \
    --disable-xmlreader --disable-xmlwriter \
    --disable-phar --disable-fileinfo \
    --disable-json --without-pspell --disable-wddx \
    --without-curl --disable-posix \
    --disable-sysvmsg --disable-sysvshm --disable-sysvsem"

# Build Apache module, and the CLI SAPI, /usr/bin/php
pushd build-apache
build --with-apxs2=/usr/apache2/2.4/bin/apxs \
    --enable-pdo=shared \
    --with-pdo-sqlite=shared,%{_prefix} \
    ${without_shared}
popd

# Build php-fpm
pushd build-fpm
build --enable-fpm \
    --without-mysql --disable-pdo \
    ${without_shared}
popd

# Build for inclusion as embedded script language into applications,
# /usr/lib[64]/libphp5.so
pushd build-embedded
build --enable-embed \
    --without-mysql --disable-pdo \
    ${without_shared}
popd

# Build a special thread-safe (mainly for modules)
pushd build-ztscli

EXTENSION_DIR=%{_libdir}/php-zts/modules
build --enable-force-cgi-redirect \
    --includedir=/usr/php/7.0/include/php-zts \
    --libdir=/usr/php/7.0/lib/php-zts \
    --enable-maintainer-zts \
    --with-config-file-scan-dir=%{_sysconfdir}/php/7.0/php-zts.d \
    --enable-pcntl \
    --enable-mbstring=shared \
    --enable-mbregex \
    --with-gd=shared \
    --enable-bcmath=shared \
    --enable-dba=shared --with-db4=%{_prefix} \
    --with-xmlrpc=shared \
    --enable-dom=shared \
    --enable-wddx=shared \
    --with-snmp=shared \
    --enable-soap=shared \
    --with-xsl=shared \
    --enable-xmlreader=shared --enable-xmlwriter=shared \
    --with-curl=shared \
    --enable-fastcgi \
    --enable-mysqlnd=shared \
    --enable-mysqlnd-threading \
    --with-mysqli=shared,mysqlnd \
    --enable-pdo=shared \
    --with-pdo-mysql=shared,mysqlnd \
    --with-pdo-sqlite=shared \
    --with-sqlite3=shared \
    --enable-json=shared \
    --enable-zip=shared \
    --without-readline \
    --with-libedit \
    --enable-phar=shared \
    --disable-mcrypt \
    --with-tidy=shared \
    --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
    --enable-posix=shared \
    --enable-fileinfo=shared \
    --with-enchant=shared
popd

# Build a special thread-safe Apache SAPI
pushd build-zts
build --with-apxs2=/usr/apache2/2.4/bin/apxs \
    --includedir=/usr/php/7.0/include/php-zts \
    --libdir=/usr/php/7.0/lib/php-zts \
    --enable-maintainer-zts \
    --with-config-file-scan-dir=%{_sysconfdir}/php/7.0/php-zts.d \
    --enable-pdo=shared \
    --with-pdo-sqlite=shared \
    --with-sqlite3=shared \
    ${without_shared}
popd

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Install the extensions for the ZTS version
make -C build-ztscli install \
    INSTALL_ROOT=$RPM_BUILD_ROOT

# Install the extensions for the ZTS version modules for libmysql
make -C build-zts install-modules \
    INSTALL_ROOT=$RPM_BUILD_ROOT

# rename ZTS binary
mv $RPM_BUILD_ROOT/usr/php/7.0/bin/php        $RPM_BUILD_ROOT/usr/php/7.0/bin/zts-php
mv $RPM_BUILD_ROOT/usr/php/7.0/bin/phpize     $RPM_BUILD_ROOT/usr/php/7.0/bin/zts-phpize
mv $RPM_BUILD_ROOT/usr/php/7.0/bin/php-config $RPM_BUILD_ROOT/usr/php/7.0/bin/zts-php-config

# Install the version for embedded script language in applications + php_embed.h
make -C build-embedded install-sapi install-headers \
    INSTALL_ROOT=$RPM_BUILD_ROOT

# Install the php-fpm binary
make -C build-fpm install-fpm \
    INSTALL_ROOT=$RPM_BUILD_ROOT

# Install everything from the CGI SAPI build
make -C build-cgi install \
    INSTALL_ROOT=$RPM_BUILD_ROOT


# Install the mysql extension build with libmysql
make -C build-apache install-modules \
    INSTALL_ROOT=$RPM_BUILD_ROOT

# Install the default configuration file and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
# install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
#install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
#install -m 644 php.gif $RPM_BUILD_ROOT%{contentdir}/icons/php.gif

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/php

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT/usr/apache2/2.4/libexec
install -m 755 build-apache/libs/libphp7.so $RPM_BUILD_ROOT/usr/apache2/2.4/libexec/mod_php7.0.so

# install the ZTS DSO
# install -m 755 build-zts/libs/libphp5.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules/libphp5-zts.so

# Apache config fragment
%if "%{_httpd_modconfdir}" == "%{_httpd_confdir}"
# Single config file with httpd < 2.4
# install -D -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_httpd_confdir}/php.conf
# cat %{SOURCE1} >>$RPM_BUILD_ROOT%{_httpd_confdir}/php.conf
%else
# Dual config file with httpd >= 2.4
# install -D -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-php.conf
# install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}/php.conf
%endif

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/conf.d
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/php.ini
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/php.ini-production
install -m 644 php.ini-development $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/php.ini-development
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/conf.d/opcache.ini
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/zts-conf.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/7.0
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/7.0/include
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/7.0/modules
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/7.0/pear
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/php/7.0/sessions

# PHP-FPM stuff
# SMF manifest
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/var/svc/manifest/php-fpm70.xml

# Log
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/php-fpm
# install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/php-fpm
# Config
# install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/fpm-conf.d
# install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/php-fpm.conf
# install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php/7.0/fpm-conf.d/www.conf
# mv $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf.default .
# tmpfiles.d
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/tmpfiles.d
# install -m 644 php-fpm.tmpfiles $RPM_BUILD_ROOT%{_sysconfdir}/tmpfiles.d/php-fpm.conf
# install systemd unit files and scripts for handling server startup
# install -m 755 -d $RPM_BUILD_ROOT%{_unitdir}
# install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/
# LogRotate
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
# install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/php-fpm
# Environment file
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
# install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/php-fpm
# Fix the link
cd $RPM_BUILD_ROOT/usr/php/7.0/bin
rm phar
ln -s phar.phar phar

mkdir $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../php/7.0/bin/phar .
ln -s ../php/7.0/bin/php .
ln -s ../php/7.0/bin/php-config .
ln -s ../php/7.0/bin/phpize .

rm -rf $RPM_BUILD_ROOT/usr/php/share/
rm -rf $RPM_BUILD_ROOT/etc/logrotate.d
rm -rf $RPM_BUILD_ROOT/etc/tmpfiles.d
rm -rf $RPM_BUILD_ROOT/etc/sysconfig

rm -rf $RPM_BUILD_ROOT/.filemap
rm -rf $RPM_BUILD_ROOT/.channels
rm -rf $RPM_BUILD_ROOT/.lock
rm -rf $RPM_BUILD_ROOT/.depdb
rm -rf $RPM_BUILD_ROOT/.depdblock
rm -rf $RPM_BUILD_ROOT/.registry

# ini file for extension
for mod in mysqlnd  mysqli pdo_mysql
do
    cat > $RPM_BUILD_ROOT/etc/php/7.0/conf.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, sys) /etc
%dir %attr (0755, root, bin) /etc/php
%dir %attr (0755, root, bin) /etc/php/7.0
%attr (0644, root, bin) %config(noreplace) /etc/php/7.0/php.ini
%attr (0644, root, bin) %config(noreplace) /etc/php/7.0/php.ini-production
%attr (0644, root, bin) %config(noreplace) /etc/php/7.0/php.ini-development
%dir %attr (0755, root, bin) /etc/php/7.0/conf.d
%attr (0755, root, bin) %config(noreplace) /etc/php/7.0/conf.d/*.ini
%dir %attr (0755, root, bin) /etc/php/7.0/zts-conf.d
# %dir %attr (0755, root, bin) /etc/php/7.0/fpm-conf.d
%attr (0755, root, bin) %config(noreplace) /etc/php/7.0/php-fpm.conf.default
%dir %attr (0755, root, bin) /etc/php/7.0/php-fpm.d
%attr (0755, root, bin) %config(noreplace) /etc/php/7.0/php-fpm.d/www.conf.default
%attr (0755, root, bin) %config(noreplace) /etc/php/7.0/pear.conf
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/phar
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php-config
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/phpize
%dir %attr (0755, root, sys)/var
%attr (0755, root, bin) /var/php/7.0/include
%attr (0755, root, bin) /var/php/7.0/modules
%attr (0755, root, bin) /var/php/7.0/pear
%attr (0750, webservd, bin) /var/php/7.0/sessions
%dir %attr (0755, root, sys) /var/log
%attr (0755, root, sys) /var/log/php-fpm
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%attr (0644, root, sys) /var/svc/manifest/php-fpm70.xml
# %dir %attr (0755, root, sys) /var/run
# %attr (0755, root, root) /var/run/php-fpm
%dir %attr (0755, root, bin) /usr/apache2
%dir %attr (0755, root, bin) /usr/apache2/2.4
%dir %attr (0755, root, bin) /usr/apache2/2.4/libexec
%attr (0444, root, bin) /usr/apache2/2.4/libexec/mod_php7.0.so

%changelog
* Mon May 14 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.30
* Fri Mar 02 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.28
* Wed Nov 29 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.26 and disable intl
- add isfinite definition to main/php_config.h.in to build intl
* Mon Feb 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.16
* Thu Jan 26 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.15
* Mon Dec 12 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.14
* Fri Oct 28 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use mysqlng instead of libmysqlclient
* Thu Oct 20 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.12
* Fri Sep 30 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.11
* Fri Jul 22 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.9
* Fri Jun 24 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.8
* Wed Jun 01 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.7 and disable mcrypt
* Mon Mar 07 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.4 and use apache-24
* Fri Jan 08 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.2
* Sat Dec 19 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.0.1
* Sun Dec 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
