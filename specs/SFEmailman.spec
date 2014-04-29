#
# spec file for package mailman
# Rewritten for OpenSolaris
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc
Name:           SFEmailman
IPS_package_name: application/internet/mailman
SUNW_Copyright:   %{name}.copyright
%define src_name mailman
%define versionjp +j7
# Now, the user and group the scripts will actually execute as.
%define mmuser       mailman
%define mmuserid     41
%define mmgroup      mailman
%define mmgroupid    41
%define fakemailgroup   nobody
%define fakecgigroup   webservd
%define svcdir %{_localstatedir}/svc/manifest/application/internet
%include default-depend.inc
#!BuildIgnore: sendmail
BuildRequires:  %{pnm_buildrequires_krb}
BuildRequires:  %{pnm_buildrequires_SUNWpcre_devel}
BuildRequires:  %{pnm_buildrequires_runtime_python_26}
#BuildRequires:  postfix
#BuildRequires:  pwdutils
Requires:  %{pnm_requires_runtime_python_26}
#%define DISTRIBUTABLE 1
Url:            http://docs.python.jp/contrib/mailman/
#Requires:       cron
#Requires:       logrotate
Requires:       %{pnm_requires_runtime_python_26}
Requires:       service/network/smtp/postfix
Requires:       %{pnm_requires_web_browser_w3m}
Requires:       %{pnm_requires_runtime_python_26}
Requires:       library/python-2/kanjifilter
#PreReq:         /usr/sbin/useradd /usr/sbin/groupadd /bin/echo /bin/cp /bin/rm /bin/mkdir /usr/bin/awk /usr/bin/touch /usr/bin/getent openssl
#PreReq:         permissions
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc
Requires:      system/library/gcc-runtime
%endif
Summary:        The GNU Mailing List Manager
License:        GPL-2.0+
Group:          Productivity/Networking/Email/Mailinglists
Version:        2.1.14
Release:        14.1.3
Source0:        http://docs.python.jp/contrib/mailman/_static/%{src_name}-%{version}%{versionjp}.tgz
#Source1:        README.SuSE
Source2:        mailman-2.1-manpages.tgz
#%if %DISTRIBUTABLE
#Source4:        SuSEconfig.mailman
#%else
#Source4:        SuSEconfig.mailman-SuSE
#%endif
#Source5:        rcmailman
Source6:        %{name}-aliases
#Source7:        sysconfig.mailman
Source8:        %{name}-mailman.sgidlist
Source9:        %{name}-mailman-apache2.conf
#Source11:       logrotate.mailman
Source12:       %{name}-mm-text.png
Source20:	%{name}-mailman.xml
Source21:	%{name}-svc-mailman
#That's a SuSEism.  They patch the mail-wrapper program so that it fetches the mail group number from
#/etc/mailman.mail-gid at runtime rather than building it (options --with-cgi-gid and --with-mail-gid)
#into the wrapper the way the normal Mailman distribution does.  Check what has happened to your
#/etc/mailman.mail-gid file.
Patch1:         mailman-wrapper.patch
#%if %DISTRIBUTABLE
#%else
#Patch2:         mailman-SuSE.patch
#%endif
Patch3:         mailman-2.1.14-python.dif
Patch5:         mailman-2.1.14-editarch.patch
Patch6:         mailman-2.1.14-misc-PACKAGES.diff
Patch7:         mailman-2.1.2-list_lists.patch
Patch10:        mailman-2.1.4-dirmode.patch
Patch11:        mailman-2.1.4-notavaliduser.patch
Patch17:        mailman-weak-password.diff
Patch19:        mailman-python24.patch
#%if %DISTRIBUTABLE
#%else
#Patch20:        mailman-SuSE2.patch
#%endif
# created by the jposug
Patch30:	mailman-2.1.14-defaults.patch
Patch31:	mailman-2.1.14-mm_cfg.patch
BuildRoot:      %{_tmppath}/%{src_name}-%{version}-build
#%define       m_uid %mmgroupid
#/etc/mailman.mail-gid
#%define       m_gid %mmgroupid
%define       apache2_confd       %(/usr/bin/apxs -q sysconfdir 2>/dev/null)/conf.d
%define       sendmail_libd       %{_libdir}/sendmail.d
%define       mailman_confd       /etc/mailman
# ----------------------------------------------------------------------------

