%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug/php
%define tarball_name     php
%define tarball_version  7.2.13
%define major_version    7.2
%define prefix_name      SFEphp72jposug
%define _basedir         %{_prefix}/%{major_version}
%define zts              20160731

%define oracle_solaris_11_2 %(egrep 'Oracle Solaris (11.[23]|12.0)' /etc/release > /dev/null ; if [ $? -eq 0 ]; then echo '1'; else echo '0'; fi)

%define gcc_version %(pkg mediator -H gcc | awk '{print $3}')

Name:                    %{prefix_name}
IPS_package_name:        web/php-72jposug
Summary:                 php
Version:                 %{tarball_version}
License:                 PHP
Url:                     http://php.net/
Source:                  http://jp2.php.net/distributions/%{tarball_name}-%{tarball_version}.tar.xz
Source1:                 php-fpm72jposug.xml
Distribution:            OpenSolaris
Vendor:                  OpenSolaris Community
SUNW_Copyright:          %{prefix_name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:  library/spell-checking/enchant
#BuildRequires:  text/nkf
#%if %{oracle_solaris_11_2}
BuildRequires: library/libedit
#%else
#BuildRequires: SFEeditline
#%endif
BuildRequires: developer/icu
BuildRequires: developer/gcc-%{gcc_version}

Requires:       system/management/snmp/net-snmp >= 5.4.1
# Requires:       system/library/security/libmcrypt
Requires:       text/tidy
Requires:       library/libtool/libltdl
Requires:       web/php-common
#%if %{oracle_solaris_11_2}
Requires:       library/libedit
#%else
#Requires:       SFEeditline
#%endif
Requires:       library/icu
Requires:       system/library/gcc/gcc-runtime

%description
PHP


%prep
%setup -n %{tarball_name}-%{tarball_version}

# fix opcache build problem with SolarisStudio
# see https://bugs.php.net/bug.php?id=65207
#for i in ext/opcache/Optimizer/zend_optimizer{.c,.h,_internal.h}
# looks like this is no longer necessary 2018-12-22
#do
#nkf -Lu --overwrite=.bak ${i}
#done

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
export CFLAGS="-std=gnu99 -m64 -O2"
export CPPFLAGS="-std=gnu99 -m64 -O2 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
export LDFLAGS="-L/lib/%{_arch64} -L/usr/lib/%{_arch64} -R/lib/%{_arch64} -R/usr/lib/%{_arch64} -R%{_basedir}/lib/extensions/no-debug-non-zts-%{zts}"


CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

build() {
    # bison-1.875-2 seems to produce a broken parser; workaround.
    # mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
    ln -sf ../configure
CC=${CC} CXX=${CXX} ./configure --prefix=%{_prefix} \
    --bindir=%{_basedir}/bin \
    --datadir=%{_basedir}/share \
    --exec-prefix=%{_basedir} \
    --includedir=%{_basedir}/include \
    --libdir=%{_basedir}/lib \
    --libexecdir=%{_basedir}/modules \
    --mandir=%{_basedir}/man \
    --oldincludedir=%{_basedir}/share \
    --prefix=%{_basedir} \
    --sbindir=%{_basedir}/sbin \
    --sysconfdir=/etc/php/%{major_version}jposug \
    --with-config-file-path=/etc/php/%{major_version}jposug \
    --with-config-file-scan-dir=/etc/php/%{major_version}jposug/conf.d \
    --with-pear=/var/php/%{major_version}jposug/pear \
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
build \
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
    --with-sqlite3=shared \
    --enable-mysqlnd=shared \
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
    --disable-pdo \
    ${without_shared}
popd

# Build for inclusion as embedded script language into applications,
pushd build-embedded
build --enable-embed \
    --disable-pdo \
    ${without_shared}
popd

# # Build a special thread-safe (mainly for modules)
# pushd build-ztscli

# EXTENSION_DIR=%{_libdir}/php-zts/modules
# build \
#     --includedir=%{_basedir}/include/php-zts \
#     --libdir=%{_basedir}/lib/php-zts \
#     --enable-maintainer-zts \
#     --with-config-file-scan-dir=%{_sysconfdir}/php/%{major_version}/php-zts.d \
#     --enable-pcntl \
#     --enable-mbstring=shared \
#     --enable-mbregex \
#     --with-gd=shared \
#     --enable-bcmath=shared \
#     --enable-dba=shared --with-db4=%{_prefix} \
#     --with-xmlrpc=shared \
#     --enable-dom=shared \
#     --enable-wddx=shared \
#     --with-snmp=shared \
#     --enable-soap=shared \
#     --with-xsl=shared \
#     --enable-xmlreader=shared --enable-xmlwriter=shared \
#     --with-curl=shared \
#     --enable-mysqlnd=shared \
#     --with-mysqli=shared,mysqlnd \
#     --enable-pdo=shared \
#     --with-pdo-mysql=shared,mysqlnd \
#     --with-pdo-sqlite=shared \
#     --with-sqlite3=shared \
#     --enable-json=shared \
#     --enable-zip=shared \
#     --without-readline \
#     --with-libedit \
#     --enable-phar=shared \
#     --with-tidy=shared \
#     --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
#     --enable-posix=shared \
#     --enable-fileinfo=shared \
#     --with-enchant=shared
# popd

# Build a special thread-safe Apache SAPI
# pushd build-zts
# build --with-apxs2=/usr/apache2/2.4/bin/apxs \
#     --includedir=%{_basedir}/include/php-zts \
#     --libdir=%{_basedir}/lib/php-zts \
#     --enable-maintainer-zts \
#     --with-config-file-scan-dir=%{_sysconfdir}/php/%{major_version}/php-zts.d \
#     --enable-pdo=shared \
#     --with-pdo-sqlite=shared \
#     --with-sqlite3=shared \
#     ${without_shared}
# popd

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# # Install the extensions for the ZTS version
# make -C build-ztscli install \
#     INSTALL_ROOT=$RPM_BUILD_ROOT

# # Install the extensions for the ZTS version modules for libmysql
# make -C build-zts install-modules \
#     INSTALL_ROOT=$RPM_BUILD_ROOT

# # rename ZTS binary
# mv $RPM_BUILD_ROOT%{_basedir}/bin/php        $RPM_BUILD_ROOT%{_basedir}/bin/zts-php
# mv $RPM_BUILD_ROOT%{_basedir}/bin/phpize     $RPM_BUILD_ROOT%{_basedir}/bin/zts-phpize
# mv $RPM_BUILD_ROOT%{_basedir}/bin/php-config $RPM_BUILD_ROOT%{_basedir}/bin/zts-php-config

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
#install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
#install -m 644 php.gif $RPM_BUILD_ROOT%{contentdir}/icons/php.gif

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/php

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT/usr/apache2/2.4/libexec
install -m 755 build-apache/libs/libphp7.so $RPM_BUILD_ROOT/usr/apache2/2.4/libexec/mod_php%{major_version}jposug.so

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
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}jposug
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}jposug/conf.d
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}jposug/php.ini
install -m 644 php.ini-production $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}jposug/php.ini-production
install -m 644 php.ini-development $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}jposug/php.ini-development
# install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}jposug/conf.d/opcache.ini
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}jposug/zts-conf.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}jposug
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}jposug/include
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}jposug/modules
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}jposug/pear
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}jposug/sessions

