%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define php_version 5.3
%define tarball_version  1.6.2
%define tarball_name     Net_SMTP
%define pear_dir   %(/usr/php/5.3/bin/pear config-get php_dir)

Name:                    SFEphp53-net-smtp
IPS_package_name:	 web/php-53/extension/php-net-smtp
Summary:                 PHP 5.3 module for Net_SMTP
Version:                 1.6.2
License:		 PHP License
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
# SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-53
# BuildRequires: %{pnm_buildrequires_SUNWgsed_devel}

Requires: web/php-53
Requires: web/php-53/extension/php-net-socket

%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

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
%{pear_dir}/.registry/net_smtp.reg

%changelog
* Tue Nov 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.2
* Fri Jan 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requies
* Sat Dec 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
