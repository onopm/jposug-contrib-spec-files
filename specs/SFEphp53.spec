#
# spec file for package SFEphp-53
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 0
%define _gpp g++
%include base.inc

%define with_cclient 1
%define with_pgsql 0
%define with_mysql 1
%define with_unixodbc 1
%define with_pspell 0
%define with_recode 0
%define with_libedit 0
%define with_mediator_in_directory_usr_php_bin 0
%define build_cgi 1
%define build_apache 1
%define build_embedded 1
%define build_zts 1
%define build_rpm_macros 0
%define skip_prep 0
%define skip_build 0
%define skip_check 1

%define contentdir  /var/apache2/2.2/htdocs
# API/ABI check
%define apiver      20090626
%define zendver     20090626
%define pdover      20080721
# Extension version
%define fileinfover 1.0.5-dev
%define pharver     2.0.1
%define zipver      1.11.0
%define jsonver     1.2.1

#%define httpd_mmn %(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)
#/usr/apache2/2.2/include/ap_mmn.h:#define MODULE_MAGIC_NUMBER_MAJOR 20051115
%define httpd_mmn %(grep '#define MODULE_MAGIC_NUMBER_MAJOR' /usr/apache2/2.2/include/ap_mmn.h | awk '{print $3}' || echo missing-httpd-devel)

# Use the arch-specific mysql_config binary to avoid mismatch with the
# arch detection heuristic used by bindir/mysql_config.
#%define mysql_config %{_libdir}/mysql/mysql_config
%if %{with_mysql}
%define mysql_config /usr/mysql/5.1/bin/mysql_config
%define mysql_prefix %(/usr/mysql/5.1/bin/mysql_config --include | sed -e 's/\-I//')/../..
%endif

Summary: PHP scripting language for creating dynamic web sites
IPS_package_name:        web/php-53
SUNW_Copyright:   SFEphp53.copyright
Name: SFEphp53
Version: 5.3.20
%define major_version 5.3
#Release: 14%{?dist}
License: PHP
Group: Development/Languages
URL: http://www.php.net/
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
%define src_name php-%{version}

%define usr_prefix /usr
%define usr_bindir %{usr_prefix}/bin
%define _prefix /usr/php/%{major_version}
%define _sysconfdir /etc/php/%{major_version}
%define _bindir %{_prefix}/bin
%define _libdir %{_prefix}/lib
%define _mandir %{_prefix}/man
%define _pkg_docdir %{usr_prefix}/share/doc/SFEphp53

Source0: http://downloads.php.net/johannes/%{src_name}.tar.bz2
Source1: SFEphp53-php.conf
Source2: SFEphp53-php.ini
Source3: SFEphp53-macros.php

# Build fixes
Patch1: SFEphp53-gnusrc.patch
Patch2: SFEphp53-install.patch
Patch3: SFEphp53-norpath.patch
Patch4: SFEphp53-phpize64.patch
Patch6: SFEphp53-embed.patch
Patch7: SFEphp53-recode.patch
Patch8: SFEphp53-aconf26x.patch
Patch9: SFEphp53-ext_standard_config.patch

Patch12: SFEphp53-ldap_config.patch
Patch13: SFEphp53-odbc_config.patch
Patch14: SFEphp53-pdo_odbc_config.patch
Patch15: SFEphp53-mysqli_exception.patch
Patch16: SFEphp53-php_filter.patch
Patch17: SFEphp53-zend_execute_API.patch
Patch18: SFEphp53-iconv_config.patch

# Fixes for extensions
Patch20: SFEphp53-shutdown.patch

# Functional changes
Patch40: SFEphp53-dlopen.patch
Patch41: SFEphp53-easter.patch
Patch42: SFEphp53-systzdata-v7.patch

# Fixes for tests
Patch61: SFEphp53-tests-wddx.patch

# Bug fixes
Patch100: SFEphp53-extrglob.patch

#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

BuildRequires:  database/berkeleydb-48
BuildRequires:  %pnm_buildrequires_library_spell_checking_enchant
BuildRequires:  developer/build/autoconf259
BuildRequires:  library/text/gnu-iconv/developer
BuildRequires:  %{pnm_buildrequires_developer_icu}
BuildRequires:  library/gmp-5/developer
#BuildRequires: bzip2-devel, curl-devel >= 7.9, db4-devel, gmp-devel
#BuildRequires: httpd-devel >= 2.0.46-1, pam-devel
#BuildRequires: libstdc++-devel, openssl-devel, sqlite-devel >= 3.6.0
#BuildRequires: zlib-devel, pcre-devel >= 6.6, smtpdaemon, libedit-devel
#BuildRequires: bzip2, perl, libtool >= 1.4.3, gcc-c++
#Obsoletes: php-dbg, php3, phpfi, stronghold-php
#Requires: httpd-mmn = %{httpd_mmn}
#Provides: mod_php = %{version}-%{release}
#Requires: php-common = %{version}-%{release}
## For backwards-compatibility, require php-cli for the time being:
#Requires: php-cli = %{version}-%{release}
## To ensure correct /var/lib/php/session ownership:
#Requires(pre): httpd
Requires:       database/berkeleydb-48
Requires:  %pnm_requires_library_spell_checking_enchant
Requires:  library/text/gnu-iconv
Requires:  %{pnm_requires_developer_icu}
Requires:  library/gmp-5/developer

