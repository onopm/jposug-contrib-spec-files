#
# spec file for package SFEredis-32
#

%include Solaris.inc
%include default-depend.inc
%include packagenamemacros.inc
%define cc_is_gcc 1

%define _prefix          /usr/redis
%define _var_prefix      /var/redis
%define _etc_prefix      /etc/redis
%define tarball_name     redis
%define major_version	 3.2
%define _basedir         %{_prefix}/%{major_version}

%define runuser         redis
%define runuserid       200
%define runusergroup    redis
%define runusergroupid  200

Name:		SFEredis-32
Version:        3.2.11
Summary:	Redis is an open source, advanced key-value store
IPS_package_name:    service/redis-32
URL:		http://redis.io
Source:		http://download.redis.io/releases/redis-%{version}.tar.gz
Source1:	redis_32
Source2:	redis_32.xml
Source3:	redis-32-auth_attr
Source4:	redis-32-prof_attr
Source5:	redis-32-exec_attr
Source6:        redis-32-user_attr
Source7:        redis-32.conf
Source8:        redis-32_64.conf
# Patch0:         redis-32.patch
Group:		Applications/Archivers
SUNW_Copyright:	SFEredis.copyright
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Redis is an open source, advanced key-value store.
It is often referred to as a data structure server since keys can contain strings, hashes, lists, sets and sorted sets.
You can run atomic operations on these types, like appending to a string incrementing the value in a hash
pushing to a list computing set intersection, union and difference; or getting the member with highest ranking in a sorted set.
In order to achieve its outstanding performance, Redis works with an in-memory dataset.
Depending on your use case, you can persist it either by dumping the dataset to disk every once in a while, or by appending each command to a log.
Redis also supports trivial-to-setup master-slave replication, with very fast non-blocking first synchronization, auto-reconnection on net split and so forth.
Other features include a simple check-and-set mechanism, pub/sub and configuration settings to make Redis behave like a cache.
You can use Redis from most programming languages out there.
Redis is written in ANSI C and works in most POSIX systems like Linux, *BSD, OS X and Solaris without external dependencies.
There is no official support for Windows builds, although you may have some options.

%prep
%setup -c -n %{tarball_name}-%{version}
# pushd %{tarball_name}-%{version}
# %patch0 -p1
# popd

%ifarch amd64 sparcv9
rm -rf %{tarball_name}-%{version}-64
cp -rp %{tarball_name}-%{version} %{tarball_name}-%{version}-64
%endif

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

cd %{tarball_name}-%{version}
export CC=gcc
make PREFIX=%{_prefix}/%{major_version} -j$CPUS

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{version}-64
export CC=gcc
export CFLAGS="-m64 $CFLASG"
export LDFLAGS="-m64"
make PREFIX=%{_prefix}/%{major_version} -j$CPUS
%endif

%install
cd %{tarball_name}-%{version}
export CC=gcc
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_BIN=$RPM_BUILD_ROOT%{_prefix}/%{major_version}/bin
install -m 0755 src/redis-trib.rb $RPM_BUILD_ROOT%{_prefix}/%{major_version}/bin/

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{version}-64
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_BIN=$RPM_BUILD_ROOT%{_prefix}/%{major_version}/bin/%{_arch64}
install -m 0755 src/redis-trib.rb $RPM_BUILD_ROOT%{_prefix}/%{major_version}/bin/%{_arch64}/
%endif


mkdir -p $RPM_BUILD_ROOT/etc/security
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/data
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/data_64
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/log

mkdir -p $RPM_BUILD_ROOT/lib/svc/method/
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method/redis_32
chmod +x $RPM_BUILD_ROOT/lib/svc/method/redis_32
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/application/database/
cp %{SOURCE2} $RPM_BUILD_ROOT/var/svc/manifest/application/database/redis_32.xml


# attribute
mkdir -p $RPM_BUILD_ROOT/etc/security/auth_attr.d/
cp %{SOURCE3} $RPM_BUILD_ROOT/etc/security/auth_attr.d/redis-32
mkdir -p $RPM_BUILD_ROOT/etc/security/exec_attr.d/
cp %{SOURCE4} $RPM_BUILD_ROOT/etc/security/exec_attr.d/redis-32
mkdir -p $RPM_BUILD_ROOT/etc/security/prof_attr.d/
cp %{SOURCE5} $RPM_BUILD_ROOT/etc/security/prof_attr.d/redis-32
mkdir -p $RPM_BUILD_ROOT/etc/user_attr.d/
cp %{SOURCE6} $RPM_BUILD_ROOT/etc/user_attr.d/redis-32

# etc conf
mkdir -p $RPM_BUILD_ROOT%{_etc_prefix}/%{major_version}/
cp %{SOURCE7} $RPM_BUILD_ROOT%{_etc_prefix}/%{major_version}/
cp %{SOURCE8} $RPM_BUILD_ROOT%{_etc_prefix}/%{major_version}/

