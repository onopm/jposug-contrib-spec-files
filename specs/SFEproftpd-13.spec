#
# spec file for package SFEproftpd-13
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#
%include Solaris.inc
%include packagenamemacros.inc

%define _prefix		 /usr/proftpd
%define major_version	 1.3
%define tarball_name     proftpd
%define tarball_version  1.3.4d
%define gss_version      1.3.4
%define _basedir	 /

%define postgres_version 9.2
%define mysql_version    5.1

Name:                    SFEproftpd-13
IPS_package_name:        service/network/proftpd-13
Summary:                 Highly configurable GPL-licensed FTP server software
Version:                 1.3.4
IPS_component_version:   1.3.4.0.4
License:		 GPL
Url:                     http://www.proftpd.org/
Source:                  ftp://ftp.proftpd.org/distrib/source/%{tarball_name}-%{tarball_version}.tar.gz
Source1:		 %{name}-proftpd
Source2:		 %{name}-proftpd.xml
Source3:		 %{name}-proftpd.conf
Source4:		 %{name}-postgres.conf
Source5:		 %{name}-mysql.conf
Source6:		 %{name}-ftppasswd.conf
Source7:		 %{name}-resume.conf
Source8:		 %{name}-ftppasswd.sample
Source9:		 %{name}-logs.conf
Source10:		 %{sf_download}/gssmod/mod_gss-%{gss_version}.tar.gz

Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            %{_basedir}
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: %{pnm_buildrequires_SUNWmysql51}
BuildRequires: %{pnm_buildrequires_SUNWmysql51_devel}
BuildRequires: %{pnm_buildrequires_database_mysql_51_library}
BuildRequires: %{pnm_buildrequires_SUNWopenssl_devel}
BuildRequires: %{pnm_buildrequires_SUNWgss}
BuildRequires: %{pnm_buildrequires_SUNWgssc_devel}
#BuildRequires: SFEpostgres-92
BuildRequires: database/postgres-92/developer

Requires: %{pnm_requires_library_security_openssl}
Requires: %{pnm_requires_SUNWgssc}

# OpenSolaris IPS Package Manifest Fields
Meta(info.upstream):	 	The ProFTPD Project team
Meta(info.maintainer):	 	pkglabo.justplayer.com <pkgadmin@justplayer.com>
# Meta(info.repository_url):	[open source code repository]
Meta(info.classification):	System Libraries

%description
Highly configurable GPL-licensed FTP server software

%package devel
IPS_package_name:        service/network/proftpd-13/developer
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}/%{major_version}
Requires:                %{name}

%package doc
IPS_package_name:        service/network/proftpd-13/documentation
Summary:                 %{summary} - documentation files
SUNW_BaseDir:            /usr/share
Requires:                %{name}

%package sql
IPS_package_name:	 service/network/proftpd-13/module/sql-common
Summary:		 %{summary} - SQL commin module
SUNW_BaseDir:            %{_prefix}/%{major_version}
Requires:                %{name}

%package postgres
IPS_package_name:	 service/network/proftpd-13/module/postgres-92
Summary:		 %{summary} - PostgreSQL module
SUNW_BaseDir:            /
Requires:                %{name}
Requires:                %{name}-sql
#Requires:	         SFEpostgres-92-library
Requires:	         database/postgres-92/library

%package mysql
IPS_package_name:	 service/network/proftpd-13/module/mysql-51
Summary:		 %{summary} - MySQL module
SUNW_BaseDir:            /
Requires:                %{name}
Requires:                %{name}-sql
Requires:	         %{pnm_requires_database_mysql_51_library}

%package tls
IPS_package_name:	 service/network/proftpd-13/module/tls
Summary:		 %{summary} - TLS module
SUNW_BaseDir:            /
Requires:                %{name}


%prep
%setup -c -n %{tarball_name}-%{tarball_version}
gzcat %{SOURCE10} | tar xf -

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS="%optflags -I /usr/include/kerberosv5"
export LDFLAGS="%_ldflags -lkrb5"
export install_user=$LOGNAME
export install_group=`groups | awk '{print $1}'`

%if %( expr %{osbuild} '=' 175 )
# Solaris
pushd mod_gss-%{gss_version}
./configure
popd
cp mod_gss-%{gss_version}/mod_gss.h include
cp mod_gss-%{gss_version}/mod_gss.c contrib
%endif

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

LD_RUN_PATH=/lib:/usr/lib:/usr/lib/krb5:/usr/postgres/%{postgres_version}/lib:/usr/mysql/%{mysql_version}/lib/mysql ; export LD_RUN_PATH
./configure \
 --prefix=%{_prefix}/%{major_version}/\
 --mandir=/usr/share/man \
 --sysconfdir=%{_sysconfdir}/proftpd/%{major_version} \
 --localstatedir=%{_localstatedir}/run \
 --with-includes=/usr/postgres/%{postgres_version}/include/:/usr/mysql/%{mysql_version}/include/mysql/ \
 --with-libraries=/usr/postgres/%{postgres_version}/lib/:/usr/mysql/%{mysql_version}/lib/mysql/:/usr/lib/krb5 \
 --enable-ipv6 \
 --enable-ctrls \
 --enable-facl \
 --enable-nls \
 --enable-dso \
 --enable-openssl \
 --with-shared=mod_sql:mod_sql_mysql:mod_sql_postgres:mod_tls