%description
PHP is an HTML-embedded scripting language. PHP attempts to make it
easy for developers to write dynamically generated webpages. PHP also
offers built-in database integration for several commercial and
non-commercial database management systems, so writing a
database-enabled webpage with PHP is fairly simple. The most common
use of PHP coding is probably as a replacement for CGI scripts. 

The php package contains the module which adds support for the PHP
language to Apache HTTP Server.

%package cli
Group: Development/Languages
Summary: Command-line interface for PHP
#Requires: php-common = %{version}-%{release}
#Provides: php-cgi = %{version}-%{release}
#Provides: php-pcntl, php-readline
Requires: web/php-53

%description cli
The php-cli package contains the command-line interface 
executing PHP scripts, /usr/bin/php, and the CGI interface.

%package zts
Group: Development/Languages
Summary: Thread-safe PHP interpreter for use with the Apache HTTP Server
#Requires: php-common = %{version}-%{release}
#Requires: httpd-mmn = %{httpd_mmn}
#BuildRequires: libtool-ltdl-devel
Requires: web/php-53
BuildRequires: %{pnm_buildrequires_web_server_apache_22}
Requires: %{pnm_requires_web_server_apache_22}

%description zts
The php-zts package contains a module for use with the Apache HTTP
Server which can operate under a threaded server processing model.

%package common
Group: Development/Languages
Summary: Common files for PHP
#Provides: php-api = %{apiver}, php-zend-abi = %{zendver}
#Provides: php(api) = %{apiver}, php(zend-abi) = %{zendver}
## Provides for all builtin modules:
#Provides: php-bz2, php-calendar, php-ctype, php-curl, php-date, php-exif
#Provides: php-ftp, php-gettext, php-gmp, php-hash, php-iconv, php-libxml
#Provides: php-reflection, php-session, php-shmop, php-simplexml, php-sockets
#Provides: php-spl, php-tokenizer, php-openssl, php-pcre
#Provides: php-zlib, php-json, php-zip, php-fileinfo
#Obsoletes: php-openssl, php-pecl-zip, php-pecl-json, php-json, php-pecl-phar, php-pecl-Fileinfo
## For obsoleted pecl extension
#Provides: php-pecl-json = %{jsonver}, php-pecl(json) = %{jsonver}
#Provides: php-pecl-zip = %{zipver}, php-pecl(zip) = %{zipver}
#Provides: php-pecl-phar = %{pharver}, php-pecl(phar) = %{pharver}
#Provides: php-pecl-Fileinfo = %{fileinfover}, php-pecl(Fileinfo) = %{fileinfover}
Summary: Files needed for building PHP extensions
Requires: web/php-53

%description common
The php-common package contains files used by both the php
package and the php-cli package.

%package devel
Group: Development/Libraries
Summary: Files needed for building PHP extensions
Requires: web/php-53
#Obsoletes: php-pecl-pdo-devel

%description devel
The php-devel package contains the files needed for building PHP
extensions. If you need to compile your own PHP extensions, you will
need to install this package.

%if %{with_cclient}
%package imap
# standard package of php-53
Summary: A module for PHP applications that use IMAP
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
#Obsoletes: mod_php3-imap, stronghold-php-imap
Requires: web/php-53
Requires: library/mail/libc-client-2007
Requires: library/mail/libc-client-2007/developer
BuildRequires: library/mail/libc-client-2007
BuildRequires: library/mail/libc-client-2007/developer

%description imap
The php-imap package contains a dynamic shared object that will
add support for the IMAP protocol to PHP.
%endif

%package ldap
# standard package of php-53
Summary: A module for PHP applications that use LDAP
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
#Obsoletes: mod_php3-ldap, stronghold-php-ldap
#BuildRequires: cyrus-sasl-devel, openldap-devel, openssl-devel
Requires: web/php-53
BuildRequires: %{pnm_buildrequires_library_openldap}
Requires: %{pnm_requires_library_openldap}

%description ldap
The php-ldap package is a dynamic shared object (DSO) for the Apache
Web server that adds Lightweight Directory Access Protocol (LDAP)
support to PHP. LDAP is a set of protocols for accessing directory
services over the Internet. PHP is an HTML-embedded scripting
language. If you need LDAP support for PHP applications, you will
need to install this package in addition to the php package.

%package pdo
# standard package of php-53
Summary: A database access abstraction module for PHP applications
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
#Obsoletes: php-pecl-pdo-sqlite, php-pecl-pdo
#Provides: php-pdo-abi = %{pdover}
#Provides: php-sqlite3, php-pdo_sqlite
Requires: web/php-53

%description pdo
The php-pdo package contains a dynamic shared object that will add
a database access abstraction layer to PHP.  This module provides
a common interface for accessing MySQL, PostgreSQL or other 
databases.

