%include Solaris.inc

%define jetty_version 9.1.5
%define jetty_date 20140505

Name:			SFEjetty
IPS_package_name:	web/server/jetty
Version:		%{jetty_version}
Summary:		Jetty provides a Web server and javax.servlet container
License:		Apache License 2.0
URL:			http://www.eclipse.org/jetty/
Source:		http://ftp.yz.yamagata-u.ac.jp/pub/eclipse//jetty/stable-9/dist/jetty-distribution-%{jetty_version}.v%{jetty_date}.tar.gz
Source1:		svc-jetty
Source2:		jetty.xml

Requires:		runtime/java/jre

%description
Jetty provides a Web server and javax.servlet container, plus support for SPDY, WebSocket, OSGi, JMX, JNDI, JAAS and many other integrations. These components are open source and available for commercial use and distribution.

%prep
%setup -q -n jetty-distribution-%{jetty_version}.v%{jetty_date}

%build

%install
rm -rf %{buildroot}

install -d -m 0755 %{buildroot}/usr/jetty
install -d -m 0755 %{buildroot}/usr/jetty/webapps
cp -r etc %{buildroot}/usr/jetty
cp -r lib %{buildroot}/usr/jetty
cp -r modules %{buildroot}/usr/jetty
cp -r resources %{buildroot}/usr/jetty
cp -r start.d %{buildroot}/usr/jetty
install start.ini %{buildroot}/usr/jetty
install start.jar %{buildroot}/usr/jetty

install -d %{buildroot}/lib/svc/method
install %{SOURCE1} %{buildroot}/lib/svc/method/svc-jetty

install -d %{buildroot}/var/svc/manifest/network
install %{SOURCE2} %{buildroot}/var/svc/manifest/network/jetty.xml


exit

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, sys)
%dir %attr(0755, root, bin) /lib
%dir %attr(0755, root, bin) /lib/svc
%dir %attr(0755, root, bin) /lib/svc/method
%attr(0555, root, bin) /lib/svc/method/svc-jetty

%dir %attr(0755, root, sys) /var
%dir %attr(0755, root, sys) /var/svc
%dir %attr(0755, root, sys) /var/svc/manifest
%dir %attr(0755, root, sys) /var/svc/manifest/network
%class(manifest) %attr(0644, root, sys) /var/svc/manifest/network/jetty.xml

%dir %attr(0755, root, sys) /usr
%attr(0755, root, bin) /usr/jetty

%changelog
* Tue May 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
