%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr/mysql
%define _var_prefix /var/mysql
%define tarball_name     mysql
%define tarball_version  5.6.10
%define major_version	 5.6
%define prefix_name      SFEmysql-56
%define _basedir         %{_prefix}/%{major_version}

Name:                    %{prefix_name}
IPS_package_name:        database/mysql-56
Summary:	         MySQL 5.6
Version:                 5.6.10
License:		 GPL v2
Group:		System/Databases
Url:                     http://www.mysql.com/
# Source:                  http://dev.mysql.com/get/Downloads/MySQL-%{major_version}/mysql-%{version}.tar.gz/from/http://cdn.mysql.com/
Source:                  http://dev.mysql.com/get/Downloads/MySQL-%{major_version}/mysql-%{version}.tar.gz
Source1:                 mysql_56
Source2:                 mysql_56.xml
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: cmake


%description
MySQL

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

cmake .
cmake . -DBUILD_CONFIG=mysql_release \
    -DFEATURE_SET="community" \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}/%{major_version}" \
    -DINSTALL_LIBDIR="lib/mysql" \
    -DMYSQL_DATADIR="/var/mysql" \
    -DMYSQL_UNIX_ADDR="/var/mysql/mysql.sock" \
    -DENABLED_LOCAL_INFILE=ON \
    -DENABLE_DTRACE=ON \
    -DWITH_EMBEDDED_SERVER=ON \
    -DWITH_READLINE=ON


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



%clean
rm -rf $RPM_BUILD_ROOT

%actions
group groupname="mysql"
user ftpuser=false gcos-field="MySQL Reserved UID" username="mysql" password=NP group="mysql"

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
* Fri Mar 15 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