%if %{with_mysql}
%package mysql
IPS_package_name:        web/php-53/extension/php-mysql
Summary: A module for PHP applications that use MySQL databases
Group: Development/Languages
Requires: web/php-53
#Provides: php_database, php-mysqli, php-pdo_mysql
#Obsoletes: mod_php3-mysql, stronghold-php-mysql
BuildRequires: %{pnm_buildrequires_database_mysql_51}
Requires: %{pnm_requires_database_mysql_51}

%description mysql
The php-mysql package contains a dynamic shared object that will add
MySQL database support to PHP. MySQL is an object-relational database
management system. PHP is an HTML-embeddable scripting language. If
you need MySQL support for PHP applications, you will need to install
this package and the php package.
%endif

%if %{with_pgsql}
%package pgsql
IPS_package_name: web/php-53/extension/php-pgsql
Summary: A PostgreSQL database module for PHP
Group: Development/Languages
#Requires: php-common = %{version}-%{release}, php-pdo
#Provides: php_database, php-pdo_pgsql
#Obsoletes: mod_php3-pgsql, stronghold-php-pgsql
BuildRequires: database/postgres-92/library
BuildRequires: database/postgres-92/developer
BuildRequires: %{pnm_buildrequires_text_gnu_sed}
BuildRequires: SFEre2c
Requires: database/postgres-92/library
Requires: web/php-53

%description pgsql
The php-pgsql package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL database
support to PHP. PostgreSQL is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL, you should install this package in addition to the main
php package.
%endif

%package process
IPS_package_name: web/php-53/extension/php-process
Summary: Modules for PHP script using system process interfaces
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
#Provides: php-posix, php-sysvsem, php-sysvshm, php-sysvmsg
Requires: web/php-53

%description process
The php-process package contains dynamic shared objects which add
support to PHP using system interfaces for inter-process
communication.

%if %{with_unixodbc}
%package odbc
IPS_package_name: web/php-53/extension/php-odbc
Group: Development/Languages
#Requires: php-common = %{version}-%{release}, php-pdo
Summary: A module for PHP applications that use ODBC databases
#Provides: php_database, php-pdo_odbc
#Obsoletes: stronghold-php-odbc
#BuildRequires: unixODBC-devel
Requires: web/php-53

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
IPS_package_name: web/php-53/extension/php-soap
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
Summary: A module for PHP applications that use the SOAP protocol
#BuildRequires: libxml2-devel
BuildRequires: %{pnm_buildrequires_library_libxml2}
Requires: web/php-53

%description soap
The php-soap package contains a dynamic shared object that will add
support to PHP for using the SOAP web services protocol.

%package snmp
# standard package of php-53
Summary: A module for PHP applications that query SNMP-managed devices
Group: Development/Languages
#Requires: php-common = %{version}-%{release}, net-snmp
#BuildRequires: net-snmp-devel
BuildRequires: %{pnm_buildrequires_system_management_snmp_net_snmp}
Requires: %{pnm_requires_system_management_snmp_net_snmp}

%description snmp
The php-snmp package contains a dynamic shared object that will add
support for querying SNMP devices to PHP.  PHP is an HTML-embeddable
scripting language. If you need SNMP support for PHP applications, you
will need to install this package and the php package.

%package xml
# standard package of php-53
Summary: A module for PHP applications which use XML
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
#Obsoletes: php-domxml, php-dom
#Provides: php-dom, php-xsl, php-domxml, php-wddx
#BuildRequires: libxslt-devel >= 1.0.18-1, libxml2-devel >= 2.4.14-1
Requires: web/php-53
BuildRequires: %{pnm_buildrequires_library_libxml2}
BuildRequires: %{pnm_buildrequires_library_libxslt}

%description xml
The php-xml package contains dynamic shared objects which add support
to PHP for manipulating XML documents using the DOM tree,
and performing XSL transformations on XML documents.

%package xmlrpc
IPS_package_name: web/php-53/extension/php-xmlrpc
Summary: A module for PHP applications which use the XML-RPC protocol
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
Requires: web/php-53

%description xmlrpc
The php-xmlrpc package contains a dynamic shared object that will add
support for the XML-RPC protocol to PHP.

%package mbstring
# standard package of php-53
Summary: A module for PHP applications which need multi-byte string handling
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
Requires: web/php-53

%description mbstring
The php-mbstring package contains a dynamic shared object that will add
support for multi-byte string handling to PHP.

%package gd
# standard package of php-53
Summary: A module for PHP applications for using the gd graphics library
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
## Required to build the bundled GD library
#BuildRequires: libXpm-devel, libjpeg-devel, libpng-devel, freetype-devel
BuildRequires: x11/library/libxpm
BuildRequires: %{pnm_buildrequires_image_library_libjpeg}
Requires: web/php-53

%description gd
The php-gd package contains a dynamic shared object that will add
support for using the gd graphics library to PHP.

%package bcmath
IPS_package_name: web/php-53/extension/php-bcmath
Summary: A module for PHP applications for using the bcmath library
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
Requires: web/php-53

%description bcmath
The php-bcmath package contains a dynamic shared object that will add
support for using the bcmath library to PHP.

