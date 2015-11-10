#
# spec file for package SFEmysql-56
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 0
%define _gpp g++
%include base.inc

%define _prefix /usr/mysql
%define _var_prefix /var/mysql
%define tarball_name     mysql
%define tarball_version  5.6.27
%define major_version	 5.6
%define q4m_ver          0.9.14
%define prefix_name      SFEmysql-56
%define _basedir         %{_prefix}/%{major_version}

Name:                    %{prefix_name}
IPS_package_name:        database/mysql-56
Summary:	         MySQL 5.6
Version:                 %{tarball_version}
License:		 GPL v2
Group:		System/Databases
Url:                     http://www.mysql.com/
Source:                  http://dev.mysql.com/get/Downloads/MySQL-%{major_version}/mysql-%{version}.tar.gz
Source1:                 mysql_56
Source2:                 mysql_56.xml
Source3:                 http://github.com/q4m/q4m/archive/%{q4m_ver}.tar.gz
Source4:                 my-5.6.cnf.master
Patch1:                  5.6-select-where-queue-wait.patch
Patch2:                  5.6-queue_cond.cc-0.9.14.patch
Patch3:                  5.6-queue_cond.h-0.9.14.patch
Patch4:                  5.6-ha_queue.cc-0.9.14.patch
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: developer/build/cmake
Requires:      database/mysql-common
Requires:      database/mysql-56/library = %{version}

%description
The MySQL(TM) software delivers a very fast, multi-threaded, multi-user,
and robust SQL (Structured Query Language) database server. MySQL Server
is intended for mission-critical, heavy-load production systems as well
as for embedding into mass-deployed software. MySQL is a trademark of
Oracle and/or its affiliates

The MySQL software has Dual Licensing, which means you can use the MySQL
software free of charge under the GNU General Public License
(http://www.gnu.org/licenses/). You can also purchase commercial MySQL
licenses from Oracle and/or its affiliates if you do not wish to be bound by the terms of
the GPL. See the chapter "Licensing and Support" in the manual for
further info.

The MySQL web site (http://www.mysql.com/) provides the latest news and
information about the MySQL software.  Also please see the documentation
and the manual for more information.

This package includes the MySQL server binary as well as related utilities
to run and administer a MySQL server.

%package mysql64
IPS_package_name: database/mysql-56/64
Summary: MySQL 64bit binary
Requires: database/mysql-56
Requires: database/mysql-56/library = %{version}

%package library
IPS_package_name: database/mysql-56/library
Summary: MySQL library (32bit/64bit)

%package tests
IPS_package_name: database/mysql-56/tests
Summary: MySQL tests
Requires:      library/perl-5/dbi-512
Requires:      library/perl-5/dbd-mysql-512

%package devel
IPS_package_name: database/mysql-56/devel
Summary: MySQL devel

%prep
%setup -c -n %{tarball_name}-%{tarball_version}
cd %{tarball_name}-%{tarball_version}
%patch1 -p0
cd ..
tar -xzvf %{SOURCE3}
mv q4m-%{q4m_ver} %{tarball_name}-%{tarball_version}/storage/q4m
cd %{tarball_name}-%{tarball_version}
%patch2 -p1
%patch3 -p1
%patch4 -p1
cd ..


%ifarch amd64 sparcv9
rm -rf %{tarball_name}-%{tarball_version}-64
cp -rp %{tarball_name}-%{tarball_version} %{tarball_name}-%{tarball_version}-64
%endif


%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

cmake . -DBUILD_CONFIG=mysql_release \
    -DFEATURE_SET="community" \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}/%{major_version}" \
    -DINSTALL_LIBDIR="lib/mysql" \
    -DMYSQL_DATADIR="/var/mysql" \
    -DMYSQL_UNIX_ADDR="/var/tmp/mysql.sock" \
    -DENABLED_LOCAL_INFILE=ON \
    -DENABLE_DTRACE=ON \
    -DWITH_EMBEDDED_SERVER=OFF \
    -DWITH_EDITLINE=bundled \
    -DSYSCONFDIR=/etc/mysql \
    -DCMAKE_C_FLAGS="-O3 -m32 -mt -KPIC" \
    -DCMAKE_CXX_FLAGS="-O3 -m32 -mt -KPIC"

gmake -j$CPUS
gmake -j$CPUS test

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{tarball_version}-64

cmake . -DBUILD_CONFIG=mysql_release \
    -DFEATURE_SET="community" \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}/%{major_version}" \
    -DINSTALL_LIBDIR="lib/%{_arch64}/mysql" \
    -DINSTALL_BINDIR="bin/%{_arch64}" \
    -DINSTALL_PLUGINDIR="lib/%{_arch64}/plugin" \
    -DMYSQL_DATADIR="/var/mysql" \
    -DMYSQL_UNIX_ADDR="/var/tmp/mysql.sock" \
    -DENABLED_LOCAL_INFILE=ON \
    -DENABLE_DTRACE=ON \
    -DWITH_EMBEDDED_SERVER=OFF \
    -DWITH_EDITLINE=bundled \
    -DSYSCONFDIR=/etc/mysql \
    -DCMAKE_C_FLAGS="-O3 -m64 -mt -KPIC" \
    -DCMAKE_CXX_FLAGS="-O3 -m64 -mt -KPIC -library=stlport4"

