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
%define tarball_version  5.6.13
%define major_version	 5.6
%define prefix_name      SFEmysql-56
%define _basedir         %{_prefix}/%{major_version}

Name:                    %{prefix_name}
IPS_package_name:        database/mysql-56
Summary:	         MySQL 5.6
Version:                 5.6.13
License:		 GPL v2
Group:		System/Databases
Url:                     http://www.mysql.com/
# Source:                  http://dev.mysql.com/get/Downloads/MySQL-%{major_version}/mysql-%{version}.tar.gz/from/http://cdn.mysql.com/
Source:                  http://cdn.mysql.com/Downloads/MySQL-%{major_version}/mysql-%{version}.tar.gz
Source1:                 mysql_56
Source2:                 mysql_56.xml
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
BuildRequires: developer/build/cmake
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif
%include default-depend.inc
Requires:      database/mysql-common

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

%package library
IPS_package_name: database/mysql-56/library
Summary: MySQL library

%package tests
IPS_package_name: database/mysql-56/tests
Summary: MySQL tests

%package devel
IPS_package_name: database/mysql-56/devel
Summary: MySQL devel

%prep
%setup -n %{tarball_name}-%{tarball_version}


%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

%if %{cc_is_gcc}
    export CC=gcc
    export CXX=g++
    export CFLAGS="%optflags -fno-strict-aliasing -Wno-pointer-sign"
%else
    export CFLAGS="%optflags"
%endif

cmake . -DBUILD_CONFIG=mysql_release \
    -DFEATURE_SET="community" \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}/%{major_version}" \
    -DINSTALL_LIBDIR="lib/mysql" \
    -DMYSQL_DATADIR="/var/mysql" \
    -DMYSQL_UNIX_ADDR="/var/mysql/mysql.sock" \
    -DENABLED_LOCAL_INFILE=ON \
    -DENABLE_DTRACE=ON \
    -DWITH_EMBEDDED_SERVER=OFF \
    -DWITH_LIBEDIT=ON \
    -DSYSCONFDIR=/etc/mysql \
    -DCMAKE_C_FLAGS="-O3 -m64 -mt -KPIC" \
    -DCMAKE_CXX_FLAGS="-O3 -m64 -mt -KPIC"

#    -DCMAKE_C_FLAGS="-O3 -m64 -KPIC -g -mt -fsimple=1 -ftrap=%none -nofstore -xbuiltin=%all -xlibmil -xlibmopt -xtarget=generic" \
#    -DCMAKE_CXX_FLAGS="-O3 -m64 -KPIC -library=stlport4 -g0 -mt -fsimple=1 -ftrap=%none -nofstore -xbuiltin=%all -xlibmil -xlibmopt -xtarget=generic -library=stlport4"

gmake -j$CPUS
gmake -j$CPUS test

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/data
mkdir -p $RPM_BUILD_ROOT/lib/svc/method
install -m 0555 %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/application/database
install -m 0444 %{SOURCE2} $RPM_BUILD_ROOT/var/svc/manifest/application/database
mkdir -p $RPM_BUILD_ROOT/etc/mysql/5.6
install support-files/my-default.cnf $RPM_BUILD_ROOT/etc/mysql/5.6/my.cnf

# # make symbolic links for mediator
# cd $RPM_BUILD_ROOT/etc/mysql
# ln -s 5.6/my.cnf .

cd $RPM_BUILD_ROOT/usr/mysql
# mysql-51/lib is required by some packages
# like apr-util-13/dbd-mysql which is required by apache-22
# and is not mediator ready.
# then can not create symbolic link to /usr/mysql/lib 
# ln -s 5.6/lib .

