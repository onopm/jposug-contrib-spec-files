%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  1.0.10
%define tarball_name     Net_Socket
%define pear_dir   %(/usr/php/5.3/bin/pear config-get php_dir)

Name:                    SFEphp53-net-socket
IPS_package_name:	 web/php-53/extension/php-net-socket
Summary:                 PHP 5.3 module for Net_Socket
Version:                 1.0.10
License:		 PHP License
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-53
# BuildRequires: %{pnm_buildrequires_SUNWgsed_devel}

Requires: web/php-53
# "pear/Net_Socket"
# "pear/Auth_SASL"

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep

%setup -c -T

%build

%install

rm -rf %{buildroot}
/usr/php/5.3/bin/pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}

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
%{pear_dir}/.registry/net_socket.reg

%changelog
* Sat Dec 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