gmake -j$CPUS
gmake -j$CPUS test
%endif

%install
rm -rf $RPM_BUILD_ROOT

# install 32bit
cd %{tarball_name}-%{tarball_version}
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/mysql/%{major_version}
install support-files/my-default.cnf $RPM_BUILD_ROOT/etc/mysql/%{major_version}/my.cnf
install %{SOURCE4} $RPM_BUILD_ROOT/etc/mysql/%{major_version}/my-5.6.cnf.master
install storage/q4m/support-files/install.sql $RPM_BUILD_ROOT/usr/mysql/%{major_version}/share/install.sql
install storage/q4m/support-files/q4m-forward $RPM_BUILD_ROOT/usr/mysql/%{major_version}/share/q4m-forward

mkdir -p $RPM_BUILD_ROOT/usr/lib
pushd $RPM_BUILD_ROOT/usr/lib
ln -s ../mysql/%{major_version}/lib/mysql/libstlport.so.1 .
popd

# install 64bit
%ifarch amd64 sparcv9

pushd $RPM_BUILD_ROOT/usr/mysql/%{major_version}
mv bin bin32
popd

cd ../%{tarball_name}-%{tarball_version}-64
make install DESTDIR=$RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT/usr/mysql/%{major_version}/lib
%ifarch amd64
ln -s amd64 64
%endif
%ifarch sparcv9
%endif

