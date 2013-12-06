#
# spec file for package SFEredis
#
# includes module(s): redis
#

%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1

%define tarball_name     redis

Name:		SFEredis
Version:        2.8.2
Summary:	Redis is an open source, advanced key-value store
IPS_package_name:    service/redis-28
URL:		http://redis.io
Source:		http://download.redis.io/releases/redis-%{version}.tar.gz
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
make

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{version}-64
export CC=gcc
export CFLAGS="-m64 $CFLASG"
export LDFLAGS="-m64"
make
%endif

%install
cd %{tarball_name}-%{version}
export CC=gcc
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir}

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{version}-64
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir}/%{_arch64}
%endif

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(0755, root, sys)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/redis-benchmark
%{_bindir}/redis-cli
%{_bindir}/redis-check-dump
%{_bindir}/redis-check-aof
%{_bindir}/redis-server
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/redis-check-aof
%{_bindir}/%{_arch64}/redis-check-dump
%{_bindir}/%{_arch64}/redis-cli
%{_bindir}/%{_arch64}/redis-server
%{_bindir}/%{_arch64}/redis-benchmark

%changelog
* Fri Dec 6 2013 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris11 and Bump up to 2.8.2
* Sun Feb 26 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
