e%include Solaris.inc
%include packagenamemacros.inc

%define tarball_name     mod_limitipconn
%define tarball_version  0.24

Name:                    SFEapache24-limitipconn
IPS_package_name:        web/server/apache-24/module/apache-limitipconn
Summary:                 mod_xsendfile is a small Apache2 module that processes X-SENDFILE headers registered by the original output handler.
Version:                 0.24
License:                 ASL 2.0
Url:                     http://dominia.org/djao/limitipconn2.html
Source:                  http://dominia.org/djao/limit/%{tarball_name}-%{tarball_version}.tar.bz2
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: web/server/apache-24
Requires: web/server/apache-24

%description
Apache module mod_limitipconn.c, which allows web server administrators to limit the number of simultaneous downloads permitted from a single IP address.

%prep
%setup -n %{tarball_name}-%{tarball_version}

%build
/usr/apache2/2.4/bin/apxs -c mod_limitipconn.c

%install
[ -d $$RPM_BUILD_ROOT ] && rm -r $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/apache2/2.4/libexec
cp .libs/mod_limitipconn.so $RPM_BUILD_ROOT/usr/apache2/2.4/libexec/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/apache2
%dir %attr (0755, root, bin) /usr/apache2/2.4
%dir %attr (0755, root, bin) /usr/apache2/2.4/libexec
%attr (0444, root, bin) /usr/apache2/2.4/libexec/mod_limitipconn.so

%changelog
* Sat Mar 28 2020 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