%package dba
IPS_package_name: web/php-53/extension/php-dba
Summary: A database abstraction layer module for PHP applications
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
Requires: web/php-53

%description dba
The php-dba package contains a dynamic shared object that will add
support for using the DBA database abstraction layer to PHP.

%package tidy
# standard package of php-53
Summary: Standard PHP module provides tidy library support
Group: Development/Languages
#Requires: php-common = %{version}-%{release}
#BuildRequires: libtidy-devel
BuildRequires: %{pnm_buildrequires_text_tidy}
Requires: web/php-53

%description tidy
The php-tidy package contains a dynamic shared object that will add
support for using the tidy library to PHP.

%package embedded
IPS_package_name: web/php-53/extension/php-embedded
Summary: PHP library for embedding in applications
Group: System Environment/Libraries
#Requires: php-common = %{version}-%{release}
# doing a real -devel package for just the .so symlink is a bit overkill
#Provides: php-embedded-devel = %{version}-%{release}
Requires: web/php-53

%description embedded
The php-embedded package contains a library which can be embedded
into applications to provide PHP scripting language support.

%if %{with_pspell}
%package pspell
IPS_package_name: web/php-53/extension/php-pspell
Summary: A module for PHP applications for using pspell interfaces
Group: System Environment/Libraries
#Requires: php-common = %{version}-%{release}
#BuildRequires: aspell-devel >= 0.50.0
Requires: web/php-53

%description pspell
The php-pspell package contains a dynamic shared object that will add
support for using the pspell library to PHP.
%endif

%if %{with_recode}
%package recode
IPS_package_name: web/php-53/extension/php-recode
Summary: A module for PHP applications for using the recode library
Group: System Environment/Libraries
#Requires: php-common = %{version}-%{release}
#BuildRequires: recode-devel
Requires: web/php-53

%description recode
The php-recode package contains a dynamic shared object that will add
support for using the recode library to PHP.
%endif

%package intl
IPS_package_name: web/php-53/extension/php-intl
Summary: Internationalization extension for PHP applications
Group: System Environment/Libraries
#Requires: php-common = %{version}-%{release}
#BuildRequires: libicu-devel >= 3.6
Requires: web/php-53

%description intl
The php-intl package contains a dynamic shared object that will add
support for using the ICU library to PHP.

%package enchant
IPS_package_name: web/php-53/extension/php-enchant
Summary: Human Language and Character Encoding Support
Group: System Environment/Libraries
#Requires: php-common = %{version}-%{release}
#BuildRequires: enchant-devel >= 1.2.4
BuildRequires: %{pnm_buildrequires_library_spell_checking_enchant}
Requires: web/php-53

%description enchant
The php-intl package contains a dynamic shared object that will add
support for using the enchant library to PHP.

%prep
%if %{skip_prep}
#cd php-%{version}
%else
%setup -q -n php-%version
%patch1 -p1 -b .gnusrc
%patch2 -p1 -b .install
%patch3 -p1 -b .norpath
%patch4 -p1 -b .phpize64
%patch6 -p1 -b .embed
%patch7 -p1 -b .recode
%patch8 -p1 -b .aconf26x
%patch9 -p1

%patch12 -p1
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p1

%patch20 -p1 -b .shutdown
#%patch21 -p1 -b .zipmemset

%patch40 -p1 -b .dlopen
%patch41 -p1 -b .easter
#%patch42 -p1 -b .systzdata

%patch61 -p1 -b .tests-wddx

%patch100 -p1 -b .extrglob

# Prevent %doc confusion over LICENSE files
cp Zend/LICENSE Zend/ZEND_LICENSE
cp TSRM/LICENSE TSRM_LICENSE
cp ext/ereg/regex/COPYRIGHT regex_COPYRIGHT
cp ext/gd/libgd/README gd_README

# Multiple builds for multiple SAPIs
mkdir build-cgi build-apache build-embedded build-zts

# Remove bogus test; position of read position after fopen(, "a+")
# is not defined by C standard, so don't presume anything.
rm -f ext/standard/tests/file/bug21131.phpt

# Tests that fail.
rm -f ext/standard/tests/file/bug22414.phpt \
      ext/iconv/tests/bug16069.phpt

# Safety check for API version change.
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

# Fix some bogus permissions
find . -name \*.[ch] -exec chmod 644 {} \;
chmod 644 README.*
%endif

%build
%if %{skip_build}
    cd php-%{version}
%else
export PHP_AUTOCONF=autoconf-2.59
#export CXXFLAGS="%cxx_optflags -I%{gnu_inc} %{gnu_lib_path} -L/opt/solarisstudio12.3/lib"
export CXXFLAGS="%cxx_optflags -L/opt/solarisstudio12.3/lib"
export LDFLAGS="%_ldflags %gnu_lib_path -L/opt/solarisstudio12.3/lib"
#export LDFLAGS="%_ldflags -L/opt/solarisstudio12.3/lib"

%if %( expr %{skip_prep} '=' 0 )
# aclocal workaround - to be improved
#cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >>aclocal.m4
cat `aclocal --print-ac-dir`/libtool.m4 >>aclocal.m4

