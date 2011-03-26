#
# spec file for package: postfix
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s): [postfix]
#

%define   postfix_usr_dir  %{_prefix}/postfix
%define   postfix_var_dir  %{_var}/postfix
%define   postfix_etc_dir  /etc/postfix
%define postfix_user   postfix
%define postfix_group  postfix
%define postdrop_group postdrop
%define maildrop_group %{postdrop_group}
%define maildrop_gid   %{POSTDROP_GID}
%include Solaris.inc

Name:           postfix
Summary:        postfix mail server
Version:        2.8.0
IPS_package_name: service/network/smtp/postfix
License:        IBM Public License
Url:            http://www.postfix.org
Source:         ftp://ftp.cs.uu.nl/mirror/postfix/postfix-release/official/%{name}-%{version}.tar.gz
Source1:	postfix-manifest.xml
Patch1:		SFEpostfix-01-sys_defs.h.diff
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Release:	2
SUNW_Basedir:   /
SUNW_Copyright: %{name}.copyright

%include default-depend.inc
BuildRequires: developer/gnu-binutils
BuildRequires: library/pcre
BuildRequires: consolidation/sfw/sfw-incorporation
Requires: library/pcre
Requires: consolidation/sfw/sfw-incorporation


# OpenSolaris IPS Manifest Fields
Meta(info.maintainer_url):      http://sourceforge.jp/forum/forum.php?forum_id=25193
Meta(info.repository_url):      www.postfix.org
Meta(info.classification):      org.opensolaris.category.2008:System/Services


%description
Postfix is an attempt to provide an alternative to the widely-used Sendmail program. Postfix attempts to be fast, easy to administer, and hopefully secure, while at the same time being sendmail compatible enough to not upset your users.

%prep
rm -rf %name-%version
%setup -q -n %name-%version
%patch1

%build

#
# Change some default locations
#
make makefiles CCARGS='-DDEF_CONFIG_DIR=\"%{postfix_etc_dir}\" \
 -DDEF_COMMAND_DIR=\"%{postfix_usr_dir}/sbin\" \
 -DDEF_DAEMON_DIR=\"%{postfix_usr_dir}/libexec\" \
 -DDEF_DATA_DIR=\"%{postfix_usr_dir}/lib\" \
 -DDEF_MANPAGE_DIR=\"%{postfix_usr_dir}/man\" \
 -DDEF_QUEUE_DIR=\"%{postfix_var_dir}/spool\" \
 -DDEF_MAILQ_PATH=\"%{postfix_usr_dir}/bin/mailq\" \
 -DDEF_NEWALIASPATH=\"%{postfix_usr_dir}/bin/newaliases\" \
 -DDEF_SENDMAIL_PATH=\"%{postfix_usr_dir}/sbin/sendmail\" \
 -UHAS_NISPLUS \
'

make

%install
rm -rf $RPM_BUILD_ROOT
env -i "LD_LIBRARY_PATH=%buildroot%_libdir" \
        sh postfix-install -non-interactive \
                install_root=%buildroot \
                tempdir=%_tmppath

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
mv %buildroot/usr/bin/newaliases %buildroot%{postfix_usr_dir}/bin/newaliases
rm -rf %buildroot/usr/bin
%define svcdir /var/lib/svc/manifest/network
mkdir -p "${RPM_BUILD_ROOT}/%{svcdir}"
cp "%{SOURCE1}" "${RPM_BUILD_ROOT}/%{svcdir}/smtp-postfix.xml"

%files
%defattr (0755, root, bin)
%dir %{postfix_usr_dir}/bin    
%dir %{postfix_usr_dir}/libexec
%dir %{postfix_usr_dir}/man    
%dir %{postfix_usr_dir}/man/man1
%dir %{postfix_usr_dir}/man/man5
%dir %{postfix_usr_dir}/man/man8
%dir %{postfix_var_dir}/spool/pid
%defattr (0700, smmsp, mail)
%dir %{postfix_etc_dir} 
%dir %{postfix_usr_dir}/lib
%dir %{postfix_var_dir}/spool
%dir %{postfix_var_dir}/spool/active
%dir %{postfix_var_dir}/spool/bounce
%dir %{postfix_var_dir}/spool/corrupt
%dir %{postfix_var_dir}/spool/defer  
%dir %{postfix_var_dir}/spool/deferred
%dir %{postfix_var_dir}/spool/flush   
%dir %{postfix_var_dir}/spool/hold    
%dir %{postfix_var_dir}/spool/incoming
%dir %{postfix_var_dir}/spool/private 
%dir %{postfix_var_dir}/spool/maildrop
%dir %{postfix_var_dir}/spool/public  
%dir %{postfix_var_dir}/spool/saved   
%dir %{postfix_var_dir}/spool/trace   
%defattr (0755, root, bin)
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
%attr (2755, root, mail) %{postfix_usr_dir}/sbin/postqueue
%attr (2755, root, mail) %{postfix_usr_dir}/sbin/postdrop
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
%{postfix_usr_dir}/man/man1/*
%{postfix_usr_dir}/man/man5/*
%{postfix_usr_dir}/man/man8/*
%dir %attr (0755, root, sys) %{svcdir}
%class(manifest) %attr (0444, root, sys) %{svcdir}/smtp-postfix.xml

%changelog
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

