%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  2.1.1
%define tarball_name     Net_URL2
%define pear_dir   %(/usr/php/5.5/bin/pear config-get php_dir)

Name:                    SFEphp55-net-url2
IPS_package_name:	 web/php-55/extension/php-net-url2
Summary:                 PHP 5.5 module for Net_URL2
Version:                 %{tarball_version}
License:		 BSD-3-Clause
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
Provides parsing of URLs into their constituent parts (scheme, host, path etc.), URL generation, and resolving of relative URLs.

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
%{pear_dir}/.registry/net_url2.reg

%changelog
* Wed Mar 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.1
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
