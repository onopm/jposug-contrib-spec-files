#
# spec file for package: postfix
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s): [postfix]
#

%include Solaris.inc
%include packagenamemacros.inc
%if %( expr %{osbuild} '=' 175 )
# Solaris
%define with_mysql 0
%else
# OI
%define with_mysql 1
%endif
%define src_name postfix
%define postfix_usr_dir  %{_prefix}/postfix
%define postfix_var_dir  %{_var}/postfix
%define postfix_etc_dir  /etc/postfix
%define postfix_user   postfix
%define postfix_group  postfix
%define postdrop_group postdrop
%define maildrop_group %{postdrop_group}
%define maildrop_gid   %{POSTDROP_GID}
%define svcdir /var/svc/manifest/network

%define postfix_config_dir      %{_sysconfdir}/postfix
%define postfix_daemon_dir      %{postfix_usr_dir}/libexec
%define postfix_command_dir     %{postfix_usr_dir}/sbin
%define postfix_queue_dir       %{postfix_var_dir}/spool
%define postfix_data_dir        %{postfix_usr_dir}/lib
%define postfix_doc_dir         %{_docdir}/%{src_name}-%{version}
%define postfix_sample_dir      %{postfix_doc_dir}/samples
%define postfix_readme_dir      %{postfix_doc_dir}/README_FILES

#if userid is already engaged
#for other users/groups then postfix/postfix/postdrop, then
#the user or group will be created with a numeric id given by
#the system. Currently the UID/GID is possibly taken twice
%define runuser         postfix
%define runuserid       161
%define runusergroup    other

%define rungroup        postfix
%define rungroupid      181
%define rundropgroup    postdrop
%define rundropgroupid  182

Name:           SFEpostfix
Summary:        postfix mail server
Version:        2.9.9
IPS_package_name: service/network/smtp/postfix
License:        IBM Public License
Url:            http://www.postfix.org
Source:         ftp://ftp.cs.uu.nl/mirror/postfix/postfix-release/official/%{src_name}-%{version}.tar.gz
Source1:	smtp-postfix.xml
Source2:	svc-postfix
# http://estseg.blogspot.jp/2010/03/postfix-w-opensolaris-nis.html
# Если кто-то будет собирать Postfix на OpenSolaris b130 позднее получает следующее сообщение об ошибке:
Patch1:		SFEpostfix-294-sys_defs.h.diff
Patch100:	SFEpostfix-299-postfix-install.diff
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Release:	1
SUNW_Basedir:   /
SUNW_Copyright: %{name}.copyright

%include default-depend.inc
BuildRequires:  %{pnm_buildrequires_developer_gnu_binutils}
BuildRequires:  %{pnm_buildrequires_library_pcre}
BuildRequires:  consolidation/sfw/sfw-incorporation
Requires:       %{pnm_requires_library_pcre}
Requires:       consolidation/sfw/sfw-incorporation
Requires:       library/security/cyrus-sasl
BuildRequires:  library/security/cyrus-sasl
%if %( expr %{osbuild} '=' 175 )
# Solaris
BuildRequires:  database/berkeleydb-5
Requires:       database/berkeleydb-5
%else
# OI
BuildRequires:  database/berkeleydb-48
Requires:       database/berkeleydb-48
%endif
%if %{with_mysql}
BuildRequires:  %{pnm_buildrequires_database_mysql_51_library}
BuildRequires:  %{pnm_buildrequires_mysql51}
Requires:       %{pnm_requires_database_mysql_51_library}
Requires:       %{pnm_requires_mysql51}
%endif
BuildRequires:  %{pnm_buildrequires_library_zlib}
Requires:       %{pnm_requires_library_zlib}
BuildRequires:  %{pnm_buildrequires_system_library_math}
Requires:       %{pnm_requires_system_library_math}
BuildRequires:  %{pnm_buildrequires_library_openldap}
Requires:       %{pnm_requires_library_openldap}
BuildRequires:  %pnm_buildrequires_openssl
Requires:       %pnm_requires_openssl
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif

# OpenSolaris IPS Manifest Fields
Meta(info.maintainer_url):      http://sourceforge.jp/forum/forum.php?forum_id=25193
Meta(info.repository_url):      www.postfix.org
Meta(info.classification):      org.opensolaris.category.2008:System/Services


%description
Postfix is an attempt to provide an alternative to the widely-used Sendmail program. Postfix attempts to be fast, easy to administer, and hopefully secure, while at the same time being sendmail compatible enough to not upset your users.

%prep
rm -rf %src_name-%version
%setup -q -n %src_name-%version
%patch1 -p0
%patch100 -p0 -b .orig

%build

