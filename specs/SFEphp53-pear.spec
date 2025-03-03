#
# spec file for package SFEphp53-pear
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 0
%define _gpp g++
%include base.inc
%define php_major_version 5.3

%define peardir %{_localstatedir}/php/%{php_major_version}/pear
%define _prefix /usr/php/%{php_major_version}
%define _sysconfdir /etc/php/%{php_major_version}
%define usr_prefix /usr
%define xmlrpcver 1.5.4
%define getoptver 1.2.3
%define arctarver 1.3.7
%define structver 1.0.4
%define xmlutil   1.2.1
%define _pkg_docdir %{usr_prefix}/share/doc/SFEphp53-pear

Summary: PHP Extension and Application Repository framework
Name: SFEphp53-pear
IPS_package_name:        web/php-53/extension/php-pear
SUNW_Copyright:   %{name}.copyright
Version: 1.9.4
#Release: 4%{?dist}
#Epoch: 1
# PEAR, Archive_Tar, XML_Util are BSD
# XML-RPC, Console_Getopt are PHP
# Structures_Graph is LGPLv2+
License: BSD and PHP and LGPLv2+
Group: Development/Languages
URL: http://pear.php.net/package/PEAR
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Source0: http://download.pear.php.net/package/PEAR-%{version}.tgz
# wget http://cvs.php.net/viewvc.cgi/pear-core/install-pear.php?revision=1.39 -O install-pear.php
Source1: SFEphp53-pear_install-pear.php
Source2: SFEphp53-pear_relocate.php
Source3: SFEphp53-pear_strip.php
Source4: SFEphp53-pear_LICENSE
Source5: SFEphp53-pear_LICENSE-XML_RPC
Source10: SFEphp53-pear_pear.sh
Source11: SFEphp53-pear_pecl.sh
Source12: SFEphp53-pear_peardev.sh
Source13: SFEphp53-pear_macros.pear
Source20: http://pear.php.net/get/XML_RPC-%{xmlrpcver}.tgz
Source21: http://pear.php.net/get/Archive_Tar-%{arctarver}.tgz
Source22: http://pear.php.net/get/Console_Getopt-%{getoptver}.tgz
Source23: http://pear.php.net/get/Structures_Graph-%{structver}.tgz
Source24: http://pear.php.net/get/XML_Util-%{xmlutil}.tgz
Patch0: SFEphp53-pear_php-pear-1.9.4-restcache.patch

%include default-depend.inc
#BuildArch: noarch
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
BuildRequires: web/php-53
#BuildRequires: php-cli >= 5.1.0-1, php-xml, gnupg
#Provides: php-pear(Console_Getopt) = %{getoptver}
#Provides: php-pear(Archive_Tar) = %{arctarver}
#Provides: php-pear(PEAR) = %{version}
#Provides: php-pear(Structures_Graph) = %{structver}
#Provides: php-pear(XML_RPC) = %{xmlrpcver}
#Provides: php-pear(XML_Util) = %{xmlutil}
#Obsoletes: php-pear-XML-Util <= %{xmlutil}
# Hold release string in legacy provide, since XML_Util has not changed:
#Provides:  php-pear-XML-Util = %{xmlutil}-2%{?dist}
Requires: web/php-53

%description
PEAR is a framework and distribution system for reusable PHP
components.  This package contains the basic PEAR components.

%prep
%setup -c -T

