#
# spec file for package SFEnagios
#
# includes module(s): nagios
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_name    GrowthForecast
%define tarball_version 0.30

Name:		growthforecast
IPS_package_name:        diagnostic/growthforecast
Version:	0.30
Summary:	GrowthForecast - Lightning Fast Graphing/Visualization
Group:		Applications/System
License:	Perl5
URL:		http://kazeburo.github.com/GrowthForecast/
Source:		http://github.com/downloads/kazeburo/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512

%description
GrowthForecast - Lightning Fast Graphing/Visualization

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
# make test


%install
rm -rf $RPM_BUILD_ROOT
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

mkdir -p $RPM_BUILD_ROOT/usr/perl5/5.12
mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/5.12

mkdir -p %{buildroot}%{_localstatedir}/growthforecast

%clean
rm -rf %{buildroot}

%actions
group groupname="growthforecast"
user ftpuser=false gcos-field="GrowthForecast Reserved UID" username="growthforecast" password=NP group="growthforecast"

%files
%defattr(-,root,bin)
%doc README
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(0755,root,bin) %dir %{_bindir}
#%{_bindir}/*
%{_prefix}/perl5/5.12/bin
%{_prefix}/perl5/vendor_perl/5.12
%dir %attr (0755, growthforecast, growthforecast) %{_localstatedir}/growthforecast

%changelog
* Sat Jun 23 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
