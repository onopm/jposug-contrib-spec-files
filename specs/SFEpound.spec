#
# spec file for package: pound
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#

##TODO## make SMF manifest more nice, check for /etc/pound.cfg present

%include Solaris.inc
%include packagenamemacros.inc

Name:           SFEpound
IPS_package_name: web/proxy/pound
Summary:        The Pound program is a reverse proxy, load balancer and HTTPS front-end for Web server(s)
Version:        2.6
License:        GPLv3
URL:            http://www.apsis.ch/pound/
Source:         http://www.apsis.ch/pound/Pound-%{version}.tgz
Source1:	%{name}-manifest.xml
Source2:	%{name}.cfg
Patch1:		pound-01-Makefile.in.diff
Distribution:	OpenSolaris
Vendor:		OpenSolaris Community

# OpenSolaris IPS Manifest Fields
Meta(info.upstream): Robert Segall <roseg@apsis.ch>
Meta(info.maintainer): Thomas Wagner <tom68@users.sourceforge.net>
Meta(info.classification): org.opensolaris.category.2008:Applications/Internet


BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_Basedir:   /
SUNW_Copyright: %{name}.copyright


#####################################
##  Package Requirements Section   ##
#####################################

%include default-depend.inc
BuildRequires: %{pnm_buildrequires_SUNWopenssl}
BuildRequires: %{pnm_buildrequires_SUNWbtool}
BuildRequires: %{pnm_buildrequires_SUNWggrp}
BuildRequires: %{pnm_buildrequires_SUNWlibm}
Requires: %{pnm_requires_SUNWopenssl}
Requires: %{pnm_requires_SUNWlibms}
Requires: %{pnm_requires_SUNWpcre}
Requires: %{pnm_requires_SUNWzlib}
Requires: %{pnm_requires_SUNWbzip}


%description
The Pound program is a reverse proxy, load balancer and
HTTPS front-end for Web server(s). Pound was developed
to enable distributing the load among several Web-servers
and to allow for a convenient SSL wrapper for those Web
servers that do not offer it natively.

%prep
%setup -q -n Pound-%{version}
%patch1 -p0


%build
export CC=cc
export LDFLAGS="%_ldflags -L/usr/sfw/lib -R/usr/sfw/lib -lmtmalloc"
export CFLAGS="%{optflags} -I/usr/sfw/include -I/usr/include/pcre"
./configure --prefix=%{_prefix} --sysconfdir=/etc || (cat config.log; false)

# regexec() in libpcreposix behaves differently than in libc
# libc version works properly with pound
#perl -pi -e 's/-lpcreposix//g' Makefile
#change hard-coded "gcc" binary to the  
perl -pi -e 's/gcc/\${CC}/g' Makefile

make


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#Install example config file
mkdir "${RPM_BUILD_ROOT}/etc/"
cp "%{SOURCE2}" "${RPM_BUILD_ROOT}/etc/pound.cfg.example"

#Install manifest
%define svcdir /var/svc/manifest/network
mkdir -p "${RPM_BUILD_ROOT}/%{svcdir}"
cp "%{SOURCE1}" "${RPM_BUILD_ROOT}/%{svcdir}/%{name}.xml"



%clean
rm -rf %{buildroot}

%if %(test -f /usr/sadm/install/scripts/i.manifest && echo 0 || echo 1)
%iclass manifest -f i.manifest
%endif


%files
%defattr(-,root,sys)
%dir %attr (0755, root, bin) %{_sbindir}
%attr(0555, root, bin) %{_sbindir}/pound
%attr(0555, root, bin) %{_sbindir}/poundctl

%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man8
%attr(0444, root, bin) %{_mandir}/man8/pound.8
%attr(0444, root, bin) %{_mandir}/man8/poundctl.8

%dir %attr(755,root,sys) /etc
#%config(noreplace) %attr(644,root,root) /etc/*
/etc/*

%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) %{svcdir}
%class(manifest) %attr (0444, root, sys) %{svcdir}/*

%dir %attr(0755, root, sys) %{_datadir}


%changelog
* Sat Feb 25 2012 Yoichi Imai <sunnyone41@gmail.com>
- new upstream release 2.6
- use packagesnamemacros.inc
- add BuildRequres for math.h
- renamed service name /site... /network...

* Thr Sep 16 2010 - Thomas Wagner
- bump version to 2.5
- re-enable IPS manifest informations, change maintainer
- name the example config file /etc/pound.cfg.example
- fix %files globbing for config file, pound.cfg.example is no longer editable
* Thu Nov 26 2009 - Thomas Wagner
- ported to SFE
* Wed Aug 12 2009 - Robert Milkowski
- spec changes after jucr update
* Thu May 05 2009 - Robert Milkowski
- initial version
