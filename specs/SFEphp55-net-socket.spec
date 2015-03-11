%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  1.0.14
%define tarball_name     Net_Socket
%define pear_dir   %(/usr/php/5.5/bin/pear config-get php_dir)

Name:                    SFEphp55-net-socket
IPS_package_name:	 web/php-55/extension/php-net-socket
Summary:                 PHP 5.5 module for Net_Socket
Version:                 1.0.10
License:		 PHP License
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-55
Requires: web/php-55

%description
Net_Socket is a class interface to TCP sockets. It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep

%setup -c -T

%build
gzip -dc %{SOURCE0} > %{tarball_name}-%{tarball_version}.tar

%install

rm -rf %{buildroot}
/usr/php/5.5/bin/pear -c pearrc install --nodeps --packagingroot %{buildroot} %{tarball_name}-%{tarball_version}.tar

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
%dir %attr(0755, root, bin) %{pear_dir}
%{pear_dir}/*
%{pear_dir}/.registry/net_socket.reg

%changelog
* Wed Mar 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.14
* Thu Jul 10 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
