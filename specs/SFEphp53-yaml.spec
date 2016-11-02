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
%define php_version 5.3
%define tarball_version  1.1.1
%define tarball_name     yaml

Name:                    SFEphp53-yaml
IPS_package_name:	 web/php-53/extension/php-yaml
Summary:                 PHP 5.3 module for YAML
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

BuildRequires: web/php-53
BuildRequires: library/text/yaml >= 0.1.6

Requires: web/php-53
Requires: library/text/yaml >= 0.1.6
Requires: web/php-53/extension/php-date

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
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="%_ldflags"
export CC=cc

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
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/modules/
cp modules/yaml.so $RPM_BUILD_ROOT/%{_prefix}/php/%{php_version}/modules/
mkdir -p  $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d/%{tarball_name}.ini

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/modules
%attr(0444, root, bin) /usr/php/5.3/modules/yaml.so
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/php/%{php_version}/conf.d/*

%changelog
* Thu Mar 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.1.1
* Wed Apr 02 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- specify required version of library/text/yaml (CVE-2014-2525)
* Wed Jan 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify %files
* Sat Dec 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- add BuildRequires
