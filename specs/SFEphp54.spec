#
# spec file for package SFEphp-54
#
%include Solaris.inc
%include packagenamemacros.inc
# You can also compile on SunStudio.
%define cc_is_gcc 1
%include base.inc
#
%define with_imap 1
%define with_pgsql 1
%define with_unixodbc 0
%define with_pspell 0
%define with_recode 0
%if %( expr %{osbuild} '=' 175 )
# Solaris
%define with_mediator_in_directory_usr_php_bin 0
%else
# OI
%define with_mediator_in_directory_usr_php_bin 1
%endif
# if this option is 0, all mysql modules will not build
%define with_mysql 1
%define with_embed 1
%define build_cgi 1
%define build_apache 1
%define build_zts 0
%define build_rpm_macros 0
%define skip_prep 0
%define skip_build 0
%define skip_check 1
#
%define major_version 5.4
#
%define usr_prefix /usr
%define usr_bindir %{usr_prefix}/bin
%define usr_libdir %{usr_prefix}/lib
%define usr_sharedir %{usr_prefix}/share
%define _prefix /usr/php/%{major_version}
%define _sysconfdir /etc/php/%{major_version}
%define _bindir %{_prefix}/bin
%define _libdir %{_prefix}/lib
%define _mandir %{_prefix}/man
#
%define _root_sysconfdir  %{_sysconfdir}
%define _root_bindir      %{_bindir}
%define _root_sbindir     %{_sbindir}
%define _root_includedir  %{_includedir}
%define _root_libdir      %{_libdir}
%define _root_prefix      %{_prefix}
#TODO:
%define _root_initddir    /etc/init.d
%define svcdir /var/svc/manifest/site

# thing to see
# MySQL : system or scl one, or only mysqlnd*
# Http  : system* 2.2 of scl one (2.4 ??)
# readline or libedit (not available for el5)
# * for current 

# API/ABI check
%define apiver      20100412
%define zendver     20100525
%define pdover      20080721
# Extension version
%define fileinfover 1.0.5
%define pharver     2.0.1
%define zipver      1.11.0
%define jsonver     1.2.1

# Adds -z now to the linker flags
%define _hardened_build 1

# version used for php embedded library soname
%define embed_version 5.4

# Ugly hack. Harcoded values to avoid relocation.
#%define _httpd_mmn         %(cat %{_root_includedir}/httpd/.mmn 2>/dev/null || echo missing-httpd-devel)
%define httpd_mmn %(grep '#define MODULE_MAGIC_NUMBER_MAJOR' /usr/apache2/2.2/include/ap_mmn.h | awk '{print $3}' || echo missing-httpd-devel)
%define _httpd_confdir     %(apxs -q sysconfdir 2>/dev/null)/conf.d
%define _httpd_moddir      %(apxs -q libexecdir 2>/dev/null)
%define _root_httpd_moddir %{_prefix}%(apxs -q libexecdir 2>/dev/null | sed -e 's|/[^/]*||')
# httpd 2.2 values
%define _httpd_apxs        /bin/apxs
%define _httpd_modconfdir  %(apxs -q sysconfdir 2>/dev/null)/conf.d
%define _httpd_contentdir  %(apxs -q datadir 2>/dev/null)/

%if %{with_mysql}
%define mysql_sock %(mysql_config --socket  2>/dev/null || echo /tmp/mysql.sock)
%endif

# Regression tests take a long time, you can skip 'em with this
%{!?runselftest: %{expand: %%define runselftest 1}}

# Use the arch-specific mysql_config binary to avoid mismatch with the
# arch detection heuristic used by bindir/mysql_config.
%if %{with_mysql}
%define mysql_config /usr/mysql/5.1/bin/mysql_config
%define mysql_prefix %(/usr/mysql/5.1/bin/mysql_config --include | sed -e 's/\-I//')/../..
%endif

#FastCGI Process Manager (FPM) 
%define with_fpm       1

# Build mysql/mysqli/pdo extensions using libmysqlclient or only mysqlnd
%define with_libmysql  1

# Build ZTS extension or only NTS
%define with_zts       0
#
%define with_interbase 0
%define with_mcrypt    1
%define with_mssql     0
#
%define with_tidy      1
#
%define with_sqlite3   1
%define with_pdo_sqlite3 1
%define with_libedit   1
%define with_enchant   1
%define with_recode    0
%define with_t1lib     0
#
%define with_pcre      1
#
#%if 0%{?__isa_bits:1}
#%define isasuffix -%{__isa_bits}
#%else
%define isasuffix %nil
#%endif
#
%define with_systemd 0
#
%define with_libzip  0
#
%define with_zip     1
%define zipmod       zip
#
%define db_devel  db4-devel
#%define db_devel  libdb-devel

Summary:  PHP scripting language for creating dynamic web sites
Name:     SFEphp54
%define pkg_name          %{name}
%define _pkg_docdir %{usr_prefix}/share/doc/SFEphp54
SUNW_Copyright:   %name.copyright
IPS_package_name:        web/php-54
Version:  5.4.29
%define src_name php-%{version}
# All files licensed under PHP version 3.01, except
# Zend is licensed under Zend
# TSRM is licensed under BSD
License:  PHP and Zend and BSD
Group:    Development/Languages
URL:      http://www.php.net/

Source0: http://downloads.php.net/stas/php-%{version}.tar.bz2
Source1: %name-php.conf
Source2: %name-php.ini
Source3: %name-macros.php
Source4: %name-php-fpm.conf
Source5: %name-php-fpm-www.conf
Source6: %name-php-fpm.service
#Source7: %name-php-fpm.logrotate
Source8: %name-php-fpm.sysconfig
Source9: %name-php.modconf
Source10: %name-php.ztsmodconf
Source11: %name-php-fpm.init
# below the jposug made.
Source200: %{name}-php-fpm
Source201: %{name}-php54-fpm.xml

# Build fixes
Patch5: %name-php-5.2.0-includedir.patch
Patch6: %name-php-5.2.4-embed.patch
Patch7: %name-php-5.3.0-recode.patch
Patch8: %name-php-5.4.7-libdb.patch

# Fixes for extension modules
# https://bugs.php.net/63171 no odbc call during timeout
Patch21: %name-php-5.4.7-odbctimer.patch

# Functional changes
Patch40: %name-php-5.4.0-dlopen.patch
Patch41: %name-php-5.4.0-easter.patch
Patch42: %name-php-5.3.1-systzdata-v10.patch
# See http://bugs.php.net/53436
Patch43: %name-php-5.4.0-phpize.patch
# Use system libzip instead of bundled one
Patch44: %name-php-5.4.15-system-libzip.patch
# Use -lldap_r for OpenLDAP
Patch45: %name-php-5.4.8-ldap_r.patch
# Make php_config.h constant across builds
Patch46: %name-php-5.4.9-fixheader.patch
# drop "Configure command" from phpinfo output
Patch47: %name-php-5.4.9-phpinfo.patch

# below the jposug made patches.
# This function (mem'p'cpy) is a GNU extension. So put compatible codes.
Patch200: %name-php-5.4.16-mempcpy.patch
Patch201: %name-php-5.4.16-ldap.patch
Patch202: %name-php-5.4.16-odbc.patch
# See https://bugs.php.net/bug.php?id=62692
Patch203: %name-php-5.4-dtrace_update.patch
Patch204: %name-php-5.4.16-mysql.patch
# to prevent:
# ld: fatal: file /usr/ucblib/libtermcap.so.1: version 'ILLUMOS_0.1' does not exist:
#        required by file /usr/lib/libreadline.so
Patch205: %name-php-5.4.16-ucblib.patch
Patch206: %name-php-5.4.16-iconv.patch
%if %cc_is_gcc
Patch207: %name-php-5.4.16-apache2handler.patch
Patch208: %name-php-5.4.16-apache2filter.patch
%endif

%include default-depend.inc

BuildRoot: %{_tmppath}/%{name}-%{version}-build

#BuildRequires: bzip2-devel, curl-devel >= 7.9, %{db_devel}, gmp-devel
BuildRequires: library/gmp-5/developer
Requires: library/gmp-5
BuildRequires: %pnm_buildrequires_web_curl
Requires: %pnm_requires_web_curl
Requires: database/berkeleydb-48
BuildRequires: database/berkeleydb-48
Requires: library/text/gnu-iconv
BuildRequires: library/text/gnu-iconv/developer
#TODO: BuildRequires: httpd-devel >= 2.0.46-1, pam-devel
BuildRequires: %pnm_buildrequires_web_server_apache_22
#BuildRequires: libstdc++-devel, openssl-devel
BuildRequires: %pnm_buildrequires_openssl
Requires: %pnm_requires_openssl

#%if %{with_sqlite3}
## For SQLite3 extension
#BuildRequires: sqlite-devel >= 3.6.0
#%else
## Enough for pdo_sqlite
#BuildRequires: sqlite-devel >= 3.0.0
#%endif
BuildRequires: %pnm_buildrequires_SUNWsqlite3_devel
Requires: %pnm_requires_SUNWsqlite3

#BuildRequires: zlib-devel, smtpdaemon
#BuildRequires: libedit-devel
#%else
#BuildRequires: readline-devel
#%endif
#TODO: %if %{with_pcre}
#TODO: BuildRequires: pcre-devel >= 8.10
#TODO: %endif
#BuildRequires: bzip2, perl, libtool >= 1.4.3, gcc-c++
BuildRequires: %pnm_buildrequires_compress_bzip2
Requires: %pnm_requires_compress_bzip2
BuildRequires: %pnm_buildrequires_perl510core
Requires: %pnm_requires_perl510core
BuildRequires: library/editline
Requires: library/editline
#BuildRequires: libtool-ltdl-devel
#TODO: %if %{with_libzip}
#TODO: BuildRequires: libzip-devel >= 0.10
#TODO: %endif
BuildRequires: %pnm_buildrequires_apch22
#configure: WARNING: You will need re2c 0.13.4 or later if you want to regenerate PHP parsers.
BuildRequires: developer/lexer/re2c
%if %cc_is_gcc
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc
Requires:      system/library/gcc-runtime
%endif
%endif

#%{!?scl:Obsoletes: php-dbg, php3, phpfi, stronghold-php}
#%if %{with_zts}
#Provides: %{?scl_prefix}php-zts = %{version}-%{release}
#Provides: %{?scl_prefix}php-zts%{?_isa} = %{version}-%{release}
#%{!?scl:Obsoletes: php-zts < 5.3.7}
#%endif

#Requires: httpd-mmn = %{_httpd_mmn}
#Provides: %{?scl_prefix}mod_php = %{version}-%{release}
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
# For backwards-compatibility, require php-cli for the time being:
#Requires: %{?scl_prefix}php-cli%{?_isa} = %{version}-%{release}
# To ensure correct /var/lib/php/session ownership:
#Requires(pre): httpd
Requires:	%pnm_requires_web_server_apache_22

# Don't provides extensions, which are not shared library, as .so
%{?filter_provides_in: %filter_provides_in %{_libdir}/php/modules/.*\.so$}
%{?filter_provides_in: %filter_provides_in %{_libdir}/php-zts/modules/.*\.so$}
%{?filter_provides_in: %filter_provides_in %{_httpd_moddir}/.*\.so$}
%{?filter_setup}


%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated web pages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. 

The php package contains the module (often referred to as mod_php)
which adds support for the PHP language to Apache HTTP Server.

%package cli
Group: Development/Languages
Summary: Command-line interface for PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
#Provides: %{?scl_prefix}php-cgi = %{version}-%{release}, %{?scl_prefix}php-cgi%{?_isa} = %{version}-%{release}
#Provides: %{?scl_prefix}php-pcntl, %{?scl_prefix}php-pcntl%{?_isa}
#Provides: %{?scl_prefix}php-readline, %{?scl_prefix}php-readline%{?_isa}
BuildRequires: library/security/cyrus-sasl
Requires: library/security/cyrus-sasl
Requires: web/php-54

%description cli
The php-cli package contains the command-line interface 
executing PHP scripts, /usr/bin/php, and the CGI interface.


%if %{with_fpm}
%package fpm
Group: Development/Languages
Summary: PHP FastCGI Process Manager
IPS_package_name: web/php-54/extension/php-fpm
# All files licensed under PHP version 3.01, except
# Zend is licensed under Zend
# TSRM and fpm are licensed under BSD
License: PHP and Zend and BSD
#Requires(pre): %{_root_sbindir}/useradd
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
%if %{with_systemd}
BuildRequires: systemd-devel
BuildRequires: systemd-units
Requires: systemd-units
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# This is actually needed for the %%triggerun script but Requires(triggerun)
# is not valid.  We can use %%post because this particular %%triggerun script
# should fire just after this package is installed.
Requires(post): systemd-sysv
%else
# This is for /sbin/service
#Requires(preun): initscripts
#Requires(postun): initscripts
Requires: web/php-54
%endif

%description fpm
PHP-FPM (FastCGI Process Manager) is an alternative PHP FastCGI
implementation with some additional features useful for sites of
any size, especially busier sites.
%endif

