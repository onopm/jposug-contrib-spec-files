%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug
%define tarball_version 3.0.2
%define tarball_name libressl
%define src_url https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/

Name:             SFElibressl
Summary:          LibreSSL is a version of the TLS/crypto stack forked from OpenSSL in 2014
Version:          %{tarball_version}
IPS_package_name: jposug/library/security/libressl
License:          OpenSSL License
Source:           %{src_url}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:   %{name}.copyright

Meta(info.upstream_url): https://www.libressl.org

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
export CFLAGS="-m64 -lmd"

./configure --prefix=%{_prefix}
make -j$CPUS
gmake check -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/bin
%dir %attr(0755, root, sys) %{_prefix}/etc
%dir %attr(0755, root, sys) %{_prefix}/etc/ssl
%dir %attr(0755, root, bin) %{_prefix}/lib
%dir %attr(0755, root, other) %{_prefix}/lib/pkgconfig
%dir %attr(0755, root, bin) %{_prefix}/include
%dir %attr(0755, root, sys) %{_prefix}/share
%dir %attr(0755, root, bin) %{_prefix}/share/man
%dir %attr(0755, root, bin) %{_prefix}/share/man/man1
%dir %attr(0755, root, bin) %{_prefix}/share/man/man3
%dir %attr(0755, root, bin) %{_prefix}/share/man/man5
%{_prefix}/bin/*
%{_prefix}/etc/ssl/*
%{_prefix}/lib/lib*
%{_prefix}/lib/pkgconfig/*
%{_prefix}/include/*
%{_prefix}/share/man/man1/*
%{_prefix}/share/man/man3/*
%{_prefix}/share/man/man5/*

%changelog
* Thu Oct 31 2019 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.0.2 and add 'make check'
* Thu Oct 03 2019 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