%description
This is the GNU Mailing List manager. Mailman provides an
easy-to-configure means of maintaining mailing lists including Web
administration. Mailman is written in Python.



Authors:
--------
    John Viega <mailman-users@python.org>

%prep
%setup -q -n %{src_name}-%{version}%{versionjp}
%patch1
#%if %DISTRIBUTABLE
#%else
#%patch2
#%endif
%patch3
%patch5 -p1
%patch6 -p1
%patch7
%patch10 -p1
%patch11 -p1
%patch17 -p1
%patch19
#%if %DISTRIBUTABLE
#%else
#%patch20
#%endif
%patch30 -p1 -b .orig
%patch31 -p1 -b .orig
#cp -av %{S:1} .
# ----------------------------------------------------------------------------

%build
export CC=gcc
export CXX=g++
export CFLAGS="%optflags -fno-strict-aliasing -Wno-pointer-sign"
export CPPFLAGS=""
export LDFLAGS="%{_ldflags}"
#/usr/sbin/groupadd -g %{m_gid} -o -r mailman 2> /dev/null || :
#/usr/sbin/useradd -r -o -g mailman -u %{m_uid} -s /bin/bash -c "GNU mailing list manager" -d /var/lib/mailman mailman 2> /dev/null || :
./configure --prefix=%{_libdir}/mailman --sysconfdir=/etc --with-python=/bin/python \
	--localstatedir=/var/run --libexecdir=%{_libdir}/mailman \
	--mandir=%{_mandir} --with-groupname=mailman --with-username=mailman \
	--with-var-prefix=/var/lib/mailman \
        --without-permcheck \
	--with-cgi-gid=%{fakecgigroup} --with-mail-gid=%{fakemailgroup} # fake
make OPT="$RPM_OPT_FLAGS -fpie -pie"
# ----------------------------------------------------------------------------

%install
#install -d $RPM_BUILD_ROOT/{usr/sbin,etc/{mailman,sysconfig,init.d,logrotate.d},var/adm/fillup-templates,sbin/conf.d}/
install -d $RPM_BUILD_ROOT/etc/mailman/
make DESTDIR=$RPM_BUILD_ROOT install
# add a hint to the crontab
cat <<EOF > $RPM_BUILD_ROOT%{_libdir}/mailman/cron/crontab
#
# if you want to make changes to this file, please modify 
# /usr/lib/mailman/cron/crontab and restart mailman
#
EOF
# add user mailman in column 6 since we are going to use it as system crontab
awk '/^[0-9,\*]/ { print $1 " " $2 " " $3 " " $4 " " $5 " mailman " $6 " " $7 " " $8 } /^\#/ { print $0 }' \
	$RPM_BUILD_ROOT%{_libdir}/mailman/cron/crontab.in \
	>> $RPM_BUILD_ROOT%{_libdir}/mailman/cron/crontab