mkdir -p $RPM_BUILD_ROOT/usr/bin/
cd $RPM_BUILD_ROOT/usr/bin/
ln -fs ../redis/%{major_version}/bin/redis-benchmark
ln -fs ../redis/%{major_version}/bin/redis-check-rdb
ln -fs ../redis/%{major_version}/bin/redis-cli
ln -fs ../redis/%{major_version}/bin/redis-check-aof
ln -fs ../redis/%{major_version}/bin/redis-server
ln -fs ../redis/%{major_version}/bin/redis-trib.rb
ln -fs ../redis/%{major_version}/bin/redis-sentinel

mkdir -p $RPM_BUILD_ROOT/usr/bin/%{_arch64}
cd $RPM_BUILD_ROOT/usr/bin/%{_arch64}
ln -fs ../../redis/%{major_version}/bin/%{_arch64}/redis-benchmark
ln -fs ../../redis/%{major_version}/bin/%{_arch64}/redis-check-rdb
ln -fs ../../redis/%{major_version}/bin/%{_arch64}/redis-cli
ln -fs ../../redis/%{major_version}/bin/%{_arch64}/redis-check-aof
ln -fs ../../redis/%{major_version}/bin/%{_arch64}/redis-server
ln -fs ../../redis/%{major_version}/bin/%{_arch64}/redis-trib.rb
ln -fs ../../redis/%{major_version}/bin/%{_arch64}/redis-sentinel

%clean
rm -rf ${RPM_BUILD_ROOT}


%actions
group groupname="%{runusergroup}" gid="%{runusergroupid}"
user ftpuser=false gcos-field="redis Reserved UID" username="%{runuser}" uid="%{runuserid}" password=NP group="%{runusergroup}" home-dir="%{_var_prefix}" login-shell="/bin/false" group-list="redis"


%files
%defattr(0755, root, sys)
%defattr(-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin/%{_arch64}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin/%{_arch64}


%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/redis-benchmark
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/redis-check-rdb
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/redis-cli
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/redis-check-aof
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/redis-server
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/redis-trib.rb
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/redis-sentinel
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/%{_arch64}/redis-benchmark
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/%{_arch64}/redis-check-rdb
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/%{_arch64}/redis-cli
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/%{_arch64}/redis-check-aof
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/%{_arch64}/redis-server
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/%{_arch64}/redis-trib.rb
%attr (0555, root, bin) %ips_tag (mediator=redis mediator-version=%{major_version}) /usr/bin/%{_arch64}/redis-sentinel


%attr (0555, root, bin) /usr/redis/%{major_version}/bin/redis-benchmark
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/redis-check-rdb
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/redis-cli
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/redis-check-aof
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/redis-server
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/redis-trib.rb
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/redis-sentinel
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/%{_arch64}/redis-benchmark
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/%{_arch64}/redis-check-rdb
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/%{_arch64}/redis-cli
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/%{_arch64}/redis-check-aof
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/%{_arch64}/redis-server
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/%{_arch64}/redis-trib.rb
%attr (0555, root, bin) /usr/redis/%{major_version}/bin/%{_arch64}/redis-sentinel

%dir %attr (0755, redis, redis) %{_var_prefix}
%dir %attr (0755, redis, redis) %{_var_prefix}/%{major_version}
%dir %attr (0700, redis, redis) %{_var_prefix}/%{major_version}/data
%dir %attr (0700, redis, redis) %{_var_prefix}/%{major_version}/data_64
%dir %attr (0700, redis, redis) %{_var_prefix}/%{major_version}/log

%dir %attr (0755, root, sys) /etc
%dir %attr (0755, root, sys) /etc/security
%dir %attr (0755, root, sys) /etc/security/auth_attr.d
%dir %attr (0755, root, sys) /etc/security/exec_attr.d
%dir %attr (0755, root, sys) /etc/security/prof_attr.d
%dir %attr (0755, root, sys) /etc/user_attr.d
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/application
%dir %attr (0755, root, sys) /var/svc/manifest/application/database

%attr (0555, root, bin) /lib/svc/method/redis_32
%attr (0644, root, sys) /etc/security/auth_attr.d/redis-32
%attr (0644, root, sys) /etc/security/exec_attr.d/redis-32
%attr (0644, root, sys) /etc/security/prof_attr.d/redis-32
%attr (0644, root, sys) /etc/user_attr.d/redis-32

%dir %attr (0755, root, sys) /etc/redis
%dir %attr (0755, root, sys) /etc/redis/%{major_version}
%dir %attr (0755, root, sys) /etc/redis/%{major_version}/redis-32.conf
%dir %attr (0755, root, sys) /etc/redis/%{major_version}/redis-32_64.conf
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/application/database/redis_32.xml

%changelog
* Sat Nov 03 2017 - Osamu Tabata <cantimerny.g@gmail.com>
- bump up to 3.2.11
* Sun Jan 29 2017 - Osamu Tabata <cantimerny.g@gmail.com>
- initial commit
