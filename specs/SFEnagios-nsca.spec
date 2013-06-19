#
# spec file for package SFEnagios-nsca
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc

Name:		SFEnagios-nsca
IPS_package_name:        diagnostic/nagios/nsca
Version:	2.7.2
Summary:	NSCA - Nagios Service Check Acceptor
Group:		Applications/System
License:	GPL
URL:		http://www.nagios.org/
Source:		%{sf_download}/nagios/nsca-%{version}.tar.gz
# Source1:	nagios.xml
# Source2:	svc-nagios
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

# BuildRequires:  library/perl-512/clone
Requires:       diagnostic/nagios/common

%description
NSCA is a Linux/Unix daemon allows you to integrate passive alerts and checks from remote machines and applications with Nagios. Useful for processing security alerts, as well as redundant and distributed Nagios setups.

%prep
%setup -q -n nsca-%{version}

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CC=/usr/bin/gcc

./configure \
    --prefix=/usr \
    --bindir=%{_sbindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir}/nagios \
    --with-nsca-user=nagios \
    --with-nsca-grp=nagios

make -j$CPUS all

# tests requires library/perl-512/clone
# cd nsca_tests
# ./runtests 

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/sbin
install -m 00755 src/nsca %{buildroot}/usr/sbin 
install -m 00755 src/send_nsca %{buildroot}/usr/sbin 

mkdir -p %{buildroot}/etc/nagios
touch %{buildroot}/etc/nagios/nsca.cfg

rm sample-config/*.in

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc Changelog  LEGAL README SECURITY sample-config
%dir %attr (0755, root, sys) /usr
%attr (0755, root, bin) /usr/sbin/*
%dir %attr(0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, nagios) %{_sysconfdir}/nagios
%attr (0640, root, nagios) %config(noreplace) %{_sysconfdir}/nagios/nsca.cfg


%changelog
* Wed Jun 19 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