# PHP-FPM stuff
# SMF manifest
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/network
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/var/svc/manifest/network/php-fpm72jposug.xml

# Log
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/php-fpm
# install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/php-fpm
# Config
# install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}/fpm-conf.d
# install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}/php-fpm.conf
# install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php/%{major_version}/fpm-conf.d/www.conf
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
cd $RPM_BUILD_ROOT%{_basedir}/bin
rm phar
ln -s phar.phar phar

mkdir $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../../opt/jposug/php/%{major_version}/bin/phar .
ln -s ../../opt/jposug/php/%{major_version}/bin/php .
ln -s ../../opt/jposug/php/%{major_version}/bin/php-config .
ln -s ../../opt/jposug/php/%{major_version}/bin/phpize .

rm -rf $RPM_BUILD_ROOT%{_prefix}/share/
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
    cat > $RPM_BUILD_ROOT/etc/php/%{major_version}jposug/conf.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%attr (0755, root, bin) %{_basedir}
%dir %attr (0755, root, sys) /etc
%dir %attr (0755, root, bin) /etc/php
%dir %attr (0755, root, bin) /etc/php/%{major_version}jposug
%attr (0644, root, bin) %config(noreplace) /etc/php/%{major_version}jposug/php.ini
%attr (0644, root, bin) %config(noreplace) /etc/php/%{major_version}jposug/php.ini-production
%attr (0644, root, bin) %config(noreplace) /etc/php/%{major_version}jposug/php.ini-development
%dir %attr (0755, root, bin) /etc/php/%{major_version}jposug/conf.d
%attr (0644, root, bin) %config(noreplace) /etc/php/%{major_version}jposug/conf.d/*.ini
%dir %attr (0755, root, bin) /etc/php/%{major_version}jposug/zts-conf.d
# %dir %attr (0755, root, bin) /etc/php/%{major_version}jposug/fpm-conf.d
%attr (0755, root, bin) %config(noreplace) /etc/php/%{major_version}jposug/php-fpm.conf.default
%dir %attr (0755, root, bin) /etc/php/%{major_version}jposug/php-fpm.d
%attr (0755, root, bin) %config(noreplace) /etc/php/%{major_version}jposug/php-fpm.d/www.conf.default
%attr (0755, root, bin) %config(noreplace) /etc/php/%{major_version}jposug/pear.conf
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version} mediator-implementation=jposug) /usr/bin/phar
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version} mediator-implementation=jposug) /usr/bin/php
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version} mediator-implementation=jposug) /usr/bin/php-config
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version} mediator-implementation=jposug) /usr/bin/phpize
%dir %attr (0755, root, sys)/var
%attr (0755, root, bin) /var/php/%{major_version}jposug/include
%attr (0755, root, bin) /var/php/%{major_version}jposug/modules
%attr (0755, root, bin) /var/php/%{major_version}jposug/pear
%attr (0750, webservd, bin) /var/php/%{major_version}jposug/sessions
%dir %attr (0755, root, sys) /var/log
%attr (0755, root, sys) /var/log/php-fpm
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/network
%class(manifest) %attr (0644, root, sys) /var/svc/manifest/network/*
# %dir %attr (0755, root, sys) /var/run
# %attr (0755, root, root) /var/run/php-fpm
%dir %attr (0755, root, bin) /usr/apache2
%dir %attr (0755, root, bin) /usr/apache2/2.4
%dir %attr (0755, root, bin) /usr/apache2/2.4/libexec
%attr (0444, root, bin) /usr/apache2/2.4/libexec/mod_php%{major_version}jposug.so

%changelog
* Sat Dec 22 2018 - me@tsundoku.ne.jp
- bump to 7.2.13
- remove nkf operaton - the files come with LF endings now
* Sun Oct 28 2018 - <me@tsundoku.ne.jp>
- bump to 7.2.11
* Sun Sep 30 2018 - <me@tsundoku.ne.jp>
- bump to 7.2.10
- fix some minor issues with /opt/jposug path
* Mon Jul 30 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.2.8
* Fri Jun 01 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.2.6
* Mon May 14 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.2.5
* Thu Mar 29 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.2.4
* Fri Mar 02 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.2.3
* Fri Dec 01 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
