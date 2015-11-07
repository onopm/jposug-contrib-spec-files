#
# spec file for package: zabbix
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc
%define _prefix /usr/zabbix
%define usr_prefix /usr
%define plain_name zabbix
%define major_version   1.8
%define major_version_no_dot 18
%define _var_prefix /var/zabbix
%define runuser         zabbix
%define runusergroup    zabbix

%define skip_prep 0
%define skip_build 0

Name:           SFEzabbix18
%define _pkg_docdir %{usr_prefix}/share/doc/%{name}
IPS_package_name:  diagnostic/zabbix18
SUNW_Copyright:   %{name}.copyright
Version:        1.8.16
Release:        1%{?dist}
Summary:        Open-source monitoring solution for your IT infrastructure
Group:          Applications/Internet
License:        GPL
URL:            http://www.zabbix.com/
Source0:        http://downloads.sourceforge.net/%{plain_name}/%{plain_name}-%{version}.tar.gz
Source1:        zabbix18-zabbix-web.conf
Source2:        zabbix18-zabbix-server.init
Source3:        zabbix18-zabbix-agent.init
Source4:        zabbix18-zabbix-proxy.init
#Source5:        zabbix18-zabbix-logrotate.in
Source6:        zabbix18-zabbix_agentd.conf
Source7:        zabbix18-zabbix_server.conf
Source8:        zabbix18-zabbix_proxy.conf
Source9:        zabbix18-ipagui.ttf
Source10:        zabbix18-zabbix_enduser_license.txt
Source11:        zabbix-1.8.16-ja_jp.inc.php
#Source12:        eventlog.c
#Source13:       eventlog.h
Source20:        SFEzabbix18-zabbix18_server.xml
Source21:        SFEzabbix18-zabbix18_agent.xml
Source22:        SFEzabbix18-zabbix18_proxy.xml
Patch1:         zabbix-1.8-datasql.patch
Patch2:         zabbix-1.8.4-powered_by_zabbixjp.patch
#Patch3:         zabbix-1.8.2-fix_to_compile_visualstudio_proj.patch
Patch4:         zabbix-1.8.4-graph_font.patch
#Patch5:         zabbix-1.8-parentservice_translate.patch
#Patch6:         zabbix-1.8-chart4_use_imagetext.patch
#Patch7:         zabbix-1.8-loginmenu_translate.patch
#Patch8:         zabbix-1.8-wrong_usergroup_permission.patch
#Patch9:         zabbix-1.8-chart5_use_imagetext.patch
#Patch10:        zabbix-1.8-discoveryconf_seconds_translate.patch
Patch11:        zabbix-1.8-itservice_popup_translate.patch
#Patch12:        zabbix-1.8-installer_require_wrong_phpversion.patch
#Patch13:        zabbix-1.8-template_import.patch
#Patch14:        zabbix-1.8-popup_media_status_translate.patch
#Patch15:        zabbix-1.8-pie_chart.patch
Patch16:         zabbix-1.8.4-setup_from_empty_conf.patch
Patch17:         zabbix-1.8.4-default_period.patch
#Patch18:         zabbix-1.8.3-initial_datasql_status_and_error.patch
#Patch19:         zabbix-1.8.7-zbx4099.patch
Patch100:	zabbix-1.8.18_m4_solaris.patch
Patch101:	zabbix-1.8.16_ldap_m4_solaris.patch

#Buildroot:       %{_tmppath}/%{plain_name}-%{version}-build

BuildRequires:   %pnm_buildrequires_mysql51
#BuildRequires:   postgresql-devel

BuildRequires:   database/postgres-92/library
BuildRequires:   database/postgres-92/developer
BuildRequires:   %pnm_buildrequires_mysql51lib
BuildRequires:   %pnm_buildrequires_mysql51
BuildRequires:   %pnm_requires_system_management_snmp_net_snmp
BuildRequires:   %pnm_buildrequires_library_openldap
BuildRequires:   %pnm_buildrequires_library_gnutls
BuildRequires:   library/iksemel
BuildRequires:   %pnm_buildrequires_sqlite3
BuildRequires:   %pnm_buildrequires_library_unixodbc
BuildRequires:   library/security/ssh2/developer

BuildRequires:   %pnm_buildrequires_curl
BuildRequires:   system/management/openipmi/developer
BuildRequires:   developer/build/autoconf268
BuildRequires:   library/text/gnu-iconv/developer
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc
Requires:      system/library/gcc-runtime
%endif
#Requires:        logrotate
#Requires(pre):   /usr/sbin/useradd

%description
ZABBIX is software that monitors numerous parameters of a
network and the health and integrity of servers. ZABBIX
uses a flexible notification mechanism that allows users
to configure e-mail based alerts for virtually any event.
This allows a fast reaction to server problems. ZABBIX
offers excellent reporting and data visualisation features
based on the stored data. This makes ZABBIX ideal for
capacity planning.

ZABBIX supports both polling and trapping. All ZABBIX
reports and statistics, as well as configuration
parameters are accessed through a web-based front end. A
web-based front end ensures that the status of your network
and the health of your servers can be assessed from any
location. Properly configured, ZABBIX can play an important
role in monitoring IT infrastructure. This is equally true
for small organisations with a few servers and for large
companies with a multitude of servers.

