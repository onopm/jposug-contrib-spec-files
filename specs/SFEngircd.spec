%include Solaris.inc

%define tarball_name ngircd
%define tarball_version 23

Name:                  SFEngircd
IPS_package_name:      service/network/irc/ngircd
Summary:               A lightweight daemon for the Internet Relay Chat (IRC)
Version:               %{tarball_version}
IPS_component_version: 23.0
License:               GPLv2
Source:                http://ngircd.barton.de/pub/ngircd/%{tarball_name}-%{tarball_version}.tar.gz
Source1:               ngircd
Source2:               ngircd.xml
URL:                   http://ngircd.barton.de

%description
ngIRCd is a free open source daemon for the Internet Relay Chat (IRC),
developed under the GNU General Public License (GPL). It's written from
scratch and is not based upon the original IRCd like many others.

Advantages:
 - no problems with servers using changing/non-static IP addresses.
 - small and lean configuration file.
 - free, modern and open source C code.
 - still under active development.

%prep
if [ -d %{tarball_name}-%{tarball_version} ]
then
  rm -rf %{tarball_name}-%{tarball_version}
fi
%setup -q -n %{tarball_name}-%{tarball_version}

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

CFLAGS='-m64'

./configure --prefix=%{_prefix} \
            --mandir=%{_mandir} \
            --libdir=%{_libdir} \
            --sysconfdir=%{_sysconfdir} \
            --with-openssl \
            --without-devpoll

make -j$CPUS

%install

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/lib/svc/method
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/network
install --mode=755 %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method
cp %{SOURCE2} $RPM_BUILD_ROOT/var/svc/manifest/network


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_sbindir}
%{_sbindir}/ngircd
%dir %attr (0755, root, other) %{_docdir}/ngircd
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man5
%dir %attr(0755, root, bin) %{_mandir}/man8
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_docdir}/ngircd/*
%defattr (-, root, sys)
%attr (0755, root, sys) %dir %{_sysconfdir}
%attr (0644, root, sys) %{_sysconfdir}/ngircd.conf
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/ngircd
%dir %attr (0755, root, sys) /var
/var/svc/*

%changelog
* Tue Mar 29 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- fix IPS_package_name
