%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug
%define tarball_version 6.9.4
%define tarball_name onig
%define src_url https://github.com/kkos/oniguruma/releases/download/

Name:           SFEoniguruma
Summary:        regular expression library
Version:        %{tarball_version}
IPS_package_name:  jposug/library/oniguruma
License:        BSD license
Source:         %{src_url}/v%{tarball_version}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          %{name}.copyright

%prep
%setup -c -n %{tarball_name}-%{version}

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

export CC=/usr/bin/gcc
export CFLAGS="-m64 "
export PKG_CONFIG_PATH=/opt/jposug/lib/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig

./configure\
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --libdir=%{_libdir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir}

gmake -j$CPUS

%install
cd %{tarball_name}-%{tarball_version}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/bin
%{_prefix}/bin/onig-config
%dir %attr(0755, root, bin) %{_prefix}/lib
%dir %attr(0755, root, other) %{_prefix}/lib/pkgconfig
%dir %attr(0755, root, bin) %{_prefix}/include
%{_prefix}/lib/libonig*
%{_prefix}/lib/pkgconfig/*
%{_prefix}/include/*

%changelog
* Wed Jan 29 2020 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