%package server
Summary:         Zabbix server common files
IPS_package_name:  diagnostic/zabbix18/server
Group:           Applications/Internet
Requires:        diagnostic/zabbix18
#Requires:        diagnostic/zabbix18/server-implementation
Requires:        %pnm_requires_diagnostic_fping
Requires:        library/iksemel
Requires:        %pnm_requires_system_management_snmp_net_snmp
Requires:        %pnm_requires_library_unixodbc
Requires:	 library/security/ssh2
Requires:        %pnm_requires_curl
Requires:        system/management/openipmi/libs
Requires:        library/text/gnu-iconv
#Conflicts:       diagnostic/zabbix18/proxy
#Requires(post):  /sbin/chkconfig
#Requires(preun): /sbin/chkconfig
#Requires(preun): /sbin/service

%description server
Zabbix server common files

%package server-mysql
Summary:         Zabbix server compiled to use MySQL
IPS_package_name:  diagnostic/zabbix18/server/mysql
Group:           Applications/Internet
Requires:        diagnostic/zabbix18
Requires:        diagnostic/zabbix18/server
Requires:        %pnm_requires_mysql51lib
#Provides:        diagnostic/zabbix18/server-implementation
#Obsoletes:       zabbix <= 1.5.3-0.1
#Conflicts:       diagnostic/zabbix18/server/pgsql

%description server-mysql
Zabbix server compiled to use MySQL

%package server-pgsql
Summary:         Zabbix server compiled to use PostgresSQL
IPS_package_name:  diagnostic/zabbix18/server/pgsql
Group:           Applications/Internet
Requires:        diagnostic/zabbix18
Requires:        diagnostic/zabbix18/server
Requires:        database/postgres-92/library
#Provides:        zabbix-server-implementation = %{version}-%{release}
#Conflicts:       zabbix-server-mysql
#%description server-pgsql
#Zabbix server compiled to use PostgresSQL

%package agent
Summary:         Zabbix Agent
IPS_package_name:  diagnostic/zabbix18/agent
Group:           Applications/Internet
Requires:        diagnostic/zabbix18
#Requires(post):  /sbin/chkconfig
#Requires(preun): /sbin/chkconfig
#Requires(preun): /sbin/service

%description agent
The Zabbix client agent, to be installed on monitored systems.

%package proxy
Summary:         Zabbix Proxy
IPS_package_name:        diagnostic/zabbix18/proxy
Group:           Applications/Internet
Requires:        diagnostic/zabbix18
#Requires:        diagnostic/zabbix18/proxy-implementation
#Requires(post):  /sbin/chkconfig
#Requires(preun): /sbin/chkconfig
#Requires(preun): /sbin/service
Requires:        %pnm_requires_diagnostic_fping
Requires:        %pnm_requires_system_management_snmp_net_snmp
Requires:        %pnm_requires_library_unixodbc
Requires:        library/security/ssh2
Requires:        %pnm_requires_curl
Requires:        system/management/openipmi/libs
#Conflicts:       diagnostic/zabbix18/web
#Conflicts:       diagnostic/zabbix18/server

%description proxy
The Zabbix proxy

%package proxy-mysql
Summary:         Zabbix proxy compiled to use MySQL
IPS_package_name:        diagnostic/zabbix18/proxy/mysql
Group:           Applications/Internet
Requires:        diagnostic/zabbix18/proxy
Requires:        %pnm_requires_mysql51lib
#Provides:        diagnostic/zabbix18/proxy-implementation
#Conflicts:       diagnostic/zabbix18/proxy/pgsql
#Conflicts:       diagnostic/zabbix18/proxy/sqlite3

%description proxy-mysql
The Zabbix proxy compiled to use MySQL

%package proxy-pgsql
Summary:         Zabbix proxy compiled to use PostgreSQL
IPS_package_name:        diagnostic/zabbix18/proxy/pgsql
Group:           Applications/Internet
Requires:        diagnostic/zabbix18/zabbix-proxy
Requires:        database/postgres-92/library
#Provides:        diagnostic/zabbix18/zabbix-proxy-implementation
#Conflicts:       diagnostic/zabbix18/proxy/mysql
#Conflicts:       diagnostic/zabbix18/proxy/pgsql

#%description proxy-pgsql
#The Zabbix proxy compiled to use PostgreSQL

%package proxy-sqlite3
Summary:         Zabbix proxy compiled to use SQLite
IPS_package_name:        diagnostic/zabbix18/proxy/sqlite3
Group:           Applications/Internet
Requires:        diagnostic/zabbix18/proxy
Requires:        %pnm_requires_sqlite3
#Provides:        diagnostic/zabbix18/proxy-implementation
#Conflicts:       diagnostic/zabbix18/proxy/mysql
#Conflicts:       diagnostic/zabbix18/proxy/pgsql

%description proxy-sqlite3
The Zabbix proxy compiled to use SQLite

%package web
Summary:         Zabbix Web Frontend
IPS_package_name:        diagnostic/zabbix18/web
Group:           Applications/Internet
Requires:        %pnm_requires_web_server_apache_22
Requires:        web/php-53
Requires:        diagnostic/zabbix18
#Requires:        diagnostic/zabbix18/web-database
Requires:        web/php-53/extension/php-bcmath
#Conflicts:       diagnostic/zabbix18/proxy

%description web
The php frontend to display the zabbix web interface.

#%package web-mysql
#Summary:         Zabbix web frontend for MySQL
#IPS_package_name:        diagnostic/zabbix18/web/mysql
#Group:           Applications/Internet
#Requires:        diagnostic/zabbix18/web
#Requires:        web/php-53/extension/php-mysql
#Provides:        diagnostic/zabbix18/web-database
#Obsoletes:       diagnostic/zabbix18/web
#Conflicts:       diagnostic/zabbix18/web-pgsql

#%description web-mysql
#Zabbix web frontend for MySQL

