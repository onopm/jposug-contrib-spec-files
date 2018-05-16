#
# spec file for package postfixadmin
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
%include Solaris.inc
%include packagenamemacros.inc
%include base.inc
Name:           SFEpostfixadmin
%define src_name postfixadmin
IPS_Package_Name:       web/frontends/postfixadmin
Version:        2.3.7
Url:            http://ftp.jaist.ac.jp/pub/sourceforge/p/po/postfixadmin/postfixadmin/ 
License:        GPL
SUNW_Copyright: %{name}.copyright
Source0:        %{url}/%{src_name}-%{version}/%{src_name}-%{version}.tar.gz
Source1:	%{name}-%{src_name}.conf	
SUNW_BaseDir:   /
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%define runuser         vacation
#%define runuserid       161
%define runusergroup    vacation
#%define rungroupid      181

# Web interface
#%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
#  # Requires:   mod_php_any # no idea in which fedora package mod_php5 is...
#Requires:       php_database
#%else
#Requires:       mod_php_any
#Requires:       php_any_db
#Requires:     web/php-53
#Requires:     web/php-53/extension/php-mysql
#%endif

Requires:       service/network/smtp/postfix
#Requires:       php-mbstring
#Requires:       php-spl

# test/*, xmlrpc.php, squirrelmail plugin
# big dependency, not needed by all users - therefore no hard Requirement
#%if 0%{?suse_version}
#Recommends:     php5-ZendFramework
#%endif

#TODO: not yet supported
## vacation.pl
#Requires:       perl(DBI)
#Requires:       perl(Email::Valid)
#Requires:       perl(Getopt::Std)
#Requires:       perl(Log::Log4perl)
#Requires:       perl(MIME::Base64)
#Requires:       perl(MIME::EncWords)
#Requires:       perl(Mail::Sender)
#Requires:       perl(strict)

## cleanupdirs.pl
#Requires:       perl(File::Path)
#Requires:       perl(Getopt::Long)
## mkeveryone.pl
#Requires:       perl(Fcntl)
#Requires:       perl(IO)
#Requires:       perl(IO::File)
#Requires:       perl(POSIX)
#Requires:       perl(Time::Local)
## fetchmail.pl
#Requires:       perl(File::Temp)
#Requires:       perl(LockFile::Simple)
#Requires:       perl(Sys::Syslog)

#%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
# create vacation user/group
#PreReq:         shadow-utils
#BuildRequires:  httpd-devel
#%define serverroot %(/usr/sbin/apxs -q datadir 2>/dev/null || /usr/sbin/apxs -q PREFIX)
#%else
# create vacation user/group
#PreReq:         pwdutils
BuildRequires:   %pnm_buildrequires_apch22 
Requires:   %pnm_requires_apch22 
%define serverroot %(/usr/bin/apxs -q datadir 2>/dev/null)/
%define apacheconfdir %(/usr/bin/apxs -q sysconfdir 2>/dev/null)/conf.d
#Suggests:       php-pgsql
#%endif
#BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:        %{pnm_requires_runtime_python_26}

Summary:        Web-based management tool for Postfix virtual domains, mailboxes and aliases
License:        GPL-2.0+
Group:          Productivity/Networking/Web/Frontends

%description
PostfixAdmin is a PHP based application that handles Postfix Style Virtual Domains and
Users that are stored in MySQL or PostgreSQL.

Postfix Admin supports:
- Virtual Mailboxes / Virtual Aliases / Forwarders
- Alias domains (Domain to Domain forwarding with recipient validation)
- Vacation (auto-response) for Virtual Mailboxes.
- Quota / Alias & Mailbox limits per domain.
- Fetchmail integration
- Packaged with over 25 languages.

%prep
%setup -q -n %{src_name}-%version

%build
echo "*** serverroot: %{serverroot} ***"
echo "*** buildroot: %{buildroot} ***"
/bin/rm -rf %{buildroot}

%install
#mkdir -p -m0755 %{buildroot}%{_sysconfdir}/%{src_name}
#mkdir -p -m0755 %{buildroot}%{_datadir}/%{src_name}
mkdir -p -m0755 %{buildroot}%{serverroot}/%{src_name}
mkdir -p -m0755 %{buildroot}%{_localstatedir}/spool/vacation
mkdir -p -m0755 %{buildroot}/%{_prefix}/lib/%{src_name}

# install the config files
#install -m 0640 config.inc.php.sample %{buildroot}%{_sysconfdir}/%{src_name}/config.inc.php
#ln -s ../../../..%{_sysconfdir}/%{src_name}/config.inc.php \
#    %{buildroot}%{_datadir}/%{src_name}/config.inc.php

