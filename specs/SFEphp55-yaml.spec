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
%define php_version 5.5
%define tarball_version  1.3.0
%define tarball_name     yaml

Name:                    SFEphp55-yaml
IPS_package_name:	 web/php-55/extension/php-yaml
Summary:                 PHP 5.5 module for YAML
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

BuildRequires: web/php-55
BuildRequires: library/text/yaml >= 0.1.6
Requires: web/php-55
Requires: library/text/yaml >= 0.1.6
Requires: web/php-55/extension/php-date

# OpenSolaris IPS Package Manifest Fields
Meta(info.upstream):	 	http://code.google.com/p/php-yaml/
Meta(info.maintainer):	 	taki@justplayer.com
Meta(info.classification):	Development/PHP

%prep
%setup -c -n %tarball_name-%tarball_version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="-m64 -xO4 -xchip=pentium -xregs=no%frameptr -mt"
export CPPFLAGS="-m64 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
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

gmake -j$CPUS CFLAGS="$CFLAGS"
echo no | gmake test

%install

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/
cp modules/yaml.so $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/
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
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-20121212/yaml.so
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/php/%{php_version}/conf.d/*

%changelog
* Fri Sep 30 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Wed Mar 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.1.1
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