# Force use of system libtool:
libtoolize --force --copy
#cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4
cat `aclocal --print-ac-dir`/libtool.m4 >build/libtool.m4

# Regenerate configure scripts (patches change config.m4's)
touch configure.in
./buildconf --force
%endif

#CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
#export CFLAGS
%if %{cc_is_gcc}
    export CC=gcc
    export CXX=g++
    export CFLAGS="%optflags -fno-strict-aliasing -Wno-pointer-sign"
%else
    export CFLAGS="%optflags"
%endif

# Install extension modules in %{_libdir}/modules.
#EXTENSION_DIR and libexecdir need not be identical
EXTENSION_DIR=%{_prefix}/modules; export EXTENSION_DIR

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{_localstatedir}/php/%{major_version}/pear:%{_localstatedir}/php/libs; export PEAR_INSTALLDIR

# Shell function to configure and build a PHP tree.
build() {
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
# bison-1.875-2 seems to produce a broken parser; workaround.
mkdir Zend && cp ../Zend/zend_{language,ini}_{parser,scanner}.[ch] Zend
ln -sf ../configure
%configure \
	--cache-file=../config.cache \
   	--mandir=%{_mandir} \
        --with-libdir=%{_lib} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/conf.d \
	--disable-debug \
	--with-pic \
	--disable-rpath \
	--without-pear \
	--with-bz2 \
	--with-exec-dir=%{_bindir} \
	--with-freetype-dir=%{usr_prefix} \
	--with-png-dir=%{usr_prefix} \
	--with-xpm-dir=%{usr_prefix} \
	--enable-gd-native-ttf \
	--without-gdbm \
	--with-gettext \
	--with-gmp=%{gnu_inc}/../\
	--with-iconv \
	--with-jpeg-dir=%{usr_prefix} \
	--with-openssl \
        --with-pcre-regex=%{usr_prefix} \
	--with-zlib \
	--with-layout=GNU \
	--enable-exif \
	--enable-ftp \
	--enable-magic-quotes \
	--enable-sockets \
	--enable-sysvsem --enable-sysvshm --enable-sysvmsg \
	--with-kerberos \
	--enable-ucd-snmp-hack \
	--enable-shmop \
	--enable-calendar \
        --without-sqlite \
        --with-libxml-dir=%{usr_prefix} \
	--enable-xml \
        --with-system-tzdata \
	$* 
if test $? != 0; then 
  tail -500 config.log
  : configure failed
  exit 1
fi

make -j$CPUS
}

%if %{build_cgi}
# Build /usr/bin/php-cgi with the CGI SAPI, and all the shared extensions
%if %{with_mysql}
export LDFLAGS="$LDFLAGS -R%{mysql_prefix}/lib/mysql"
%endif
pushd build-cgi
build --enable-force-cgi-redirect \
      --enable-pcntl \
      --libexecdir=%{_prefix}/modules \
%if %{with_cclient}
      --with-imap=shared --with-imap-ssl \
%endif
      --enable-mbstring=shared \
      --enable-mbregex \
      --enable-gd-jis-conv --enable-gd-native-ttf \
      --with-gd=shared \
      --enable-bcmath=shared \
      --enable-dba=shared --with-db4=%{gnu_inc}/../ \
      --with-xmlrpc=shared \
      --with-ldap=shared --with-ldap-sasl \
%if %{with_mysql}
      --with-mysql=shared,%{mysql_prefix} \
      --with-mysqli=shared,%{mysql_config} \
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
      --enable-fastcgi \
      --enable-pdo=shared \
%if %{with_unixodbc}
      --with-pdo-odbc=shared,unixODBC,%{usr_prefix} \
%endif
%if %{with_mysql}
      --with-pdo-mysql=shared,%{mysql_prefix} \
%endif
%if %{with_pgsql}
      --with-pdo-pgsql=shared,%{usr_prefix} \
%endif
      --with-pdo-sqlite=shared,%{usr_prefix} \
      --with-sqlite3=shared,%{usr_prefix} \
      --enable-json=shared \
      --enable-zip=shared \
      --without-readline \
%if %{with_libedit}
      --with-libedit \
%endif
%if %{with_pspell}
      --with-pspell=shared \
%endif
      --enable-phar=shared \
      --with-tidy=shared,%{usr_prefix} \
      --enable-sysvmsg=shared --enable-sysvshm=shared --enable-sysvsem=shared \
      --enable-posix=shared \
%if %{with_unixodbc}
      --with-unixODBC=shared,%{usr_prefix} \
%endif
      --enable-fileinfo=shared \
      --enable-intl=shared \
      --with-icu-dir=%{usr_prefix} \
%if %{with_recode}
      --with-recode=shared,%{usr_prefix} \
%endif
      --with-enchant=shared,%{usr_prefix}
