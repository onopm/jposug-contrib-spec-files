%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define php_version 5.3
%define tarball_version  1.4.7
%define tarball_name     Date
%define pear_dir   %(/usr/php/5.3/bin/pear config-get php_dir)

Name:                    SFEphp53-date
IPS_package_name:	 web/php-53/extension/php-date
Summary:                 PHP 5.3 module for Date
Version:                 1.4.7
License:		 BSD License
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
# Source1:                 %{name}.ini
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
#SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-53
BuildRequires: web/php-53/extension/php-net-smtp
# BuildRequires: %{pnm_buildrequires_SUNWgsed_devel}

Requires: web/php-53
Requires: web/php-53/extension/php-net-smtp

%description
Generic classes for representation and manipulation of
dates, times and time zones without the need of timestamps,
which is a huge limitation for PHP programs. Includes time zone data,
time zone conversions and many date/time conversions.
It does not rely on 32-bit system date stamps, so
you can display calendars and compare dates that date
pre 1970 and post 2038.

%prep

%setup -c -T

%build

%install

rm -rf %{buildroot}
/usr/php/%{php_version}/bin/pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}

# Clean up unnecessary files
rm %{buildroot}/%{pear_dir}/.filemap
rm %{buildroot}/%{pear_dir}/.lock
rm -rf %{buildroot}/%{pear_dir}/.registry/.channel*
rm -rf %{buildroot}%{pear_dir}/.channels
rm %{buildroot}%{pear_dir}/.depdb
rm %{buildroot}%{pear_dir}/.depdblock

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) /var/
%dir %attr(0755, root, bin) %{pear_dir}
%{pear_dir}/*
%{pear_dir}/.registry/date.reg

%changelog
* Sat Dec 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
