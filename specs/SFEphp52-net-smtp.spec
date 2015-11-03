%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  1.6.1
%define tarball_name     Net_SMTP
%define pear_dir   %(/usr/php/5.2/bin/pear config-get php_dir)

Name:                    SFEphp52-net-smtp
IPS_package_name:	 web/php-52/extension/php-net-smtp
Summary:                 PHP 5.2 module for Net_SMTP
Version:                 1.6.1
License:		 PHP License
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: %{pnm_buildrequires_SUNWphp52}
# BuildRequires: %{pnm_buildrequires_SUNWgsed_devel}

Requires: %{pnm_requires_SUNWphp52}
Requires: web/php-52/extension/php-net-socket

%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket class.

%prep

%setup -c -T

%build

%install

rm -rf %{buildroot}
/usr/php/5.2/bin/pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}

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
* Fri Jan 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requies
* Thu Oct 04 JST 2001 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Initial Commit