popd
%endif
%if %{build_apache}
without_shared="--without-mysql --without-gd \
      --disable-dom --disable-dba --without-unixODBC \
      --disable-pdo --disable-xmlreader --disable-xmlwriter \
      --without-sqlite3 --disable-phar --disable-fileinfo \
      --disable-json --without-pspell --disable-wddx \
      --without-curl --disable-posix \
      --disable-sysvmsg --disable-sysvshm --disable-sysvsem"

# Build Apache module, and the CLI SAPI, /usr/bin/php
pushd build-apache
build --with-apxs2=%{usr_bindir}/apxs ${without_shared}
popd
%endif
%if %{build_embedded}
# Build for inclusion as embedded script language into applications,
# /usr/lib[64]/libphp5.so
pushd build-embedded
build --enable-embed ${without_shared}
popd
%endif
%if %{build_zts}
# Build a special thread-safe Apache SAPI
pushd build-zts
#EXTENSION_DIR and libexecdir need not be identical
EXTENSION_DIR=%{_prefix}/modules-zts
build --with-apxs2=%{usr_bindir}/apxs ${without_shared} \
      --enable-maintainer-zts \
      --with-config-file-scan-dir=%{_sysconfdir}/php-zts.d \
      --libexecdir=%{_prefix}/zts-modules
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
%if %{build_apache}
cd build-apache
# Run tests, using the CLI SAPI
export NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2
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
# Install the version for embedded script language in applications + php_embed.h
make -C build-embedded install-sapi install-headers INSTALL_ROOT=$RPM_BUILD_ROOT

# Install everything from the CGI SAPI build
make -C build-cgi install INSTALL_ROOT=$RPM_BUILD_ROOT 

# Install the default configuration file and icons
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/php.ini
install -m 755 -d $RPM_BUILD_ROOT%{contentdir}/icons
install -m 644    *.gif $RPM_BUILD_ROOT%{contentdir}/icons/

# For third-party packaging:
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}/pear \
                  $RPM_BUILD_ROOT%{_localstatedir}/php/libs

# install the DSO
install -m 755 -d $RPM_BUILD_ROOT%{_prefix}/apache2/2.2/libexec/
install -m 755 build-apache/libs/libphp5.so $RPM_BUILD_ROOT%{_prefix}/apache2/2.2/libexec
install -m 755 -d $RPM_BUILD_ROOT%{usr_prefix}/apache2/2.2/libexec/
pushd $RPM_BUILD_ROOT/%{usr_prefix}/apache2/2.2/libexec
ln -s ../../../php/%{major_version}/apache2/2.2/libexec/libphp5.so .
popd 

# install the ZTS DSO
install -m 755 build-zts/libs/libphp5.so $RPM_BUILD_ROOT%{_prefix}/apache2/2.2/libexec/libphp5-zts.so
pushd $RPM_BUILD_ROOT/%{usr_prefix}/apache2/2.2/libexec
ln -s ../../../php/%{major_version}/apache2/2.2/libexec/libphp5-zts.so .
popd

# Apache config fragment
install -m 755 -d $RPM_BUILD_ROOT/etc/apache2/2.2/conf.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/apache2/2.2/conf.d/php53-32.load
pushd $RPM_BUILD_ROOT/etc/apache2/2.2/conf.d
ln -s php53-32.load php-32.load
popd

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/conf.d
#install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php-zts.d
install -m 755 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}
install -m 700 -d $RPM_BUILD_ROOT%{_localstatedir}/php/%{major_version}/session

# Fix the link
(cd $RPM_BUILD_ROOT%{_bindir}; ln -sfn phar.phar phar)

#install -d 755 $RPM_BUILD_ROOT/sapi/cgi
#install -d 755 $RPM_BUILD_ROOT/sapi/cli
#install -m 644 sapi/cgi/README* $RPM_BUILD_ROOT/sapi/cgi
#install -m 644 sapi/cli/README $RPM_BUILD_ROOT/sapi/cli

# Generate files lists and stub .ini files for each subpackage
for mod in \
%if %{with_pgsql}
    pgsql \
%endif
%if %{with_mysql}
    mysql \
    mysqli \
%endif
%if %{with_unixodbc}
    odbc \
%endif
    ldap snmp xmlrpc \
%if %{with_cclient}
    imap \
%endif
    mbstring gd dom xsl soap bcmath dba xmlreader xmlwriter \
    pdo \
%if %{with_mysql}
    pdo_mysql \
%endif
%if %{with_pgsql}
    pdo_pgsql \
%endif
%if %{with_unixodbc}
    pdo_odbc \
%endif
%if %{with_recode}
    recode \
%endif
    pdo_sqlite json zip \
    sqlite3 enchant phar fileinfo intl \
    tidy \
%if %{with_pspell}
    pspell \
%endif
    curl wddx \
    posix sysvshm sysvsem sysvmsg; \
do
    cat > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
    cat > files.${mod} <<EOF
%defattr(-,root,bin)
%attr(555,root,bin) %{_prefix}/modules/${mod}.so
%config(noreplace) %attr(644,root,bin) %{_sysconfdir}/conf.d/${mod}.ini
EOF
done

# The dom, xsl and xml* modules are all packaged in php-xml
cat files.dom files.xsl files.xml{reader,writer} files.wddx > files.xml

