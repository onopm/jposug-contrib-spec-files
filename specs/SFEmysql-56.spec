#
# spec file for package SFEmysql-56
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

%define _prefix /usr/mysql
%define _var_prefix /var/mysql
%define tarball_name     mysql
%define tarball_version  5.6.11
%define major_version	 5.6
%define prefix_name      SFEmysql-56
%define _basedir         %{_prefix}/%{major_version}

Name:                    %{prefix_name}
IPS_package_name:        database/mysql-56
Summary:	         MySQL 5.6
Version:                 5.6.11
License:		 GPL v2
Group:		System/Databases
Url:                     http://www.mysql.com/
# Source:                  http://dev.mysql.com/get/Downloads/MySQL-%{major_version}/mysql-%{version}.tar.gz/from/http://cdn.mysql.com/
Source:                  http://cdn.mysql.com/Downloads/MySQL-%{major_version}/mysql-%{version}.tar.gz
Source1:                 mysql_56
Source2:                 mysql_56.xml
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
BuildRequires: cmake
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
    -DWITH_EMBEDDED_SERVER=ON \
    -DWITH_READLINE=ON \
    -DSYSCONFDIR=/etc/mysql

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
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

%files library
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib

%files tests
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%attr (0755, root, bin) %{_prefix}/%{major_version}/mysql-test
%attr (0755, root, bin) %{_prefix}/%{major_version}/sql-bench

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%attr (0755, root, bin) %{_prefix}/%{major_version}/include

%changelog
* Sat Mar 23 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.6.11
- add -DSYSCONFDIR to specify my.cnf directory
- delete %actions to avoid conflict with database/mysql-common
- add Requires
* Mon Apr 15 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- build with gcc by default
* Sat Mar 23 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix source url
* Fri Mar 15 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
