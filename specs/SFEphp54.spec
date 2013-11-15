%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr/php
%define tarball_name     php
%define tarball_version  5.4.21
%define major_version	 5.4
%define prefix_name      SFEphp54
%define _basedir         %{_prefix}/%{major_version}

Name:                    %{prefix_name}
IPS_package_name:        web/php-54
Summary:	         php
Version:                 5.4.21
License:		 PHP
Url:                     http://php.net/
Source:                  http://jp1.php.net/distributions/php-%{version}.tar.bz2
Source1:                 php5.4.conf
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Copyright:          %{prefix_name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: library/spell-checking/enchant

%description
PHP


%prep
%setup -n %{tarball_name}-%{tarball_version}

%build
mkdir build-cgi build-apache build-embedded build-zts build-ztscli build-fpm

export CFLAGS="-m32 -xO4 -xchip=pentium -xregs=no%frameptr -mt"
export CPPFLAGS="-D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
build() {
    # bison-1.875-2 seems to produce a broken parser; workaround.
    # mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
    ln -sf ../configure
./configure --prefix=/usr \
    --bindir=/usr/php/5.4/bin \
    --datadir=/usr/php/5.4/share \
    --exec-prefix=/usr/php/5.4 \
    --includedir=/usr/php/5.4/include \
    --libdir=/usr/php/5.4/lib \
    --libexecdir=/usr/php/5.4/modules \
    --mandir=/usr/php/5.4/man \
    --oldincludedir=/usr/php/5.4/share \
    --prefix=/usr/php/5.4 \
    --sbindir=/usr/php/5.4/sbin \
    --sysconfdir=/etc/php/5.4 \
    --with-config-file-path=/etc/php/5.4 \
    --with-config-file-scan-dir=/etc/php/5.4/conf.d \
    --with-exec-dir=/usr/php/5.4/bin \
    --with-pear=/var/php/5.4/pear \
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
    --without-gdbm \
    --with-gettext \
    --with-iconv \
    --with-openssl \
    --with-zlib \
    --with-layout=PHP \
    --enable-exif \
    --enable-ftp \
    --enable-magic-quotes \
    --enable-sockets \
    --with-kerberos \
    --enable-ucd-snmp-hack \
    --enable-shmop \
    --enable-calendar \
    --enable-xml \
    --with-system-tzdata \
    --with-mhash \
    $*
    if test $? != 0; then
	tail -500 config.log
	: configure failed
	exit 1
    fi
    make -j$CPUS
}

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
    --enable-pdo=shared \
    --with-pdo-sqlite=shared \
    --with-sqlite3=shared \
    --enable-json=shared \
    --enable-zip=shared \
    --without-readline \
    --with-libedit \
    --enable-phar=shared \
    --with-mcrypt=shared \
    --with-tidy=shared \
    --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
    --enable-posix=shared \
    --enable-fileinfo=shared \
    --with-icu-dir= \
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
build --with-apxs2=/usr/apache2/2.2/bin/apxs \
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
    --includedir=/usr/php/5.4/include/php-zts \
    --libdir=/usr/php/5.4/lib/php-zts \
    --enable-maintainer-zts \
    --with-config-file-scan-dir=%{_sysconfdir}/php/5.4/php-zts.d \
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
    --enable-pdo=shared \
    --with-pdo-mysql=shared \
    --with-pdo-sqlite=shared \
    --with-sqlite3=shared \
    --enable-json=shared \
    --enable-zip=shared \
    --without-readline \
    --with-libedit \
    --enable-phar=shared \
    --with-mcrypt=shared \
    --with-tidy=shared \
    --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
    --enable-posix=shared \
    --enable-fileinfo=shared \
    --with-icu-dir=%{_prefix} \
    --with-enchant=shared
popd

# Build a special thread-safe Apache SAPI
pushd build-zts
build --with-apxs2=/usr/apache2/2.2/bin/apxs \
    --includedir=/usr/php/5.4/include/php-zts \
    --libdir=/usr/php/5.4/lib/php-zts \
    --enable-maintainer-zts \
    --with-config-file-scan-dir=%{_sysconfdir}/php/5.4/php-zts.d \
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
mv $RPM_BUILD_ROOT/usr/php/5.4/bin/php        $RPM_BUILD_ROOT/usr/php/5.4/bin/zts-php
mv $RPM_BUILD_ROOT/usr/php/5.4/bin/phpize     $RPM_BUILD_ROOT/usr/php/5.4/bin/zts-phpize
mv $RPM_BUILD_ROOT/usr/php/5.4/bin/php-config $RPM_BUILD_ROOT/usr/php/5.4/bin/zts-php-config

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
install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
install -m 644 php.gif $RPM_BUILD_ROOT%{contentdir}/icons/php.gif

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/php

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT/usr/apache2/2.2/libexec
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT/usr/apache2/2.2/libexec/mod_php5.4.so

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
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/5.4
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/5.4/conf.d
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/5.4/zts-conf.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/5.4
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/5.4/include
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/5.4/modules
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/5.4/pear
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/php/5.4/sessions

# PHP-FPM stuff
# Log
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/php-fpm
# install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/php-fpm
# Config
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php/5.4/fpm-conf.d
# install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php/5.4/php-fpm.conf
# install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php/5.4/fpm-conf.d/www.conf
# mv $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf.default .
# tmpfiles.d
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/tmpfiles.d
# install -m 644 php-fpm.tmpfiles $RPM_BUILD_ROOT%{_sysconfdir}/tmpfiles.d/php-fpm.conf
# install systemd unit files and scripts for handling server startup
install -m 755 -d $RPM_BUILD_ROOT%{_unitdir}
# install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/
# LogRotate
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
# install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/php-fpm
# Environment file
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
# install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/php-fpm
# Fix the link
cd $RPM_BUILD_ROOT/usr/php/5.4/bin
rm phar
ln -s phar.phar phar

mkdir $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../php/5.4/bin/phar .
ln -s ../php/5.4/bin/php .
ln -s ../php/5.4/bin/php-config .
ln -s ../php/5.4/bin/phpize .

mkdir $RPM_BUILD_ROOT/usr/sbin
cd $RPM_BUILD_ROOT/usr/sbin
ln -s ../php/5.4/sbin/php-fpm .

mkdir -p $RPM_BUILD_ROOT/etc/apache2/2.2/conf.d/php
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/etc/apache2/2.2/conf.d/php/php5.4.conf
cd $RPM_BUILD_ROOT/etc/apache2/2.2/conf.d/php
ln -s php5.4.conf php.conf


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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, sys) /etc
%dir %attr (0755, root, bin) /etc/php
%attr (0755, root, bin) /etc/php/5.4
%dir %attr (0755, root, bin) /etc/apache2
%dir %attr (0755, root, bin) /etc/apache2/2.2
%dir %attr (0755, root, bin) /etc/apache2/2.2/conf.d
%dir %attr (0755, root, bin) /etc/apache2/2.2/conf.d/php
%attr (0644, root, bin) /etc/apache2/2.2/conf.d/php/php5.4.conf
%attr (0755, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /etc/apache2/2.2/conf.d/php/php.conf
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/phar
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php-config
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/phpize
%dir %attr (0755, root, bin) /usr/sbin
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/sbin/php-fpm
%dir %attr (0755, root, sys)/var
%attr (0755, root, bin) /var/php/5.4/include
%attr (0755, root, bin) /var/php/5.4/modules
%attr (0755, root, bin) /var/php/5.4/pear
%attr (0750, webservd, bin) /var/php/5.4/sessions
%dir %attr (0755, root, sys) /var/log
%attr (0755, root, sys) /var/log/php-fpm
# %dir %attr (0755, root, sys) /var/run
# %attr (0755, root, root) /var/run/php-fpm
%dir %attr (0755, root, bin) /usr/apache2
%dir %attr (0755, root, bin) /usr/apache2/2.2
%dir %attr (0755, root, bin) /usr/apache2/2.2/libexec
%attr (0444, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/apache2/2.2/libexec/mod_php5.4.so

%changelog
* Fri Nov 15 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.4.21
* Tue Sep 24 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.4.20
* Fri Aug 09 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Mon Jul 29 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add php5.4.conf for Apache
* Sun Jul 28 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add symbolic link for php-fpm
- add %ips_tag to mod_php5.4.so
* Sat Jul 27 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
