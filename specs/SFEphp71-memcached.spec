%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define php_version 7.1
%define zts_version 20160303
%define tarball_version  3.0.3
%define tarball_name     memcached

Name:             SFEphp71-memcached
IPS_package_name: web/php-71/extension/php-memcached
Summary:          PHP 7.1 module for MEMCACHED
Version:          %{tarball_version}
License:          PHP License
Url:              http://pecl.php.net/package/%{tarball_name}
Source:           http://pecl.php.net/get/%{tarball_name}-%{tarball_version}.tgz
Source1:          php-memcached.ini
SUNW_Basedir:     /
SUNW_Copyright:   %{name}.copyright
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-71
BuildRequires: library/memcached-1
Requires: web/php-71
Requires: library/memcached-1

%prep
%setup -c -n %{name}-%{tarball_version}

%build

export CC=/usr/bin/gcc
export CXX=/usr/bin/g++
export CFLAGS="-m64 -I/usr/include/libmemcached-1.0"
export CXXFLAGS="-m64 -I/usr/include/libmemcached-1.0 "
export LDFLAGS="-m64 -L/lib/`isainfo -k` -L/usr/lib/`isainfo -k` -R/lib/`isainfo -k` -R/usr/lib/`isainfo -k`"

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

/usr/php/%{php_version}/bin/phpize
./configure \
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir} \
 --disable-memcached-sasl \
 --with-php-config=/usr/php/%{php_version}/bin/php-config 

gmake -j$CPUS CFLAGS="$CFLAGS"
echo no | gmake test

%install
[ -d $RPM_BUILD_ROOT ] && rm -r $RPM_BUILD_ROOT

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-%{zts_version}/
cp modules/memcached.so $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-%{zts_version}/
mkdir -p  $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d/memcached.ini

## %{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-%{zts_version}/
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-%{zts_version}/memcached.so
%dir %attr(0755, root, sys) %{_sysconfdir}
%dir %attr(0755, root, bin) %{_sysconfdir}/php
%dir %attr(0755, root, bin) %{_sysconfdir}/php/%{php_version}
%dir %attr(0755, root, bin) %{_sysconfdir}/php/%{php_version}/conf.d
%config %attr(0644, root, bin) %{_sysconfdir}/php/%{php_version}/conf.d/memcached.ini

%changelog
* Sun Sep 24 2017 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
