#
# spec file for package libyaml
#
# includes module(s): libyaml
#
%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version 1.0.18
%define tarball_name libmemcached

Name:           SFElibmemcached-1
Summary:        libmemcached
Version:        %{tarball_version}
IPS_package_name:  library/memcached-1
License:        BSD
Source:         https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
Patch1:        SFElibmemcached-htonll.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          %{name}.copyright

%prep
%setup -c -n %{name}-%{version}
pushd %{tarball_name}-%{tarball_version}
%patch1 -p0
popd

%ifarch amd64 sparcv9
rm -rf %{tarball_name}-%{tarball_version}-64
cp -rp %{tarball_name}-%{tarball_version} %{tarball_name}-%{tarball_version}-64
%endif

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

export CC=/usr/bin/gcc
export CXX=/usr/bin/g++
export LD=/usr/gnu/bin/ld
# export MEMCACHED_BINARY=/usr/lib/memcached

cd %{tarball_name}-%{tarball_version}
export CFLAGS="-m32"
export CXXFLAGS="-m32"
export LDFLAGS='-m32 -lsocket'

./configure\
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --libdir=%{_libdir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir}
# --without-memcached

gmake -j$CPUS

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{tarball_version}-64
export CFLAGS="-m64"
export CXXFLAGS="-m64"
export LDFLAGS='-m64 -lsocket'

./configure\
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --bindir=%{_bindir}/%{_arch64} \
 --libdir=%{_libdir}/%{_arch64} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir}
# --without-memcached

gmake -j$CPUS
cd ../
%endif

%install
pwd
cd %{tarball_name}-%{tarball_version}
make install DESTDIR=$RPM_BUILD_ROOT

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{tarball_version}-64
make install DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) %{_prefix}
%dir %attr(0755, root, bin) %{_bindir}
%attr(0755, root, bin) %{_bindir}/*
%dir %attr(0755, root, bin) %{_libdir}
%attr(0755, root, bin) %{_libdir}/libmemcached*
%attr(0755, root, bin) %{_libdir}/libhashkit*
%dir %attr(0755, root, bin) %{_libdir}/%{_arch64}
%attr(0755, root, bin) %{_libdir}/%{_arch64}/libmemcached*
%attr(0755, root, bin) %{_libdir}/%{_arch64}/libhashkit*
%dir %attr(0755, root, other) %{_libdir}/pkgconfig
%attr(0444, root, bin) %{_libdir}/pkgconfig/*
%dir %attr(0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%attr(0444, root, bin) %{_libdir}/%{_arch64}/pkgconfig/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_datadir}/aclocal
%attr(0444, root, bin) %{_datadir}/aclocal/*
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%dir %attr(0444, root, bin) %{_mandir}/man1/*
%dir %attr(0755, root, bin) %{_mandir}/man3
%dir %attr(0444, root, bin) %{_mandir}/man3/*
%dir %attr(0755, root, bin) %{_prefix}/include
%{_prefix}/include/*

%changelog
* Sun Sep 24 2017 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Initial commit