gmake -j$CPUS

%install
cd %{tarball_name}-%{tarball_version}
gmake install DESTDIR=$RPM_BUILD_ROOT
if test -d sun-manpages; then
	cd sun-manpages
	make install DESTDIR=$RPM_BUILD_ROOT
	cd ..
fi

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

# boot method
mkdir -p ${RPM_BUILD_ROOT}/lib/svc/method/
cp %{SOURCE1} ${RPM_BUILD_ROOT}/lib/svc/method/proftpd
chmod +x ${RPM_BUILD_ROOT}/lib/svc/method/proftpd

# manifest
mkdir -p ${RPM_BUILD_ROOT}/var/svc/manifest/network/
cp %{SOURCE2} ${RPM_BUILD_ROOT}/var/svc/manifest/network/proftpd.xml

# configuration
mv ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/proftpd.conf ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/proftpd.conf.original
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/proftpd.conf
cp %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/proftpd.conf.dist
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/conf.d

# Sample Configuration
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d
cp %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/postgres.conf
cp %{SOURCE5} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/mysql.conf
cp %{SOURCE6} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/ftppasswd.conf
cp %{SOURCE7} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/resume.conf
cp %{SOURCE8} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/ftppasswd.sample
cp %{SOURCE9} ${RPM_BUILD_ROOT}%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/logs.conf

# Other Directories
mkdir -p ${RPM_BUILD_ROOT}/var/proftpd/%{major_version}/pub
mkdir -p ${RPM_BUILD_ROOT}/var/proftpd/%{major_version}/logs

rmdir ${RPM_BUILD_ROOT}/var/run

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/sbin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/libexec
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/share
%{_prefix}/%{major_version}/bin/*
%{_prefix}/%{major_version}/sbin/*
%{_prefix}/%{major_version}/share/*

%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/proftpd
%dir %attr (0755, root, bin) %{_sysconfdir}/proftpd/%{major_version}
%dir %attr (0755, root, bin) %{_sysconfdir}/proftpd/%{major_version}/conf.d/
%dir %attr (0755, root, bin) %{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/
%config(noreplace) %{_sysconfdir}/proftpd/%{major_version}/proftpd.conf
%{_sysconfdir}/proftpd/%{major_version}/proftpd.conf.dist
%{_sysconfdir}/proftpd/%{major_version}/proftpd.conf.original
%{_sysconfdir}/proftpd/%{major_version}/ftppasswd.sample
%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/ftppasswd.conf
%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/resume.conf
%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/logs.conf
%dir %attr (0755, root, sys) /var/proftpd
%dir %attr (0755, root, sys) /var/proftpd/%{major_version}
%dir %attr (0755, root, bin) /var/proftpd/%{major_version}/pub
%dir %attr (0755, nobody, nogroup) /var/proftpd/%{major_version}/logs
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/network
%class(manifest) %attr(0444, root, sys) /var/svc/manifest/network/proftpd.xml
%attr (0511,root,bin) /lib/svc/method/proftpd

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib
%{_prefix}/%{major_version}/include/*
%{_prefix}/%{major_version}/lib/*

%files doc
%defattr (-, root, bin)
%dir %attr (0755, root, bin) /usr/share/man
/usr/share/man/*

%files sql
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/libexec
%{_prefix}/%{major_version}/libexec/mod_sql.a
%{_prefix}/%{major_version}/libexec/mod_sql.la
%{_prefix}/%{major_version}/libexec/mod_sql.so

%files postgres
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/libexec
%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/postgres.conf
%{_prefix}/%{major_version}/libexec/mod_sql_postgres.a
%{_prefix}/%{major_version}/libexec/mod_sql_postgres.la
%{_prefix}/%{major_version}/libexec/mod_sql_postgres.so

%files mysql
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/libexec
%{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/mysql.conf
%{_prefix}/%{major_version}/libexec/mod_sql_mysql.a
%{_prefix}/%{major_version}/libexec/mod_sql_mysql.la
%{_prefix}/%{major_version}/libexec/mod_sql_mysql.so

%files tls
%defattr (-, root, bin)
# %dir %attr (0755, root, sys) %{_sysconfdir}
# %dir %attr (0755, root, bin) %{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/libexec
# %{_sysconfdir}/proftpd/%{major_version}/samples-conf.d/tls.conf
%{_prefix}/%{major_version}/libexec/mod_tls.a
%{_prefix}/%{major_version}/libexec/mod_tls.la
%{_prefix}/%{major_version}/libexec/mod_tls.so



%changelog
* Sun May 11 2014 YAMAMOTO Takashi <yamachan@selfnavi.com>
- disable GSSAPI when compile on the OpenIndiana
- change log directory owner
* Tue Aug 27 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add service/network/proftpd-13/module/tls
* Thu Aug 08 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix typo
* Wed May  6 2009 TAKI, Yasushi <taki@justplayer.com>
- Initial Revision
* Tue Jan 12 2010 TAKI, Yasushi <taki@justplayer.com>
- Support 1.3.2c
* Wed Feb  2 2011 TAKI, Yasushi <taki@justplayer.com>
- Support 1.3.3d and mod_gss
* Sun Mar 27 2011 TAKI, Yasushi <taki@justplayer.com>
- Change Permission at /etc
* Mon Aug  5 2013 TAKI, Yasushi <taki@justplayer.com>
- Bump to 1.3.4d
