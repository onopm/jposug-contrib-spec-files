%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug
%define tarball_version 1.5.1
%define tarball_name libzip
%define src_url https://libzip.org/download/

Name:             SFElibzip
Summary:          A C library for reading, creating, and modifying zip archives.
Version:          %{tarball_version}
IPS_package_name: jposug/library/libzip
License:          3-clause BSD license
Source:           %{src_url}/%{tarball_name}-%{tarball_version}.tar.xz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:   %{name}.copyright

BuildRequires: jposug/developer/build/cmake

%prep
%setup -n %{tarball_name}-%{version}

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

export CC=cc
export CFLAGS="-m64 -i -xO4 -xspace -xstrconst -Kpic -xregs=no%frameptr -xCC"

mkdir build
cd build
/opt/jposug/bin/cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_SHARED_LIBS=on \
    ..
make -j$CPUS
make test

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf ${RPM_BUILD_ROOT}
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/bin
%dir %attr(0755, root, bin) %{_prefix}/lib
%dir %attr(0755, root, other) %{_prefix}/lib/pkgconfig
%dir %attr(0755, root, bin) %{_prefix}/include
%dir %attr(0755, root, sys) %{_prefix}/share
%dir %attr(0755, root, bin) %{_prefix}/share/man
%{_prefix}/bin/*
%{_prefix}/include/*
%{_prefix}/lib/libzip*
%{_prefix}/lib/pkgconfig/*
%{_prefix}/share/man/*

%changelog
* Mon Feb 25 2019 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
