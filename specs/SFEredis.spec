#
# spec file for package SFEredis
#
# includes module(s): redis
#

%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1

Name:		SFEredis
Version:        2.4.8
Summary:	Redis is an open source, advanced key-value store
IPS_package_name:    service/redis
URL:		http://redis.io
Source:		http://redis.googlecode.com/files/redis-%{version}.tar.gz
Group:		Applications/Archivers
SUNW_Copyright:	SFEredis.copyright
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

#BuildRequires:  SFEtcl.spec

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
%setup -q -c -n %{name}-%{version}

%build
cd redis-%{version}
export CC=gcc
make

%install
cd redis-%{version}
export CC=gcc
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir}
#find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(0755, root, sys)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*

%changelog
* Sun Feb 26 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