# Create a usable PEAR directory (used by install-pear.php)
for archive in %{SOURCE0} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24}
do
    tar xzf  $archive --strip-components 1 || tar xzf  $archive --strip-path 1
    file=${archive##*/}
    [ -f LICENSE ] && mv LICENSE LICENSE-${file%%-*}
    [ -f README ]  && mv README  README-${file%%-*}
done
tar xzf %{SOURCE24} package.xml
mv package.xml XML_Util.xml

# apply patches on used PEAR during install
# - no patch

%build
# This is an empty build section.

%install
rm -rf $RPM_BUILD_ROOT

export PHP_PEAR_SYSCONF_DIR=%{_sysconfdir}
export PHP_PEAR_SIG_KEYDIR=%{_sysconfdir}/pearkeys
export PHP_PEAR_SIG_BIN=%{_bindir}/gpg
export PHP_PEAR_INSTALL_DIR=%{peardir}

# 1.4.11 tries to write to the cache directory during installation
# so it's not possible to set a sane default via the environment.
# The ${PWD} bit will be stripped via relocate.php later.
export PHP_PEAR_CACHE_DIR=${PWD}%{_localstatedir}/cache/php-pear
export PHP_PEAR_TEMP_DIR=/var/tmp

install -d $RPM_BUILD_ROOT%{peardir} \
           $RPM_BUILD_ROOT%{_localstatedir}/cache/php-pear \
           $RPM_BUILD_ROOT%{_localstatedir}/apache2/2.2/htdocs \
           $RPM_BUILD_ROOT%{peardir}/.pkgxml \
           $RPM_BUILD_ROOT%{_sysconfdir}/rpm \
           $RPM_BUILD_ROOT%{_sysconfdir}/pear

export INSTALL_ROOT=$RPM_BUILD_ROOT

/usr/php/5.3/bin/php -n -dmemory_limit=32M -dshort_open_tag=0 -dsafe_mode=0 \
         -derror_reporting=E_ALL -ddetect_unicode=0 \
      %{SOURCE1} -d %{peardir} \
                 -c %{_sysconfdir}/pear \
                 -b %{_bindir} \
                 -w %{_localstatedir}/www/html \
                 %{SOURCE0} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE20}

# Replace /usr/bin/* with simple scripts:
install -m 755 %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}/pear
install -m 755 %{SOURCE11} $RPM_BUILD_ROOT%{_bindir}/pecl
install -m 755 %{SOURCE12} $RPM_BUILD_ROOT%{_bindir}/peardev

# Sanitize the pear.conf
/usr/php/5.3/bin/php -n %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pear.conf $RPM_BUILD_ROOT | 
  /usr/php/5.3/bin/php -n %{SOURCE2} php://stdin $PWD > new-pear.conf
/usr/php/5.3/bin/php -n %{SOURCE3} new-pear.conf ext_dir |
  /usr/php/5.3/bin/php -n %{SOURCE3} php://stdin http_proxy > $RPM_BUILD_ROOT%{_sysconfdir}/pear.conf

/usr/php/5.3/bin/php -r "print_r(unserialize(substr(file_get_contents('$RPM_BUILD_ROOT%{_sysconfdir}/pear.conf'),17)));"

install -m 644 -c %{SOURCE4} LICENSE
install -m 644 -c %{SOURCE5} LICENSE-XML_RPC

install -m 644 -c %{SOURCE13} \
           $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.pear     

# apply patches on installed PEAR tree
pushd $RPM_BUILD_ROOT%{peardir} 
 pushd PEAR
  %__patch -s --no-backup --fuzz 0 -p0 < %{PATCH0}
 popd
popd

# Why this file here ?
rm -rf $RPM_BUILD_ROOT/.depdb* $RPM_BUILD_ROOT/.lock $RPM_BUILD_ROOT/.channels $RPM_BUILD_ROOT/.filemap $RPM_BUILD_ROOT/.registry
# no effect for OI
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/apache2 $RPM_BUILD_ROOT%{_sysconfdir}/rpm

# Need for re-registrying XML_Util
install -m 644 XML_Util.xml $RPM_BUILD_ROOT%{peardir}/.pkgxml/

mkdir -p $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT/usr/bin
for file in pear peardev pecl
do
   ln -s ../php/%{php_major_version}/bin/$file .
done
popd

%check
# Check that no bogus paths are left in the configuration, or in
# the generated registry files.
grep $RPM_BUILD_ROOT $RPM_BUILD_ROOT%{_sysconfdir}/pear.conf && exit 1
grep %{_libdir} $RPM_BUILD_ROOT%{_sysconfdir}/pear.conf && exit 1
grep '"/tmp"' $RPM_BUILD_ROOT%{_sysconfdir}/pear.conf && exit 1
grep /usr/local $RPM_BUILD_ROOT%{_sysconfdir}/pear.conf && exit 1
grep -rl $RPM_BUILD_ROOT $RPM_BUILD_ROOT && exit 1


