#
# spec file for package SFEunbound
#
# includes module(s): unbound
#
%include Solaris.inc

Summary:	Validating, recursive, and caching DNS resolver
IPS_Package_Name:	network/dns/unbound
Name:		SFEunbound
Version:	1.7.1
License:	BSD
URL:		http://www.nlnetlabs.nl/unbound/
Source:		http://www.unbound.net/downloads/unbound-%{version}.tar.gz
Source1:	unbound.xml
Group: System Environment/Daemons
BuildRoot:	%{_tmppath}/unbound-%{version}-build
SUNW_Copyright:	unbound.copyright
SUNW_BaseDir:	/
BuildRequires: SUNWflexlex
BuildRequires: library/security/openssl
Requires: library/security/openssl
BuildRequires: SUNWlexpt
Requires: SUNWlexpt
BuildRequires: SFEldns-devel
Requires: SFEldns

%description
Unbound is a validating, recursive, and caching DNS resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

The source code is under a BSD License.

%prep
%setup -q -n unbound-%{version}

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

LDFLAGS="-lsocket -lnsl" \
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--libdir=%{_libdir} \
	--enable-static=no \
	--enable-sha2 \
	--with-solaris-threads \
	--without-pthreads \
	--disable-gost \
	--with-conf-file=%{_sysconfdir}/unbound/unbound.conf \
	--with-pidfile=%{_localstatedir}/run/unbound.pid \
        --disable-ecdsa

make -j$CPUS

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
install -d 0755 %{buildroot}%{_datadir}/doc/unbound
install -m 0644 doc/README %{buildroot}%{_datadir}/doc/unbound
install -m 0644 doc/CREDITS %{buildroot}%{_datadir}/doc/unbound
install -m 0644 doc/LICENSE %{buildroot}%{_datadir}/doc/unbound
install -m 0644 doc/FEATURES %{buildroot}%{_datadir}/doc/unbound
install -d 0700 %{buildroot}%{_sysconfdir}/unbound
install -d 0755 %{buildroot}%/var/svc/manifest/network/dns
install -m 0644 %{SOURCE1} %{buildroot}%/var/svc/manifest/network/dns

# no section 8
install -d 0755 %{buildroot}%{_datadir}/man/man1m
for i in %{buildroot}%{_datadir}/man/man8/*.8
do
  base=`basename $i 8`
  name1m=${base}1m
  mv $i %{buildroot}%{_datadir}/man/man1m/${name1m}
done
rmdir %{buildroot}%{_datadir}/man/man8
for i in %{buildroot}%{_datadir}/man/*/*
do
  sed 's/(8)/(1M)/g' $i | sed '/^\.TH/s/ \"8\" / \"1M\" /g' > $i.new
  mv $i.new $i
done

%clean
rm -rf ${RPM_BUILD_ROOT}

%pre
test -x $BASEDIR/var/lib/postrun/postrun || exit 0
( echo '/usr/sbin/groupadd unbound';
  echo '/usr/sbin/useradd -d %{_sysconfdir}/unbound -s /bin/true -g unbound unbound';
) | $BASEDIR/var/lib/postrun/postrun -i -a

%postun
test -x $BASEDIR/var/lib/postrun/postrun || exit 0
( echo '/usr/sbin/userdel unbound';
  echo '/usr/sbin/groupdel unbound';
) | $BASEDIR/var/lib/postrun/postrun -i -a

%actions
group groupname="unbound"
user ftpuser=false gcos-field="Unbound Reserved UID" username="unbound" password=NP group="unbound"


%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) %{_prefix}
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/unbound
%attr(0644, root, other) %{_datadir}/doc/unbound/*
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr(0700, unbound, unbound) %{_sysconfdir}/unbound
%attr(0644, unbound, unbound) %config(noreplace) %{_sysconfdir}/unbound/unbound.conf
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/network
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/network/dns
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/network/dns/unbound.xml
%{_sbindir}/*
%{_mandir}/*/*
%{_includedir}/*
%{_libdir}/libunbound*
%dir %attr (0755, root, sys) /usr/lib/pkgconfig
%attr (0444, root, bin) /usr/lib/pkgconfig/libunbound.pc

%changelog
* Thu May 10 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.1
* Fri Mar 16 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.0
* Fri Jan 26 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.8
* Thu Oct 12 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.7
* Tue Aug 21 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.5
* Tue Jun 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.3
* Wed Feb 22 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.1
* Fri Dec 16 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.0
* Wed Mar 09 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.8
* Mon Dec 14 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.7
* Thu Oct 15 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.5
* Thu Sep 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.4
* Mon Jun 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.3
* Tue Dec 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.1
* Tue Nov 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.0
* Wed May 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4.22
* Fri Dec 07 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify requires to build Solaris 11.1
* Thu Jun 07 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4.17
- add --disable-ecdsa because ecdsa is enabled by default
* Sun Feb 26 2012 - Satoru MIYAZAKI<s.miyaza@gmail.com>
- bump to 1.4.16
* Mon Dec 19 2011 - Milan Jurik
- bump to 1.4.14
* Fri Sep 16 2011 - Milan Jurik
- bump to 1.4.13
* Mon Jul 25 2011 - N.B.Prashanth
- add SUNW_Copyright
* Thu Jul 14 2011 - Milan Jurik
- bump to 1.4.12
* Thu Jun 30 2011 - Milan Jurik
- bump to 1.4.11
* Wed May 25 2011 - Milan Jurik
- bump to 1.4.10
* Fri Mar 25 2011 - Milan Jurik
- bump to 1.4.9
* Fri Feb 04 2011 - Milan Jurik
- fix deps
* Mon Jan 24 2011 - Milan Jurik
- bump to 1.4.8
* Mon Nov 08 2010 - Milan Jurik
- bump to 1.4.7
- disable GOST because of old OpenSSL
* Sun Aug 08 2010 - Milan Jurik
- update to 1.4.6
* Tue Jun 15 2010 - Milan Jurik
- update to 1.4.5
* Thu Apr 22 2010 - Milan Jurik
- update to 1.4.4
* Thu Apr 08 2010 - Milan Jurik
- added IPS support
* Wed Mar 11 2010 - Milan Jurik
- update to 1.4.3
* Wed Mar 10 2010 - Milan Jurik
- use Solaris native threads
* Tue Mar 09 2010 - Milan Jurik
- update to 1.4.2
* Thu Dec 17 2009 - Milan Jurik
- update to 1.4.1
* Thu Oct 08 2009 - Milan Jurik
- update to 1.3.4
* Sun Aug 16 2009 - Milan Jurik
- fix libdir
* Wed Aug 5 2009 - Milan Jurik
- upgrade to 1.3.3
* Sun Jul 12 2009 - Milan Jurik
- Added SMF manifest, removed init.d script
- Initial version.
