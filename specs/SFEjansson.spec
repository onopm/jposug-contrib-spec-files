%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug
%define tarball_version 2.12
%define tarball_name jansson
%define src_url http://www.digip.org/jansson/releases

Name:             SFEjansson
Summary:          Jansson is a C library for encoding, decoding and manipulating JSON data
Version:          %{tarball_version}
IPS_package_name: jposug/library/jansson
License:          MIT license
Source:           %{src_url}/%{tarball_name}-%{tarball_version}.tar.bz2
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:   %{name}.copyright

Meta(info.upstream_url): http://www.digip.org/jansson/

%prep
%setup -n %{tarball_name}-%{tarball_version}
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
export CFLAGS="-m64"

./configure --prefix=%{_prefix}
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/lib
%dir %attr(0755, root, other) %{_prefix}/lib/pkgconfig
%dir %attr(0755, root, bin) %{_prefix}/include
%{_prefix}/lib/lib*
%{_prefix}/lib/pkgconfig/*
%{_prefix}/include/*

%changelog
* Thu Oct 03 2019 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
