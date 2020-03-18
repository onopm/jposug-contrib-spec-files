%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug
%define tarball_version 2.1.11
%define tarball_name libevent
%define src_url https://github.com/libevent/libevent/releases/download/release-%{tarball_version}-stable

Name:           SFElibevent
Summary:        libevent - an event notification library
Version:        %{tarball_version}
IPS_package_name:  jposug/library/libevent
License:        3-clause BSD
Source:         %{src_url}/%{tarball_name}-%{tarball_version}-stable.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          %{name}.copyright

%description
The libevent API provides a mechanism to execute a callback function when a specific event occurs on a file descriptor or after a timeout has been reached. Furthermore, libevent also support callbacks due to signals or regular timeouts.

%prep
%setup -q -n %{tarball_name}-%{tarball_version}-stable

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
export CFLAGS="-std=gnu99 -m64 -O2"
# export CPPFLAGS="-std=gnu99 -m64 -O2 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
export LDFLAGS="-L/opt/jposug/lib -L/lib/%{_arch64} -L/usr/lib/%{_arch64} -R/opt/jposug/lib -R/lib/%{_arch64} -R/usr/lib/%{_arch64} -R%{_basedir}/lib/extensions/no-debug-non-zts-%{zts}"
export PKG_CONFIG_PATH=/opt/jposug/lib/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig

./configure\
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --libdir=%{_libdir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir}

gmake -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/bin
%attr(0755, root, bin) %{_prefix}/bin/*
%dir %attr(0755, root, bin) %{_prefix}/lib
%dir %attr(0755, root, other) %{_prefix}/lib/pkgconfig
%dir %attr(0755, root, bin) %{_prefix}/include
%{_prefix}/lib/libevent*
%{_prefix}/lib/pkgconfig/*
%{_prefix}/include/*

%changelog
* Wed Mar 18 2020 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