#
# Change some default locations
#
export CC=gcc
export CXX=g++
make makefiles OPT=' \
 -O3 \
' \
CCARGS='-DDEF_CONFIG_DIR=\"%{postfix_etc_dir}\" \
 -DDEF_COMMAND_DIR=\"%{postfix_usr_dir}/sbin\" \
 -DDEF_DAEMON_DIR=\"%{postfix_usr_dir}/libexec\" \
 -DDEF_DATA_DIR=\"%{postfix_usr_dir}/lib\" \
 -DDEF_MANPAGE_DIR=\"%{_mandir}\" \
 -DDEF_QUEUE_DIR=\"%{postfix_var_dir}/spool\" \
 -DDEF_MAILQ_PATH=\"%{postfix_usr_dir}/bin/mailq\" \
 -DDEF_NEWALIASPATH=\"%{postfix_usr_dir}/bin/newaliases\" \
 -DDEF_SENDMAIL_PATH=\"%{postfix_usr_dir}/sbin/sendmail\" \
 -UHAS_NISPLUS \
 -DHAS_PCRE -I/usr/include/pcre \
 -DHAS_DB -I/usr/gnu/include \
 -DUSE_SASL_AUTH \
 -DUSE_CYRUS_SASL -I/usr/include/sasl2/sasl \
 -DUSE_TLS \
%if %{with_mysql}
 -DHAS_MYSQL -I/usr/mysql/include/mysql \
%endif
 -DHAS_LDAP -I/usr/include/openldap \
' \
AUXLIBS=' \
 -L/usr/sfw/lib -R/usr/sfw/lib -lz -lm \
%if %{with_mysql}
 -L/usr/mysql/lib/mysql -R/usr/mysql/lib/mysql -lmysqlclient \
%endif
 -L/usr/gnu/lib -R/usr/gnu/lib -ldb \
 -lpcre \
 -L/usr/lib/sasl2 -R/usr/lib/sasl2 -lsasl2 \
 -lldap-2.4 -llber-2.4 \
 -lssl -lcrypto \
'
make

%install
rm -rf %{buildroot}

env -i "LD_LIBRARY_PATH=%buildroot%_libdir" \
    sh postfix-install -non-interactive \
    install_root=%buildroot \
    tempdir=%_tmppath \
    config_directory=%{postfix_config_dir} \
    daemon_directory=%{postfix_daemon_dir} \
    command_directory=%{postfix_command_dir} \
    queue_directory=%{postfix_queue_dir} \
    data_directory=%{postfix_data_dir} \
    sendmail_path=%{postfix_command_dir}/sendmail \
    newaliases_path=%{postfix_usr_dir}/bin/newaliases \
    mailq_path=%{postfix_usr_dir}/bin/mailq \
    mail_owner=%{postfix_user} \
    setgid_group=%{maildrop_group} \
    manpage_directory=%{_mandir} \
    sample_directory=%{postfix_sample_dir} \
    readme_directory=%{postfix_readme_dir} \
    default_database_type=hash \
    alias_maps=hash:/etc/mail/aliases,nis:mail.aliases \
    alias_database=hash:/etc/mail/aliases || exit 1

mv %buildroot%{_mandir}/man1/mailq.1 %buildroot%{_mandir}/man1/mailq.postfix.1
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mkdir -p "${RPM_BUILD_ROOT}%{svcdir}"
cp "%{SOURCE1}" "${RPM_BUILD_ROOT}%{svcdir}"
mkdir -p "${RPM_BUILD_ROOT}/lib/svc/method"
cp "%{SOURCE2}" "${RPM_BUILD_ROOT}/lib/svc/method/postfix"

%post
# upgrade configuration files if necessary
%{_sbindir}/postfix set-permissions upgrade-configuration \
        daemon_directory=%{postfix_daemon_dir} \
        command_directory=%{postfix_command_dir} \
        mail_owner=%{postfix_user} \
        setgid_group=%{maildrop_group} \
        manpage_directory=%{_mandir} \
        sample_directory=%{postfix_sample_dir} \
        readme_directory=%{postfix_readme_dir} &> /dev/null

%actions
group groupname="%{rundropgroup}" gid="%{rundropgroupid}"
group groupname="%{rungroup}" gid="%{rungroupid}"
user ftpuser=false gcos-field="Postfix user" username="%{runuser}" uid="%{runuserid}" password=NP group="%{runusergroup}" home-dir="%{_localstatedir}/spool/postfix" login-shell="/bin/true" group-list="mail"

