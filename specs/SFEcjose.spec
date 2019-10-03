%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug
%define tarball_version 0.6.1
%define tarball_name cjose

Name:             SFEcjose
Summary:          C library implementing the Javascript Object Signing and Encryption (JOSE)
Version:          %{tarball_version}
IPS_package_name: jposug/library/cjose
License:          MIT license
Source:           %{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:   %{name}.copyright

Meta(info.upstream_url): https://github.com/cisco/cjose

BuildREquires: jposug/library/security/libressl
BuildREquires: jposug/library/jansson
BuildRequires: developer/documentation-tool/doxygen
REquires:      jposug/library/security/libressl
REquires:      jposug/library/jansson

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


export PKG_CONFIG_PATH=/opt/jposug/lib/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig
export CC=/usr/bin/gcc
export CFLAGS='-m64 -I/opt/jposug/include -I/opt/jposug/include/openssl'
export LD_FLAGS='-L/opt/jposug/lib -R/opt/jposug/lib'

./configure \
  --prefix=%{_prefix} \
  --with-jansson=/opt/jposug \
  --with-openssl=/opt/jposug
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
%dir %attr(0755, root, sys) %{_prefix}/share
%dir %attr(0755, root, other) %{_prefix}/share/doc
%dir %attr(0755, root, bin) %{_prefix}/share/doc/cjose
%dir %attr(0755, root, bin) %{_prefix}/share/doc/cjose/html
%{_prefix}/lib/libcjose*
%{_prefix}/lib/pkgconfig/cjose.pc
%{_prefix}/include/*
%{_prefix}/share/doc/cjose/html/*

%changelog
* Thu Oct 03 2019 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- build documents
