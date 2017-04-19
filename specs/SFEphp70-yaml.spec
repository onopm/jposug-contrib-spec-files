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
%define php_version 7.0
%define tarball_version  2.0.0
%define tarball_name     yaml

Name:                    SFEphp70-yaml
IPS_package_name:	 web/php-70/extension/php-yaml
Summary:                 PHP 7.0 module for YAML
Version:                 %{tarball_version}
License:		 PHP License
Url:                     http://pecl.php.net/package/%{tarball_name}
Source:                  http://pecl.php.net/get/%{tarball_name}-%{tarball_version}.tgz
Source1:                 %{name}.ini
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
# SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-70
BuildRequires: library/text/yaml >= 0.1.6
Requires: web/php-70
Requires: library/text/yaml >= 0.1.6
Requires: web/php-70/extension/php-date

%prep
%setup -c -n %tarball_name-%tarball_version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

# export CFLAGS="-m64 -xO4 -xchip=pentium -xregs=no%frameptr -mt"
# export CXXFLAGS="-m64 -xO4 -xchip=pentium -xregs=no%frameptr -mt"
# export CPPFLAGS="-m64 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"

export CC=/usr/bin/gcc
export CFLAGS='-m64'
export CXX=/usr/bin/g++
export CXXFLAGS='-m64'

export LDFLAGS="-L/lib/`isainfo -k` -L/usr/lib/`isainfo -k` -R/lib/`isainfo -k` -R/usr/lib/`isainfo -k`"

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
 --with-php-config=/usr/php/%{php_version}/bin/php-config \
 --with-yaml=/usr

gmake -j$CPUS
echo no | gmake test

%install

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20151012/
cp modules/yaml.so $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20151012/
mkdir -p  $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d/%{tarball_name}.ini

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20151012/
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20151012/yaml.so
%dir %attr(0755, root, sys) %{_sysconfdir}
%dir %attr(0755, root, bin) %{_sysconfdir}/php
%dir %attr(0755, root, bin) %{_sysconfdir}/php/%{php_version}
%dir %attr(0755, root, bin) %{_sysconfdir}/php/%{php_version}/conf.d
%{_sysconfdir}/php/%{php_version}/conf.d/*

%changelog
* Thu Oct 20 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
