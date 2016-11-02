%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  1.2.0
%define tarball_name     Mail
%define pear_dir   %(/usr/php/5.3/bin/pear config-get php_dir)

Name:                    SFEphp53-mail
IPS_package_name:	 web/php-53/extension/php-mail
Summary:                 PHP 5.3 module for MAIL
Version:                 1.2.0
License:		 BSD Style
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
# Source1:                 %{name}.ini
Patch0:                   Mail-1.2.0-php53.patch
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/php-53
BuildRequires: web/php-53/extension/php-net-smtp

Requires: web/php-53
Requires: web/php-53/extension/php-net-smtp

%description
PEAR's Mail package defines an interface for implementing mailers under the PEAR hierarchy. It also provides supporting functions useful to multiple mailer backends. Currently supported backends include: PHP's native mail() function, sendmail, and SMTP. This package also provides a RFC822 email address list validation utility class.

%prep

# %setup -c -T
%setup -c -n %{tarball_name}-%{tarball_version}
%patch0 -p0

%build

%install

rm -rf %{buildroot}
/usr/php/5.3/bin/pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}
install Mail-1.2.0/Mail/smtp.php %{buildroot}/var/php/5.3/pear/Mail/smtp.php

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
%{pear_dir}/.registry/mail.reg

%changelog
* Thu Jan 17 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add patch0
* Sat Dec 15 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