#%package web-pgsql
#Summary:         Zabbix web frontend for PostgreSQL
#IPS_package_name:        diagnostic/zabbix18/web/pgsql
#Group:           Applications/Internet
#Requires:        zabbix-web = %{version}-%{release}
#Requires:        php/pgsql
#Provides:        diagnostic/zabbix18/web-database
#Conflicts:       diagnostic/zabbix18/web-mysql

#%description web-pgsql
#Zabbix web frontend for PostgreSQL

%prep
%if %{skip_prep}
%else
%setup -q -n %{plain_name}-%{version}
%patch1 -p1 -b .datasql.orig
%patch2 -p1 -b .powered_by_zabbixjp.orig
#%patch3 -p1 -b .fix_to_compile_visualstudio_proj.orig
%patch4 -p1 -b .graph_font.orig
#%patch5 -p1 -b .parentservice_translate.orig
#%patch6 -p1 -b .chart4_use_imagestring.orig
#%patch7 -p1 -b .loginmenu_translate.orig
#%patch8 -p1 -b .wrong_usergroup_permission.orig
#%patch9 -p1 -b .chart5_use_imagetext.orig
#%patch10 -p1 -b .discoveryconf_seconds_translate.orig
%patch11 -p1 -b .itservice_popup_translate.orig
#%patch12 -p1 -b .installer_require_wrong_phpversion.orig
#%patch13 -p1 -b .template_import.orig
#%patch14 -p1 -b .popup_media_status_translate.orig
#%patch15 -p1 -b .pie_chart.orig
%patch16 -p1 -b .setup_from_empty_conf.orig
%patch17 -p1 -b .default_period.orig
#%patch18 -p1 -b .initial_datasql_status_and_error.orig
#%patch19 -p1 -b .zbx4099.orig
%patch100 -p1 -b .m4.orig
%patch101 -p1 -b .ldap_m4.orig

rm frontends/php/fonts/DejaVuSans.ttf
cp %{SOURCE9} frontends/php/fonts/ipagui.ttf
cp %{SOURCE10} frontends/php/fonts/zabbix_enduser_license.txt
rm frontends/php/include/locales/ja_jp.inc.php
cp %{SOURCE11} frontends/php/include/locales/ja_jp.inc.php
#cp %{SOURCE12} %{SOURCE13} src/zabbix_agent/

chmod -R a+rX .

# fix up some lib64 issues
%{__perl} -pi.orig -e 's|_LIBDIR=/usr/lib|_LIBDIR=%{_libdir}|g' \
    configure
# skip_prep
%endif

%build
%if %{skip_build}
    cd %{plain_name}-%{version}
%else
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi
common_flags="
    --prefix=%{_prefix}/%{major_version} \
    --exec-prefix=%{_prefix}/%{major_version} \
    --bindir=%{_prefix}/%{major_version}/bin \
    --libexecdir=%{_prefix}/%{major_version}/bin \
    --sbindir=%{_prefix}/%{major_version}/sbin \
    --datadir=%{usr_prefix}/share/%{plain_name}/%{major_version} \
    --sysconfdir=/etc/%{plain_name}/%{major_version} \
    --mandir=%{_prefix}/%{major_version}/man \
    --libdir=%{_prefix}/%{major_version}/lib \
    --includedir=%{_prefix}/%{major_version}/include \
    --sharedstatedir=%{_var_prefix}/%{major_version} \
    --localstatedir=%{_var_prefix}/%{major_version} \
    --localedir=%{usr_prefix}/share/locale/ \
    --docdir=%{_prefix}/%{major_version}/doc \
    --enable-server \
    --enable-agent \
    --enable-proxy \
    --enable-ipv6 \
    --with-net-snmp \
    --with-ldap \
    --with-unixodbc \
    --with-ssh2 \
    --with-openipmi \
    --with-libcurl \
    --with-jabber
"
export CC=gcc
export CXX=g++
export CFLAGS="%optflags -fno-strict-aliasing -Wno-pointer-sign"
export CPPFLAGS=""
export LDFLAGS="%{_ldflags}"
autoconf-2.68
export LD_OPTIONS="%gnu_lib_path -L/usr/mysql/5.1/lib/mysql -R/usr/mysql/5.1/lib/mysql"
%configure $common_flags --with-mysql=/usr/mysql/bin/mysql_config
make -j$CPUS
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_mysql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_mysql

export LD_OPTIONS="%gnu_lib_path"
%configure $common_flags --with-pgsql
make -j$CPUS
mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_pgsql
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_pgsql

%configure $common_flags --with-sqlite3
make -j$CPUS
#mv src/zabbix_server/zabbix_server src/zabbix_server/zabbix_server_sqlite3
mv src/zabbix_proxy/zabbix_proxy src/zabbix_proxy/zabbix_proxy_sqlite3
# skip_build
%endif

%install
%if %{skip_prep}
  cd %{plain_name}-%{version}
%endif
touch src/zabbix_server/zabbix_server
touch src/zabbix_proxy/zabbix_proxy
rm -rf $RPM_BUILD_ROOT
# set up some required directories
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
mkdir -p $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}/alertscripts
mkdir -p $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}/externalscripts
#mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{major_version}/etc/zabbix_agentd.d
mkdir -p $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/log
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/run
mkdir -p $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}

# php frontend
find ./frontends/php -name '*.orig'|xargs rm -f
find ./create -name '*.orig'|xargs rm -f
cp -a frontends/php $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}
mv $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}/php/conf/maintenance.inc.php \
    $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}
ln -s ../../../../../../etc/%{plain_name}/%{major_version}/maintenance.inc.php \
    $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}/php/conf/maintenance.inc.php
touch $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}/zabbix.conf.php
ln -s ../../../../../../etc/%{plain_name}/%{major_version}/zabbix.conf.php \
    $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}/php/conf/zabbix.conf.php
