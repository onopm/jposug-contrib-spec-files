%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  1.8.9
%define tarball_name     Mail_Mime
%define pear_dir   %(/usr/php/5.3/bin/pear config-get php_dir)

Name:                    SFEphp53-mail-mime
IPS_package_name:	 web/php-53/extension/php-mail-mime
Summary:                 PHP 5.3 module for MAIL_Mime
Version:                 %{tarball_version}
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
Mail_Mime provides classes to deal with the creation and manipulation of MIME messages.
It allows people to create e-mail messages consisting of:
* Text Parts
* HTML Parts
* Inline HTML Images
* Attachments
* Attached messages

It supports big messages, base64 and quoted-printable encodings and
non-ASCII characters in filenames, subjects, recipients, etc. encoded
using RFC2047 and/or RFC2231.

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
%{pear_dir}/.registry/mail_mime.reg

%changelog
* Thu Mar 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.8.9
* Sat Dec 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