%package common
Group: Development/Languages
Summary: Common files for PHP
# All files licensed under PHP version 3.01, except
# fileinfo is licensed under PHP version 3.0
# regex, libmagic are licensed under BSD
# main/snprintf.c, main/spprintf.c and main/rfc1867.c are ASL 1.0
License: PHP and BSD and ASL 1.0
# ABI/API check - Arch specific
#Provides: %{?scl_prefix}php-api = %{apiver}%{isasuffix}
#Provides: %{?scl_prefix}php-zend-abi = %{zendver}%{isasuffix}
#Provides: %{?scl_prefix}php(api) = %{apiver}%{isasuffix}
#Provides: %{?scl_prefix}php(zend-abi) = %{zendver}%{isasuffix}
#Provides: %{?scl_prefix}php(language) = %{version}
#Provides: %{?scl_prefix}php(language)%{?_isa} = %{version}
## Provides for all builtin/shared modules:
#Provides: %{?scl_prefix}php-bz2, %{?scl_prefix}php-bz2%{?_isa}
#Provides: %{?scl_prefix}php-calendar, %{?scl_prefix}php-calendar%{?_isa}
#Provides: %{?scl_prefix}php-core = %{version}, %{?scl_prefix}php-core%{?_isa} = %{version}
#Provides: %{?scl_prefix}php-ctype, %{?scl_prefix}php-ctype%{?_isa}
#Provides: %{?scl_prefix}php-curl, %{?scl_prefix}php-curl%{?_isa}
#Provides: %{?scl_prefix}php-date, %{?scl_prefix}php-date%{?_isa}
#Provides: %{?scl_prefix}php-ereg, %{?scl_prefix}php-ereg%{?_isa}
#Provides: %{?scl_prefix}php-exif, %{?scl_prefix}php-exif%{?_isa}
#Provides: %{?scl_prefix}php-fileinfo, %{?scl_prefix}php-fileinfo%{?_isa}
#Provides: %{?scl_prefix}php-pecl-Fileinfo = %{fileinfover}, %{?scl_prefix}php-pecl-Fileinfo%{?_isa} = %{fileinfover}
#Provides: %{?scl_prefix}php-pecl(Fileinfo) = %{fileinfover}, %{?scl_prefix}php-pecl(Fileinfo)%{?_isa} = %{fileinfover}
#Provides: %{?scl_prefix}php-filter, %{?scl_prefix}php-filter%{?_isa}
#Provides: %{?scl_prefix}php-ftp, %{?scl_prefix}php-ftp%{?_isa}
#Provides: %{?scl_prefix}php-gettext, %{?scl_prefix}php-gettext%{?_isa}
#Provides: %{?scl_prefix}php-gmp, %{?scl_prefix}php-gmp%{?_isa}
#Provides: %{?scl_prefix}php-hash, %{?scl_prefix}php-hash%{?_isa}
#Provides: %{?scl_prefix}php-mhash = %{version}, %{?scl_prefix}php-mhash%{?_isa} = %{version}
#Provides: %{?scl_prefix}php-iconv, %{?scl_prefix}php-iconv%{?_isa}
#Provides: %{?scl_prefix}php-json, %{?scl_prefix}php-json%{?_isa}
#Provides: %{?scl_prefix}php-pecl-json = %{jsonver}, %{?scl_prefix}php-pecl-json%{?_isa} = %{jsonver}
#Provides: %{?scl_prefix}php-pecl(json) = %{jsonver}, %{?scl_prefix}php-pecl(json)%{?_isa} = %{jsonver}
#Provides: %{?scl_prefix}php-libxml, %{?scl_prefix}php-libxml%{?_isa}
#Provides: %{?scl_prefix}php-openssl, %{?scl_prefix}php-openssl%{?_isa}
#Provides: %{?scl_prefix}php-pecl-phar = %{pharver}, %{?scl_prefix}php-pecl-phar%{?_isa} = %{pharver}
#Provides: %{?scl_prefix}php-pecl(phar) = %{pharver}, %{?scl_prefix}php-pecl(phar)%{?_isa} = %{pharver}
#Provides: %{?scl_prefix}php-phar, %{?scl_prefix}php-phar%{?_isa}
#Provides: %{?scl_prefix}php-pcre, %{?scl_prefix}php-pcre%{?_isa}
#Provides: %{?scl_prefix}php-reflection, %{?scl_prefix}php-reflection%{?_isa}
#Provides: %{?scl_prefix}php-session, %{?scl_prefix}php-session%{?_isa}
#Provides: %{?scl_prefix}php-shmop, %{?scl_prefix}php-shmop%{?_isa}
#Provides: %{?scl_prefix}php-simplexml, %{?scl_prefix}php-simplexml%{?_isa}
#Provides: %{?scl_prefix}php-sockets, %{?scl_prefix}php-sockets%{?_isa}
#Provides: %{?scl_prefix}php-spl, %{?scl_prefix}php-spl%{?_isa}
#Provides: %{?scl_prefix}php-standard = %{version}, %{?scl_prefix}php-standard%{?_isa} = %{version}
#Provides: %{?scl_prefix}php-tokenizer, %{?scl_prefix}php-tokenizer%{?_isa}
#%if %{with_zip}
#Provides: %{?scl_prefix}php-zip, %{?scl_prefix}php-zip%{?_isa}
#Provides: %{?scl_prefix}php-pecl-zip = %{zipver}, %{?scl_prefix}php-pecl-zip%{?_isa} = %{zipver}
#Provides: %{?scl_prefix}php-pecl(zip) = %{zipver}, %{?scl_prefix}php-pecl(zip)%{?_isa} = %{zipver}
#%{!?scl:Obsoletes: php-pecl-zip}
#%endif
#Provides: %{?scl_prefix}php-zlib, %{?scl_prefix}php-zlib%{?_isa}
#%{!?scl:Obsoletes: php-openssl, php-pecl-json, php-json, php-pecl-phar, php-pecl-Fileinfo}
#%{!?scl:Obsoletes: php-mhash < 5.3.0}
#%{?scl:Requires: %{scl}-runtime}
Requires: web/php-54

%description common
The php-common package contains files used by both the php
package and the php-cli package.

%package devel
Group: Development/Libraries
Summary: Files needed for building PHP extensions
IPS_package_name: web/php-54/developer
Requires: web/php-54
#Requires: %{?scl_prefix}php-cli%{?_isa} = %{version}-%{release}, TODO: autoconf, automake
%if %{with_pcre}
#Requires: pcre-devel%{?_isa} >= 8.10
Requires: %pnm_buildrequires_library_pcre
%endif
#%{!?scl:Obsoletes: php-pecl-pdo-devel}
#%if %{with_zts}
#Provides: %{?scl_prefix}php-zts-devel = %{version}-%{release}
#Provides: %{?scl_prefix}php-zts-devel%{?_isa} = %{version}-%{release}
#%endif

%description devel
The php-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%if %{with_imap}
%package imap
Summary: A module for PHP applications that use IMAP
IPS_package_name: web/php-54/extension/php-imap
Group: Development/Languages
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
#%{!?scl:Obsoletes: mod_php3-imap, stronghold-php-imap}
#BuildRequires: krb5-devel, openssl-devel, libc-client-devel
Requires: web/php-54
Requires: library/mail/libc-client-2007
BuildRequires: library/mail/libc-client-2007
BuildRequires: library/mail/libc-client-2007/developer

%description imap
The php-imap package contains a dynamic shared object (DSO) for the
Apache Web server. When compiled into Apache, the php-imap module will
add IMAP (Internet Message Access Protocol) support to PHP. IMAP is a
protocol for retrieving and uploading e-mail messages on mail
servers. PHP is an HTML-embedded scripting language. If you need IMAP
support for PHP applications, you will need to install this package
and the php package.
%endif

%package ldap
Summary: A module for PHP applications that use LDAP
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-ldap
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
#%{!?scl:Obsoletes: mod_php3-ldap, stronghold-php-ldap}
#BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel
#Requires: web/php-54
BuildRequires: %{pnm_buildrequires_library_openldap}
Requires: %{pnm_requires_library_openldap}

%description ldap
The php-ldap package adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language.

%package pdo
Summary: A database access abstraction module for PHP applications
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-pdo
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
#%{!?scl:Obsoletes: php-pecl-pdo-sqlite, php-pecl-pdo}
## ABI/API check - Arch specific
#Provides: %{?scl_prefix}php-pdo-abi = %{pdover}%{isasuffix}
#Provides: %{?scl_prefix}php(pdo-abi) = %{pdover}%{isasuffix}
#%if %{with_sqlite3}
#Provides: %{?scl_prefix}php-sqlite3, %{?scl_prefix}php-sqlite3%{?_isa}
#%endif
#Provides: %{?scl_prefix}php-pdo_sqlite, %{?scl_prefix}php-pdo_sqlite%{?_isa}

%description pdo
The php-pdo package contains a dynamic shared object that will add
a database access abstraction layer to PHP.  This module provides
a common interface for accessing MySQL, PostgreSQL or other 
databases.

%if %{with_mysql}
%if %{with_libmysql}
%package mysql
Summary: A module for PHP applications that use MySQL databases
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-mysql
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-pdo%{?_isa} = %{version}-%{release}
Requires: web/php-54/extension/php-pdo
Requires: web/php-54
Requires: %{pnm_requires_mysql51}
Requires: %{pnm_requires_mysql51lib}
#Provides: %{?scl_prefix}php_database
#Provides: %{?scl_prefix}php-mysqli = %{version}-%{release}
#Provides: %{?scl_prefix}php-mysqli%{?_isa} = %{version}-%{release}
#Provides: %{?scl_prefix}php-pdo_mysql, %{?scl_prefix}php-pdo_mysql%{?_isa}
#%{!?scl:Obsoletes: mod_php3-mysql, stronghold-php-mysql}
#BuildRequires: mysql-devel >= 4.1.0
BuildRequires: %{pnm_buildrequires_mysql51}
BuildRequires: %{pnm_buildrequires_mysql51lib}
#Conflicts: %{?scl_prefix}php-mysqlnd

%description mysql
The php-mysql package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php package.
%endif

%package mysqlnd
Summary: A module for PHP applications that use MySQL databases
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-mysqlnd
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-pdo%{?_isa} = %{version}-%{release}
Requires: web/php-54/extension/php-pdo
Requires: web/php-54
#Provides: %{?scl_prefix}php_database
#Provides: %{?scl_prefix}php-mysql = %{version}-%{release}
#Provides: %{?scl_prefix}php-mysql%{?_isa} = %{version}-%{release}
#Provides: %{?scl_prefix}php-mysqli = %{version}-%{release}
#Provides: %{?scl_prefix}php-mysqli%{?_isa} = %{version}-%{release}
#Provides: %{?scl_prefix}php-pdo_mysql, %{?scl_prefix}php-pdo_mysql%{?_isa}
#%if ! %{with_libmysql}
#Obsoletes: %{?scl_prefix}php-mysql < %{version}-%{release}
#%endif

%description mysqlnd
The php-mysqlnd package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php package.

This package use the MySQL Native Driver
%endif

%if %{with_pgsql}
%package pgsql
Summary: A PostgreSQL database module for PHP
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-postgres
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-pdo%{?_isa} = %{version}-%{release}
Requires: web/php-54/extension/php-pdo
Requires: web/php-54
Requires: database/postgres-92/library
#Provides: %{?scl_prefix}php_database
#Provides: %{?scl_prefix}php-pdo_pgsql, %{?scl_prefix}php-pdo_pgsql%{?_isa}
#%{!?scl:Obsoletes: mod_php3-pgsql, stronghold-php-pgsql}
#BuildRequires: krb5-devel, openssl-devel, postgresql-devel
BuildRequires: %{pnm_buildrequires_service_security_kerberos_5}
BuildRequires: %{pnm_buildrequires_SUNWopenssl}
BuildRequires: database/postgres-92/library
BuildRequires: database/postgres-92/developer
BuildRequires: %{pnm_buildrequires_text_gnu_sed}
BuildRequires: SFEre2c

%description pgsql
The php-pgsql package add PostgreSQL database support to PHP.
PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.
%endif

%package process
Summary: Modules for PHP script using system process interfaces
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-process
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
#Provides: %{?scl_prefix}php-posix, %{?scl_prefix}php-posix%{?_isa}
#Provides: %{?scl_prefix}php-sysvsem, %{?scl_prefix}php-sysvsem%{?_isa}
#Provides: %{?scl_prefix}php-sysvshm, %{?scl_prefix}php-sysvshm%{?_isa}
#Provides: %{?scl_prefix}php-sysvmsg, %{?scl_prefix}php-sysvmsg%{?_isa}

%description process
The php-process package contains dynamic shared objects which add
support to PHP using system interfaces for inter-process
communication.

%if %{with_unixodbc}
%package odbc
Summary: A module for PHP applications that use ODBC databases
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-odbc
# All files licensed under PHP version 3.01, except
# pdo_odbc is licensed under PHP version 3.0
License: PHP
#Requires: %{?scl_prefix}php-pdo%{?_isa} = %{version}-%{release}
Requires: web/php-54
Requires: web/php-54/extension/php-pdo
#Provides: %{?scl_prefix}php_database
#Provides: %{?scl_prefix}php-pdo_odbc, %{?scl_prefix}php-pdo_odbc%{?_isa}
#%{!?scl:Obsoletes: stronghold-php-odbc}
#TODO: BuildRequires: unixODBC-devel

%description odbc
The php-odbc package contains a dynamic shared object that will add
database support through ODBC to PHP. ODBC is an open specification
which provides a consistent API for developers to use for accessing
data sources (which are often, but not always, databases). PHP is an
HTML-embeddable scripting language. If you need ODBC support for PHP
applications, you will need to install this package and the php
package.
%endif

%package soap
Summary: A module for PHP applications that use the SOAP protocol
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-soap
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
Requires: %{pnm_requires_library_libxml2}
#BuildRequires: libxml2-devel
BuildRequires: %{pnm_buildrequires_library_libxml2}

%description soap
The php-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%if %{with_interbase}
%package interbase
Summary: A module for PHP applications that use Interbase/Firebird databases
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-interbase
# All files licensed under PHP version 3.01
License: PHP
BuildRequires:  firebird-devel
#Requires: %{?scl_prefix}php-pdo%{?_isa} = %{version}-%{release}
Requires: web/php-54
Requires: web/php-54/extension/php-pdo
#Provides: %{?scl_prefix}php_database
#Provides: %{?scl_prefix}php-firebird, %{?scl_prefix}php-firebird%{?_isa}
#Provides: %{?scl_prefix}php-pdo_firebird, %{?scl_prefix}php-pdo_firebird%{?_isa}

%description interbase
The php-interbase package contains a dynamic shared object that will add
database support through Interbase/Firebird to PHP.

InterBase is the name of the closed-source variant of this RDBMS that was
developed by Borland/Inprise. 

Firebird is a commercially independent project of C and C++ programmers, 
technical advisors and supporters developing and enhancing a multi-platform 
relational database management system based on the source code released by 
Inprise Corp (now known as Borland Software Corp) under the InterBase Public
License.
%endif

