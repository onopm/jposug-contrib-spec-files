%include Solaris.inc

Name:			SFEGeoIP
IPS_Package_Name:	library/GeoIP
Summary:		Library for country/city/organization to IP address or hostname mapping
Version:		1.6.9
IPS_component_version:	%{version}
License: 		LGPLv2+
URL:			http://www.maxmind.com/app/c
Source0:		https://github.com/maxmind/geoip-api-c/releases/download/v%{version}/GeoIP-%{version}.tar.gz

BuildRequires:	developer/gcc
# BuildRequires:	sed
BuildRequires:	library/zlib

%description
GeoIP is a C library that enables the user to find the country that any IP
address or hostname originates from.

It uses file based databases that can optionally be updated on a weekly basis
by installing the geoipupdate-cron (IPv4) and/or geoipupdate-cron6 (IPv6)
packages.



%package devel
IPS_package_name:	library/GeoIP/devel
Summary:		Development headers and libraries for GeoIP
Group:			Development/Libraries
Requires:		library/GeoIP = %{version}

%prep
%setup -n GeoIP-%{version}

%build
export CC=/usr/bin/gcc
export CFLAGS='-m64'

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

%configure \
    --prefix=/usr \
    --libdir=/usr/lib/%{_arch64} \
    --disable-static \
    --disable-dependency-tracking

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%doc AUTHORS ChangeLog NEWS.md README.md
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/geoiplookup
%{_bindir}/geoiplookup6
%dir %attr (0755, root, bin) /usr/lib
%dir %attr (0755, root, bin) /usr/lib/%{_arch64}
/usr/lib/%{_arch64}/libGeoIP.la
/usr/lib/%{_arch64}/libGeoIP.so.1
/usr/lib/%{_arch64}/libGeoIP.so.1.*
%dir %attr (0755, root, sys) %{_datadir}
%{_mandir}/man1/geoiplookup.1*
%{_mandir}/man1/geoiplookup6.1*

%files devel
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/GeoIP.h
%{_includedir}/GeoIPCity.h
%dir %attr (0755, root, bin) /usr/lib
%dir %attr (0755, root, bin) /usr/lib/%{_arch64}
/usr/lib/%{_arch64}/libGeoIP.so
%dir %attr (0755, root, other) /usr/lib/%{_arch64}/pkgconfig
/usr/lib/%{_arch64}/pkgconfig/geoip.pc

%changelog
* Wed Mar 08 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use %{_arch64} instead of amd64
* Fri Jan 15 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