cd $RPM_BUILD_ROOT/usr/mysql/%{major_version}
mv bin/m* bin/%{_arch64}
mv bin32/* bin/
rmdir bin32
cd bin
ln -s %{_arch64} 64

mkdir -p $RPM_BUILD_ROOT/usr/lib/%{_arch64}
cd $RPM_BUILD_ROOT/usr/lib/%{_arch64}
ln -s ../../mysql/%{major_version}/lib/%{_arch64}/mysql/libstlport.so.1 .
%endif

#
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/data
mkdir -p $RPM_BUILD_ROOT/lib/svc/method
install -m 0555 %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/application/database
install -m 0444 %{SOURCE2} $RPM_BUILD_ROOT/var/svc/manifest/application/database

cd $RPM_BUILD_ROOT/usr/mysql/%{major_version}/bin
ln -s ../scripts/mysql_install_db .
cd $RPM_BUILD_ROOT/usr/mysql/%{major_version}/bin/64
ln -s ../../scripts/mysql_install_db .

cd $RPM_BUILD_ROOT/usr/mysql

mkdir -p $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../mysql/%{major_version}/bin/innochecksum .
ln -s ../mysql/%{major_version}/bin/msql2mysql .
ln -s ../mysql/%{major_version}/bin/my_print_defaults .
ln -s ../mysql/%{major_version}/bin/myisam_ftdump .
ln -s ../mysql/%{major_version}/bin/myisamchk .
ln -s ../mysql/%{major_version}/bin/myisamlog .
ln -s ../mysql/%{major_version}/bin/myisampack .
ln -s ../mysql/%{major_version}/bin/mysql .
ln -s ../mysql/%{major_version}/bin/mysql_client_test .
ln -s ../mysql/%{major_version}/bin/mysql_config .
ln -s ../mysql/%{major_version}/bin/mysql_config_editor .
ln -s ../mysql/%{major_version}/bin/mysql_convert_table_format .
ln -s ../mysql/%{major_version}/bin/mysql_find_rows .
ln -s ../mysql/%{major_version}/bin/mysql_fix_extensions .
ln -s ../mysql/%{major_version}/bin/mysql_plugin .
ln -s ../mysql/%{major_version}/bin/mysql_secure_installation .
ln -s ../mysql/%{major_version}/bin/mysql_setpermission .
ln -s ../mysql/%{major_version}/bin/mysql_tzinfo_to_sql .
ln -s ../mysql/%{major_version}/bin/mysql_upgrade .
ln -s ../mysql/%{major_version}/bin/mysql_waitpid .
ln -s ../mysql/%{major_version}/bin/mysql_zap .
ln -s ../mysql/%{major_version}/bin/mysqlaccess .
ln -s ../mysql/%{major_version}/bin/mysqlaccess.conf .
ln -s ../mysql/%{major_version}/bin/mysqladmin .
ln -s ../mysql/%{major_version}/bin/mysqlbinlog .
ln -s ../mysql/%{major_version}/bin/mysqlbug .
ln -s ../mysql/%{major_version}/bin/mysqlcheck .
ln -s ../mysql/%{major_version}/bin/mysqld .
ln -s ../mysql/%{major_version}/bin/mysqld_multi .
ln -s ../mysql/%{major_version}/bin/mysqld_safe .
ln -s ../mysql/%{major_version}/bin/mysqldump .
ln -s ../mysql/%{major_version}/bin/mysqldumpslow .
ln -s ../mysql/%{major_version}/bin/mysqlhotcopy .
ln -s ../mysql/%{major_version}/bin/mysqlimport .
ln -s ../mysql/%{major_version}/bin/mysqlshow .
ln -s ../mysql/%{major_version}/bin/mysqlslap .
ln -s ../mysql/%{major_version}/bin/mysqltest .
ln -s ../mysql/%{major_version}/bin/perror .
ln -s ../mysql/%{major_version}/bin/replace .
ln -s ../mysql/%{major_version}/bin/resolve_stack_dump .
ln -s ../mysql/%{major_version}/bin/resolveip .

mkdir -p $RPM_BUILD_ROOT/usr/bin/amd64
cd $RPM_BUILD_ROOT/usr/bin/amd64
ln -s ../../mysql/%{major_version}/bin/amd64/innochecksum .
ln -s ../../mysql/%{major_version}/bin/amd64/msql2mysql .
ln -s ../../mysql/%{major_version}/bin/amd64/my_print_defaults .
ln -s ../../mysql/%{major_version}/bin/amd64/myisam_ftdump .
ln -s ../../mysql/%{major_version}/bin/amd64/myisamchk .
ln -s ../../mysql/%{major_version}/bin/amd64/myisamlog .
ln -s ../../mysql/%{major_version}/bin/amd64/myisampack .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_client_test .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_config .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_config_editor .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_convert_table_format .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_find_rows .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_fix_extensions .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_plugin .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_secure_installation .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_setpermission .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_tzinfo_to_sql .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_upgrade .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_waitpid .
ln -s ../../mysql/%{major_version}/bin/amd64/mysql_zap .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlaccess .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlaccess.conf .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqladmin .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlbinlog .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlbug .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlcheck .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqld .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqld_multi .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqld_safe .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqldump .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqldumpslow .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlhotcopy .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlimport .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlshow .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqlslap .
ln -s ../../mysql/%{major_version}/bin/amd64/mysqltest .
ln -s ../../mysql/%{major_version}/bin/amd64/perror .
ln -s ../../mysql/%{major_version}/bin/amd64/replace .
ln -s ../../mysql/%{major_version}/bin/amd64/resolve_stack_dump .
ln -s ../../mysql/%{major_version}/bin/amd64/resolveip .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/share
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/docs
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/support-files
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/data
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/data/test
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/man
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/scripts
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/innochecksum
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/msql2mysql
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/my_print_defaults
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/myisam_ftdump
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/myisamchk
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/myisamlog
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/myisampack
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_client_test
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_config
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_config_editor
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_convert_table_format
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_find_rows
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_fix_extensions
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_plugin
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_secure_installation
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_setpermission
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_tzinfo_to_sql
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_upgrade
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_waitpid
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_zap
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlaccess
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlaccess.conf
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqladmin
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlbinlog
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlbug
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlcheck
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqld
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqld_multi
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqld_safe
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqldump
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqldumpslow
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlhotcopy
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlimport
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlshow
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqlslap
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysqltest
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/perror
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/replace
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/resolve_stack_dump
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/resolveip
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/mysql_install_db
%attr (0444, root, bin) %{_prefix}/%{major_version}/README
%attr (0444, root, bin) %{_prefix}/%{major_version}/COPYING
%attr (0444, root, bin) %{_prefix}/%{major_version}/INSTALL-BINARY
%attr (0444, root, bin) %{_prefix}/%{major_version}/data/test/db.opt
%attr (0444, root, bin) %{_prefix}/%{major_version}/docs/INFO_BIN
%attr (0444, root, bin) %{_prefix}/%{major_version}/docs/INFO_SRC
%attr (0444, root, bin) %{_prefix}/%{major_version}/docs/ChangeLog
%attr (0555, root, bin) %{_prefix}/%{major_version}/scripts/mysql_install_db
%{_prefix}/%{major_version}/support-files/*
%{_prefix}/%{major_version}/man/*
%{_prefix}/%{major_version}/share/*


%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/mysql_56

%dir %attr (0755, root, sys) /var
%dir %attr (0700, mysql, mysql) %{_var_prefix}
%dir %attr (0700, mysql, mysql) %{_var_prefix}/%{major_version}
%dir %attr (0700, mysql, mysql) %{_var_prefix}/%{major_version}/data
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/application
%dir %attr (0755, root, sys) /var/svc/manifest/application/database
%attr (0444, root, sys) /var/svc/manifest/application/database/mysql_56.xml

%dir %attr (0755, root, sys) /etc
%dir %attr (0755, root, bin) /etc/mysql
%dir %attr (0755, root, bin) /etc/mysql/%{major_version}
%attr (0444, root, bin) %config(noreplace) /etc/mysql/%{major_version}/my.cnf
%attr (0444, root, bin) %config(noreplace) /etc/mysql/%{major_version}/my-5.6.cnf.master
# %attr (0444, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /etc/mysql/my.cnf

# /usr/bin
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/innochecksum
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/msql2mysql
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/my_print_defaults
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisam_ftdump
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisamchk
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisamlog
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisampack
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_client_test
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_config
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_config_editor
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_convert_table_format
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_find_rows
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_fix_extensions
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_plugin
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_secure_installation
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_setpermission
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_tzinfo_to_sql
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_upgrade
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_waitpid
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_zap
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlaccess
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlaccess.conf
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqladmin
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlbinlog
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlbug
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlcheck
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqld
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqld_multi
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqld_safe
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqldump
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqldumpslow
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlhotcopy
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlimport
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlshow
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlslap
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqltest
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/perror
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/replace
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/resolve_stack_dump
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/resolveip

%dir %attr (0755, root, bin) /usr/bin/amd64
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/innochecksum
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/msql2mysql
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/my_print_defaults
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/myisam_ftdump
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/myisamchk
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/myisamlog
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/myisampack
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_client_test
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_config
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_config_editor
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_convert_table_format
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_find_rows
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_fix_extensions
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_plugin
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_secure_installation
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_setpermission
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_tzinfo_to_sql
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_upgrade
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_waitpid
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysql_zap
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlaccess
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlaccess.conf
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqladmin
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlbinlog
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlbug
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlcheck
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqld
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqld_multi
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqld_safe
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqldump
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqldumpslow
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlhotcopy
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlimport
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlshow
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqlslap
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/mysqltest
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/perror
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/replace
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/resolve_stack_dump
%attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/amd64/resolveip


%files mysql64
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin/%{_arch64}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin/64
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/%{_arch64}/*


%files library
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/mysql
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/plugin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/64
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/%{_arch64}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/%{_arch64}/mysql
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/%{_arch64}/plugin
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/mysql/*
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/plugin/*
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/%{_arch64}/mysql/*
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/%{_arch64}/plugin/*
%dir %attr (0755, root, bin) /usr/lib
/usr/lib/libstlport.so.1
%dir %attr (0755, root, bin) /usr/lib/amd64
/usr/lib/amd64/libstlport.so.1

# mysql-51/lib is required by some packages
# like apr-util-13/dbd-mysql which is required by apache-22
# and is not mediator ready.
# then can not create symbolic link to /usr/mysql/lib
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) %{_prefix}/lib

%files tests
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/mysql-test
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/sql-bench
%{_prefix}/%{major_version}/mysql-test/*
%{_prefix}/%{major_version}/sql-bench/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/mysql
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/mysql/psi
%attr (0444, root, bin) %{_prefix}/%{major_version}/include/*.h
%attr (0444, root, bin) %{_prefix}/%{major_version}/include/mysql/*.h
%attr (0444, root, bin) %{_prefix}/%{major_version}/include/mysql/*.pp
%attr (0444, root, bin) %{_prefix}/%{major_version}/include/mysql/psi/*.h

%changelog
* Fri Nov 07 JST 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.27
* Thu Sep 17 JST 2015 Osamu Tabata <cantimerny.g@gmail.com>
- add my.cnf sample file
* Fri Aug 07 JST 2015 Osamu Tabata <cantimerny.g@gmail.com>
- change configure option
* Sun Apr 27 JST 2015 Osamu Tabata <cantimerny.g@gmail.com>
- files permission change
* Sun Apr 27 JST 2015 Osamu Tabata <cantimerny.g@gmail.com>
- Q4M patches rename
* Sun Apr 27 JST 2015 Osamu Tabata <cantimerny.g@gmail.com>
- bump to 5.6.24 and add Q4M storage engine
* Tue Dec 02 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.22
* Thu Aug 01 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.20
* Thu Jul 31 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.19
* Mon Mar 31 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.17
* Fri Mar 14 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Tue Feb 04 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.16
* Mon Jan 27 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- divede packages
* Mon Jan 20 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate 32bit and 64bit binary
* Sat Dec 14 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.15
* Thu Sep 26 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add some symbolic links
* Tue Sep 24 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.14
* Sun Sep 08 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate 64 bit binary instead of 32 bit binary
- add %config(noreplace) to /etc/mysql/5.6/my.cnf
* Mon Aug 12 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.13
* Mon Jun 10 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- exclude some symbolic links because mysql-51 is not mediator ready and conflicts
* Thu Jun 06 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.12
* Mon May 27 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- exclude symbolic link to /usr/mysql/lib because mysql-51/library is not mediator ready and conflicts
- modify %attr
* Fri May 10 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.11
- add -DSYSCONFDIR to specify my.cnf directory
- delete %actions to avoid conflict with database/mysql-common
- add Requires
- support mediator
- modify BuildRequires. cmake -> developer/build/cmake
* Mon Apr 15 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- build with gcc by default
* Sat Mar 23 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix source url
* Fri Mar 15 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