%package snmp
Summary: A module for PHP applications that query SNMP-managed devices
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-snmp
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}, net-snmp
Requires: web/php-54
Requires: %{pnm_requires_system_management_snmp_net_snmp}
#BuildRequires: net-snmp-devel
BuildRequires: %{pnm_buildrequires_system_management_snmp_net_snmp}

%description snmp
The php-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package xml
Summary: A module for PHP applications which use XML
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-xml
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
Requires: %{pnm_requires_library_libxml2}
Requires: %{pnm_requires_library_libxslt}
#%{!?scl:Obsoletes: php-domxml, php-dom}
#Provides: %{?scl_prefix}php-dom, %{?scl_prefix}php-dom%{?_isa}
#Provides: %{?scl_prefix}php-xsl, %{?scl_prefix}php-xsl%{?_isa}
#Provides: %{?scl_prefix}php-domxml, %{?scl_prefix}php-domxml%{?_isa}
#Provides: %{?scl_prefix}php-wddx, %{?scl_prefix}php-wddx%{?_isa}
#Provides: %{?scl_prefix}php-xmlreader, %{?scl_prefix}php-xmlreader%{?_isa}
#Provides: %{?scl_prefix}php-xmlwriter, %{?scl_prefix}php-xmlwriter%{?_isa}
##BuildRequires: libxslt-devel >= 1.0.18-1, libxml2-devel >= 2.4.14-1
BuildRequires: %{pnm_buildrequires_library_libxml2}
BuildRequires: %{pnm_buildrequires_library_libxslt}

%description xml
The php-xml package contains dynamic shared objects which add support
to PHP for manipulating XML documents using the DOM tree,
and performing XSL transformations on XML documents.

%package xmlrpc
Summary: A module for PHP applications which use the XML-RPC protocol
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-xmlrpc
# All files licensed under PHP version 3.01, except
# libXMLRPC is licensed under BSD
License: PHP and BSD
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54

%description xmlrpc
The php-xmlrpc package contains a dynamic shared object that will add
support for the XML-RPC protocol to PHP.

%package mbstring
Summary: A module for PHP applications which need multi-byte string handling
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-mbstring
# All files licensed under PHP version 3.01, except
# libmbfl is licensed under LGPLv2
# onigurama is licensed under BSD
# ucgendat is licensed under OpenLDAP
License: PHP and LGPLv2 and BSD and OpenLDAP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54

%description mbstring
The php-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package gd
Summary: A module for PHP applications for using the gd graphics library
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-gd
# All files licensed under PHP version 3.01, except
# libgd is licensed under BSD
License: PHP and BSD
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
Requires: x11/library/libxpm
Requires: %{pnm_requires_image_library_libjpeg}
Requires: %pnm_requires_image_library_libpng
Requires: %pnm_requires_system_library_freetype_2
# Required to build the bundled GD library
#BuildRequires: libjpeg-devel, libpng-devel, freetype-devel
#BuildRequires: libXpm-devel
%if %{with_t1lib}
BuildRequires: t1lib-devel
%endif
BuildRequires: x11/library/libxpm
BuildRequires: %{pnm_buildrequires_image_library_libjpeg}
BuildRequires: %pnm_buildrequires_image_library_libpng
BuildRequires: %pnm_buildrequires_system_library_freetype_2

%description gd
The php-gd package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%package bcmath
Summary: A module for PHP applications for using the bcmath library
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-bcmath
# All files licensed under PHP version 3.01, except
# libbcmath is licensed under LGPLv2+
License: PHP and LGPLv2+
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54

%description bcmath
The php-bcmath package contains a dynamic shared object that will add
support for using the bcmath library to PHP.

%package dba
Summary: A database abstraction layer module for PHP applications
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-dba
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54

%description dba
The php-dba package contains a dynamic shared object that will add
support for using the DBA database abstraction layer to PHP.

%if %{with_mcrypt}
%package mcrypt
Summary: Standard PHP module provides mcrypt library support
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-mcrypt
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: %pnm_requires_system_library_security_libmcrypt
Requires: web/php-54
#BuildRequires: libmcrypt-devel
BuildRequires: %pnm_buildrequires_system_library_security_libmcrypt

%description mcrypt
The php-mcrypt package contains a dynamic shared object that will add
support for using the mcrypt library to PHP.
%endif

%if %{with_tidy}
%package tidy
Summary: Standard PHP module provides tidy library support
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-tidy
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: %pnm_requires_text_tidy
Requires: web/php-54
#BuildRequires: libtidy-devel
BuildRequires: %pnm_buildrequires_text_tidy

%description tidy
The php-tidy package contains a dynamic shared object that will add
support for using the tidy library to PHP.
%endif

%if %{with_mssql}
%package mssql
Summary: MSSQL database module for PHP
Group: Development/Languages
IPS_package_name: web/php-54/extension/php-mssql
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-pdo%{?_isa} = %{version}-%{release}
Requires: web/php-54
#TODO: BuildRequires: freetds-devel
#Provides: %{?scl_prefix}php-pdo_dblib, %{?scl_prefix}php-pdo_dblib%{?_isa}

%description mssql
The php-mssql package contains a dynamic shared object that will
add MSSQL database support to PHP.  It uses the TDS (Tabular
DataStream) protocol through the freetds library, hence any
database server which supports TDS can be accessed.
%endif

%if %{with_embed}
%package embedded
Summary: PHP library for embedding in applications
Group: System Environment/Libraries
IPS_package_name: web/php-54/extension/php-embedded
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
# doing a real -devel package for just the .so symlink is a bit overkill
#Provides: %{?scl_prefix}php-embedded-devel = %{version}-%{release}
#Provides: %{?scl_prefix}php-embedded-devel%{?_isa} = %{version}-%{release}

%description embedded
The php-embedded package contains a library which can be embedded
into applications to provide PHP scripting language support.
%endif

%if %{with_pspell}
%package pspell
Summary: A module for PHP applications for using pspell interfaces
Group: System Environment/Libraries
IPS_package_name: web/php-54/extension/php-pspell
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
#TODO: BuildRequires: aspell-devel >= 0.50.0
Requires: web/php-54

%description pspell
The php-pspell package contains a dynamic shared object that will add
support for using the pspell library to PHP.
%endif

%if %{with_recode}
%package recode
Summary: A module for PHP applications for using the recode library
Group: System Environment/Libraries
IPS_package_name: web/php-54/extension/php-recode
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
#TODO: BuildRequires: recode-devel

%description recode
The php-recode package contains a dynamic shared object that will add
support for using the recode library to PHP.
%endif

%package intl
Summary: Internationalization extension for PHP applications
Group: System Environment/Libraries
IPS_package_name: web/php-54/extension/php-intl
# All files licensed under PHP version 3.01
License: PHP
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
Requires: %pnm_requires_icu
#TODO: pnm_buildrequires_developer_icu developer ? BuildRequires: libicu-devel >= 3.6
BuildRequires: %pnm_buildrequires_icu

%description intl
The php-intl package contains a dynamic shared object that will add
support for using the ICU library to PHP.

%if %{with_enchant}
%package enchant
Summary: Enchant spelling extension for PHP applications
IPS_package_name: web/php-54/extension/php-enchant
# All files licensed under PHP version 3.0
License: PHP
Group: System Environment/Libraries
#Requires: %{?scl_prefix}php-common%{?_isa} = %{version}-%{release}
Requires: web/php-54
Requires: %{pnm_requires_library_spell_checking_enchant}
#BuildRequires: enchant-devel >= 1.2.4
BuildRequires: %{pnm_buildrequires_library_spell_checking_enchant}

%description enchant
The php-enchant package contains a dynamic shared object that will add
support for using the enchant library to PHP.
%endif


%prep
#: Building %{name}-%{version}-%{release} with systemd=%{with_systemd} imap=%{with_imap} interbase=%{with_interbase} mcrypt=%{with_mcrypt} mssql=%{with_mssql} sqlite3=%{with_sqlite3} tidy=%{with_tidy} zip=%{with_zip}
%if %{skip_prep}
%else
%setup -q -n php-%{version}
%patch5 -p1 -b .includedir
%patch6 -p1 -b .embed
%patch7 -p1 -b .recode
%patch8 -p1 -b .libdb

%patch21 -p1 -b .odbctimer

%patch40 -p1 -b .dlopen
%patch41 -p1 -b .easter
%patch42 -p1 -b .systzdata
%patch43 -p1 -b .headers
%if %{with_libzip}
%patch44 -p1 -b .systzip
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%patch45 -p1 -b .ldap_r
%endif
%patch46 -p1 -b .fixheader
%patch47 -p1 -b .phpinfo

%patch200 -p1 -b .mempcpy
%patch201 -p1 -b .orig
%patch202 -p1 -b .orig
%patch203 -p1
%patch204 -p1 -b .orig
%patch205 -p1 -b .orig
%patch206 -p1 -b .orig
%if %cc_is_gcc
%patch207 -p1 -b .orig
%patch208 -p1 -b .orig
%endif

# Prevent %%doc confusion over LICENSE files
cp Zend/LICENSE Zend/ZEND_LICENSE
cp TSRM/LICENSE TSRM_LICENSE
cp ext/ereg/regex/COPYRIGHT regex_COPYRIGHT
cp ext/gd/libgd/README libgd_README
cp ext/gd/libgd/COPYING libgd_COPYING
cp sapi/fpm/LICENSE fpm_LICENSE
cp ext/mbstring/libmbfl/LICENSE libmbfl_LICENSE
cp ext/mbstring/oniguruma/COPYING oniguruma_COPYING
cp ext/mbstring/ucgendat/OPENLDAP_LICENSE ucgendat_LICENSE
cp ext/fileinfo/libmagic/LICENSE libmagic_LICENSE
cp ext/phar/LICENSE phar_LICENSE
cp ext/bcmath/libbcmath/COPYING.LIB libbcmath_COPYING

# Multiple builds for multiple SAPIs
mkdir \
%if %{with_embed}
    build-embedded \
%endif
%if %{with_fpm}
    build-fpm \
%endif
%if %{with_zts}
    build-zts build-ztscli \
%endif
    build-cgi build-apache

# ----- Manage known as failed test -------
# php_egg_logo_guid() removed by patch41
rm -f tests/basic/php_egg_logo_guid.phpt
# affected by systzdata patch
rm -f ext/date/tests/timezone_location_get.phpt
# fails sometime
rm -f ext/sockets/tests/mcast_ipv?_recv.phpt

# Safety check for API version change.
pver=$(sed -n '/#define PHP_VERSION /{s/.* "//;s/".*$//;p}' main/php_version.h)
if test "x${pver}" != "x%{version}%{?rcver}"; then
   : Error: Upstream PHP version is now ${pver}, expecting %{version}%{?rcver}.
   : Update the version/rcver macros and rebuild.
   exit 1
fi

vapi=`sed -n '/#define PHP_API_VERSION/{s/.* //;p}' main/php.h`
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

vzend=`sed -n '/#define ZEND_MODULE_API_NO/{s/^[^0-9]*//;p;}' Zend/zend_modules.h`
if test "x${vzend}" != "x%{zendver}"; then
   : Error: Upstream Zend ABI version is now ${vzend}, expecting %{zendver}.
   : Update the zendver macro and rebuild.
   exit 1
fi

# Safety check for PDO ABI version change
vpdo=`sed -n '/#define PDO_DRIVER_API/{s/.*[ 	]//;p}' ext/pdo/php_pdo_driver.h`
if test "x${vpdo}" != "x%{pdover}"; then
   : Error: Upstream PDO ABI version is now ${vpdo}, expecting %{pdover}.
   : Update the pdover macro and rebuild.
   exit 1
fi

