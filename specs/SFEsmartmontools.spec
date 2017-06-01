%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc
%define cc_is_gcc 1

%define srcname smartmontools

Name:           SFEsmartmontools
IPS_package_name:        system/smartmontools
Summary:        utility programs to control and monitor storage systems using SMART
Version:        6.5
License:        GPLv2
Url:            http://sourceforge.net/apps/trac/smartmontools/
Source:         %{sf_download}/smartmontools/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
Requires: system/library/gcc/gcc-runtime

%description
The smartmontools package contains two utility programs (smartctl and smartd) to control and monitor storage systems using the Self-Monitoring, Analysis and Reporting Technology System (SMART) built into most modern ATA and SCSI harddisks. In many cases, these utilities will provide advanced warning of disk degradation and failure.

%prep
%setup -q -n %{srcname}-%{version}

%build
CPUS=$(psrinfo | gawk '$2=="on-line"{cpus++}END{print (cpus==0)?1:cpus}')

export CC=/usr/bin/gcc
export CXX=/usr/bin/g++
./configure --prefix=/usr
make -j$CPUS

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
# temporarly delete /etc
rm -rf %{buildroot}/usr/etc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_sbindir}
%{_sbindir}/smartd
%{_sbindir}/update-smart-drivedb
%{_sbindir}/smartctl
%dir %attr (0755, root, other) %{_docdir}
%dir %attr (0755, root, bin) %{_docdir}/smartmontools
%{_docdir}/smartmontools/ChangeLog
%{_docdir}/smartmontools/ChangeLog-5.0-6.0
%dir %attr (0755, root, bin) %{_docdir}/smartmontools/examplescripts
%{_docdir}/smartmontools/examplescripts/Example2
%{_docdir}/smartmontools/examplescripts/Example1
%{_docdir}/smartmontools/examplescripts/Example3
%{_docdir}/smartmontools/examplescripts/Example4
%{_docdir}/smartmontools/examplescripts/Example5
%{_docdir}/smartmontools/examplescripts/Example6
%{_docdir}/smartmontools/examplescripts/README
%{_docdir}/smartmontools/AUTHORS
%{_docdir}/smartmontools/NEWS
%{_docdir}/smartmontools/COPYING
%{_docdir}/smartmontools/smartd.conf
%{_docdir}/smartmontools/TODO
%{_docdir}/smartmontools/INSTALL
%{_docdir}/smartmontools/README
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man4
%{_mandir}/man4/smartd.conf.4
%dir %attr (0755, root, bin) %{_mandir}/man1m
%{_mandir}/man1m/smartd.1m
%{_mandir}/man1m/smartctl.1m
%{_mandir}/man1m/update-smart-drivedb.1m
%dir %attr (0755, root, bin) %{_datadir}/smartmontools
%{_datadir}/smartmontools/drivedb.h

%changelog
* Tue Nov 15 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.5
* Wed Mar 09 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.4
* Fri Dec 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.3
* Sat Feb 09 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- add Requires