# write initial wrapper id files:
#. %{S:7}
getent group %{fakecgigroup} | cut -d: -f3 > $RPM_BUILD_ROOT/%{mailman_confd}/mailman.cgi-gid
getent group %{fakemailgroup} | cut -d: -f3 > $RPM_BUILD_ROOT/%{mailman_confd}/mailman.mail-gid
# SuSEconfig stuff:
#install -m 644 %{S:7} $RPM_BUILD_ROOT/var/adm/fillup-templates/
#install -m 755 %{S:4} $RPM_BUILD_ROOT/sbin/conf.d/SuSEconfig.mailman
install -m 644 %{S:8} %{buildroot}%{_libdir}/mailman/sgidlist
# start script:
#ln -sf ../../etc/init.d/mailman $RPM_BUILD_ROOT/usr/sbin/rcmailman
#install -m 755 %{S:5} $RPM_BUILD_ROOT/etc/init.d/mailman
# make sure there is a valid  group writable aliases.db
# if the aliases.db would be generated later on, list creation
# through the web interface would not work!
install -m 664 %{S:6} $RPM_BUILD_ROOT/var/lib/mailman/data/aliases
# created in %%post and marked as %%ghost in the file section, so simply fake it:
/usr/bin/touch $RPM_BUILD_ROOT/var/lib/mailman/data/aliases.db
# apache stuff:
mkdir -p $RPM_BUILD_ROOT/%{apache2_confd}
cp -av %{S:9} $RPM_BUILD_ROOT/%{apache2_confd}/mailman.conf
# link to enhance interoperability with Sendmail
mkdir -p $RPM_BUILD_ROOT/%{sendmail_libd}/bin
ln -sf ../../../lib/mailman/mail/mailman $RPM_BUILD_ROOT/%{sendmail_libd}/bin/mailman
/bin/rm -rf $RPM_BUILD_ROOT%{_mandir}/man8/*
install -d $RPM_BUILD_ROOT%{_mandir}/man8/
tar xz --overwrite -C $RPM_BUILD_ROOT%{_mandir}/man8/ -f %SOURCE2
gzip -f $RPM_BUILD_ROOT%{_mandir}/man8/*
#install -m 644 %{S:11} $RPM_BUILD_ROOT/etc/logrotate.d/mailman
#%if %DISTRIBUTABLE
#%else
cp %SOURCE12 $RPM_BUILD_ROOT%{_libdir}/mailman/icons/mm-text.png
#%endif
mkdir -p "${RPM_BUILD_ROOT}%{svcdir}"
cp "%{SOURCE20}" "${RPM_BUILD_ROOT}%{svcdir}/mailman.xml"
mkdir -p "${RPM_BUILD_ROOT}/lib/svc/method"
cp "%{SOURCE21}" "${RPM_BUILD_ROOT}/lib/svc/method/svc-mailman"
# ----------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT
# ----------------------------------------------------------------------------

#%pre
#/usr/sbin/groupadd -g %{m_gid} -o -r mailman 2> /dev/null || :
#/usr/sbin/useradd -r -o -g mailman -u %{m_uid} -s /bin/bash -c "GNU mailing list manager" -d /var/lib/mailman mailman 2> /dev/null || :
#exit 0
# ----------------------------------------------------------------------------

#%post
#%{fillup_and_insserv mailman}
#%run_permissions
#if [ -e var/lib/mailman/logs/error ]; then
#	chown wwwrun.mailman var/lib/mailman/logs/error
#else
#	install -m 664 -o wwwrun -g mailman /dev/null var/lib/mailman/logs/error 
#fi
## handle very old installations
#test -d var/spool/mailman && {
#	echo -n "Moving /var/spool/mailman -> /var/lib/mailman... "
#	(cd var/lib/mailman && cp -a var/spool/mailman/* .)  && rm -rf var/spool/mailman
#	echo "Done."
#}
#echo "All done."
## use Mailman facilities for updating old data
#usr/lib/mailman/bin/update
#if test -z "$YAST_IS_RUNNING" ; then
#	echo "Please remember to run 'SuSEconfig --module mailman' to configure mailman"
#fi
## re-create the list aliases 
#usr/lib/mailman/bin/genaliases > /dev/null
## update the alias db file and make it group-writeable (important for being able to create mailing lists thru the web interface)
#if [ -x usr/sbin/postalias -a -r var/lib/mailman/data/aliases ]; then usr/sbin/postalias var/lib/mailman/data/aliases; chmod g+w var/lib/mailman/data/aliases.db; fi
#exit 0
# ----------------------------------------------------------------------------
#%verifyscript
#%verify_permissions -f %{_libdir}/mailman/sgidlist

#%preun
#%stop_on_removal mailman
## ----------------------------------------------------------------------------

#%postun
#%restart_on_update mailman
#%{insserv_cleanup}
## ----------------------------------------------------------------------------

%actions
group groupname="%{mmgroup}" gid="%{mmgroupid}"
user ftpuser=false gcos-field="GNU Mailing List Manager" username="%{mmuser}" uid="%{mmuserid}" password=NP group="%{mmgroup}" home-dir="%{_localstatedir}/lib/%{src_name}" login-shell="/bin/true"

%files
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/application
%dir %attr (0755, root, sys) %svcdir
%class(manifest) %attr (0444, root, sys) %svcdir/mailman.xml
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/svc-mailman
%defattr(0755, root, bin)
%doc ACKNOWLEDGMENTS BUGS FAQ INSTALL NEWS TODO UPGRADING contrib doc/mailman-admin
%doc README README.*
%dir %attr (0755, root, sys) /usr/share
%dir %{_mandir}
%dir %{_mandir}/man8
%{_mandir}/man8/*.8.gz
%dir %{mailman_confd}
#%config(noreplace) /etc/logrotate.d/mailman
%config(noreplace) %attr(644, root, bin) %{mailman_confd}/mailman.*-gid
%dir %attr(2755, root, mailman) %{_libdir}/mailman/
%{_libdir}/mailman/sgidlist
#%{_libdir}/mailman/sgidlist/*
#%attr(-, root, mailman) %{_libdir}/mailman/[^Mmc]*
%dir %attr(-, root, mailman) %{_libdir}/mailman/cron
%attr(-, root, mailman) %{_libdir}/mailman/cron/*
%dir %attr(-, root, mailman) %{_libdir}/mailman/cgi-bin
%attr(2755, root, mailman) %{_libdir}/mailman/cgi-bin/*
#%verify(not mode) %attr(2755, root, mailman) %{_libdir}/mailman/cgi-bin/*
%dir %attr(2755, root, mailman) %{_libdir}/mailman/Mailman/
#%{_libdir}/mailman/Mailman/[^m]*
%{_libdir}/mailman/Mailman/A*
%{_libdir}/mailman/Mailman/B*
%{_libdir}/mailman/Mailman/C*
%{_libdir}/mailman/Mailman/D*
%{_libdir}/mailman/Mailman/E*
%{_libdir}/mailman/Mailman/G*
%{_libdir}/mailman/Mailman/H*
%{_libdir}/mailman/Mailman/L*
%{_libdir}/mailman/Mailman/M*
%{_libdir}/mailman/Mailman/P*
%{_libdir}/mailman/Mailman/Q*
%{_libdir}/mailman/Mailman/S*
%{_libdir}/mailman/Mailman/T*
%{_libdir}/mailman/Mailman/U*
%{_libdir}/mailman/Mailman/V*
%{_libdir}/mailman/b*
%{_libdir}/mailman/i*
%{_libdir}/mailman/p*
%{_libdir}/mailman/t*
%{_libdir}/mailman/Mailman/OldStyleMemberships.py*
%{_libdir}/mailman/Mailman/__init__.py*
%{_libdir}/mailman/Mailman/htmlformat.py*
%{_libdir}/mailman/Mailman/i18n.py*
%{_libdir}/mailman/Mailman/versions.py*
%{_libdir}/mailman/scripts/*
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr(0755, root, other) %{_localstatedir}/lib
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/archives
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/archives/public
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/archives/private
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/lists
%attr(644, root, %{fakemailgroup}) %{_localstatedir}/lib/mailman/data/sitelist.cfg
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/logs
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/qfiles
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/locks
%dir %attr(2775, root, mailman) %{_localstatedir}/lib/mailman/spam
#%attr(-, root, mailman) %{_libdir}/mailman/Mailman/[^m]*
%attr(-, root, mailman) %{_libdir}/mailman/messages
%dir %attr(-, root, mailman) %{_libdir}/mailman/mail
%verify(not mode) %attr(2755, root, mailman) %{_libdir}/mailman/mail/mailman
%config(noreplace) %attr(-, root, mailman) %{_libdir}/mailman/Mailman/m*
%dir %attr(2755, root, mailman) /var/lib/mailman/
#%attr(-, root, mailman) /var/lib/mailman/[^d]*
%dir %attr(2775, root, mailman) /var/lib/mailman/data
#%config(noreplace) %attr(-, root, mailman) /var/lib/mailman/data/[^a]*
%config(noreplace) %attr(-, root, mailman) /var/lib/mailman/data/aliases
%ghost %attr(0664, root, mailman) /var/lib/mailman/data/aliases.db
#%dir %attr(0775, root, sys) %{_localstatedir}/adm
#%{_localstatedir}/adm/fillup-templates/*
#%dir %attr (0755, root, sys) /sbin
#/sbin/conf.d/*
#%dir %attr (0755, root, bin) /usr/sbin
#/etc/init.d/*
%dir /etc/apache2
%dir %{apache2_confd}
%config (noreplace) %attr(644, root, bin) %{apache2_confd}/mailman.conf
%dir %{sendmail_libd}
%dir %{sendmail_libd}/bin
%{sendmail_libd}/bin/mailman
# ----------------------------------------------------------------------------

%changelog
* Tue Apr 29 2014 YAMAMOTO Takashi <yamachan@selfnavi.com>
- delete a patch mailman-2.1.5-no_extra_asian.dif 
* Mon Apr 28 2014 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Rewritten for OpenSolaris.
- Introduced Japanese version (+j*) and python kanji code filter.
* Fri Mar  2 2012 opensuse@cboltz.de
- add "su mailman mailman" to logrotate config (bnc#750259)
* Wed Apr 20 2011 jmatejek@novell.com
- fixed bug where it is impossible to edit archives (updated
  patch 2.1.14-editarch.patch)
* Wed Feb 23 2011 matejcik@suse.cz
- fixed a XSS vulnerability in confirm.py (CVE-2011-0707, bnc#671745)
* Mon Nov 15 2010 dmueller@suse.de
- update to 2.1.14:
  - Two potential XSS vulnerabilities have been identified and fixed.
  - Various i18n updates
  - A new feature for controlling the addition/replacement of the Sender:
  header in outgoing mail has been implemented.  This allows a list owner
  to set include_sender_header on the list's General Options page in the
  admin GUI.  The default for this setting is Yes which preserves the prior
  behavior of removing any pre-existing Sender: and setting it to the
  list's -bounces address.  Setting this to No stops Mailman from adding or
  modifying the Sender: at all.
  - long list of bug fixes and enhancements, see included NEWS for details
* Tue Nov  3 2009 coolo@novell.com
- updated patches to apply with fuzz=0
* Sun Nov 30 2008 rommel@suse.de
- the previous 'fix' of removing Mailman's own version of email was a bit crude
  and broke Mailman in several places (bug #448530)
  I replaced it with the upstream fix to 'configure' by Barry Warshaw
  (see http://bazaar.launchpad.net/~barry/mailman/py26/changes)
* Wed Nov 12 2008 rommel@suse.de
- added fix to work around md5/sha deprecation warning when hashlib is available
  (mailman-python-26-deprecation-md5-sha.diff)
- removed group writable bit from /usr/lib/mailman/Mailman/
- removing Mailman's own version of email when building against >= Python 2.6
* Tue Aug 26 2008 rommel@suse.de
- version update to 2.1.11 (security fixes and small, but compatible enhancements)
- removed outdated (>4y) extra FAQ
- updated README.SuSE
- reworked (internally used) category patch + added referenced mm-text.png
* Thu Mar 29 2007 ro@suse.de
- added pwdutils to buildreq
* Fri Oct 20 2006 lmuelle@suse.de
- ensure not to quote None if set in /etc/sysconfig/mailman:MAILMAN_MTA
* Thu Oct 12 2006 rommel@suse.de
- upgrade to Mailman 2.1.9 which
  + fixes some security issues (CVE-2006-2941, CVE-2006-3636, CVE-2006-2191)
  + adds support for languages "Arabic" and "Vietnamese"
  + makes the queue handling more robust
  + makes the handling of header/footers more robust
* Fri Jun 23 2006 poeml@suse.de
- add more info about adding "MAILMAN" to the apache server flags to
  README.SuSE and /etc/apache2/conf.d/mailman.conf
* Fri Jun 16 2006 rommel@suse.de
- update to version 2.1.8 which btw obsoletes these patches:
  mailman-2.1.4-mktime_overflowerror.patch
  mailman-2.1.4-cleanarch.patch
  mailman-2.1.7-patch-20060114.txt
- fixed an error in the comments of sysconfig.mailman
  (MAILMAN_SMTPPORT is relevant for MAILMAN_SMTPHOST, not MAILMAN_DEFAULT_EMAIL_HOST)
* Thu Mar 16 2006 rommel@suse.de
- applied a bugfix collection for Mailman 2.1.7 from
  http://sourceforge.net/tracker/index.php?func=detail&aid=1405790&group_id=103&atid=300103
- reworked the handling of the alias db file (using the %%ghost tag)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 23 2006 rommel@suse.de
- fixed cleanarch [bug #144675]
- reworked mailman-2.1.4-mktime_overflowerror.patch [bug #143390]
- removed python-xml from Requires: (was introduced by obsolete patch)
* Mon Jan  9 2006 rommel@suse.de
- update to version 2.1.7 (rediff of mailman-wrapper.patch,
  mailman-python24.patch, mailman-2.1.5-no_extra_asian.dif)
* Thu Aug 11 2005 lnussel@suse.de
- fix permission handling (#66315)
* Tue Jul 12 2005 rommel@suse.de
- fixed check_perms [bug #76172]
- added support for logrotate [bug #94379]
* Sat Jul  2 2005 dmueller@suse.de
- update to Mailman 2.1.6, rediff and remove patches
  which are already included upstream
* Wed Jun 15 2005 meissner@suse.de
- use RPM_OPT_FLAGS and PIE support for C binaries (CGI bins mostly)
* Wed Feb 16 2005 rommel@suse.de
- added mailman-2.1.5-dirtraversal.patch [bug #50563, CAN-2005-0202]
* Mon Feb 14 2005 ro@suse.de
- should not need explicit importing of japanese and korean
  any more with current python, remove it
* Thu Feb 10 2005 ro@suse.de
- remove python-korean and python-japanese (pkgs dropped)
* Mon Feb  7 2005 rommel@suse.de
- added python-xml to requires [bug #50100]
- fixed permissions on default error log file [bug #48208]
- fixed possible data loss situation while updating [bug #48209]
* Sat Jan 15 2005 schwab@suse.de
- Use <owner>:<group> in permissions file.
* Fri Jan 14 2005 rommel@suse.de
- added hints in README.SuSE on how to activate the web interface [bug #43292]
- added documentation tree from admin/www and debian's man pages [bug #37394]
- added sysconfig support for SMTPPORT [bug #49551]
* Wed Jan 12 2005 rommel@suse.de
- added mailman-weak-password.diff [bug #49468, CAN-2004-1144]
- added mailman-CAN-2004-1177.patch [bug #49468, CAN-2004-1177]
- added mailman-2.1.4-avoid-headerfolding-python21.diff [bug #45355]
- reworked undistributable mailman patch (archive fallback path)
* Wed Dec 15 2004 ro@suse.de
- another permissions fix
* Fri Dec  3 2004 ro@suse.de
- package according to permissions
* Wed Nov 10 2004 rommel@suse.de
- reworked start script (bug #42652)
* Thu Sep 16 2004 mmj@suse.de
- Include latest and greatest FAQ [#38461]
* Thu Sep  2 2004 mmj@suse.de
- Remove mail to root telling him to RTFM [#44365]
* Mon Aug 30 2004 ro@suse.de
- remove apache1 traces
* Sat Aug  7 2004 rommel@suse.de
- update to version 2.1.5
- fix of start script (bug #42652)
* Mon Jun 21 2004 ro@suse.de
- fix filelist
* Sun Jun 20 2004 rommel@suse.de
- relocating mm_cfg.py doesn't work, switched back to old behauviour (won't fix
  bug #41344)
- re-generating aliases in %%post section (important for update)
* Thu Jun  3 2004 rommel@suse.de
- fixed bug introduced by relocation of config files (bug #41344)
- updating mailing list aliases on install or update (important for
  autogenerated aliases)
- updated README.SuSE to reflect recent changes
* Fri May  7 2004 rommel@suse.de
- new configuration directory /etc/mailman
- moved mm_cfg.py to /etc/mailman (bug #38868)
- precompiled stuff in /usr/lib/mailman/bin (bug #38868)
- added support for https per default (bug #38460)
- added patch agains overflow in ArchRunner
  (Request ID 938301 on http://sourceforge.net/projects/mailman/)
- added glue patch for Scrubber
  (Request ID 891491 on http://sourceforge.net/projects/mailman/)
* Thu Mar 25 2004 rommel@suse.de
- added python-japanese and python-korean to Prereq (bug #36214)
* Wed Mar  3 2004 rommel@suse.de
- fixed traceback in options page (bug #35267)
- fixed german messages file (bug #35109)
* Wed Feb 18 2004 rommel@suse.de
- fixed some bugs concerning the wrapper gid files
  (/etc/mailman.*-gid) (see bugs #34614 #34382)
* Thu Feb 12 2004 rommel@suse.de
- removing stale lockfiles on start (bug #34016)
- fixed a typo in SuSEconfig.mailman (bug #34015)
- fixed Defaults.py to work around upgrade problem (bug #33793)
- fixed permissions in /usr/lib/mailman (bug #33792)
- added support for virtual hosts through SuSEconfig.mailman (feature request)
- added a hint to crontab where the master crontab is (feature request)
- added a patch for more options to list_lists (feature request)
- fixed a permission problem caused by editarch
* Thu Jan 15 2004 rommel@suse.de
- upgrade to version 2.1.4 (includes fix for latest XSS vulnerability)
- added link for better Sendmail interoperability
- added "--with-python-lib" to configure to work around hard coded /usr/lib
  manifestations
* Tue Dec 16 2003 rommel@suse.de
- added fix against XSS vulnerability (bug #32187)
- avoiding copies of mailman icons in /srv/www/icon;
  using the IMAGE_LOGOS config switch and an apache/apache2 config instead
  (bug #32496)
- added missing contrib directory to /usr/share/doc/packages/mailman/
- changed ownership of /var/lib/mailman to 2755 so pam ssh doesn't complain
* Tue Nov 25 2003 rommel@suse.de
- added missing calls "stop" on uninstall and "try-restart" on update (bug #29047)
- added w3m as requirement (bug #32706)
- not marking mm_cfg.pyc as config (bug #32851)
- added apache2 config (bug #33187)
* Sat Nov  1 2003 adrian@suse.de
- update to version 2.1.3
* Thu Aug 21 2003 mmj@suse.de
- The fix below from mcihar@suse.cz was a little to rough, since
  mailman broke without it's own copy of email. So include email
  in the installation, but keep korean and japanese disabled.
* Thu Aug 14 2003 rommel@suse.de
- added activation metadata in sysconfig templates
* Mon Aug 11 2003 mcihar@suse.cz
- don't include in mailman package python modules we also ship (korean,
  japanese, email)
- notify user about running 'SuSEconfig --module mailman' if not in YaST
* Mon Aug 11 2003 rommel@suse.de
- bug-fix update to version 2.1.2
- removed now-obsolete mailman-destdir.patch
- linkage of /etc/aliases.d/mailman to /var/lib/mailman/data/aliases
  has been dropped (unmaintainable)
- fixed mailmanctl to not freeze YaST2 [Bug #26990]
- fixed mail gid auto detection in SuSEconfig.mailman [Bug #27369]
- fixed Defaults.py to not reference build host [Bug #26988]
* Tue Aug  5 2003 ro@suse.de
- don't leave buildroot traces in installed files
* Fri Jun 13 2003 kukuk@suse.de
- Fix filelist
* Mon May 12 2003 rommel@suse.de
- added DISTRIBUTABLE to be able to build the version used interally
* Mon Mar 17 2003 kukuk@suse.de
- Don't enable mailman per default, does not work without correct
  configuration
* Mon Mar 10 2003 rommel@suse.de
- test for presence of /usr/sbin/postalias (reported by Eberhard Moenkeberg)
- added RPM Summary [Bug #24810]
- added Description to rcmailman (shows in runlevel editor)
* Thu Mar  6 2003 kukuk@suse.de
- Add openssl PreRequires [Bug #24785]
* Mon Feb 10 2003 rommel@suse.de
- update to version 2.1.1 which obsoletes both mailman-xss.patch and
  mailman-syncmember.patch and fixes the rmlist bug
- added the config attribute to the alias file generated by mailman
  so it does not get lost on package removal
- added MAILMAN_LINK_ALIASES variable to the sysconfig stuff so one
  can create links in /etc/aliases.d that point to
  /var/lib/mailman/data/aliases* independent on the value of MAILMAN_MTA
* Sat Feb  1 2003 rommel@suse.de
- fixed the start script to not freeze the runlevel editor on service start
- added metadata to sysconfig.apache-mailman
* Thu Jan 30 2003 rommel@suse.de
- added missing metadata to sysconfig file
- added official patch against cross-site-scripting (XSS) vulnerability
* Wed Jan 29 2003 rommel@suse.de
- update to version 2.1
- new start script
- new README.SuSE
- added SuSEconfig script that generates the wrapper gid files
  (/etc/mailman.*-gid) and provides an easy way to generate mm_cfg.py
  (Mailman's site configuration file)
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Fri Aug 30 2002 vinil@suse.cz
- enhanced PreRequires
- fixed default hostname in SuSEconfig (bug #17696)
- defaults set for Postfix MTA (Sendmail made optional)
* Mon Aug 12 2002 vinil@suse.de
- new version: 2.0.13
* Fri Aug  2 2002 ro@suse.de
- adapted server root
* Thu Jul 11 2002 vinil@suse.cz
- new version: 2.0.12
- own user and group 'mailman'
- use /etc/aliases.d/mailman instead of /etc/aliases
- paragraph about creating ML added into README.SuSE
* Mon Jun  3 2002 ro@suse.de
- fix build on lib64
- added openssl to neededforbuild
* Thu Jan 31 2002 vinil@suse.cz
- README.SuSE typo fixed
* Thu Jan 24 2002 vinil@suse.cz
- add rcscript, that moves crontab entry in /etc/cron.d/ and out
* Wed Jan 16 2002 ro@suse.de
- adapted for /etc/sysconfig/apache
* Wed Jan 16 2002 vinil@suse.cz
- installation is able to handle old /var/spool/mailman, now
- /var/lib/mailman/Mailman/mm_cfg.py* is %%config(noreplace)
* Tue Dec 11 2001 vinil@suse.cz
- update to 2.0.8
- web frontend prepared for apache
- patch for configuratable cgi-gid and mail-gid
- taking care about /etc/aliases now
* Sun Aug 19 2001 iboernig@suse.de
- update to new stable version 2.0.6
* Sun Aug 19 2001 iboernig@suse.de
- fixed bug in specfile (Bug #9519) Apache GID is now nogroup again.
* Wed Apr 25 2001 iboernig@suse.de
- changed mailgid to "daemon". It should work now with sendmail.
  Postfix users have to change default_privs
* Fri Mar 16 2001 iboernig@suse.de
- updated to version 2.0.3, includes minor security fix
* Fri Jan  5 2001 iboernig@suse.de
- bugfix: move crontab entry to /etc/cron.d/mailman
- notify user in %%post-section
- created README.SuSE
* Thu Dec 28 2000 choeger@suse.de
- bugfix: --prefix=$RPM_BUILD_ROOT does NOT work, because then
    /var/tmp/mailman-* would be compiled into some .c files
    changed Makefiles to allow DESTDIR=/path
- create crontab entries in postinstall
- use gid of nogroup also for mail-wrapper
* Thu Nov 30 2000 iboernig@suse.de
- changed default user.group to mdom.mdom
* Wed Nov 29 2000 iboernig@suse.de
- initial version