# Check for some extension version
ver=$(sed -n '/#define PHP_FILEINFO_VERSION /{s/.* "//;s/".*$//;p}' ext/fileinfo/php_fileinfo.h)
if test "$ver" != "%{fileinfover}"; then
   : Error: Upstream FILEINFO version is now ${ver}, expecting %{fileinfover}.
   : Update the fileinfover macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_PHAR_VERSION /{s/.* "//;s/".*$//;p}' ext/phar/php_phar.h)
if test "$ver" != "%{pharver}"; then
   : Error: Upstream PHAR version is now ${ver}, expecting %{pharver}.
   : Update the pharver macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_ZIP_VERSION_STRING /{s/.* "//;s/".*$//;p}' ext/zip/php_zip.h)
if test "$ver" != "%{zipver}"; then
   : Error: Upstream ZIP version is now ${ver}, expecting %{zipver}.
   : Update the zipver macro and rebuild.
   exit 1
fi
ver=$(sed -n '/#define PHP_JSON_VERSION /{s/.* "//;s/".*$//;p}' ext/json/php_json.h)
if test "$ver" != "%{jsonver}"; then
   : Error: Upstream JSON version is now ${ver}, expecting %{jsonver}.
   : Update the jsonver macro and rebuild.
   exit 1
fi

# https://bugs.php.net/63362 - Not needed but installed headers.
# Drop some Windows specific headers to avoid installation,
# before build to ensure they are really not needed.
rm -f TSRM/tsrm_win32.h \
      TSRM/tsrm_config.w32.h \
      Zend/zend_config.w32.h \
      ext/mysqlnd/config-win.h \
      ext/standard/winver.h \
      main/win32_internal_function_disabled.h \
      main/win95nt.h

# Fix some bogus permissions
find . -name \*.[ch] -exec chmod 644 {} \;
chmod 644 README.*

# php-fpm configuration files for tmpfiles.d
# TODO echo "d /run/php-fpm 755 root root" >php-fpm.tmpfiles
%endif

%build
%if %{skip_prep}
 cd php-%{version}
%endif
%if %{skip_build}
%else
# aclocal workaround - to be improved
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >>aclocal.m4
%endif

# Force use of system libtool:
libtoolize --force --copy
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4
%else
cat `aclocal --print-ac-dir`/libtool.m4 > build/libtool.m4
%endif
%if %cc_is_gcc
# to remove warning gcc: -i: linker input file unused because linking not done 
sed -i -e 's/-Xlinker//' -e 's/-i//' aclocal.m4
sed -i -e 's/-Xlinker//' -e 's/-i//' build/libtool.m4
%endif

# Regenerate configure scripts (patches change config.m4's)
touch configure.in
./buildconf --force

#CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
#export CFLAGS
export LDFLAGS="%_ldflags %gnu_lib_path -L/opt/solarisstudio12.3/lib -R%{mysql_prefix}/lib/mysql"
%if %cc_is_gcc
export CXXFLAGS=$(echo "%cxx_optflags" | sed -e 's/-Xlinker//' -e 's/-i//')
export CFLAGS=$(echo "%optflags" | sed -e 's/-Xlinker//' -e 's/-i//')
export CC=gcc
export CXX=g++
%else
export CXXFLAGS="%cxx_optflags"
export CFLAGS="%optflags"
%endif
# Install extension modules in %{_libdir}/php/modules.
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{usr_sharedir}/pear/%{major_version}; export PEAR_INSTALLDIR

# Shell function to configure and build a PHP tree.
build() {
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
# Old/recent bison version seems to produce a broken parser;
# upstream uses GNU Bison 2.3. Workaround:
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
ln -sf ../configure
#configure: WARNING: unrecognized options: --with-exec-dir
#    --with-exec-dir=%{_bindir} \
#    --with-iconv=%{gnu_inc}/.. \
%configure \
    --cache-file=../config.cache \
    --with-libdir=%{_lib} \
    --with-config-file-path=%{_sysconfdir} \
    --with-config-file-scan-dir=%{_sysconfdir}/php.d \
    --disable-debug \
    --with-pic \
    --disable-rpath \
    --without-pear \
    --with-bz2 \
    --with-freetype-dir=%{usr_prefix} \
    --with-png-dir=%{usr_prefix} \
    --with-xpm-dir=%{usr_prefix} \
    --enable-gd-native-ttf \
%if %{with_t1lib}
    --with-t1lib=%{usr_prefix} \
%endif
    --without-gdbm \
    --with-gettext \
    --with-gmp=%{gnu_inc}/.. \
    --with-iconv \
    --with-jpeg-dir=%{usr_prefix} \
    --with-openssl \
%if %{with_pcre}
    --with-pcre-regex=%{usr_prefix} \
%endif
    --with-zlib \
    --with-layout=GNU \
    --enable-exif \
    --enable-ftp \
    --enable-sockets \
    --with-kerberos \
    --enable-shmop \
    --enable-calendar \
    --with-libxml-dir=%{usr_prefix} \
    --enable-xml \
    --with-mhash \
    --with-system-tzdata=/usr/share/lib/zoneinfo \
    --enable-dtrace \
    $*
if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi
# https://bugs.php.net/bug.php?id=62692
sed -i -e 's|BUILD_CLI = |BUILD_CLI = sh ../update.sh; |' Makefile
make -j$CPUS
}

%if %{build_cgi}
# Build /usr/bin/php-cgi with the CGI SAPI, and all the shared extensions

pushd build-cgi

build --libdir=%{_libdir}/php \
      --enable-pcntl \
%if %{with_imap}
      --with-imap=shared --with-imap-ssl \
%endif
      --enable-mbstring=shared \
      --enable-mbregex \
      --with-gd=shared \
      --enable-bcmath=shared \
      --enable-dba=shared --with-db4=%{gnu_inc}/.. \
      --with-xmlrpc=shared \
      --with-ldap=shared,%{usr_prefix} --with-ldap-sasl \
%if %{with_mysql}
      --enable-mysqlnd=shared \
      --with-mysql=shared,mysqlnd \
      --with-mysqli=shared,mysqlnd \
      --with-mysql-sock=%{mysql_sock} \
%endif
%if %{with_interbase}
      --with-interbase=shared,%{_libdir}/firebird \
      --with-pdo-firebird=shared,%{_libdir}/firebird \
%endif
      --enable-dom=shared \
%if %{with_pgsql}
      --with-pgsql=shared \
%endif
      --enable-wddx=shared \
      --with-snmp=shared,%{usr_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{usr_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --with-curl=shared,%{usr_prefix} \
      --enable-pdo=shared \
%if %{with_unixodbc}
      --with-pdo-odbc=shared,unixODBC,%{usr_prefix} \
%endif
      --with-pdo-mysql=shared,mysqlnd \
%if %{with_pgsql}
      --with-pdo-pgsql=shared,%{usr_prefix} \
%endif
%if %with_pdo_sqlite3
      --with-pdo-sqlite=shared,%{usr_prefix} \
%endif
%if %{with_sqlite3}
      --with-sqlite3=shared,%{usr_prefix} \
%else
      --without-sqlite3 \
%endif
      --enable-json=shared \
%if %{with_zip}
      --enable-zip=shared \
%endif
%if %{with_libzip}
      --with-libzip \
%endif
      --without-readline \
%if %{with_libedit}
      --with-libedit \
%else
      --with-readline \
%endif
%if %{with_pspell}
      --with-pspell=shared \
%endif
      --enable-phar=shared \
%if %{with_mcrypt}
      --with-mcrypt=shared,%{usr_prefix} \
%endif
%if %{with_tidy}
      --with-tidy=shared,%{usr_prefix} \
%endif
%if %{with_mssql}
      --with-mssql=shared,%{usr_prefix} \
      --with-pdo-dblib=shared,%{usr_prefix} \
%endif
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-posix=shared \
%if %{with_unixodbc}
      --with-unixODBC=shared,%{usr_prefix} \
%endif
      --enable-intl=shared \
      --with-icu-dir=%{usr_prefix} \
%if %{with_enchant}
      --with-enchant=shared,%{usr_prefix} \
%endif
%if %{with_recode}
      --with-recode=shared,%{usr_prefix} \
%endif
      --enable-fileinfo=shared
popd
# with_cgi
%endif
%if %{build_apache}
without_shared="--without-gd \
      --disable-dom --disable-dba --without-unixODBC \
      --disable-xmlreader --disable-xmlwriter \
      --without-sqlite3 --without-pdo-sqlite --disable-phar --disable-fileinfo \
      --disable-json --without-pspell --disable-wddx \
      --without-curl --disable-posix \
      --disable-sysvmsg --disable-sysvshm --disable-sysvsem"

# Build Apache module, and the CLI SAPI, /usr/bin/php
pushd build-apache
build --with-apxs2=%{_httpd_apxs} \
      --libdir=%{_libdir}/php \
%if %{with_mysql}
%if %{with_libmysql}
      --enable-pdo=shared \
      --with-mysql=shared,%{mysql_prefix} \
      --with-mysqli=shared,%{mysql_config} \
      --with-pdo-mysql=shared,%{mysql_config} \
      --without-pdo-sqlite \
%else
      --without-mysql \
      --disable-pdo \
%endif
%endif
      ${without_shared}
popd
%endif
%if %{with_fpm}
# Build php-fpm
pushd build-fpm
build --enable-fpm \
%if %{with_systemd}
      --with-fpm-systemd \
%endif
      --libdir=%{_libdir}/php \
      --without-mysql \
      --disable-pdo \
      ${without_shared}
popd
%endif

%if %{with_embed}
# Build for inclusion as embedded script language into applications,
# /usr/lib[64]/libphp5.so
pushd build-embedded
build --enable-embed \
      --without-mysql --disable-pdo \
      ${without_shared}
popd
%endif

%if %{with_zts}
# Build a special thread-safe (mainly for modules)
pushd build-ztscli

EXTENSION_DIR=%{_libdir}/php-zts/modules
build --includedir=%{_includedir}/php-zts \
      --libdir=%{_libdir}/php-zts \
      --enable-maintainer-zts \
      --with-config-file-scan-dir=%{_sysconfdir}/php-zts.d \
      --enable-pcntl \
%if %{with_imap}
      --with-imap=shared --with-imap-ssl \
%endif
      --enable-mbstring=shared \
      --enable-mbregex \
      --with-gd=shared \
      --enable-bcmath=shared \
      --enable-dba=shared --with-db4=%{gnu_inc}/.. \
      --with-xmlrpc=shared \
      --with-ldap=shared,%{usr_prefix} --with-ldap-sasl \
      --enable-mysqlnd=shared \
%if %{with_libmysql}
      --with-mysql=shared,mysqlnd \
      --with-mysqli=shared,mysqlnd \
%endif
%if %{with_mysql}
      --with-mysql-sock=%{mysql_sock} \
      --enable-mysqlnd-threading \
%endif
%if %{with_interbase}
#TODO:      --with-interbase=shared,%{_root_libdir}/firebird \
#TODO:      --with-pdo-firebird=shared,%{_root_libdir}/firebird \
%endif
      --enable-dom=shared \
%if %{with_pgsql}
      --with-pgsql=shared \
%endif
      --enable-wddx=shared \
      --with-snmp=shared,%{usr_prefix} \
      --enable-soap=shared \
      --with-xsl=shared,%{usr_prefix} \
      --enable-xmlreader=shared --enable-xmlwriter=shared \
      --with-curl=shared,%{usr_prefix} \
      --enable-pdo=shared \
      --with-pdo-odbc=shared,unixODBC,%{usr_prefix} \
%if %{with_libmysql}
      --with-pdo-mysql=shared,mysqlnd \
%endif
%if %{with_pgsql}
      --with-pdo-pgsql=shared,%{usr_prefix} \
%endif
%if %with_pdo_sqlite3
      --with-pdo-sqlite=shared,%{usr_prefix} \
%endif
%if %{with_sqlite3}
      --with-sqlite3=shared,%{usr_prefix} \
%else
      --without-sqlite3 \
%endif
      --enable-json=shared \
%if %{with_zip}
      --enable-zip=shared \
%endif
%if %{with_libzip}
      --with-libzip \
%endif
      --without-readline \
%if %{with_libedit}
      --with-libedit \
%else
      --with-readline \
%endif
      --with-pspell=shared \
      --enable-phar=shared \
%if %{with_mcrypt}
      --with-mcrypt=shared,%{usr_prefix} \
%endif
%if %{with_tidy}
      --with-tidy=shared,%{usr_prefix} \
%endif
%if %{with_mssql}
      --with-mssql=shared,%{usr_prefix} \
      --with-pdo-dblib=shared,%{usr_prefix} \
%endif
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-posix=shared \
      --with-unixODBC=shared,%{usr_prefix} \
      --enable-intl=shared \
      --with-icu-dir=%{usr_prefix} \
%if %{with_enchant}
      --with-enchant=shared,%{usr_prefix} \
%endif
%if %{with_recode}
      --with-recode=shared,%{usr_prefix} \
%endif
      --enable-fileinfo=shared
popd

# Build a special thread-safe Apache SAPI
pushd build-zts
build --with-apxs2=%{_httpd_apxs} \
      --includedir=%{_includedir}/php-zts \
      --libdir=%{_libdir}/php-zts \
      --enable-maintainer-zts \
      --with-config-file-scan-dir=%{_sysconfdir}/php-zts.d \
%if %{with_libmysql}
      --enable-pdo=shared \
      --with-mysql=shared,%{mysql_prefix} \
      --with-mysqli=shared,%{mysql_config} \
      --with-pdo-mysql=shared,%{mysql_config} \
      --without-pdo-sqlite \
%else
      --without-mysql \
      --disable-pdo \
%endif
      ${without_shared}
popd

### NOTE!!! EXTENSION_DIR was changed for the -zts build, so it must remain
### the last SAPI to be built.
%endif
# skip_build
%endif

%check
%if %{skip_prep}
 cd php-%{version}
%endif
%if %( expr %{skip_check} '=' 0 )
%if %runselftest
cd build-apache
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
export SKIP_ONLINE_TESTS=1
unset TZ LANG LC_ALL
if ! make test; then
  set +x
  for f in `find .. -name \*.diff -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
  done
  set -x
  #exit 1
fi
unset NO_INTERACTION REPORT_EXIT_STATUS MALLOC_CHECK_
%endif
%endif

%install
%if %{skip_prep}
  cd php-%{version}
%endif
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%if %{with_zts}
# Install the extensions for the ZTS version
make -C build-ztscli install \
     INSTALL_ROOT=$RPM_BUILD_ROOT

# rename extensions build with mysqlnd
mv $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/mysql.so \
   $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/mysqlnd_mysql.so
mv $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/mysqli.so \
   $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/mysqlnd_mysqli.so
mv $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/pdo_mysql.so \
   $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/pdo_mysqlnd.so

%if %{with_libmysql}
# Install the extensions for the ZTS version modules for libmysql
make -C build-zts install-modules \
     INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# rename ZTS binary
mv $RPM_BUILD_ROOT%{_bindir}/php        $RPM_BUILD_ROOT%{_bindir}/zts-php
mv $RPM_BUILD_ROOT%{_bindir}/phpize     $RPM_BUILD_ROOT%{_bindir}/zts-phpize
mv $RPM_BUILD_ROOT%{_bindir}/php-config $RPM_BUILD_ROOT%{_bindir}/zts-php-config
%endif

%if %{with_embed}
# Install the version for embedded script language in applications + php_embed.h
make -C build-embedded install-sapi install-headers \
     INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%if %{with_fpm}
# Install the php-fpm binary
make -C build-fpm install-fpm \
     INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# Install everything from the CGI SAPI build
make -C build-cgi install \
     INSTALL_ROOT=$RPM_BUILD_ROOT

# rename extensions build with mysqlnd
mv $RPM_BUILD_ROOT%{_libdir}/php/modules/mysql.so \
   $RPM_BUILD_ROOT%{_libdir}/php/modules/mysqlnd_mysql.so
mv $RPM_BUILD_ROOT%{_libdir}/php/modules/mysqli.so \
   $RPM_BUILD_ROOT%{_libdir}/php/modules/mysqlnd_mysqli.so
mv $RPM_BUILD_ROOT%{_libdir}/php/modules/pdo_mysql.so \
   $RPM_BUILD_ROOT%{_libdir}/php/modules/pdo_mysqlnd.so

%if %{with_libmysql}
# Install the mysql extension build with libmysql
make -C build-apache install-modules \
     INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# Install the default configuration file and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
#install -m 755 -d $RPM_BUILD_ROOT%{_httpd_contentdir}/icons
#install -m 644 php.gif $RPM_BUILD_ROOT%{_httpd_contentdir}/icons/php.gif
/bin/rm -rf php.gif

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/php

# install the DSO
moddir="%{_httpd_moddir}"
moddir=${moddir#%{usr_prefix}}
install -m 755 -d $RPM_BUILD_ROOT%{_httpd_moddir}
install -d 755 $RPM_BUILD_ROOT%{_prefix}$moddir/
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT%{_prefix}$moddir/libphp5.so
pushd $RPM_BUILD_ROOT/%{_httpd_moddir}
ln -s ../../../php/%{major_version}/$moddir/libphp5.so .
popd

%if %{with_zts}
# install the ZTS DSO
install -m 755 build-zts/libs/libphp5.so $RPM_BUILD_ROOT%{_prefix}$moddir/libphp5-zts.so
pushd $RPM_BUILD_ROOT/%{_httpd_moddir}
ln -s ../../../php/%{major_version}$moddir/libphp5-zts.so .
popd
%endif

# Apache config fragment
#%if %{?scl:1}0
#install -m 755 -d $RPM_BUILD_ROOT%{_root_httpd_moddir}
#ln -s %{_httpd_moddir}/libphp5.so      $RPM_BUILD_ROOT%{_root_httpd_moddir}/libphp5.so
#%if %{with_zts}
#ln -s %{_httpd_moddir}/libphp5-zts.so  $RPM_BUILD_ROOT%{_root_httpd_moddir}/libphp5-zts.so
#%endif
#%endif
sed -e 's|modules/libphp5\.so|libexec/libphp5.so|' %{SOURCE9} >modconf

#%if "%{_httpd_modconfdir}" == "%{_httpd_confdir}"
# Single config file with httpd < 2.4 (fedora <= 17)
install -D -m 644 modconf $RPM_BUILD_ROOT%{_httpd_confdir}/php54-32.load
cat %{SOURCE1} >>$RPM_BUILD_ROOT%{_httpd_confdir}/php54-32.load
%if %{with_zts}
cat %{SOURCE10} >>$RPM_BUILD_ROOT%{_httpd_confdir}/php54-32.load
%endif

#%else
## Dual config file with httpd >= 2.4 (fedora >= 18)
#install -D -m 644 modconf    $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-php.conf
#%if %{with_zts}
#cat %{SOURCE10} >>$RPM_BUILD_ROOT%{_httpd_modconfdir}/10-php.conf
#%endif
#install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_confdir}/php.conf
#%endif
sed -e 's:/var/lib:%{_localstatedir}/lib:' \
    -i $RPM_BUILD_ROOT%{_httpd_confdir}/php54-32.load
pushd $RPM_BUILD_ROOT%{_httpd_confdir}
ln -s php54-32.load php-32.load
popd

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
%if %{with_zts}
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d
%endif
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/lib/php/session

%if %{with_fpm}
# PHP-FPM stuff
# Log
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/log/php-fpm
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/run/php-fpm
# Config
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf
sed -e 's:/run:%{_localstatedir}/run:' \
    -e 's:/var/log:%{_localstatedir}/log:' \
    -e 's:/etc:%{_sysconfdir}:' \
    -i $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/www.conf
sed -e 's:/var/lib:%{_localstatedir}/lib:' \
    -e 's:/var/log:%{_localstatedir}/log:' \
    -e 's:= apache:= webservd:' \
    -i $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.d/www.conf
mv $RPM_BUILD_ROOT%{_sysconfdir}/php-fpm.conf.default .
# tmpfiles.d
# install -m 755 -d $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d
# install -m 644 php-fpm.tmpfiles $RPM_BUILD_ROOT%{_prefix}/lib/tmpfiles.d/php-fpm.conf
# install systemd unit files and scripts for handling server startup
%if %{with_systemd}
install -m 755 -d $RPM_BUILD_ROOT%{_unitdir}
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/%{?scl_prefix}php-fpm.service
sed -e 's:/run:%{_localstatedir}/run:' \
    -e 's:/etc:%{_sysconfdir}:' \
    -e 's:/usr/sbin:%{_sbindir}:' \
    -i $RPM_BUILD_ROOT%{_unitdir}/%{?scl_prefix}php-fpm.service
%else
# Service
#install -m 755 -d $RPM_BUILD_ROOT%{_root_initddir}
#install -m 755 %{SOURCE11} $RPM_BUILD_ROOT%{_root_initddir}/%{?scl_prefix}php-fpm
# Needed relocation for SCL
#sed -e '/php-fpm.pid/s:/var:%{_localstatedir}:' \
#    -e '/subsys/s/php-fpm/%{?scl_prefix}php-fpm/' \
#    -e 's:/etc/sysconfig/php-fpm:%{_sysconfdir}/sysconfig/php-fpm:' \
#    -e 's:/etc/php-fpm.conf:%{_sysconfdir}/php-fpm.conf:' \
#    -e 's:/usr/sbin:%{_sbindir}:' \
#    -i $RPM_BUILD_ROOT%{_root_initddir}/%{?scl_prefix}php-fpm
%endif

# LogRotate
#install -m 755 -d $RPM_BUILD_ROOT%{_root_sysconfdir}/logrotate.d
#install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_root_sysconfdir}/logrotate.d/%{?scl_prefix}php-fpm
#sed -e 's:/run:%{_localstatedir}/run:' \
#    -e 's:/var/log:%{_localstatedir}/log:' \
#    -i $RPM_BUILD_ROOT%{_root_sysconfdir}/logrotate.d/%{?scl_prefix}php-fpm
# Environment file
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/php-fpm
%endif

# Fix the link
(cd $RPM_BUILD_ROOT%{_bindir}; ln -sfn phar.phar phar)

# make the cli commands available in standard root for SCL build
%if 0%{?scl:1}
#install -m 755 -d $RPM_BUILD_ROOT%{_root_bindir}
#ln -s %{_bindir}/php       $RPM_BUILD_ROOT%{_root_bindir}/%{?scl_prefix}php
#ln -s %{_bindir}/phar.phar $RPM_BUILD_ROOT%{_root_bindir}/%{?scl_prefix}phar
%endif

# Generate files lists and stub .ini files for each subpackage
for mod in \
%if %{with_pgsql}
    pgsql \
%endif
%if %{with_unixodbc}
    odbc \
%endif
ldap snmp xmlrpc \
%if %{with_imap}
    imap \
%endif
%if %{with_mysql}
    mysqlnd mysqlnd_mysql mysqlnd_mysqli pdo_mysqlnd \
%endif
    mbstring gd dom xsl soap bcmath dba xmlreader xmlwriter \
    pdo \
%if %{with_pgsql}
    pdo_pgsql \
%endif
%if %{with_unixodbc}
    pdo_odbc \
%endif
%if %with_pdo_sqlite3
    pdo_sqlite \
%endif
json %{zipmod} \
%if %{with_sqlite3}
    sqlite3 \
%endif
%if %{with_interbase}
    interbase pdo_firebird \
%endif
%if %{with_enchant}
    enchant \
%endif
    phar fileinfo intl \
%if %{with_mcrypt}
    mcrypt \
%endif
%if %{with_tidy}
    tidy \
%endif
%if %{with_mssql}
    pdo_dblib mssql \
%endif
%if %{with_recode}
    recode \
%endif
%if %{with_libmysql}
    mysql mysqli pdo_mysql \
%endif
%if %{with_pspell}
    pspell \
%endif
    curl wddx \
    posix sysvshm sysvsem sysvmsg; do
    cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
%if %{with_zts}
    cat > $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
%endif
    cat > files.${mod} <<EOF
%defattr(-,root,bin)
%attr(555,root,bin) %{_libdir}/php/modules/${mod}.so
%config(noreplace) %attr(644,root,bin) %{_sysconfdir}/php.d/${mod}.ini
%if %{with_zts}
%attr(555,root,bin) %{_libdir}/php-zts/modules/${mod}.so
%config(noreplace) %attr(644,root,bin) %{_sysconfdir}/php-zts.d/${mod}.ini
%endif
EOF
done

# The dom, xsl and xml* modules are all packaged in php-xml
cat files.dom files.xsl files.xml{reader,writer} files.wddx > files.xml

# The mysql and mysqli modules are both packaged in php-mysql
%if %{with_mysql}
%if %{with_libmysql}
cat files.mysqli >> files.mysql
cat files.pdo_mysql >> files.mysql
%endif
# mysqlnd
cat files.mysqlnd_mysql \
    files.mysqlnd_mysqli \
    files.pdo_mysqlnd \
    >> files.mysqlnd
%endif
# Split out the PDO modules
%if %{with_mssql}
cat files.pdo_dblib >> files.mssql
%endif
%if %{with_pgsql}
cat files.pdo_pgsql >> files.pgsql
%endif
%if %{with_unixodbc}
cat files.pdo_odbc >> files.odbc
%endif
%if %{with_interbase}
cat files.pdo_firebird >> files.interbase
%endif

# sysv* and posix in packaged in php-process
cat files.sysv* files.posix > files.process

# Package sqlite3 and pdo_sqlite with pdo; isolating the sqlite dependency
# isn't useful at this time since rpm itself requires sqlite.
%if %with_pdo_sqlite3
cat files.pdo_sqlite >> files.pdo
%endif
%if %{with_sqlite3}
cat files.sqlite3 >> files.pdo
%endif

# Package json, zip, curl, phar and fileinfo in -common.
cat files.json files.curl files.phar files.fileinfo > files.common
%if %{with_zip}
cat files.zip >> files.common
%endif

# Install the macros file:
%if %{build_rpm_macros}
install -d $RPM_BUILD_ROOT%{_root_sysconfdir}/rpm
sed -e "s/@PHP_APIVER@/%{apiver}%{isasuffix}/" \
    -e "s/@PHP_ZENDVER@/%{zendver}%{isasuffix}/" \
    -e "s/@PHP_PDOVER@/%{pdover}%{isasuffix}/" \
    -e "s/@PHP_VERSION@/%{version}/" \
%if ! %{with_zts}
    -e "/zts/d" \
%endif
    < %{SOURCE3} > macros.php
install -m 644 -c macros.php \
           $RPM_BUILD_ROOT%{_root_sysconfdir}/rpm/macros.php
%endif
# Remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_libdir}/php/modules/*.a \
       $RPM_BUILD_ROOT%{_libdir}/php-zts/modules/*.a \
       $RPM_BUILD_ROOT%{_bindir}/{phptar} \
       $RPM_BUILD_ROOT%{_datadir}/pear \
       $RPM_BUILD_ROOT%{_libdir}/libphp5.la

# Remove irrelevant docs
rm -f README.{Zeus,QNX,CVS-RULES}
mkdir -p $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT/usr/bin
for file in php php-cgi php-config phpize
do
   ln -s ../php/%{major_version}/bin/$file .
done
popd
%if %{with_mediator_in_directory_usr_php_bin}
pushd $RPM_BUILD_ROOT/usr/php
for directory in bin include lib man modules
do
   ln -s ./%{major_version}/$directory .
done
popd
%endif
mkdir -p "${RPM_BUILD_ROOT}/lib/svc/method"
cp "%{SOURCE200}" "${RPM_BUILD_ROOT}/lib/svc/method/php54-fpm"
mkdir -p "${RPM_BUILD_ROOT}%{svcdir}"
cp "%{SOURCE201}" "${RPM_BUILD_ROOT}%{svcdir}/php54-fpm.xml"

%clean
%if %{skip_prep}
 cd php-%{version}
%endif
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%if %{skip_build}
%else
/bin/rm -rf files.* macros.*
%endif

#%if %{with_fpm}
#%pre fpm
## Add the "apache" user (to avoid pulling httpd in our dep)
#getent group  apache >/dev/null || \
#  groupadd -g 48 -r apache
#getent passwd apache >/dev/null || \
#  useradd -r -u 48 -g apache -s /sbin/nologin \
#    -d %{_httpd_contentdir} -c "Apache" apache
#exit 0

#%post fpm
#%if 0%{?systemd_post:1}
#TODO: %systemd_post %{?scl_prefix}php-fpm.service
#%else
#if [ $1 = 1 ]; then
#    # Initial installation
#%if %{with_systemd}
#TODO:    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
#%else
#TODO:    /sbin/chkconfig --add %{?scl_prefix}php-fpm
#%endif
#fi
#%endif

#%preun fpm
#%if 0%{?systemd_preun:1}
#%systemd_preun %{?scl_prefix}php-fpm.service
#%else
#if [ $1 = 0 ]; then
#    # Package removal, not upgrade
#%if %{with_systemd}
#    /bin/systemctl --no-reload disable %{?scl_prefix}php-fpm.service >/dev/null 2>&1 || :
#    /bin/systemctl stop %{?scl_prefix}php-fpm.service >/dev/null 2>&1 || :
#%else
#    /sbin/service %{?scl_prefix}php-fpm stop >/dev/null 2>&1
#    /sbin/chkconfig --del %{?scl_prefix}php-fpm
#%endif
#fi
#%endif

#%postun fpm
#%if 0%{?systemd_postun_with_restart:1}
#%systemd_postun_with_restart %{?scl_prefix}php-fpm.service
#%else
#%if %{with_systemd}
#/bin/systemctl daemon-reload >/dev/null 2>&1 || :
#if [ $1 -ge 1 ]; then
#    # Package upgrade, not uninstall
#    /bin/systemctl try-restart %{?scl_prefix}php-fpm.service >/dev/null 2>&1 || :
#fi
#%else
#if [ $1 -ge 1 ]; then
#    /sbin/service %{?scl_prefix}php-fpm condrestart >/dev/null 2>&1 || :
#fi
#%endif
#%endif

## Handle upgrading from SysV initscript to native systemd unit.
## We can tell if a SysV version of php-fpm was previously installed by
## checking to see if the initscript is present.
#%triggerun fpm -- %{?scl_prefix}php-fpm
#%if %{with_systemd}
#if [ -f /etc/rc.d/init.d/%{?scl_prefix}php-fpm ]; then
#    # Save the current service runlevel info
#    # User must manually run systemd-sysv-convert --apply php-fpm
#    # to migrate them to systemd targets
#    /usr/bin/systemd-sysv-convert --save %{?scl_prefix}php-fpm >/dev/null 2>&1 || :
#
#    # Run these because the SysV package being removed won't do them
#    /sbin/chkconfig --del %{?scl_prefix}php-fpm >/dev/null 2>&1 || :
#    /bin/systemctl try-restart %{?scl_prefix}php-fpm.service >/dev/null 2>&1 || :
#fi
#%endif
#%endif

#%if %{with_embed}
#%post embedded -p /sbin/ldconfig
#%postun embedded -p /sbin/ldconfig
#%endif

%if %{skip_prep}
%define name php
%endif

%files
%defattr(-,root,bin)
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) %{_httpd_moddir}/libphp5.so
%if %{with_zts}
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) %{_httpd_moddir}/libphp5-zts.so
%endif
#%if 0%{?scl:1}
#%dir %{_libdir}/httpd
#%dir %{_libdir}/httpd/modules
#%{_root_httpd_moddir}/libphp5.so
#%if %{with_zts}
#%{_root_httpd_moddir}/libphp5-zts.so
#%endif
#%endif
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, other) %{_localstatedir}/lib
%attr (0770,root,webservd) %dir %{_localstatedir}/lib/php/session
%config(noreplace) %{_httpd_confdir}/php54-32.load
%ips_tag (mediator=php mediator-version=%{major_version}) %{_httpd_confdir}/php-32.load
#%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
#%config(noreplace) %{_httpd_modconfdir}/10-php.conf
#%endif
#%{_httpd_contentdir}/icons/php.gif
%if %{with_mediator_in_directory_usr_php_bin}
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/bin
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/include
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/lib
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/man
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/modules
%endif

%files common -f files.common
%defattr(-,root,bin)
%doc CODING_STANDARDS CREDITS EXTENSIONS LICENSE NEWS README*
%doc Zend/ZEND_* TSRM_LICENSE regex_COPYRIGHT
%doc libmagic_LICENSE
%doc phar_LICENSE
%doc php.ini-*
%config(noreplace) %{_sysconfdir}/php.ini
%dir %{_sysconfdir}/php.d
%dir %attr(0755, root, bin) %{_libdir}/php
%dir %attr(0755, root, bin) %{_libdir}/php/modules
%if %{with_zts}
%dir %{_sysconfdir}/php-zts.d
%dir %{_libdir}/php-zts
%dir %{_libdir}/php-zts/modules
%endif
%dir %{_localstatedir}/lib/php
%dir %{_datadir}/php
%{_prefix}/apache2

%files cli
%defattr(-,root,bin)
%{_bindir}/php
%{_bindir}/php-cgi
%{_bindir}/phar.phar
%{_bindir}/phar
# provides phpize here (not in -devel) for pecl command
%{_bindir}/phpize
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php-cgi
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/phpize
%{_mandir}/man1/php.1*
%{_mandir}/man1/php-cgi.1*
%{_mandir}/man1/phar.1*
%{_mandir}/man1/phar.phar.1*
%{_mandir}/man1/phpize.1*
%doc sapi/cgi/README* sapi/cli/README
#{?scl: %{_root_bindir}/%{?scl_prefix}php}
#{?scl: %{_root_bindir}/%{?scl_prefix}phar}

%if %{with_fpm}
%files fpm
%defattr(-,root,bin)
%doc php-fpm.conf.default
%doc fpm_LICENSE
%config(noreplace) %{_sysconfdir}/php-fpm.conf
%config(noreplace) %{_sysconfdir}/php-fpm.d/www.conf
#%config(noreplace) %{_root_sysconfdir}/logrotate.d/%{?scl_prefix}php-fpm
%config(noreplace) %{_sysconfdir}/sysconfig/php-fpm
# %{_prefix}/lib/tmpfiles.d/php-fpm.conf
#%if %{with_systemd}
#TODO: %{_unitdir}/%{?scl_prefix}php-fpm.service
#%else
#%{_root_initddir}/%{?scl_prefix}php-fpm
#%endif
%{_sbindir}/php-fpm
%dir %{_sysconfdir}/php-fpm.d
# log owned by apache for log
%dir %attr(0755, root, sys) %{_localstatedir}
%dir %attr(0755, root, sys) %{_localstatedir}/log
%attr(770,root,webservd) %dir %{_localstatedir}/log/php-fpm
%dir %attr(0755, root, sys) %{_localstatedir}/run
%dir %attr(0755, root, root) %{_localstatedir}/run/php-fpm
%{_mandir}/man8/php-fpm.8*
%dir %{_datadir}/fpm
%{_datadir}/fpm/status.html
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/site
%class(manifest) %attr (0444, root, sys) %{_localstatedir}/svc/manifest/site/php54-fpm.xml
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/php54-fpm
%endif

%files devel
%defattr(-,root,bin)
%{_bindir}/php-config
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php-config
%{_includedir}/php
%{_libdir}/php/build
%if %{with_zts}
%{_bindir}/zts-php-config
%{_includedir}/php-zts
%{_bindir}/zts-phpize
# usefull only to test other module during build
%{_bindir}/zts-php
%{_libdir}/php-zts/build
%endif
%{_mandir}/man1/php-config.1*
%if %{build_rpm_macros}
%{_root_sysconfdir}/rpm/macros.php
%endif

%if %{with_embed}
%files embedded
%defattr(-,root,bin,-)
%ips_tag (mediator=php mediator-version=%{major_version}) %{_libdir}/libphp5.so
%{_libdir}/libphp5-%{major_version}.so
%endif

%if %{with_pgsql}
%files pgsql -f files.pgsql
%endif
%if %{with_mysql}
%if %{with_libmysql}
%files mysql -f files.mysql
%endif
%endif
%if %{with_unixodbc}
%files odbc -f files.odbc
%endif
%if %{with_imap}
%files imap -f files.imap
%endif
%files ldap -f files.ldap
%files snmp -f files.snmp
%files xml -f files.xml
%files xmlrpc -f files.xmlrpc
%files mbstring -f files.mbstring
%doc libmbfl_LICENSE
%doc oniguruma_COPYING
%doc ucgendat_LICENSE
%files gd -f files.gd
%doc libgd_README
%doc libgd_COPYING
%files soap -f files.soap
%files bcmath -f files.bcmath
%doc libbcmath_COPYING
%files dba -f files.dba
%files pdo -f files.pdo
%if %{with_mcrypt}
%files mcrypt -f files.mcrypt
%endif
%if %{with_tidy}
%files tidy -f files.tidy
%endif
%if %{with_mssql}
%files mssql -f files.mssql
%endif
%if %{with_pspell}
%files pspell -f files.pspell
%endif
%files intl -f files.intl
%files process -f files.process
%if %{with_recode}
%files recode -f files.recode
%endif
%if %{with_interbase}
%files interbase -f files.interbase
%endif
%if %{with_enchant}
%files enchant -f files.enchant
%endif
%if %{with_mysql}
%files mysqlnd -f files.mysqlnd
%endif

%changelog
* Thr Jun 12 2014 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.4.29
- Ready for postgres

* Tue June 10 2014 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.4.29
- Bump up to 5.4.29
- Fixed problem:
  Warning: Linking the shared library libphp5.la against the non-libtool
- postgres still not supported
- Fix mediator for coexistence under php 5.3

* Thr May 29 2014 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.4.16
- ready for OI (151a9)
- enable dtrace
  but remaining problem:
  Warning: Linking the shared library libphp5.la against the non-libtool
  TODO: It was already fixed. Should compile over version 5.4.22.
  see http://git.php.net/?p=php-src.git;a=commitdiff;h=0ebef462ceb50094e64a8d48bf705594175f86ab
- add manifest for fpm
- ready for Sunstudio and gcc
- postgres still not supported

* Mon Aug 19 2013 Remi Collet <rcollet@redhat.com> - 5.4.16-7
- fix enchant package summary and description
- add security fix for CVE-2013-4248

* Tue Jul 18 2013 Remi Collet <rcollet@redhat.com> 5.4.16-4
- improve mod_php, pgsql and ldap description
- add missing man pages (phar, php-cgi)
- add provides php(pdo-abi) for consistency with php(api) and php(zend-abi)
- use %%__isa_bits instead of %%__isa in ABI suffix #985350

* Fri Jul 12 2013 Remi Collet <rcollet@redhat.com> - 5.4.16-3
- add security fix for CVE-2013-4113
- add missing ASL 1.0 license

* Fri Jun  7 2013 Remi Collet <rcollet@redhat.com> 5.4.16-2
- run tests during build

* Fri Jun  7 2013 Remi Collet <rcollet@redhat.com> 5.4.16-1
- rebase to 5.4.16
- fix hang in FindTishriMolad(), #965144
- patch for upstream Bug #64915 error_log ignored when daemonize=0
- patch for upstream Bug #64949 Buffer overflow in _pdo_pgsql_error, #969103
- patch for upstream bug #64960 Segfault in gc_zval_possible_root

* Thu May 23 2013 Remi Collet <rcollet@redhat.com> 5.4.14-3
- remove wrappers in /usr/bin (#966407)

* Thu Apr 25 2013 Remi Collet <rcollet@redhat.com> 5.4.14-2
- rebuild for libjpeg (instead of libjpeg_turbo)
- fix unowned dir %%{_datadir}/fpm and %%{_libdir}/httpd (#956221)

* Thu Apr 11 2013 Remi Collet <rcollet@redhat.com> 5.4.14-1
- update to 5.4.14
- clean old deprecated options

* Wed Mar 13 2013 Remi Collet <rcollet@redhat.com> 5.4.13-1
- update to 5.4.13
- security fixes for CVE-2013-1635 and CVE-2013-1643
- make php-mysql package optional (and disabled)
- make ZTS build optional (and disabled)
- always try to load mod_php (apache warning is usefull)
- Hardened build (links with -z now option)
- Remove %%config from /etc/rpm/macros.php

* Wed Jan 16 2013 Remi Collet <rcollet@redhat.com> 5.4.11-1
- update to 5.4.11
- fix php.conf to allow MultiViews managed by php scripts

* Wed Dec 19 2012 Remi Collet <rcollet@redhat.com> 5.4.10-1
- update to 5.4.10
- remove patches merged upstream
- drop "Configure Command" from phpinfo output
- prevent php_config.h changes across (otherwise identical)
  rebuilds


* Thu Nov 22 2012 Remi Collet <rcollet@redhat.com> 5.4.9-1
- update to 5.4.9

* Mon Nov 19 2012 Remi Collet <rcollet@redhat.com> 5.4.8-7
- fix php.conf

* Mon Nov 19 2012 Remi Collet <rcollet@redhat.com> 5.4.8-6
- filter private shared in _httpd_modir
- improve system libzip patch to use pkg-config
- use _httpd_contentdir macro and fix php.gif path
- switch back to upstream generated scanner/parser
- use system pcre only when recent enough

* Fri Nov 16 2012 Remi Collet <rcollet@redhat.com> 5.4.8-5
- improves php.conf, no need to be relocated

* Fri Nov  9 2012 Remi Collet <rcollet@redhat.com> 5.4.8-6
- clarify Licenses
- missing provides xmlreader and xmlwriter
- change php embedded library soname version to 5.4

* Mon Nov  5 2012 Remi Collet <rcollet@redhat.com> 5.4.8-4
- fix mysql_sock macro definition

* Thu Oct 25 2012 Remi Collet <rcollet@redhat.com> 5.4.8-4
- fix standard build (non scl)

* Thu Oct 25 2012 Remi Collet <rcollet@redhat.com> 5.4.8-3
- fix installed headers

* Tue Oct 23 2012 Joe Orton <jorton@redhat.com> - 5.4.8-2
- use libldap_r for ldap extension

* Tue Oct 23 2012 Remi Collet <rcollet@redhat.com> 5.4.8-3
- add missing scl_prefix in some provides/requires

* Tue Oct 23 2012 Remi Collet <rcollet@redhat.com> 5.4.8-2.1
- make php-enchant optionnal, not available on RHEL-5
- make php-recode optionnal, not available on RHEL-5
- disable t1lib on RHEL-5

* Tue Oct 23 2012 Remi Collet <rcollet@redhat.com> 5.4.8-2
- enable tidy on RHEL-6 only
- re-enable unit tests

* Tue Oct 23 2012 Remi Collet <rcollet@redhat.com> 5.4.8-1.2
- minor macro fixes for RHEL-5 build
- update autotools workaround for RHEL-5
- use readline when libedit not available (RHEL-5)

* Mon Oct 22 2012 Remi Collet <rcollet@redhat.com> 5.4.8-1
- update to 5.4.8
- define both session.save_handler and session.save_path
- fix possible segfault in libxml (#828526)
- use SKIP_ONLINE_TEST during make test
- php-devel requires pcre-devel and php-cli (instead of php)
- provides php-phar
- update systzdata patch to v10, timezone are case insensitive

* Mon Oct 15 2012 Remi Collet <rcollet@redhat.com> 5.4.7-4
- php-fpm: create apache user if needed
- php-cli: provides cli command in standard root (scl)

* Fri Oct 12 2012 Remi Collet <rcollet@redhat.com> 5.4.7-3
- add configtest option to init script
- test configuration before service reload
- fix php-fpm service relocation
- fix php-fpm config relocation
- drop embdded subpackage for scl

* Wed Oct  3 2012 Remi Collet <rcollet@redhat.com> 5.4.7-2
- missing requires on scl-runtime
- relocate /var/lib/session
- fix php-devel requires
- rename, but don't relocate macros.php

* Tue Oct  2 2012 Remi Collet <rcollet@redhat.com> 5.4.7-1
- initial spec rewrite for scl build

* Mon Oct  1 2012 Remi Collet <remi@fedoraproject.org> 5.4.7-10
- fix typo in systemd macro

* Mon Oct  1 2012 Remi Collet <remi@fedoraproject.org> 5.4.7-9
- php-fpm: enable PrivateTmp
- php-fpm: new systemd macros (#850268)
- php-fpm: add upstream patch for startup issue (#846858)

* Fri Sep 28 2012 Remi Collet <rcollet@redhat.com> 5.4.7-8
- systemd integration, https://bugs.php.net/63085
- no odbc call during timeout, https://bugs.php.net/63171
- check sqlite3_column_table_name, https://bugs.php.net/63149

* Mon Sep 24 2012 Remi Collet <rcollet@redhat.com> 5.4.7-7
- most failed tests explained (i386, x86_64)

* Wed Sep 19 2012 Remi Collet <rcollet@redhat.com> 5.4.7-6
- fix for http://bugs.php.net/63126 (#783967)

* Wed Sep 19 2012 Remi Collet <rcollet@redhat.com> 5.4.7-5
- patch to ensure we use latest libdb (not libdb4)

* Wed Sep 19 2012 Remi Collet <rcollet@redhat.com> 5.4.7-4
- really fix rhel tests (use libzip and libdb)

* Tue Sep 18 2012 Remi Collet <rcollet@redhat.com> 5.4.7-3
- fix test to enable zip extension on RHEL-7

* Mon Sep 17 2012 Remi Collet <remi@fedoraproject.org> 5.4.7-2
- remove session.save_path from php.ini
  move it to apache and php-fpm configuration files

* Fri Sep 14 2012 Remi Collet <remi@fedoraproject.org> 5.4.7-1
- update to 5.4.7
  http://www.php.net/releases/5_4_7.php
- php-fpm: don't daemonize

* Mon Aug 20 2012 Remi Collet <remi@fedoraproject.org> 5.4.6-2
- enable php-fpm on secondary arch (#849490)

* Fri Aug 17 2012 Remi Collet <remi@fedoraproject.org> 5.4.6-1
- update to 5.4.6
- update to v9 of systzdata patch
- backport fix for new libxml

* Fri Jul 20 2012 Remi Collet <remi@fedoraproject.org> 5.4.5-1
- update to 5.4.5

* Mon Jul 02 2012 Remi Collet <remi@fedoraproject.org> 5.4.4-4
- also provide php(language)%%{_isa}
- define %%{php_version}

* Mon Jul 02 2012 Remi Collet <remi@fedoraproject.org> 5.4.4-3
- drop BR for libevent (#835671)
- provide php(language) to allow version check

* Thu Jun 21 2012 Remi Collet <remi@fedoraproject.org> 5.4.4-2
- add missing provides (core, ereg, filter, standard)

* Thu Jun 14 2012 Remi Collet <remi@fedoraproject.org> 5.4.4-1
- update to 5.4.4 (CVE-2012-2143, CVE-2012-2386)
- use /usr/lib/tmpfiles.d instead of /etc/tmpfiles.d
- use /run/php-fpm instead of /var/run/php-fpm

* Wed May 09 2012 Remi Collet <remi@fedoraproject.org> 5.4.3-1
- update to 5.4.3 (CVE-2012-2311, CVE-2012-2329)

* Thu May 03 2012 Remi Collet <remi@fedoraproject.org> 5.4.2-1
- update to 5.4.2 (CVE-2012-1823)

* Fri Apr 27 2012 Remi Collet <remi@fedoraproject.org> 5.4.1-1
- update to 5.4.1

* Wed Apr 25 2012 Joe Orton <jorton@redhat.com> - 5.4.0-6
- rebuild for new icu
- switch (conditionally) to libdb-devel

* Sat Mar 31 2012 Remi Collet <remi@fedoraproject.org> 5.4.0-5
- fix Loadmodule with MPM event (use ZTS if not MPM worker)
- split conf.d/php.conf + conf.modules.d/10-php.conf with httpd 2.4

* Thu Mar 29 2012 Joe Orton <jorton@redhat.com> - 5.4.0-4
- rebuild for missing automatic provides (#807889)

* Mon Mar 26 2012 Joe Orton <jorton@redhat.com> - 5.4.0-3
- really use _httpd_mmn

* Mon Mar 26 2012 Joe Orton <jorton@redhat.com> - 5.4.0-2
- rebuild against httpd 2.4
- use _httpd_mmn, _httpd_apxs macros

* Fri Mar 02 2012 Remi Collet <remi@fedoraproject.org> 5.4.0-1
- update to PHP 5.4.0 finale

* Sat Feb 18 2012 Remi Collet <remi@fedoraproject.org> 5.4.0-0.4.RC8
- update to PHP 5.4.0RC8

* Sat Feb 04 2012 Remi Collet <remi@fedoraproject.org> 5.4.0-0.3.RC7
- update to PHP 5.4.0RC7
- provides env file for php-fpm (#784770)
- add patch to use system libzip (thanks to spot)
- don't provide INSTALL file

* Wed Jan 25 2012 Remi Collet <remi@fedoraproject.org> 5.4.0-0.2.RC6
- all binaries in /usr/bin with zts prefix

* Wed Jan 18 2012 Remi Collet <remi@fedoraproject.org> 5.4.0-0.1.RC6
- update to PHP 5.4.0RC6
  https://fedoraproject.org/wiki/Features/Php54

* Sun Jan 08 2012 Remi Collet <remi@fedoraproject.org> 5.3.8-4.4
- fix systemd unit

* Mon Dec 12 2011 Remi Collet <remi@fedoraproject.org> 5.3.8-4.3
- switch to systemd

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 5.3.8-4.2
- Rebuild for new libpng

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.3.8-3.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 5.3.8-3.1
- rebuild with new gmp

* Wed Sep 28 2011 Remi Collet <remi@fedoraproject.org> 5.3.8-3
- revert is_a() to php <= 5.3.6 behavior (from upstream)
  with new option (allow_string) for new behavior

* Tue Sep 13 2011 Remi Collet <remi@fedoraproject.org> 5.3.8-2
- add mysqlnd sub-package
- drop patch4, use --libdir to use /usr/lib*/php/build
- add patch to redirect mysql.sock (in mysqlnd)

* Tue Aug 23 2011 Remi Collet <remi@fedoraproject.org> 5.3.8-1
- update to 5.3.8
  http://www.php.net/ChangeLog-5.php#5.3.8

* Thu Aug 18 2011 Remi Collet <remi@fedoraproject.org> 5.3.7-1
- update to 5.3.7
  http://www.php.net/ChangeLog-5.php#5.3.7
- merge php-zts into php (#698084)

* Tue Jul 12 2011 Joe Orton <jorton@redhat.com> - 5.3.6-4
- rebuild for net-snmp SONAME bump

* Mon Apr  4 2011 Remi Collet <Fedora@famillecollet.com> 5.3.6-3
- enable mhash extension (emulated by hash extension)

* Wed Mar 23 2011 Remi Collet <Fedora@famillecollet.com> 5.3.6-2
- rebuild for new MySQL client library

* Thu Mar 17 2011 Remi Collet <Fedora@famillecollet.com> 5.3.6-1
- update to 5.3.6
  http://www.php.net/ChangeLog-5.php#5.3.6
- fix php-pdo arch specific requires

* Tue Mar 15 2011 Joe Orton <jorton@redhat.com> - 5.3.5-6
- disable zip extension per "No Bundled Libraries" policy (#551513)

* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> 5.3.5-5
- rebuild for icu 4.6

* Mon Feb 28 2011 Remi Collet <Fedora@famillecollet.com> 5.3.5-4
- fix systemd-units requires

* Thu Feb 24 2011 Remi Collet <Fedora@famillecollet.com> 5.3.5-3
- add tmpfiles.d configuration for php-fpm
- add Arch specific requires/provides

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Remi Collet <Fedora@famillecollet.com> 5.3.5-1
- update to 5.3.5
  http://www.php.net/ChangeLog-5.php#5.3.5
- clean duplicate configure options

* Tue Dec 28 2010 Remi Collet <rpms@famillecollet.com> 5.3.4-2
- rebuild against MySQL 5.5.8
- remove all RPM_SOURCE_DIR

* Sun Dec 12 2010 Remi Collet <rpms@famillecollet.com> 5.3.4-1.1
- security patch from upstream for #660517

* Sat Dec 11 2010 Remi Collet <Fedora@famillecollet.com> 5.3.4-1
- update to 5.3.4
  http://www.php.net/ChangeLog-5.php#5.3.4
- move phpize to php-cli (see #657812)

* Wed Dec  1 2010 Remi Collet <Fedora@famillecollet.com> 5.3.3-5
- ghost /var/run/php-fpm (see #656660)
- add filter_setup to not provides extensions as .so

* Mon Nov  1 2010 Joe Orton <jorton@redhat.com> - 5.3.3-4
- use mysql_config in libdir directly to avoid biarch build failures

* Fri Oct 29 2010 Joe Orton <jorton@redhat.com> - 5.3.3-3
- rebuild for new net-snmp

* Sun Oct 10 2010 Remi Collet <Fedora@famillecollet.com> 5.3.3-2
- add php-fpm sub-package

* Thu Jul 22 2010 Remi Collet <Fedora@famillecollet.com> 5.3.3-1
- PHP 5.3.3 released

* Fri Apr 30 2010 Remi Collet <Fedora@famillecollet.com> 5.3.2-3
- garbage collector upstream  patches (#580236)

* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> 5.3.2-2
- rebuild for icu 4.4

* Sat Mar 06 2010 Remi Collet <Fedora@famillecollet.com> 5.3.2-1
- PHP 5.3.2 Released!
- remove mime_magic option (now provided by fileinfo, by emu)
- add patch for http://bugs.php.net/50578
- remove patch for libedit (upstream)
- add runselftest option to allow build without test suite

* Fri Nov 27 2009 Joe Orton <jorton@redhat.com> - 5.3.1-3
- update to v7 of systzdata patch

* Wed Nov 25 2009 Joe Orton <jorton@redhat.com> - 5.3.1-2
- fix build with autoconf 2.6x

* Fri Nov 20 2009 Remi Collet <Fedora@famillecollet.com> 5.3.1-1
- update to 5.3.1
- remove openssl patch (merged upstream)
- add provides for php-pecl-json
- add prod/devel php.ini in doc

* Tue Nov 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 5.3.0-7
- use libedit instead of readline to resolve licensing issues

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 5.3.0-6
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Joe Orton <jorton@redhat.com> 5.3.0-4
- rediff systzdata patch

* Thu Jul 16 2009 Joe Orton <jorton@redhat.com> 5.3.0-3
- update to v6 of systzdata patch; various fixes

* Tue Jul 14 2009 Joe Orton <jorton@redhat.com> 5.3.0-2
- update to v5 of systzdata patch; parses zone.tab and extracts
  timezone->{country-code,long/lat,comment} mapping table

* Sun Jul 12 2009 Remi Collet <Fedora@famillecollet.com> 5.3.0-1
- update to 5.3.0
- remove ncurses, dbase, mhash extensions
- add enchant, sqlite3, intl, phar, fileinfo extensions
- raise sqlite version to 3.6.0 (for sqlite3, build with --enable-load-extension)
- sync with upstream "production" php.ini

* Sun Jun 21 2009 Remi Collet <Fedora@famillecollet.com> 5.2.10-1
- update to 5.2.10
- add interbase sub-package

* Sat Feb 28 2009 Remi Collet <Fedora@FamilleCollet.com> - 5.2.9-1
- update to 5.2.9

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  5 2009 Joe Orton <jorton@redhat.com> 5.2.8-9
- add recode support, -recode subpackage (#106755)
- add -zts subpackage with ZTS-enabled build of httpd SAPI
- adjust php.conf to use -zts SAPI build for worker MPM

* Wed Feb  4 2009 Joe Orton <jorton@redhat.com> 5.2.8-8
- fix patch fuzz, renumber patches

* Wed Feb  4 2009 Joe Orton <jorton@redhat.com> 5.2.8-7
- drop obsolete configure args
- drop -odbc patch (#483690)

* Mon Jan 26 2009 Joe Orton <jorton@redhat.com> 5.2.8-5
- split out sysvshm, sysvsem, sysvmsg, posix into php-process

* Sun Jan 25 2009 Joe Orton <jorton@redhat.com> 5.2.8-4
- move wddx to php-xml, build curl shared in -common
- remove BR for expat-devel, bogus configure option

* Fri Jan 23 2009 Joe Orton <jorton@redhat.com> 5.2.8-3
- rebuild for new MySQL

* Sat Dec 13 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.8-2
- libtool 2 workaround for phpize (#476004)
- add missing php_embed.h (#457777)

* Tue Dec 09 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.8-1
- update to 5.2.8

* Sat Dec 06 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.7-1.1
- libtool 2 workaround

* Fri Dec 05 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.7-1
- update to 5.2.7
- enable pdo_dblib driver in php-mssql

* Mon Nov 24 2008 Joe Orton <jorton@redhat.com> 5.2.6-7
- tweak Summary, thanks to Richard Hughes

* Tue Nov  4 2008 Joe Orton <jorton@redhat.com> 5.2.6-6
- move gd_README to php-gd
- update to r4 of systzdata patch; introduces a default timezone
  name of "System/Localtime", which uses /etc/localtime (#469532)

* Sat Sep 13 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.6-5
- enable XPM support in php-gd
- Fix BR for php-gd

* Sun Jul 20 2008 Remi Collet <Fedora@FamilleCollet.com> 5.2.6-4
- enable T1lib support in php-gd

* Mon Jul 14 2008 Joe Orton <jorton@redhat.com> 5.2.6-3
- update to 5.2.6
- sync default php.ini with upstream
- drop extension_dir from default php.ini, rely on hard-coded
  default, to make php-common multilib-safe (#455091)
- update to r3 of systzdata patch

* Thu Apr 24 2008 Joe Orton <jorton@redhat.com> 5.2.5-7
- split pspell extension out into php-spell (#443857)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.2.5-6
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Joe Orton <jorton@redhat.com> 5.2.5-5
- ext/date: use system timezone database

* Fri Dec 28 2007 Joe Orton <jorton@redhat.com> 5.2.5-4
- rebuild for libc-client bump

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 5.2.5-3
- Rebuild for openssl bump

* Wed Dec  5 2007 Joe Orton <jorton@redhat.com> 5.2.5-2
- update to 5.2.5

* Mon Oct 15 2007 Joe Orton <jorton@redhat.com> 5.2.4-3
- correct pcre BR version (#333021)
- restore metaphone fix (#205714)
- add READMEs to php-cli

* Sun Sep 16 2007 Joe Orton <jorton@redhat.com> 5.2.4-2
- update to 5.2.4

* Sun Sep  2 2007 Joe Orton <jorton@redhat.com> 5.2.3-9
- rebuild for fixed APR

* Tue Aug 28 2007 Joe Orton <jorton@redhat.com> 5.2.3-8
- add ldconfig post/postun for -embedded (Hans de Goede)

* Fri Aug 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 5.2.3-7
- add php-embedded sub-package

* Fri Aug 10 2007 Joe Orton <jorton@redhat.com> 5.2.3-6
- fix build with new glibc
- fix License

* Mon Jul 16 2007 Joe Orton <jorton@redhat.com> 5.2.3-5
- define php_extdir in macros.php

* Mon Jul  2 2007 Joe Orton <jorton@redhat.com> 5.2.3-4
- obsolete php-dbase

* Tue Jun 19 2007 Joe Orton <jorton@redhat.com> 5.2.3-3
- add mcrypt, mhash, tidy, mssql subpackages (Dmitry Butskoy)
- enable dbase extension and package in -common

* Fri Jun  8 2007 Joe Orton <jorton@redhat.com> 5.2.3-2
- update to 5.2.3 (thanks to Jeff Sheltren)

* Wed May  9 2007 Joe Orton <jorton@redhat.com> 5.2.2-4
- fix php-pdo *_arg_force_ref global symbol abuse (#216125)

* Tue May  8 2007 Joe Orton <jorton@redhat.com> 5.2.2-3
- rebuild against uw-imap-devel

* Fri May  4 2007 Joe Orton <jorton@redhat.com> 5.2.2-2
- update to 5.2.2
- synch changes from upstream recommended php.ini

* Thu Mar 29 2007 Joe Orton <jorton@redhat.com> 5.2.1-5
- enable SASL support in LDAP extension (#205772)

* Wed Mar 21 2007 Joe Orton <jorton@redhat.com> 5.2.1-4
- drop mime_magic extension (deprecated by php-pecl-Fileinfo)

* Mon Feb 19 2007 Joe Orton <jorton@redhat.com> 5.2.1-3
- fix regression in str_{i,}replace (from upstream)

* Thu Feb 15 2007 Joe Orton <jorton@redhat.com> 5.2.1-2
- update to 5.2.1
- add Requires(pre) for httpd
- trim %%changelog to versions >= 5.0.0

* Thu Feb  8 2007 Joe Orton <jorton@redhat.com> 5.2.0-10
- bump default memory_limit to 32M (#220821)
- mark config files noreplace again (#174251)
- drop trailing dots from Summary fields
- use standard BuildRoot
- drop libtool15 patch (#226294)

* Tue Jan 30 2007 Joe Orton <jorton@redhat.com> 5.2.0-9
- add php(api), php(zend-abi) provides (#221302)
- package /usr/share/php and append to default include_path (#225434)

* Tue Dec  5 2006 Joe Orton <jorton@redhat.com> 5.2.0-8
- fix filter.h installation path
- fix php-zend-abi version (Remi Collet, #212804)

* Tue Nov 28 2006 Joe Orton <jorton@redhat.com> 5.2.0-7
- rebuild again

* Tue Nov 28 2006 Joe Orton <jorton@redhat.com> 5.2.0-6
- rebuild for net-snmp soname bump

* Mon Nov 27 2006 Joe Orton <jorton@redhat.com> 5.2.0-5
- build json and zip shared, in -common (Remi Collet, #215966)
- obsolete php-json and php-pecl-zip
- build readline extension into /usr/bin/php* (#210585)
- change module subpackages to require php-common not php (#177821)

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 5.2.0-4
- provide php-zend-abi (#212804)
- add /etc/rpm/macros.php exporting interface versions
- synch with upstream recommended php.ini

* Wed Nov 15 2006 Joe Orton <jorton@redhat.com> 5.2.0-3
- update to 5.2.0 (#213837)
- php-xml provides php-domxml (#215656)
- fix php-pdo-abi provide (#214281)

* Tue Oct 31 2006 Joseph Orton <jorton@redhat.com> 5.1.6-4
- rebuild for curl soname bump
- add build fix for curl 7.16 API

* Wed Oct  4 2006 Joe Orton <jorton@redhat.com> 5.1.6-3
- from upstream: add safety checks against integer overflow in _ecalloc

* Tue Aug 29 2006 Joe Orton <jorton@redhat.com> 5.1.6-2
- update to 5.1.6 (security fixes)
- bump default memory_limit to 16M (#196802)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 5.1.4-8.1
- rebuild

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-8
- Provide php-posix (#194583)
- only provide php-pcntl from -cli subpackage
- add missing defattr's (thanks to Matthias Saou)

* Fri Jun  9 2006 Joe Orton <jorton@redhat.com> 5.1.4-7
- move Obsoletes for php-openssl to -common (#194501)
- Provide: php-cgi from -cli subpackage

* Fri Jun  2 2006 Joe Orton <jorton@redhat.com> 5.1.4-6
- split out php-cli, php-common subpackages (#177821)
- add php-pdo-abi version export (#193202)

* Wed May 24 2006 Radek Vokal <rvokal@redhat.com> 5.1.4-5.1
- rebuilt for new libnetsnmp

* Thu May 18 2006 Joe Orton <jorton@redhat.com> 5.1.4-5
- provide mod_php (#187891)
- provide php-cli (#192196)
- use correct LDAP fix (#181518)
- define _GNU_SOURCE in php_config.h and leave it defined
- drop (circular) dependency on php-pear

* Mon May  8 2006 Joe Orton <jorton@redhat.com> 5.1.4-3
- update to 5.1.4

* Wed May  3 2006 Joe Orton <jorton@redhat.com> 5.1.3-3
- update to 5.1.3

* Tue Feb 28 2006 Joe Orton <jorton@redhat.com> 5.1.2-5
- provide php-api (#183227)
- add provides for all builtin modules (Tim Jackson, #173804)
- own %%{_libdir}/php/pear for PEAR packages (per #176733)
- add obsoletes to allow upgrade from FE4 PDO packages (#181863)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.3
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 5.1.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 5.1.2-4
- rebuild for new libc-client soname

* Mon Jan 16 2006 Joe Orton <jorton@redhat.com> 5.1.2-3
- only build xmlreader and xmlwriter shared (#177810)

* Fri Jan 13 2006 Joe Orton <jorton@redhat.com> 5.1.2-2
- update to 5.1.2

* Thu Jan  5 2006 Joe Orton <jorton@redhat.com> 5.1.1-8
- rebuild again

* Mon Jan  2 2006 Joe Orton <jorton@redhat.com> 5.1.1-7
- rebuild for new net-snmp

* Mon Dec 12 2005 Joe Orton <jorton@redhat.com> 5.1.1-6
- enable short_open_tag in default php.ini again (#175381)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  8 2005 Joe Orton <jorton@redhat.com> 5.1.1-5
- require net-snmp for php-snmp (#174800)

* Sun Dec  4 2005 Joe Orton <jorton@redhat.com> 5.1.1-4
- add /usr/share/pear back to hard-coded include_path (#174885)

* Fri Dec  2 2005 Joe Orton <jorton@redhat.com> 5.1.1-3
- rebuild for httpd 2.2

* Mon Nov 28 2005 Joe Orton <jorton@redhat.com> 5.1.1-2
- update to 5.1.1
- remove pear subpackage
- enable pdo extensions (php-pdo subpackage)
- remove non-standard conditional module builds
- enable xmlreader extension

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> 5.0.5-6
- rebuilt against new openssl

* Mon Nov  7 2005 Joe Orton <jorton@redhat.com> 5.0.5-5
- pear: update to XML_RPC 1.4.4, XML_Parser 1.2.7, Mail 1.1.9 (#172528)

* Tue Nov  1 2005 Joe Orton <jorton@redhat.com> 5.0.5-4
- rebuild for new libnetsnmp

* Wed Sep 14 2005 Joe Orton <jorton@redhat.com> 5.0.5-3
- update to 5.0.5
- add fix for upstream #34435
- devel: require autoconf, automake (#159283)
- pear: update to HTTP-1.3.6, Mail-1.1.8, Net_SMTP-1.2.7, XML_RPC-1.4.1
- fix imagettftext et al (upstream, #161001)

* Thu Jun 16 2005 Joe Orton <jorton@redhat.com> 5.0.4-11
- ldap: restore ldap_start_tls() function

* Fri May  6 2005 Joe Orton <jorton@redhat.com> 5.0.4-10
- disable RPATHs in shared extensions (#156974)

* Tue May  3 2005 Joe Orton <jorton@redhat.com> 5.0.4-9
- build simplexml_import_dom even with shared dom (#156434)
- prevent truncation of copied files to ~2Mb (#155916)
- install /usr/bin/php from CLI build alongside CGI
- enable sysvmsg extension (#142988)

* Mon Apr 25 2005 Joe Orton <jorton@redhat.com> 5.0.4-8
- prevent build of builtin dba as well as shared extension

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-7
- split out dba and bcmath extensions into subpackages
- BuildRequire gcc-c++ to avoid AC_PROG_CXX{,CPP} failure (#155221)
- pear: update to DB-1.7.6
- enable FastCGI support in /usr/bin/php-cgi (#149596)

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-6
- build /usr/bin/php with the CLI SAPI, and add /usr/bin/php-cgi,
  built with the CGI SAPI (thanks to Edward Rudd, #137704)
- add php(1) man page for CLI
- fix more test cases to use -n when invoking php

* Wed Apr 13 2005 Joe Orton <jorton@redhat.com> 5.0.4-5
- rebuild for new libpq soname

* Tue Apr 12 2005 Joe Orton <jorton@redhat.com> 5.0.4-4
- bundle from PEAR: HTTP, Mail, XML_Parser, Net_Socket, Net_SMTP
- snmp: disable MSHUTDOWN function to prevent error_log noise (#153988)
- mysqli: add fix for crash on x86_64 (Georg Richter, upstream #32282)

* Mon Apr 11 2005 Joe Orton <jorton@redhat.com> 5.0.4-3
- build shared objects as PIC (#154195)

* Mon Apr  4 2005 Joe Orton <jorton@redhat.com> 5.0.4-2
- fix PEAR installation and bundle PEAR DB-1.7.5 package

* Fri Apr  1 2005 Joe Orton <jorton@redhat.com> 5.0.4-1
- update to 5.0.4 (#153068)
- add .phps AddType to php.conf (#152973)
- better gcc4 fix for libxmlrpc

* Wed Mar 30 2005 Joe Orton <jorton@redhat.com> 5.0.3-5
- BuildRequire mysql-devel >= 4.1
- don't mark php.ini as noreplace to make upgrades work (#152171)
- fix subpackage descriptions (#152628)
- fix memset(,,0) in Zend (thanks to Dave Jones)
- fix various compiler warnings in Zend

* Thu Mar 24 2005 Joe Orton <jorton@redhat.com> 5.0.3-4
- package mysqli extension in php-mysql
- really enable pcntl (#142903)
- don't build with --enable-safe-mode (#148969)
- use "Instant Client" libraries for oci8 module (Kai Bolay, #149873)

* Fri Feb 18 2005 Joe Orton <jorton@redhat.com> 5.0.3-3
- fix build with GCC 4

* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 5.0.3-2
- install the ext/gd headers (#145891)
- enable pcntl extension in /usr/bin/php (#142903)
- add libmbfl array arithmetic fix (dcb314@hotmail.com, #143795)
- add BuildRequire for recent pcre-devel (#147448)

* Wed Jan 12 2005 Joe Orton <jorton@redhat.com> 5.0.3-1
- update to 5.0.3 (thanks to Robert Scheck et al, #143101)
- enable xsl extension (#142174)
- package both the xsl and dom extensions in php-xml
- enable soap extension, shared (php-soap package) (#142901)
- add patches from upstream 5.0 branch:
 * Zend_strtod.c compile fixes
 * correct php_sprintf return value usage

* Mon Nov 22 2004 Joe Orton <jorton@redhat.com> 5.0.2-8
- update for db4-4.3 (Robert Scheck, #140167)
- build against mysql-devel
- run tests in %%check

* Wed Nov 10 2004 Joe Orton <jorton@redhat.com> 5.0.2-7
- truncate changelog at 4.3.1-1
- merge from 4.3.x package:
 - enable mime_magic extension and Require: file (#130276)

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-6
- fix dom/sqlite enable/without confusion

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-5
- fix phpize installation for lib64 platforms
- add fix for segfault in variable parsing introduced in 5.0.2

* Mon Nov  8 2004 Joe Orton <jorton@redhat.com> 5.0.2-4
- update to 5.0.2 (#127980)
- build against mysqlclient10-devel
- use new RTLD_DEEPBIND to load extension modules
- drop explicit requirement for elfutils-devel
- use AddHandler in default conf.d/php.conf (#135664)
- "fix" round() fudging for recent gcc on x86
- disable sqlite pending audit of warnings and subpackage split

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-4
- don't build dom extension into 2.0 SAPI

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-3
- ExclusiveArch: x86 ppc x86_64 for the moment

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 5.0.1-2
- fix default extension_dir and conf.d/php.conf

* Thu Sep  9 2004 Joe Orton <jorton@redhat.com> 5.0.1-1
- update to 5.0.1
- only build shared modules once
- put dom extension in php-dom subpackage again
- move extension modules into %%{_libdir}/php/modules
- don't use --with-regex=system, it's ignored for the apache* SAPIs

* Wed Aug 11 2004 Tom Callaway <tcallawa@redhat.com>
- Merge in some spec file changes from Jeff Stern (jastern@uci.edu)

* Mon Aug 09 2004 Tom Callaway <tcallawa@redhat.com>
- bump to 5.0.0
- add patch to prevent clobbering struct re_registers from regex.h
- remove domxml references, replaced with dom now built-in
- fix php.ini to refer to php5 not php4
