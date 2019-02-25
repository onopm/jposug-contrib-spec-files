#
# To build SFEphp71-intl, use Oracle Developer Studio 12.5 or later
#
%include Solaris.inc

%define _prefix /usr
%define php_version 7.1
%define tarball_version  7.1.18
%define tarball_name     php
%define zts 20160303

Name:                    SFEphp71-intl
IPS_package_name:	 web/php-71/extension/php-intl
Summary:                 php-intl for PHP 7.1
Version:                 %{tarball_version}
License:		 PHP License
Url:                     http://www.php.net/
Source:			 http://jp.php.net/distributions/%{tarball_name}-%{tarball_version}.tar.bz2
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
#SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-71 >= %{version}
BuildRequires: text/gnu-sed
BuildRequires: developer/icu
BuildRequires: library/icu

Requires: web/php-71 >= %{version}
Requires: library/icu

%description
php-intl for PHP 7.1

%prep
%setup -c -n %name-%version

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS='-m64'
export CXXFLAGS='-m64'

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

pushd ext/intl
/usr/php/%{php_version}/bin/phpize
CFLAGS='-m64 -I../../Zend' \
      ./configure \
      --with-php-config=/usr/php/7.1/bin/php-config \
      --enable-intl
gmake -j$CPUS
# gmake -j$CPUS test
popd

%install

cd %{tarball_name}-%{tarball_version}
mkdir -p $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d

pushd ext/intl
make install INSTALL_ROOT=$RPM_BUILD_ROOT \
     PECL_EXTENSION_DIR=%{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-%{zts}/ \
     PECL_INCLUDE_DIR=%{_prefix}/php/%{php_version}/include
popd
cat > $RPM_BUILD_ROOT/etc/php/%{php_version}/conf.d/intl.ini <<EOF
; Enable intl extension module
extension=intl.so
EOF

## %{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions
%dir %attr(0755, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-%{zts}
%attr(0444, root, bin) %{_prefix}/php/%{php_version}/lib/extensions/no-debug-non-zts-%{zts}/intl.so
%dir %attr(0755, root, sys) %{_sysconfdir}
%{_sysconfdir}/php/%{php_version}/conf.d/intl.ini

%changelog
* Fri Jun 01 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.1.18
* Wed Nov 29 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.1.12, add CFLAGS and CXXFLAGS
* Tue Nov 28 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