# The mysql and mysqli modules are both packaged in php-mysql
%if %{with_mysql}
cat files.mysqli >> files.mysql

# Split out the PDO modules
cat files.pdo_mysql >> files.mysql
%endif
%if %{with_pgsql}
cat files.pdo_pgsql >> files.pgsql
%endif
%if %{with_unixodbc}
cat files.pdo_odbc >> files.odbc
%endif

# sysv* and posix in packaged in php-process
cat files.sysv* files.posix > files.process

# Package sqlite3 and pdo_sqlite with pdo; isolating the sqlite dependency
# isn't useful at this time since rpm itself requires sqlite.
cat files.pdo_sqlite >> files.pdo
cat files.sqlite3 >> files.pdo

# Package json, zip, curl, phar and fileinfo in -common.
cat files.json files.zip files.curl files.phar files.fileinfo > files.common

# Install the macros file:
%if %{build_rpm_macros}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/rpm
sed -e "s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/;s/@PHP_PDOVER@/%{pdover}/" \
    < %{SOURCE3} > macros.php
install -m 644 -c macros.php \
           $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.php
%endif
# Remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_prefix}/modules/*.a \
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

%clean
%if %{skip_prep}
   cd php-%{version}
%endif
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
rm files.*
%if %{build_rpm_macros}
    rm macros.php
%endif

#%post embedded -p /sbin/ldconfig
#%postun embedded -p /sbin/ldconfig

%if %{skip_prep}
%define name php
%endif
%files
%defattr(-,root,bin)
%{_prefix}/apache2/2.2/libexec/libphp5.so
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, bin) %{_localstatedir}/php
%dir %attr (0755, root, bin) %{_localstatedir}/php/%{major_version}
%attr(0770,root,webservd) %dir %{_localstatedir}/php/%{major_version}/session
%config(noreplace) /etc/apache2/2.2/conf.d/php53-32.load
%ips_tag (mediator=php mediator-version=%{major_version}) /etc/apache2/2.2/conf.d/php-32.load
%config(noreplace) %{contentdir}/icons/php.gif
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/build
%dir %attr (0755, root, bin) %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/conf.d
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) %{usr_prefix}/apache2/2.2/libexec/libphp5.so
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php-cgi
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/php-config
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/bin/phpize
%if %{with_mediator_in_directory_usr_php_bin}
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/bin
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/include
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/lib
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/man
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) /usr/php/modules
%endif

%files common -f files.common
%defattr(-,root,bin)
%doc CODING_STANDARDS CREDITS EXTENSIONS INSTALL LICENSE NEWS README*
%doc Zend/ZEND_* TSRM_LICENSE regex_COPYRIGHT
%doc php.ini-production php.ini-development
%config(noreplace) %{_sysconfdir}/php.ini
%dir %{_sysconfdir}/conf.d
#dir %{_sysconfdir}/php-zts.d
%dir %{_prefix}/modules
#dir %{_prefix}/modules-zts
%dir %{_localstatedir}/php/%{major_version}/pear
%dir %{_localstatedir}/php/libs

%files cli
%defattr(-,root,bin)
%doc sapi/cgi/README* sapi/cli/README
%{_bindir}/php
%{_bindir}/php-cgi
%{_bindir}/phar.phar
%{_bindir}/phar
%{_mandir}/man1/php.1*

%files zts
%defattr(-,root,bin)
%{_prefix}/apache2/2.2/libexec/libphp5-zts.so
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{major_version}) %{usr_prefix}/apache2/2.2/libexec/libphp5-zts.so

%files devel
%defattr(-,root,bin)
%{_bindir}/php-config
%{_bindir}/phpize
%{_includedir}/php
%{_libdir}/build
%{_mandir}/man1/php-config.1*
%{_mandir}/man1/phpize.1*
%if %{build_rpm_macros}
%config %{_sysconfdir}/rpm/macros.php
%endif

%files embedded
%defattr(-,root,bin)
%{_libdir}/libphp5.so
%{_libdir}/libphp5-%{version}.so

%if %{with_pgsql}
%files pgsql -f files.pgsql
%endif
%if %{with_mysql}
%files mysql -f files.mysql
%endif
%if %{with_unixodbc}
%files odbc -f files.odbc
%endif
%if %{with_cclient}
%files imap -f files.imap
%endif
%files ldap -f files.ldap
%files snmp -f files.snmp
%files xml -f files.xml
%files xmlrpc -f files.xmlrpc
%files mbstring -f files.mbstring
%files gd -f files.gd
%defattr(-,root,bin)
%doc gd_README
%files soap -f files.soap
%files bcmath -f files.bcmath
%files dba -f files.dba
%files pdo -f files.pdo
%files tidy -f files.tidy
%if %{with_pspell}
%files pspell -f files.pspell
%endif
%files intl -f files.intl
%files process -f files.process
%if %{with_recode}
%files recode -f files.recode
%endif
%files enchant -f files.enchant

%changelog
* Mon May 19 2014 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.3.20
- Fix mediator for coexistence under php 5.4

* Mon May 19 2014 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.3.20
- Fix dependency and source url