%files
%defattr (0755, root, bin)
%dir %{postfix_usr_dir}/bin    
%dir %{postfix_usr_dir}/libexec
%dir %attr (0755, root, sys) /usr/share
%dir %{_mandir}
%dir %{_mandir}/man1
%dir %{_mandir}/man5
%dir %{_mandir}/man8
%dir %attr(0755, root, sys) /var
%dir %attr(0755, postfix, mail) %{postfix_usr_dir}/lib
%dir %{postfix_var_dir}/spool
%dir %attr(0755, postfix, postdrop) %{postfix_var_dir}/spool/maildrop
%dir %attr(0710, postfix, postdrop) %{postfix_var_dir}/spool/public  
%dir %attr(0700, root, root) %{postfix_var_dir}/spool/pid
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/active
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/bounce
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/corrupt
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/defer  
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/deferred
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/flush   
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/hold    
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/incoming
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/private 
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/saved   
%dir %attr(0700, postfix, mail) %{postfix_var_dir}/spool/trace   
%dir %attr(0755, root, sys) /etc
%dir %attr(0755, root, mail)  %{postfix_etc_dir}
%config %{postfix_etc_dir}/main.cf
%config %{postfix_etc_dir}/access
%config %{postfix_etc_dir}/master.cf
%config %{postfix_etc_dir}/aliases
%config %{postfix_etc_dir}/canonical
%config %{postfix_etc_dir}/generic
%config %{postfix_etc_dir}/header_checks
%config %{postfix_etc_dir}/relocated
%config %{postfix_etc_dir}/virtual
%config %{postfix_etc_dir}/transport
%{postfix_etc_dir}/bounce.cf.default
%{postfix_etc_dir}/LICENSE
%{postfix_etc_dir}/main.cf.default
%{postfix_etc_dir}/makedefs.out
%{postfix_etc_dir}/TLS_LICENSE
%attr (2755, root, postdrop) %{postfix_usr_dir}/sbin/postqueue
%attr (2755, root, postdrop) %{postfix_usr_dir}/sbin/postdrop
%dir %attr (0755, root, sys) /usr
%{postfix_usr_dir}/sbin/postalias
%{postfix_usr_dir}/sbin/postcat
%{postfix_usr_dir}/sbin/postconf
%{postfix_usr_dir}/sbin/postkick
%{postfix_usr_dir}/sbin/postlock
%{postfix_usr_dir}/sbin/postlog
%{postfix_usr_dir}/sbin/postmap
%{postfix_usr_dir}/sbin/postmulti
%{postfix_usr_dir}/sbin/postsuper
%{postfix_usr_dir}/sbin/sendmail
%{postfix_usr_dir}/sbin/postfix
%{postfix_usr_dir}/bin/mailq
%{postfix_usr_dir}/bin/newaliases
%{postfix_usr_dir}/libexec/*
%dir %{_mandir}/man1/*
%dir %{_mandir}/man5/*
%dir %{_mandir}/man8/*
%dir %attr(0755, root, other) %{_docdir}
%doc %{postfix_doc_dir}
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/network
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/network/smtp-postfix.xml
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/postfix


%changelog
* Mon Dec 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- disable MySQL with Oracle Solaris because build fails
- use database/berkeleydb-5 on Oracle Solaris
* Sun May 11 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- added gcc dependencies
* Fri May 02 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- enable TLS support
- set default_database_type to hash  
* Mon Feb 17 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Bump to 2.9.9
* Mon Sep 09 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.9.8
* Thu Jul 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.9.7
* Wed Jan 09 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- changed the header path to sasl2
* Wed Jan 09 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- changed the Library path to sasl2
* Mon Jan 07 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- build with gcc by default
* Thu Dec 09 2012 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Fix manifest problems. Ready for hash:, pcre, sasl, ldap and mysql.
- Bump to 2.9.4
* Thu Sep 13 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.8.12
* Mon Jun 04 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 2.8.11
- modify SMF manifest
- add %actions
- modify postfix-install options
* Mon May  7 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify some %attr for Solaris 11
* Thu Feb 10 2011 - Satoru MIYAZAKI<s.miyaza@gmail.com>
- Bump to 2.8.0
* Tue Dec 15 2009 - matthias _at_ matthias _dot_ nl
- Added config directives and additional permissions
* Wed Dec 09 2009 - matthias _at_ matthias _dot_ nl
- Changed the permissions to the smmsp mail user and mail group where relevant
* Wed Nov 25 2009 - matthias _at_ matthias _dot_ nl
- Fixed type postin to post
* Sat Nov 21 2009 - matthias _at_ matthias _dot_ nl
- Add the creation of the postfix user and the postdrop group
* Fri Nov 20 2009 - matthias _at_ matthias _dot_ nl
- Removed double reference for the files section, rpm approves but pkgbuild apparently not
* Wed Nov 18 2009 - matthias _at_ matthias _dot_ nl
- Added dependency for binutils
* Sun Nov 15 2009 - matthias _at_ matthias _dot_ nl
- First start with package that just contain the binaries, later versions should include correct users,ownerships and permissions
* Thu Nov 12 2009 - matthias _at_ matthiaswies _dot_ nl
- Initial version for the OpenSolaris postfix package