# mkdir -p $RPM_BUILD_ROOT/usr/bin
# cd $RPM_BUILD_ROOT/usr/bin
# ln -s ../mysql/%{major_version}/bin/innochecksum .
# ln -s ../mysql/%{major_version}/bin/msql2mysql .
# ln -s ../mysql/%{major_version}/bin/my_print_defaults .
# ln -s ../mysql/%{major_version}/bin/myisam_ftdump .
# ln -s ../mysql/%{major_version}/bin/myisamchk .
# ln -s ../mysql/%{major_version}/bin/myisamlog .
# ln -s ../mysql/%{major_version}/bin/myisampack .
# ln -s ../mysql/%{major_version}/bin/mysql .
# ln -s ../mysql/%{major_version}/bin/mysql_client_test .
# ln -s ../mysql/%{major_version}/bin/mysql_client_test_embedded .
# ln -s ../mysql/%{major_version}/bin/mysql_config .
# ln -s ../mysql/%{major_version}/bin/mysql_config_editor .
# ln -s ../mysql/%{major_version}/bin/mysql_convert_table_format .
# ln -s ../mysql/%{major_version}/bin/mysql_embedded .
# ln -s ../mysql/%{major_version}/bin/mysql_find_rows .
# ln -s ../mysql/%{major_version}/bin/mysql_fix_extensions .
# ln -s ../mysql/%{major_version}/bin/mysql_plugin .
# ln -s ../mysql/%{major_version}/bin/mysql_secure_installation .
# ln -s ../mysql/%{major_version}/bin/mysql_setpermission .
# ln -s ../mysql/%{major_version}/bin/mysql_tzinfo_to_sql .
# ln -s ../mysql/%{major_version}/bin/mysql_upgrade .
# ln -s ../mysql/%{major_version}/bin/mysql_waitpid .
# ln -s ../mysql/%{major_version}/bin/mysql_zap .
# ln -s ../mysql/%{major_version}/bin/mysqlaccess .
# ln -s ../mysql/%{major_version}/bin/mysqlaccess.conf .
# ln -s ../mysql/%{major_version}/bin/mysqladmin .
# ln -s ../mysql/%{major_version}/bin/mysqlbinlog .
# ln -s ../mysql/%{major_version}/bin/mysqlbug .
# ln -s ../mysql/%{major_version}/bin/mysqlcheck .
# ln -s ../mysql/%{major_version}/bin/mysqld .
# ln -s ../mysql/%{major_version}/bin/mysqld_multi .
# ln -s ../mysql/%{major_version}/bin/mysqld_safe .
# ln -s ../mysql/%{major_version}/bin/mysqldump .
# ln -s ../mysql/%{major_version}/bin/mysqldumpslow .
# ln -s ../mysql/%{major_version}/bin/mysqlhotcopy .
# ln -s ../mysql/%{major_version}/bin/mysqlimport .
# ln -s ../mysql/%{major_version}/bin/mysqlshow .
# ln -s ../mysql/%{major_version}/bin/mysqlslap .
# ln -s ../mysql/%{major_version}/bin/mysqltest .
# ln -s ../mysql/%{major_version}/bin/mysqltest_embedded .
# ln -s ../mysql/%{major_version}/bin/perror .
# ln -s ../mysql/%{major_version}/bin/replace .
# ln -s ../mysql/%{major_version}/bin/resolve_stack_dump .
# ln -s ../mysql/%{major_version}/bin/resolveip .


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/mysql_56

%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%attr (0755, root, bin) %{_prefix}/%{major_version}/README
%attr (0755, root, bin) %{_prefix}/%{major_version}/share
%attr (0755, root, bin) %{_prefix}/%{major_version}/COPYING
%attr (0755, root, bin) %{_prefix}/%{major_version}/docs
%attr (0755, root, bin) %{_prefix}/%{major_version}/support-files
%attr (0755, root, bin) %{_prefix}/%{major_version}/data
%attr (0755, root, bin) %{_prefix}/%{major_version}/man
%attr (0755, root, bin) %{_prefix}/%{major_version}/scripts
%attr (0755, root, bin) %{_prefix}/%{major_version}/INSTALL-BINARY

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
%dir %attr (0755, root, bin) /etc/mysql/5.6
%attr (0755, root, bin) /etc/mysql/5.6/my.cnf
# %attr (0555, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /etc/mysql/my.cnf

# /usr/bin
# %dir %attr (0755, root, bin) /usr/bin
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/innochecksum
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/msql2mysql
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/my_print_defaults
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisam_ftdump
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisamchk
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisamlog
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/myisampack
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_client_test
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_client_test_embedded
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_config
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_config_editor
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_convert_table_format
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_embedded
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_find_rows
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_fix_extensions
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_plugin
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_secure_installation
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_setpermission
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_tzinfo_to_sql
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_upgrade
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_waitpid
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysql_zap
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlaccess
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlaccess.conf
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqladmin
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlbinlog
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlbug
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlcheck
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqld
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqld_multi
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqld_safe
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqldump
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqldumpslow
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlhotcopy
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlimport
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlshow
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqlslap
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqltest
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/mysqltest_embedded
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/perror
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/replace
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/resolve_stack_dump
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) /usr/bin/resolveip

%files library
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib
# mysql-51/lib is required by some packages
# like apr-util-13/dbd-mysql which is required by apache-22
# and is not mediator ready.
# then can not create symbolic link to /usr/mysql/lib 
# %attr (0755, root, bin) %ips_tag (mediator=mysql mediator-version=%{major_version}) %{_prefix}/lib

%files tests
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%attr (0755, root, bin) %{_prefix}/%{major_version}/mysql-test
%attr (0755, root, bin) %{_prefix}/%{major_version}/sql-bench

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%attr (0755, root, bin) %{_prefix}/%{major_version}/include

%changelog
* Sun Sep 08 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate 64 bit binary instead of 32 bit binary
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