# kill off .htaccess files, options set in SOURCE1
rm -f $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}/php/include/.htaccess
rm -f $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}/php/include/classes/.htaccess
#ln -s /usr/%{plain_name}/%{major_version}/share $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}
# drop config files in place
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/apache2/2.2/conf.d
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache2/2.2/conf.d/%{plain_name}%{major_version_no_dot}.conf
install -m 0644 -p misc/conf/zabbix_agent.conf $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}
install -m 0644 -p %{SOURCE6} $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}/zabbix_agentd.conf
install -m 0644 -p %{SOURCE7} $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}/zabbix_server.conf
install -m 0644 -p %{SOURCE8} $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}/zabbix_proxy.conf
cp -a misc/conf/zabbix_agentd $RPM_BUILD_ROOT/etc/%{plain_name}/%{major_version}/zabbix_agentd.d
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/apache2/2.2/conf.d/%{plain_name}%{major_version_no_dot}.conf
# log rotation
#cat %{SOURCE5} | sed -e 's|COMPONENT|server|g' > \
#     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-server
#cat %{SOURCE5} | sed -e 's|COMPONENT|agentd|g' > \
#     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-agent
#cat %{SOURCE5} | sed -e 's|COMPONENT|proxy|g' > \
#     $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/zabbix-proxy
# init scripts
mkdir -p %{buildroot}/var/svc/manifest/site/
cp %{SOURCE20} %{buildroot}/var/svc/manifest/site/%{plain_name}%{major_version_no_dot}-server.xml
cp %{SOURCE21} %{buildroot}/var/svc/manifest/site/%{plain_name}%{major_version_no_dot}-agent.xml
cp %{SOURCE22} %{buildroot}/var/svc/manifest/site/%{plain_name}%{major_version_no_dot}-proxy.xml
mkdir -p $RPM_BUILD_ROOT/lib/svc/method/
install -m 0755 -p %{SOURCE2} $RPM_BUILD_ROOT/lib/svc/method/%{plain_name}%{major_version_no_dot}_server
install -m 0755 -p %{SOURCE3} $RPM_BUILD_ROOT/lib/svc/method/%{plain_name}%{major_version_no_dot}_agent
install -m 0755 -p %{SOURCE4} $RPM_BUILD_ROOT/lib/svc/method/%{plain_name}%{major_version_no_dot}_proxy
chmod -x $RPM_BUILD_ROOT/lib/svc/method/*

# set up config dir

# install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_prefix}/%{major_version}/sbin/zabbix_server
install -m 0755 -p src/zabbix_server/zabbix_server_* $RPM_BUILD_ROOT%{_prefix}/%{major_version}/sbin
rm $RPM_BUILD_ROOT%{_prefix}/%{major_version}/sbin/zabbix_proxy
install -m 0755 -p src/zabbix_proxy/zabbix_proxy_* $RPM_BUILD_ROOT%{_prefix}/%{major_version}/sbin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
pushd $RPM_BUILD_ROOT/usr/sbin
for file in zabbix_server_mysql zabbix_proxy_mysql zabbix_server_pgsql zabbix_proxy_pgsql zabbix_proxy_sqlite3 zabbix_agent zabbix_agentd
do
   ln -s ../..%{_prefix}/%{major_version}/sbin/$file .
done
popd
mkdir -p $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT/usr/bin
for file in zabbix_sender zabbix_get
do
   ln -s ../..%{_prefix}/%{major_version}/bin/$file .
done
popd
# nuke static libs and empty oracle upgrade sql
rm -rf $RPM_BUILD_ROOT%{_prefix}/%{major_version}/lib/libzbx*.a
# nuke extraneous sql files
rm -rf $RPM_BUILD_ROOT%{usr_prefix}/share/%{plain_name}/%{major_version}/create

%clean
%if %{skip_prep}
  cd %{plain_name}-%{version}
%endif
rm -rf $RPM_BUILD_ROOT

#%pre
## Add the "zabbix" user
#/usr/sbin/useradd -c "Zabbix Monitoring System" \
#        -s /sbin/nologin -r -d %{_localstatedir}/lib/%{plain_name} zabbix 2> /dev/null || :

#%post server
#/sbin/chkconfig --add zabbix-server || :

#%post server-mysql
#if [ $1 -eq 1 ]; then
#  if [ ! -f %{_sbindir}/zabbix_server ]; then
#     cd %{_sbindir}
#     ln -s zabbix_server_mysql zabbix_server || :
#  fi
#fi

#rpm -i, rpm -ivh
#%post server-pgsql
#if [ $1 -eq 1 ]; then
#  if [ ! -f %{_sbindir}/zabbix_server ]; then
#    cd %{_sbindir}
#    ln -s zabbix_server_pgsql zabbix_server || :
#  fi
#fi

#rpm -i, rpm -ivh
#%post agent
#/sbin/chkconfig --add zabbix-agent || :

#rpm -i, rpm -ivh
#%post proxy
#/sbin/chkconfig --add zabbix-proxy || :

#rpm -i, rpm -ivh
#%post proxy-mysql
#if [ $1 -eq 1 ]; then
#  if [ ! -f %{_sbindir}/zabbix_proxy ]; then
#    cd %{_sbindir}
#    ln -s zabbix_proxy_mysql zabbix_proxy || :
#  fi
#fi

#rpm -i, rpm -ivh
#%post proxy-pgsql
#if [ $1 -eq 1 ]; then
# if [ ! -f %{_sbindir}/zabbix_proxy ]; then
#    cd %{_sbindir}
#    ln -s zabbix_proxy_pgsql zabbix_proxy || :
#  fi
#fi

#rpm -i, rpm -ivh
#%post proxy-sqlite3
#if [ $1 -eq 1 ]; then
#  if [ ! -f %{_sbindir}/zabbix_proxy ]; then
#    cd %{_sbindir}
#    ln -s zabbix_proxy_sqlite3 zabbix_proxy || :
#  fi
#fi

#rpm -e
#%preun server
#if [ $1 -eq 0 ]
#then
#  /sbin/service zabbix-server stop >/dev/null 2>&1 || :
#  /sbin/chkconfig --del zabbix-server
#fi

#rpm -e
#%preun server-mysql
#if [ $1 -eq 0 ]; then
#  if [ -L %{_sbindir}/zabbix_server ]; then
#    rm -f %{_sbindir}/zabbix_server || :
#  fi
#fi

#rpm -e
#%preun server-pgsql
#if [ $1 -eq 0 ]; then
#  if [ -L %{_sbindir}/zabbix_server ]; then
#    rm -f %{_sbindir}/zabbix_server || :
#  fi
#fi

#rpm -e
#%preun agent
#if [ $1 -eq 0 ]
#then
#  /sbin/service zabbix-agent stop >/dev/null 2>&1 || :
#  /sbin/chkconfig --del zabbix-agent
#fi

#rpm -e
#%preun proxy
#if [ $1 -eq 0 ]
#then
#  /sbin/service zabbix-proxy stop >/dev/null 2>&1 || :
#  /sbin/chkconfig --del zabbix-proxy
#fi

#rpm -e
#%preun proxy-mysql 
#if [ $1 -eq 0 ]; then
#  if [ -L %{_sbindir}/zabbix_proxy ]; then
#    rm -f %{_sbindir}/zabbix_proxy || :
#  fi
#fi

#rpm -e
#%preun proxy-pgsql
#if [ $1 -eq 0 ]; then
#  if [ -L %{_sbindir}/zabbix_proxy ]; then
#    rm -f %{_sbindir}/zabbix_proxy || :
#  fi
#fi

#rpm -e
#%preun proxy-sqlite3
#if [ $1 -eq 0 ]; then
#  if [ -L %{_sbindir}/zabbix_proxy ]; then
#    rm -f %{_sbindir}/zabbix_proxy || :
#  fi
#fi

#rpm -U
#%postun server
#if [ $1 -gt 1 ]; then
#  /sbin/service zabbix-server condrestart >/dev/null 2>&1 || :
#fi

#rpm -U
#%postun agent
#if [ $1 -gt 1 ]; then
#  /sbin/service zabbix-agent condrestart >/dev/null 2>&1 || :
#fi

#rpm -U
#%postun proxy
#if [ $1 -gt 1 ]; then
#  /sbin/service zabbix-proxy condrestart >/dev/null 2>&1 || :
#fi

%actions
group groupname="%{runusergroup}"
user ftpuser=false gcos-field="zabbix user" username="%{runuser}" password=NP group="%{runusergroup}" home-dir="%{_var_prefix}/%{major_version}" login-shell="/bin/true" group-list="zabbix"

%if %{skip_prep}
%buildroot               %{_tmppath}/%{name}-%{version}-build/
%endif
%files
%defattr(-,root,bin)
%attr(0755,zabbix,zabbix) %dir %{_var_prefix}/%{major_version}/log
%attr(0755,zabbix,zabbix) %dir %{_var_prefix}/%{major_version}/run
%if %( expr %{skip_prep} '=' 0 )
%doc AUTHORS ChangeLog COPYING NEWS README
%doc upgrades/dbpatches/1.6/oracle upgrades/dbpatches/1.6/mysql upgrades/dbpatches/1.6/postgresql upgrades/dbpatches/1.8/oracle upgrades/dbpatches/1.8/mysql upgrades/dbpatches/1.8/postgresql create/data/images/* create/schema/*
%endif

%files server
%defattr(-,root,bin)
%{_prefix}/%{major_version}/man/man8/zabbix_server.8
%config(noreplace) %attr(600,zabbix,zabbix) /etc/%{plain_name}/%{major_version}/zabbix_server.conf
#%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-server
%dir /etc/%{plain_name}/%{major_version}/alertscripts
%dir /etc/%{plain_name}/%{major_version}/externalscripts
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/site
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/site/%{plain_name}%{major_version_no_dot}-server.xml
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/%{plain_name}%{major_version_no_dot}_server

%files server-mysql
%defattr(-,root,bin)
%{_prefix}/%{major_version}/sbin/zabbix_server_mysql
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/sbin/zabbix_server_mysql

%files server-pgsql
%defattr(-,root,bin)
%{_prefix}/%{major_version}/sbin/zabbix_server_pgsql
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/sbin/zabbix_server_pgsql

%files agent
%defattr(-,root,bin)
%{_prefix}/%{major_version}/man/man8/zabbix_agentd.8
%{_prefix}/%{major_version}/man/man1/zabbix_get.1
%{_prefix}/%{major_version}/man/man1/zabbix_sender.1
%config(noreplace) %attr(600,zabbix,zabbix) /etc/%{plain_name}/%{major_version}/zabbix_agent.conf
%config(noreplace) %attr(600,zabbix,zabbix) /etc/%{plain_name}/%{major_version}/zabbix_agentd.conf
#%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-agent
%dir %attr(755,zabbix,zabbix) /etc/%{plain_name}/%{major_version}/zabbix_agentd.d
%config(noreplace) /etc/%{plain_name}/%{major_version}/zabbix_agentd.d/userparameter_examples.conf
%config(noreplace) /etc/%{plain_name}/%{major_version}/zabbix_agentd.d/userparameter_mysql.conf
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/site
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/site/%{plain_name}%{major_version_no_dot}-agent.xml
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/%{plain_name}%{major_version_no_dot}_agent
%{_prefix}/%{major_version}/sbin/zabbix_agent
%{_prefix}/%{major_version}/sbin/zabbix_agentd
%{_prefix}/%{major_version}/bin/zabbix_sender
%{_prefix}/%{major_version}/bin/zabbix_get
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/sbin/zabbix_agent
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/sbin/zabbix_agentd
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/bin/zabbix_sender
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/bin/zabbix_get

%files proxy
%defattr(-,root,bin)
%{_prefix}/%{major_version}/man/man8/zabbix_proxy.8
%config(noreplace) %attr(600,zabbix,zabbix) /etc/%{plain_name}/%{major_version}/zabbix_proxy.conf
#%config(noreplace) %{_sysconfdir}/logrotate.d/zabbix-proxy
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/site
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/site/%{plain_name}%{major_version_no_dot}-proxy.xml
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/%{plain_name}%{major_version_no_dot}_proxy

%files proxy-mysql
%defattr(-,root,bin)
%{_prefix}/%{major_version}/sbin/zabbix_proxy_mysql
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/sbin/zabbix_proxy_mysql

%files proxy-pgsql
%defattr(-,root,bin)
%{_prefix}/%{major_version}/sbin/zabbix_proxy_pgsql
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/sbin/zabbix_proxy_pgsql

%files proxy-sqlite3
%defattr(-,root,bin)
%{_prefix}/%{major_version}/sbin/zabbix_proxy_sqlite3
%attr (0555, root, bin) %ips_tag (mediator=%{plain_name} mediator-version=%{major_version}) /usr/sbin/zabbix_proxy_sqlite3

%files web
%defattr(-,root,bin)
%config(noreplace) %attr(600,webservd,webservd) /etc/%{plain_name}/%{major_version}/zabbix.conf.php
%config(noreplace) /etc/%{plain_name}/%{major_version}/maintenance.inc.php
%config(noreplace) %{_sysconfdir}/apache2/2.2/conf.d/%{plain_name}%{major_version_no_dot}.conf
%{usr_prefix}/share/%{plain_name}

#%files web-mysql
#%defattr(-,root,bin)

#%files web-pgsql
#%defattr(-,root,bin)

%changelog
* Fri Dec 06 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Added database dependencies.

* Thu Dec 05 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial commit for the jposug

* Thu Jan 17 2013 Atsushi Tanaka <a.tanaka77@gmail.com> - 1.8.16-1
- Update to 1.8.16
- Update Japanese translation (Source11)
- Remove server-sqlite3 and web-sqlite3 subpackages

* Tue Aug 21 2012 Atsushi Tanaka <a.tanaka77@gmail.com> - 1.8.15-1
- Update to 1.8.15

* Fri Jun 29 2012 Atsushi Tanaka <a.tanaka77@gmail.com> - 1.8.14-1
- Update to 1.8.14
- Update Japanese translation (Source11)

* Sat May 12 2012 Atsushi Tanaka <a.tanaka77@gmail.com> - 1.8.13-1
- Update to 1.8.13
- Update Japanese translation (Source11)

* Tue Apr 24 2012 Atsushi Tanaka <a.tanaka77@gmail.com> - 1.8.12-1
- Update to 1.8.12
- Update Japanese translation (Source11)
- Update zabbix_aegntd.conf, zabbix_server.conf, zabbix_proxy.conf

* Fri Mar 23 2012 Atsushi Tanaka <a.tanaka77@gmail.com> - 1.8.11-1
- Update to 1.8.11
- Update zabbix_server.conf, zabbix_proxy.conf
- Update Japanese translation (Source11)
- Change default value of mbstring.func_overload for PHP (Source1)

* Tue Jan 3 2012 Kodai Terashima <kodai74@gmail.com> - 1.8.10-1
- Update to 1.8.10
- Update Japanese translation (Source11)

* Mon Nov 28 2011 Atsushi Tanaka <a.tanaka77@gmail.com> - 1.8.9-1
- Update to 1.8.9
- Update Japanese translation (Source11)

* Sat Oct 8 2011 Kodai Terashima <kodai74@gmail.com> - 1.8.8-1
- Update to 1.8.8
- Update Japanese translation (Source11)
- Delete ZBX-4099 patch (Source19)

* Thu Sep 22 2011 Kodai Terashima <kodai74@gmail.com> - 1.8.7-1
- Update to 1.8.7
- Update Japanese translation (Source11)
- Fix possible crash zabbix server when use sum(),min(),max(),diff() function. ZBX-4099 (Source19)

* Tue Aug 30 2011 Kodai Terashima <kodai74@gmail.com> - 1.8.6-1
- Update to 1.8.6
- Update Japanese translation (Source11)
- Update config files (Source6, Source7, Source8)
- Update init scripts for reload of a configuration cache data

* Wed Aug 10 2011 Kodai Terashima <kodai74@gmail.com> - 1.8.5-2
- Add support RHEL6/CentOS6

* Tue Apr 19 2011 Kodai Terashima <kodai74@gmail.com> - 1.8.5-1
- Update to 1.8.5
- Update config files (Source6, Source7, Source8)
- Update Japanese translation (Source11)
- Add userparameter_mysql.conf and userparameter_examples.conf

* Sun Jan 23 2011 Kodai Terashima <kodai74@gmail.com> - 1.8.4-1
- Update to 1.8.4
- Add access control to api and config directory for web interface (Source1)
- Update config files (Source6, Source7, Source8)
- Change log file rotation by logroate, not zabbix (Source7, Source8)
- Update Japanese translation (Source11)
- Update setup from empty patch (Patch 16)
- Add initial sql files for zabbix-proxy
- Delete /etc/zabbix/defines.inc.php

* Thu Aug 26 2010 Kodai Terashima <kodai74@gmail.com> - 1.8.3-1
- Update to 1.8.3
- Delete patch fix_to_compile_visualstudio_proj.patch (Patch3)
- Update config files (Source6, Source7, Source8)
- Add require net-snmp package instead of net-snmp-libs for server and proxy
- Change default time period from 23:59 to 24:00 (Patch17)
- Fix wrong status and remove error message from templates in data.sql

* Fri May 21 2010 Kodai Terashima <kodai74@gmail.com> - 1.8.2-1
- Update to 1.8.2
- Change mbstring.func_overload to 6 in zabbix-web.conf
- Add parch to redirect web installer if db parameter is empty in zabbix.conf.php (Patch16)
- Update Japanese translation (Source11)
- Update parch for windows VisualStudio project file (Patch3)
- Update zabbix_server.conf and zabbix_agentd.conf to merge 1.8.2 default config file (Source6, Source7)
- Add upload_max_filesize and max_input_time in zabbix-web.conf (Source1)
- Delete eventlog.c and eventlog.h (Source12, Source13)
- Create symlink for zabbix_server_* and zabbix_proxy_* if first install
- Add using binary filename "zabbix_server" and "zabbix_proxy" in init scripts
- Add require version for libssh, curl, OpenIPMI, php
- Add conflict proxy and web packages
- Add --without-libcurl and --without-openipmi compile options for CentOS4
- Some improvements for spec file
- Add require net-snmp-libs, unixODBC, libssh2, curl, OpenIPMI-libs for proxy package
- Add require libssh2 for server package
- Add conflicts zabbix-proxy on zabbix-server/zabbix-web

* Mon Feb 2 2010 Kodai Terashima <kodai74@gmail.com> -1.8.1-1
- Update to 1.8.1
- Update Japanese translation for zabbix 1.8.1
- Update zabbix_agentd.conf, zabbix_server.conf, zabbix_proxy.conf

* Sun Jan 17 2010 Kodai Terashima <kodai74@gmail.com> - 1.8
- Update to 1.8
- Add patch to change default language to Japanese (Patch1)
- Add patch to add link to ZABBIX-JP in header and footer (Patch2)
- Add patch to fix compile windows agent (Patch3)
- Add patch to use Japanese font in graph (Patch4)
- Add patch to translate "Parent service" in IT Service screen (patch5)
- Add patch to use imageText function in chart4.php (Patch6)
- Add patch to translate login menu (Patch7)
- Add patch to wrong usergroup permission (Patch8)
- Add patch to use imageText function in chart5.php (Patch9)
- Add patch to translate "seconds" in discovery configuration screen (Patch10)
- Add patch to translate popup menu in IT Service screen (Patch11)
- Add patch to fix installer require wrong php version (Patch12)
- Add patch to fix import template (Patch13)
- Add patch to translate user media popup screen (Patch14)
- Add patch to fix pie chart (Patch15)

* Wed Dec 10 2009 Kodai Terashima <kodai74@gmail.com> - 1.7.4-1
- Update to 1.7.4
- Delete zabbix-1.7-checks_db_few_argument.patch

* Wed Dec 10 2009 Kodai Terashima <kodai74@gmail.com> - 1.7.3-1
- Update to 1.7.3
- Replace manual pdf file by README 

* Mon Nov 11 2009 Kodai Terashima <kodai74@gmail.com> - 1.7.2-1
- Update to 1.7.2
- Add libssh compile option

* Wed Nov 4 2009 Kodai Terashima <kodai74@gmail.com> -1.7.1-1
- Update to 1.7.1

* Tue Nov 3 2009 Kodai Terashima <kodai74@gmail.com> - 1.7-1
- Update to 1.7
- add patch checks_db_few_argument.patch

* Tue Oct 27 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.6-1
- Updat zabbix-1.6.6-locale-cn_zh.patch (Patch1)
- Delete zabbix-1.6.4-pdb_parse_counter_path.patch (Patch9)
- Delete zabbix-1.6.4-display_events.patch (Patch15)

* Tue Oct 27 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.5-1
- Update zabbix-1.6.5-copyright_year.patch (Patch3)
- Update zabbix-1.6.5-graph_description.patch (Patch4)
- Update zabbix-1.6.5-powered_by_zabbixjp.patch (Patch13)
- Delete zabbix-1.6.4-localized_colors.patch (Patch5)

* Sun Oct 18 2009 Kodai Terashima <kodai74@gmail.com> - 1.6.4-1
- initialized package for ZABBIX-JP
- Update Japanese translation (Source6)
- fix the bug that cannot choose Japanese language (Patch1)
- Add a patch to support Japanese font for Graph and Map (Patch2,Patch4)
- Add a patch to fix copyright-year in locales file from MIRACLE LINUX (Patch3)
- Add a patch from MIRACLE LINUX to fix does not use color link on map when use Japanese language (Patch5)
- allow item/trigger parameter to set multibyte character from MIRACLE LINUX (Patch6)
- Add a patch to convert from SJIS to UTF-8 for Windows Event Log from MIRACLE LINUX(Patch7)
- Add a patch for fix crash windows 2000 agent from MIRACLE LINUX(Patch8,9)
- add system.swap.in and system.swap.out patch for LVM devices and other device-mapper devices from MIRACLE LINUX(Patch10)
- fix FormatMessage crash in case of aInsertStrs having more than 64 elements from MIRACLE LINUX(Patch11)
- Change data.sql to select Japanese locale by default (Patch12)
- Add link to ZABBIX-JP in header and footer (Patch13)
- Add a patch to allow multibyte trigger expression (Patch14)
- Add a patch to improve slow query to show events screen (Patch15)
- Add a patch to fix sum parameter on proc_info item (Patch16)
- Add a patch to fix LDAP library probrem when complie on Windows (Patch17)
- Add a patch to fix broken character probrem when compile on Windows (Patch18)

* Fri Jan 23 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-2
- Rebuild for MySQL 5.1.X

* Fri Jan 16 2009 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.2-1
- Update to 1.6.2: http://www.zabbix.com/rn1.6.2.php

* Thu Dec  4 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-1
- Fix BZ#474593 by adding a requires.

* Wed Nov  5 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6.1-1
- Update to 1.6.1

* Tue Sep 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6-1.1
- Bump release because forgot to add some new files.

* Thu Sep 30 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.6-1
- Update to final 1.6

* Mon Aug 11 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.4.6-2
- Fix license tag.

* Fri Jul 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.6-1
- Update to 1.4.6

* Mon Jul 07 2008 Dan Horak <dan[at]danny.cz> - 1.4.5-4
- add LSB headers into init scripts
- disable internal log rotation

* Fri May 02 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.5-3
- Seems the zabbix folks replaced the original 1.4.5 tarball with
  an updated tarball or something -- it actually does contain a
  tiny bit of additional code... So update to newer 1.4.5.

* Tue Apr 08 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.5-2
- Fix building w/postgresql (#441456)

* Tue Mar 25 2008 Jeffrey C. Ollie <jeff@ocjtech.us> - 1.4.5-1
- Update to 1.4.5

* Thu Feb 14 2008 Jarod Wilson <jwilson@redhat.com> - 1.4.4-2
- Bump and rebuild with gcc 4.3

* Mon Dec 17 2007 Jarod Wilson <jwilson@redhat.com> - 1.4.4-1
- New upstream release
- Fixes two crasher bugs in 1.4.3 release

* Wed Dec 12 2007 Jarod Wilson <jwilson@redhat.com> - 1.4.3-1
- New upstream release

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.4.2-5
- Rebuild for deps

* Sat Dec 01 2007 Dan Horak <dan[at]danny.cz> 1.4.2-4
- add security fix (#407181)

* Thu Sep 20 2007 Dan Horak <dan[at]danny.cz> 1.4.2-3
- Add a patch to clean a warning during compile
- Add a patch to fix cpu load computations

* Tue Aug 21 2007 Jarod Wilson <jwilson@redhat.com> 1.4.2-2
- Account for binaries moving from %%_bindir to %%_sbindir

* Tue Aug 21 2007 Jarod Wilson <jwilson@redhat.com> 1.4.2-1
- New upstream release

* Mon Jul 02 2007 Jarod Wilson <jwilson@redhat.com> 1.4.1-1
- New upstream release

* Fri Jun 29 2007 Jarod Wilson <jwilson@redhat.com> 1.4-3
- Install correct sql init files (#244991)
- Add Requires: php-bcmath to zabbix-web (#245767)

* Wed May 30 2007 Jarod Wilson <jwilson@redhat.com> 1.4-2
- Add placeholder zabbix.conf.php

* Tue May 29 2007 Jarod Wilson <jwilson@redhat.com> 1.4-1
- New upstream release

* Fri Mar 30 2007 Jarod Wilson <jwilson@redhat.com> 1.1.7-1
- New upstream release

* Wed Feb 07 2007 Jarod Wilson <jwilson@redhat.com> 1.1.6-1
- New upstream release

* Thu Feb 01 2007 Jarod Wilson <jwilson@redhat.com> 1.1.5-1
- New upstream release

* Tue Jan 02 2007 Jarod Wilson <jwilson@redhat.com> 1.1.4-5
- Add explicit R:php to zabbix-web (#220676)

* Wed Dec 13 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-4
- Fix snmp polling buffer overflow (#218065)

* Wed Nov 29 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-3
- Rebuild for updated libnetsnmp

* Thu Nov 16 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-2
- Fix up pt_br
- Add Req-pre on useradd

* Wed Nov 15 2006 Jarod Wilson <jwilson@redhat.com> 1.1.4-1
- Update to 1.1.4

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-3
- Add BR: gnutls-devel, R: net-snmp-libs

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-2
- Fix php-pgsql Requires

* Tue Nov 14 2006 Jarod Wilson <jwilson@redhat.com> 1.1.3-1
- Update to 1.1.3

* Mon Oct 02 2006 Jarod Wilson <jwilson@redhat.com> 1.1.2-1
- Update to 1.1.2
- Enable alternate building with postgresql support

* Thu Aug 17 2006 Jarod Wilson <jwilson@redhat.com> 1.1.1-2
- Yank out Requires: mysql-server
- Add Requires: for php-gd and fping

* Tue Aug 15 2006 Jarod Wilson <jwilson@redhat.com> 1.1.1-1
- Update to 1.1.1
- More macroification
- Fix up zabbix-web Requires:
- Prep for enabling postgres support

* Thu Jul 27 2006 Jarod Wilson <jwilson@redhat.com> 1.1-2
- Add Requires: on chkconfig and service
- Remove openssl-devel from BR, mysql-devel pulls it in
- Alter scriptlets to match Fedora conventions

* Tue Jul 11 2006 Jarod Wilson <jwilson@redhat.com> 1.1-1
- Initial build for Fedora Extras