install -m 0644 *.php motd*.txt %{buildroot}%{serverroot}/%{src_name}/

mv VIRTUAL_VACATION/vacation.pl %{buildroot}%{_prefix}/lib/%{src_name}/
# compatibility symlink to match documentation
( cd %{buildroot}%{_localstatedir}/spool/vacation/ && ln -s ../../../usr/lib/%{src_name}/vacation.pl )

# copy over the rest
for d in admin images languages model templates users css; do
    cp -rp $d %{buildroot}%{serverroot}/%{src_name}/
done

# remove files related to debian packaging (to avoid it's copied as %doc)
rm -r ADDITIONS/squirrelmail-plugin/debian/
cp -rp ADDITIONS %{buildroot}%{_prefix}/lib//%{src_name}/
chmod 755 %{buildroot}%{_prefix}/lib/%{src_name}/ADDITIONS/*.{pl,sh,py}

# install the config file
mkdir -p %{buildroot}%{apacheconfdir}
install -m 644 %{SOURCE1} %{buildroot}%{apacheconfdir}/%{src_name}.conf

#%pre
#getent group  vacation >/dev/null || groupadd vacation || :
#getent passwd vacation >/dev/null || useradd -c "Virtual Vacation" -d %{_localstatedir}/spool/vacation -s /sbin/nologin -M -r -g vacation vacation || :
## fix group for vacation user (if created by older versions (< 2012-02-13) of this package, it was created with group users)
#usermod -g vacation vacation || :
#
##if [ -z "`grep vacation /etc/postfix/master.cf 2>/dev/null`" ]; then
##cat <<'EOF' >>/etc/postfix/master.cf
### Postfix Admin Vacation
##vacation	unix	-	n	n	-	-	pipe
##	flags=Rq user=vacation argv=/usr/lib/postfixadmin/vacation.pl -f ${sender} -- ${recipient}
##EOF
##fi
#
##%preun
##if [ $1 = 0 ]; then
##    /usr/sbin/userdel vacation 2>/dev/null || :
##fi

#%actions
#group groupname="%{rundropgroup}" gid="%{rundropgroupid}"
#group groupname="%{rungroup}" gid="%{rungroupid}"
#user ftpuser=false gcos-field="Postfix user" username="%{runuser}" uid="%{runuserid}" password=NP group="%{runusergroup}" home-dir="%{_localstatedir}/spool/postfix" login-shell="/bin/true" group-list="mail"
%actions
group groupname="%{runusergroup}"
user ftpuser=false gcos-field="Postadmin user" username="%{runuser}" password=NP group="%{runusergroup}" home-dir="%{_localstatedir}/spool/vacation" login-shell="/bin/true"

%files
%defattr(-,root,bin)
%config(noreplace) %{apacheconfdir}/*.conf
%doc DOCUMENTS/* *.TXT VIRTUAL_VACATION/*
%dir %attr (0755, root, sys) /var
%dir /var/apache2
/var/apache2/2.2/%src_name/a*
/var/apache2/2.2/%src_name/b*
/var/apache2/2.2/%src_name/create*
/var/apache2/2.2/%src_name/css/*
/var/apache2/2.2/%src_name/common*
/var/apache2/2.2/%src_name/d*
/var/apache2/2.2/%src_name/e*
/var/apache2/2.2/%src_name/f*
/var/apache2/2.2/%src_name/i*
/var/apache2/2.2/%src_name/l*
/var/apache2/2.2/%src_name/m*
/var/apache2/2.2/%src_name/p*
/var/apache2/2.2/%src_name/s*
/var/apache2/2.2/%src_name/t*
/var/apache2/2.2/%src_name/u*
/var/apache2/2.2/%src_name/v*
/var/apache2/2.2/%src_name/x*
%config(noreplace) /var/apache2/2.2/%src_name/config.inc.php
#%dir %{serverroot}/%{src_name}
#%{serverroot}/%{src_name}/*
%dir %{_prefix}/lib/%{src_name}/
%{_prefix}/lib/%{src_name}/ADDITIONS/
%attr(750,root,vacation) %{_prefix}/lib/%{src_name}/vacation.pl
%attr(1770,root,vacation) %dir %{_localstatedir}/spool/vacation
%{_localstatedir}/spool/vacation/vacation.pl

%changelog
* Wed June 11 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial commit for jposug
- Erase dependency for php. Because we have different versions of php.
- TODO: vacation.pl is not yet supported
* Wed Jan  2 2013 opensuse@cboltz.de
- update to PostfixAdmin 2.3.6 (bugfix release)
  changes that were not included in the package yet:
  - fix double inclusion of config.inc.php in setup.php
  - fix bool and date handling in fetchmail
- remove upstreamed patches
* Fri Nov 30 2012 opensuse@cboltz.de
- more cross-distributin %%if: pwdutils, php_any_db
* Mon Nov 26 2012 Ralf Lang <lang@b1-systems.de>
- require php-mbstring as setup.php reports this as a hard dependency
* Thu Jun 28 2012 opensuse@cboltz.de
- fix footer link (upstream r1402)
- focus username field in login form (upstream r1404)
- change existing vacation user (< 2012-02-13) to group vacation
* Sun Jun  3 2012 opensuse@cboltz.de
- add some %%if for cross-distribution handling
* Mon Feb 13 2012 opensuse@cboltz.de
- add vacation user to the vacation group (instead of the default "users")
* Thu Feb  9 2012 opensuse@cboltz.de
- update r1342 patch to fix SLE_10 build failure
* Thu Feb  2 2012 opensuse@cboltz.de
- add patch to display domain and mailbox description with correct
  encoding (upstream r1342)
* Thu Jan 26 2012 opensuse@cboltz.de
- update to PostfixAdmin 2.3.5 (security release)
  - fixes some SQL injections (CVE-2012-0811)
  - fixes some XSS vulnerabilities (CVE-2012-0812)
  - see CHANGELOG.TXT or bnc#741455 for details
* Sun Oct 16 2011 opensuse@cboltz.de
- include a patch with fixes since the 2.3.4 release (see
  CHANGELOG.TXT for details)
- Add PreReq: pwdutils
* Fri Sep 16 2011 opensuse@cboltz.de
- 2.3.4 release (bugfix release, see CHANGELOG.TXT for details)
* Sun Aug 28 2011 opensuse@cboltz.de
- move vacation.pl and ADDITIONS to /usr/lib/postfixadmin/
* Mon Aug  1 2011 opensuse@cboltz.de
- spec cleanup (manually + spec-cleaner)
- create vacation user
- move %%changelog to .changes
* Tue Mar 15 2011 Christian Boltz <opensuse@cboltz.de>
- 2.3.3 release
  bugfix release for 2.3.2 - see CHANGELOG.TXT for details
* Tue Aug 24 2010 Christian Boltz <opensuse@cboltz.de>
- 2.3.2 release
  bugfix release for 2.3.1 - see CHANGELOG.TXT for details
* Fri Jul  9 2010 Christian Boltz <opensuse@cboltz.de>
- 2.3.1 release
  bugfix release for 2.3 - see CHANGELOG.TXT for details
* Wed Oct 28 2009 Christian Boltz <opensuse@cboltz.de>
- 2.3 release
  Most important changes:
  * Improved Aliased domains support (no longer relying on catch-all domains) -
    Note this requires Postfix configuration changes; old configuration(s) will
    continue to work.
  * Security fix for setup.php (password required to access; setup.php can
    generate this and help you)
  * Superadmin can now setup fetchmail for all users
  * Enhanced fetchmail.pl script (file locking, syslog logging, configuration
    file etc)
  * Added dovecot quota support (documentation + viewing in Postfixadmin) for
    dovecot 1.0/1.1 and >= 1.2
  * Vacation re-notification after defineable timeout (default remains to
    notify only once)
  * Refactoring of /users (see /model) and XmlRpc interface for remote mail
    clients (E.g. squirrelmail-postfixadmin)
  * Add dovecot password support (see here)
  * Added support for courier authlib authentication flavours
    ($CONF['authlib_default_flavor'])
  * update.php should handle all database updates for you
  * Lots of small updates and random new minor features
  * bug fixes ;-)
* Thu Jul 24 2008 Christian Boltz <opensuse@cboltz.de>
- updated to 2.2.1.1 (fixed version number displayed in the footer)
* Tue Jul 22 2008 Christian Boltz <opensuse@cboltz.de>
- updated to 2.2.1 (fixes several bugs, no new features)
* Sun Jun  8 2008 Christian Boltz <opensuse@cboltz.de>
- finally created a package for the 2.2.0 release
* Fri Feb 29 2008 Christian Boltz <opensuse@cboltz.de>
- updated spec to follow the *.css move to css/
* Sun Dec  2 2007 Christian Boltz <opensuse@cboltz.de>
- updated to SVN version
- commented out several sections
- auto-detect serverroot and install PHP files etc. there
* Fri Dec 15 2006 lfarkas@lfarkas.org
- initial build
