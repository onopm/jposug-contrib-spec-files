#
# spec file for package SFEphp52-pgsql90
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#
%include Solaris.inc

%define _prefix /usr
%define tarball_version  5.2.17
%define tarball_name     php
%define major_version	 9.1

Name:                    SFEphp52-pgsql91
IPS_package_name:	 web/php-52/extension/php-pgsql91
Summary:                 PHP 5.2 module for PostgreSQL 91
Version:                 5.2.17
License:		 PHP License
Url:                     http://www.php.net/
Source:			 http://museum.php.net/php5/%{tarball_name}-%{tarball_version}.tar.bz2
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
#SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-52
BuildRequires: text/gnu-sed
BuildRequires: database/postgres-90/library
BuildRequires: database/postgres-90/developer
BuildRequires: SFEre2c

Requires: database/postgres-90/library
Requires: web/php-52

%description
The SFEphp52-pgsql91 package includes a dynamic shared object (DSO) that can
be compiled in to the Apache Web server to add PostgreSQL-9.1 database
support to PHP. PostgreSQL-9.1 is an object-relational database management
system that supports almost all SQL constructs. PHP is an
HTML-embedded scripting language. If you need back-end support for
PostgreSQL-9.1, you should install this package in addition to the main
php package.

%prep
%setup -c -n %name-%version

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

pushd ext/pgsql/
/usr/php/5.2/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --with-php-config=/usr/php/5.2/bin/php-config \
 --with-pgsql=/usr/postgres/%{major_version}
gmake -j$CPUS
popd

pushd ext/pdo_pgsql/
/usr/php/5.2/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --with-php-config=/usr/php/5.2/bin/php-config \
 --with-pdo-pgsql=/usr/postgres/%{major_version}
gmake -j$CPUS
popd


%install

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/etc/php/5.2/conf.d

for mod in pgsql pdo_pgsql; do
 pushd ext/${mod}/
  make install INSTALL_ROOT=$RPM_BUILD_ROOT PECL_EXTENSION_DIR=%{_prefix}/php/5.2/modules PECL_INCLUDE_DIR=%{_prefix}/php/5.2/include
 popd
 pushd $RPM_BUILD_ROOT/%{_prefix}/php/5.2/modules/
  mv ${mod}.so ${mod}.so.%{major_version} 
  ln -s ${mod}.so.%{major_version} ${mod}.so 
 popd
 pushd $RPM_BUILD_ROOT/etc/php/5.2/conf.d/
 cat > ${mod}.ini.%{major_version} <<EOF
; Enable ${mod} extension module
extension=${mod}.so.%{major_version}
EOF
 ln -s ${mod}.ini.%{major_version} ${mod}.ini
 popd
done

#mkdir -p $RPM_BUILD_ROOT/%{_prefix}/php/5.2/modules/
#mkdir -p  $RPM_BUILD_ROOT/etc/php/5.2/conf.d

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/5.2/modules
%{_prefix}/php/5.2/modules/pdo_pgsql.so.%{major_version}
%{_prefix}/php/5.2/modules/pgsql.so.%{major_version}
%ips_tag (mediator=postgres mediator-version=%{major_version}) %{_prefix}/php/5.2/modules/pdo_pgsql.so
%ips_tag (mediator=postgres mediator-version=%{major_version}) %{_prefix}/php/5.2/modules/pgsql.so
%dir %attr(0755, root, sys) %{_sysconfdir}
# %config(noreplace) 
%{_sysconfdir}/php/5.2/conf.d/pdo_pgsql.ini.%{major_version}
%{_sysconfdir}/php/5.2/conf.d/pgsql.ini.%{major_version}
%ips_tag (mediator=postgres mediator-version=%{major_version}) %{_sysconfdir}/php/5.2/conf.d/pdo_pgsql.ini
%ips_tag (mediator=postgres mediator-version=%{major_version}) %{_sysconfdir}/php/5.2/conf.d/pgsql.ini

%changelog
* Sun Jan 27 2013 TAKI, Yasushi <taki@justplayer.com>
- add mediator
- add config
* Sat Dec 15 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
