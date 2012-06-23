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
Source1:        svc-growthforecast
Source2:        growthforecast.xml
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

mkdir -p %{buildroot}%{_localstatedir}/growthforecast/data

mkdir -p $RPM_BUILD_ROOT/lib/svc/method/
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method/svc-growthforecast
chmod +x $RPM_BUILD_ROOT/lib/svc/method/svc-growthforecast
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/site
cp %{SOURCE2} $RPM_BUILD_ROOT/var/svc/manifest/site/growthforecast.xml

%clean
rm -rf %{buildroot}

%actions
group groupname="growthforecast"
user ftpuser=false gcos-field="GrowthForecast Reserved UID" username="growthforecast" password=NP group="growthforecast"

%files
%defattr(-,root,bin)
%doc README
%dir %attr(0755,root,sys) %{_prefix}
%{_prefix}/perl5
%dir %attr(0755,root,sys) %{_datadir}
%dir %attr(0755,root,other) %{_datadir}/doc
%{_mandir}
%dir %attr(0755,root,sys) %{_localstatedir}
%attr(0755,growthforecast,growthforecast) %{_localstatedir}/growthforecast

%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0555, root, bin) /lib/svc/method/svc-growthforecast

%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/site
%class(manifest) %attr (0444, root, sys) /var/svc/manifest/site/growthforecast.xml

%changelog
* Sun Jun 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add SMF manifest and method file
- modify %attr
* Sat Jun 23 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