* Thr Apr 18 2013 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.3.20
- Ready for imap

* Feb 07 2013 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.3.20
- Fix that spec does not make the file .proto.

* Feb 07 2013 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.3.20
- add Buildrequires and Requires

* Feb 07 2013 YAMAMOTO Takashi <yamachan@selfnavi.com> - 5.3.20
- Bump to 5.3.20
- work with CBE 
- Support for OpenIndiana

* Mon Jun 25 2012 Joe Orton <jorton@redhat.com> - 5.3.3-14
- add security fix for CVE-2010-2950

* Wed Jun 13 2012 Joe Orton <jorton@redhat.com> - 5.3.3-13
- fix tests for CVE-2012-2143, CVE-2012-0789

* Tue Jun 12 2012 Joe Orton <jorton@redhat.com> - 5.3.3-12
- add fix for CVE-2012-2336

* Mon Jun 11 2012 Joe Orton <jorton@redhat.com> - 5.3.3-11
- add security fixes for CVE-2012-0781, CVE-2011-4153, CVE-2012-0057,
  CVE-2012-0789, CVE-2012-1172, CVE-2012-2143, CVE-2012-2386

* Thu May  3 2012 Joe Orton <jorton@redhat.com> - 5.3.3-9
- correct detection of = in CVE-2012-1823 fix (#818607)

* Thu May  3 2012 Joe Orton <jorton@redhat.com> - 5.3.3-8
- add security fix for CVE-2012-1823 (#818607)

* Thu Feb  2 2012 Joe Orton <jorton@redhat.com> - 5.3.3-7
- add security fix for CVE-2012-0830 (#786744)

* Thu Jan 05 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 5.3.3-6
- merge Joe's changes:
- improve CVE-2011-1466 fix to cover CAL_GREGORIAN, CAL_JEWISH
- add security fixes for CVE-2011-2483, CVE-2011-0708, CVE-2011-1148,
  CVE-2011-1466, CVE-2011-1468, CVE-2011-1469, CVE-2011-1470,
  CVE-2011-1471, CVE-2011-1938, and CVE-2011-2202 (#740732)

* Wed Jan 04 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 5.3.3-5
- remove extra php.ini-prod/devel files caused by %%patch -b

* Mon Jan 02 2012 Vojtech Vitek (V-Teq) <vvitek@redhat.com> - 5.3.3-4
- add security fixes for CVE-2011-4885, CVE-2011-4566 (#769755)

* Fri Jan 21 2011 Joe Orton <jorton@redhat.com> - 5.3.3-3
- add security fixes for CVE-2010-4645, CVE-2010-4156 (#670439)

* Fri Jan 14 2011 Joe Orton <jorton@redhat.com> - 5.3.3-2
- fix transposed memset arguments in libzip

* Wed Jan 12 2011 Joe Orton <jorton@redhat.com> - 5.3.3-1
- update to 5.3.3 (#645591)
- add security fixes for CVE-2010-3709, CVE-2010-3710,
  CVE-2010-3870, CVE-2009-5016 (#651953)
- prevent extract() cloberring $GLOBALS (#655118)
- ensure correct mysql_config is used in biarch builds

* Tue Aug 17 2010 Joe Orton <jorton@redhat.com> - 5.3.2-6
- add security fixes for CVE-2010-1866, CVE-2010-2094, CVE-2010-1917,
  CVE-2010-2531, MOPS-2010-060 (#624469)

* Fri Aug 13 2010 Joe Orton <jorton@redhat.com> - 5.3.2-5
- add security fix for CVE-2010-0397 (#575712)

* Thu Jun 24 2010 Joe Orton <jorton@redhat.com> - 5.3.2-4
- add security fix for CVE-2010-2225 (#605644)

* Wed May  5 2010 Joe Orton <jorton@redhat.com> - 5.3.2-3
- restore -imap (#586050)

* Fri Mar 26 2010 Joe Orton <jorton@redhat.com> - 5.3.2-2
- remove mcrypt support (#459804, #577257)

* Wed Mar 24 2010 Joe Orton <jorton@redhat.com> - 5.3.2-1
- update to 5.3.2 (#575158, #575712)

* Sat Mar 06 2010 Remi Collet <Fedora@famillecollet.com>
- PHP 5.3.2 Released!
- remove mime_magic option (now provided by fileinfo, by emu)
- add patch for http://bugs.php.net/50578
- remove patch for libedit (upstream)

* Fri Jan 15 2010 Joe Orton <jorton@redhat.com> - 5.3.1-7
- add security fix for CVE-2009-4142 (#552268)

* Fri Dec 18 2009 Joe Orton <jorton@redhat.com> - 5.3.1-6
- drop mssql, pdo_dblib

* Fri Dec 11 2009 Joe Orton <jorton@redhat.com> - 5.3.1-5
- drop imap

* Fri Dec 11 2009 Joe Orton <jorton@redhat.com> - 5.3.1-4
- drop t1lib, interbase/firebird support

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

* Sat Jun 21 2009 Remi Collet <Fedora@famillecollet.com> 5.2.10-1
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