%clean
rm -rf $RPM_BUILD_ROOT
rm new-pear.conf


%triggerpostun -- php-pear-XML-Util
# re-register extension unregistered during postun of obsoleted php-pear-XML-Util
%{_bindir}/pear install --nodeps --soft --force --register-only %{pear_xmldir}/XML_Util.xml >/dev/null || :


%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) %{_localstatedir}
%{peardir}
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/pear.conf
#%config %{_sysconfdir}/rpm/macros.pear
%dir %{_localstatedir}/cache/php-pear
#%dir %{_localstatedir}/apache2/2.2/htdocs
%dir %{_sysconfdir}/pear
%doc README* LICENSE*
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{php_major_version}) /usr/bin/pear
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{php_major_version}) /usr/bin/peardev
%attr (0555, root, bin) %ips_tag (mediator=php mediator-version=%{php_major_version}) /usr/bin/pecl

%changelog
* Jan 24 2011 YAMAMOTO Takashi <yamachan@selfnavi.com> - 1.9.4
- work with CBE
- Support for OpenIndiana

* Tue Oct 25 2011 Joe Orton <jorton@redhat.com> - 1:1.9.4-4
- fix patch application for #747361

* Fri Oct 21 2011 Joe Orton <jorton@redhat.com> - 1:1.9.4-3
- ignore REST cache creation failures as non-root user (#747361)

* Tue Sep 20 2011 Joe Orton <jorton@redhat.com> - 1:1.9.4-2
- fix XML-Util provides

* Tue Sep  6 2011 Joe Orton <jorton@redhat.com> - 1:1.9.4-1
- update to 1.9.4 (#651897)
- update XML_RPC to 1.5.4, Structures_Graph to 1.0.4, Archive_Tar to 1.3.7

* Tue Aug 16 2011 Joe Orton <jorton@redhat.com> - 1:1.9.1-1
- update to 1.9.1 (#651897)
- fix installation of XML_RPC license file

* Tue Jun 22 2010 Joe Orton <jorton@redhat.com> - 1:1.9.0-2
- update to XML_RPC 1.5.3 (#606280)
- bundle LICENSE files per Fedora (Remi Collet)

* Sat Sep 05 2009 Remi Collet <Fedora@FamilleCollet.com> 1:1.9.0-1
- update to PEAR 1.9.0, XML_RPC 1.5.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 30 2009 Remi Collet <Fedora@FamilleCollet.com> 1:1.8.1-1
- update to 1.8.1
- Update install-pear.php script (1.39)
- add XML_Util

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun May 18 2008 Remi Collet <Fedora@FamilleCollet.com> 1:1.7.2-2
- revert to install-pear.php script 1.31 (for cfg_dir)

* Sun May 18 2008 Remi Collet <Fedora@FamilleCollet.com> 1:1.7.2-1
- update to 1.7.2
- Update install-pear.php script (1.32)

* Tue Mar 11 2008 Tim Jackson <rpm@timj.co.uk> 1:1.7.1-2
- Set cfg_dir to be %%{_sysconfdir}/pear (and own it)
- Update install-pear.php script
- Add %%pear_cfgdir and %%pear_wwwdir macros

* Sun Feb  3 2008 Remi Collet <Fedora@FamilleCollet.com> 1:1.7.1-1
- update to 1.7.1

* Fri Feb  1 2008 Remi Collet <Fedora@FamilleCollet.com> 1:1.7.0-1
- update to 1.7.0

* Thu Oct  4 2007 Joe Orton <jorton@redhat.com> 1:1.6.2-2
- require php-cli not php

* Sun Sep  9 2007 Remi Collet <Fedora@FamilleCollet.com> 1:1.6.2-1
- update to 1.6.2
- remove patches merged upstream
- Fix : "pear install" hangs on non default channel (#283401)

* Tue Aug 21 2007 Joe Orton <jorton@redhat.com> 1:1.6.1-2
- fix License

* Thu Jul 19 2007 Remi Collet <Fedora@FamilleCollet.com> 1:1.6.1-1
- update to PEAR-1.6.1 and Console_Getopt-1.2.3

* Thu Jul 19 2007 Remi Collet <Fedora@FamilleCollet.com> 1:1.5.4-5
- new SPEC using install-pear.php instead of install-pear-nozlib-1.5.4.phar

* Mon Jul 16 2007 Remi Collet <Fedora@FamilleCollet.com> 1:1.5.4-4
- update macros.pear (without define)

* Mon Jul 16 2007 Joe Orton <jorton@redhat.com> 1:1.5.4-3
- add pecl_{un,}install macros to macros.pear (from Remi)

* Fri May 11 2007 Joe Orton <jorton@redhat.com> 1:1.5.4-2
- update to 1.5.4

* Tue Mar  6 2007 Joe Orton <jorton@redhat.com> 1:1.5.0-3
- add redundant build section (#226295)
- BR php-cli not php (#226295)

* Mon Feb 19 2007 Joe Orton <jorton@redhat.com> 1:1.5.0-2
- update builtin module provides (Remi Collet, #226295)
- drop patch 0

* Thu Feb 15 2007 Joe Orton <jorton@redhat.com> 1:1.5.0-1
- update to 1.5.0

* Mon Feb  5 2007 Joe Orton <jorton@redhat.com> 1:1.4.11-4
- fix Group, mark pear.conf noreplace (#226295)

* Mon Feb  5 2007 Joe Orton <jorton@redhat.com> 1:1.4.11-3
- use BuildArch not BuildArchitectures (#226925)
- fix to use preferred BuildRoot (#226925)
- strip more buildroot-relative paths from *.reg
- force correct gpg path in default pear.conf

* Thu Jan  4 2007 Joe Orton <jorton@redhat.com> 1:1.4.11-2
- update to 1.4.11

* Fri Jul 14 2006 Joe Orton <jorton@redhat.com> 1:1.4.9-4
- update to XML_RPC-1.5.0
- really package macros.pear

* Thu Jul 13 2006 Joe Orton <jorton@redhat.com> 1:1.4.9-3
- require php-cli
- add /etc/rpm/macros.pear (Christopher Stone)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.4.9-2.1
- rebuild

* Mon May  8 2006 Joe Orton <jorton@redhat.com> 1:1.4.9-2
- update to 1.4.9 (thanks to Remi Collet, #183359)
- package /usr/share/pear/.pkgxml (#190252)
- update to XML_RPC-1.4.8
- bundle the v3.0 LICENSE file

* Tue Feb 28 2006 Joe Orton <jorton@redhat.com> 1:1.4.6-2
- set cache_dir directory, own /var/cache/php-pear

* Mon Jan 30 2006 Joe Orton <jorton@redhat.com> 1:1.4.6-1
- update to 1.4.6
- require php >= 5.1.0 (#178821)

* Fri Dec 30 2005 Tim Jackson <tim@timj.co.uk> 1:1.4.5-6
- Patches to fix "pear makerpm"

* Wed Dec 14 2005 Joe Orton <jorton@redhat.com> 1:1.4.5-5
- set default sig_keydir to /etc/pearkeys
- remove ext_dir setting from /etc/pear.conf (#175673)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Dec  6 2005 Joe Orton <jorton@redhat.com> 1:1.4.5-4
- fix virtual provide for PEAR package (#175074)

* Sun Dec  4 2005 Joe Orton <jorton@redhat.com> 1:1.4.5-3
- fix /usr/bin/{pecl,peardev} (#174882)

* Thu Dec  1 2005 Joe Orton <jorton@redhat.com> 1:1.4.5-2
- add virtual provides (#173806) 

* Wed Nov 23 2005 Joe Orton <jorton@redhat.com> 1.4.5-1
- initial build (Epoch: 1 to allow upgrade from php-pear-5.x)
