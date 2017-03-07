%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  1.5.5
%define tarball_name     Mail_mimeDecode
%define pear_dir   %(/usr/php/5.3/bin/pear config-get php_dir)

Name:                    SFEphp53-mail-mimedecode
IPS_package_name:	 web/php-53/extension/php-mail-mimedecode
Summary:                 PHP 5.3 module for MAIL_mimeDecode
Version:                 1.5.5
License:		 BSD Style
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
# Source1:                 %{name}.ini
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-53

Requires: web/php-53

%description
Provides a class to deal with the decoding and interpreting of mime messages.
This package used to be part of the Mail_Mime package, but has been split off.

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
%{pear_dir}/.registry/mail_mimedecode.reg

%changelog
* Sat Dec 15 JST 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
