%include Solaris.inc

%define jetty_version 9.3.18
%define jetty_date 20170406

Name:			SFEjetty
IPS_package_name:	web/server/jetty
Version:		%{jetty_version}
Summary:		Jetty provides a Web server and javax.servlet container
License:		Apache License 2.0
URL:			http://www.eclipse.org/jetty/
# Source:		http://ftp.yz.yamagata-u.ac.jp/pub/eclipse//jetty/stable-9/dist/jetty-distribution-%{jetty_version}.v%{jetty_date}.tar.gz
#Source: 		http://ftp.yz.yamagata-u.ac.jp/pub/eclipse/jetty/%{jetty_version}.v%{jetty_date}/dist/jetty-distribution-%{jetty_version}.v%{jetty_date}.tar.gz
# Source: 		http://ftp.daum.net/eclipse//jetty/stable-9/dist/jetty-distribution-%{jetty_version}.v%{jetty_date}.tar.gz
Source:                 http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/%{jetty_version}.v%{jetty_date}/jetty-distribution-%{jetty_version}.v%{jetty_date}.tar.gz
Source1:		svc-jetty
Source2:		jetty.xml

Requires:		runtime/java/jre-8

%description
Jetty provides a Web server and javax.servlet container, plus support for SPDY, WebSocket, OSGi, JMX, JNDI, JAAS and many other integrations. These components are open source and available for commercial use and distribution.

%package ssl
IPS_package_name: web/server/jetty/module/ssl
Summary:          ssl module for jetty
Requires:	  web/server/jetty = %{version}

%description ssl
ssl module for jetty

%package https
IPS_package_name: web/server/jetty/module/https
Summary:          ssl module for jetty
Requires:	  web/server/jetty = %{version}
Requires:	  web/server/jetty/module/ssl = %{version}

%description https
https module for jetty

%package http2
IPS_package_name: web/server/jetty/module/http2
Summary:          http2 module for jetty
Requires:	  web/server/jetty = %{version}
Requires:	  web/server/jetty/module/ssl = %{version}
Requires:	  web/server/jetty/module/https = %{version}

%description http2
ssl module for jetty

%prep
%setup -q -n jetty-distribution-%{jetty_version}.v%{jetty_date}

%build

%install
rm -rf %{buildroot}

install -d -m 0755 %{buildroot}/usr/jetty
cp -r lib %{buildroot}/usr/jetty
cp -r modules %{buildroot}/usr/jetty
cp -r resources %{buildroot}/usr/jetty
install start.jar %{buildroot}/usr/jetty

install -d -m 0750 %{buildroot}/var/jetty/webapps
install -d -m 0640 %{buildroot}/var/jetty/logs
cp -r etc %{buildroot}/var/jetty
cp -r demo-base/start.d %{buildroot}/var/jetty
install start.ini %{buildroot}/var/jetty
install demo-base/etc/keystore %{buildroot}/var/jetty/etc

pushd %{buildroot}/usr/jetty
ln -s ../../var/jetty/etc .
ln -s ../../var/jetty/webapps .
ln -s ../../var/jetty/logs .
popd

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
%dir %attr(0755, root, bin) /usr/jetty
%attr(0755, root, bin) /usr/jetty/etc
%attr(0755, root, bin) /usr/jetty/start.jar
%attr(0755, root, bin) /usr/jetty/logs
%attr(0755, root, bin) /usr/jetty/modules/.donotdelete
%attr(0755, root, bin) /usr/jetty/webapps
%attr(0755, root, bin) /usr/jetty/lib
%attr(0755, root, bin) /usr/jetty/resources
%dir %attr(0755, root, bin) /usr/jetty/modules
%attr(0755, root, bin) /usr/jetty/modules/alpn-impl
%attr(0755, root, bin) /usr/jetty/modules/alpn.mod
%attr(0755, root, bin) /usr/jetty/modules/annotations.mod
%attr(0755, root, bin) /usr/jetty/modules/apache-jsp.mod
%attr(0755, root, bin) /usr/jetty/modules/apache-jstl.mod
%attr(0755, root, bin) /usr/jetty/modules/cdi.mod
%attr(0755, root, bin) /usr/jetty/modules/client.mod
%attr(0755, root, bin) /usr/jetty/modules/continuation.mod
%attr(0755, root, bin) /usr/jetty/modules/debug.mod
%attr(0755, root, bin) /usr/jetty/modules/debuglog.mod
%attr(0755, root, bin) /usr/jetty/modules/deploy.mod
%attr(0755, root, bin) /usr/jetty/modules/ext.mod
%attr(0755, root, bin) /usr/jetty/modules/fcgi.mod
%attr(0755, root, bin) /usr/jetty/modules/flight-recorder.mod
%attr(0755, root, bin) /usr/jetty/modules/gcloud-memcached-sessions.mod
%attr(0755, root, bin) /usr/jetty/modules/gcloud-session-idmgr.mod
%attr(0755, root, bin) /usr/jetty/modules/gcloud-sessions.mod
%attr(0755, root, bin) /usr/jetty/modules/gzip.mod
%attr(0755, root, bin) /usr/jetty/modules/hawtio.mod
%attr(0755, root, bin) /usr/jetty/modules/home-base-warning.mod
%attr(0755, root, bin) /usr/jetty/modules/http-forwarded.mod
%attr(0755, root, bin) /usr/jetty/modules/http.mod
%attr(0755, root, bin) /usr/jetty/modules/infinispan.mod
%attr(0755, root, bin) /usr/jetty/modules/ipaccess.mod
%attr(0755, root, bin) /usr/jetty/modules/jaas.mod
%attr(0755, root, bin) /usr/jetty/modules/jamon.mod
%attr(0755, root, bin) /usr/jetty/modules/jaspi.mod
%attr(0755, root, bin) /usr/jetty/modules/jdbc-sessions.mod
%attr(0755, root, bin) /usr/jetty/modules/jminix.mod
%attr(0755, root, bin) /usr/jetty/modules/jmx-remote.mod
%attr(0755, root, bin) /usr/jetty/modules/jmx.mod
%attr(0755, root, bin) /usr/jetty/modules/jndi.mod
%attr(0755, root, bin) /usr/jetty/modules/jolokia.mod
%attr(0755, root, bin) /usr/jetty/modules/jsp.mod
%attr(0755, root, bin) /usr/jetty/modules/jstl.mod
%attr(0755, root, bin) /usr/jetty/modules/jvm.mod
%attr(0755, root, bin) /usr/jetty/modules/logging.mod
%attr(0755, root, bin) /usr/jetty/modules/lowresources.mod
%attr(0755, root, bin) /usr/jetty/modules/monitor.mod
%attr(0755, root, bin) /usr/jetty/modules/nosql.mod
%attr(0755, root, bin) /usr/jetty/modules/plus.mod
%attr(0755, root, bin) /usr/jetty/modules/proxy-protocol.mod
%attr(0755, root, bin) /usr/jetty/modules/proxy.mod
%attr(0755, root, bin) /usr/jetty/modules/quickstart.mod
%attr(0755, root, bin) /usr/jetty/modules/requestlog.mod
%attr(0755, root, bin) /usr/jetty/modules/resources.mod
%attr(0755, root, bin) /usr/jetty/modules/rewrite-compactpath.mod
%attr(0755, root, bin) /usr/jetty/modules/rewrite-customizer.mod
%attr(0755, root, bin) /usr/jetty/modules/rewrite.mod
%attr(0755, root, bin) /usr/jetty/modules/security.mod
%attr(0755, root, bin) /usr/jetty/modules/server.mod
%attr(0755, root, bin) /usr/jetty/modules/servlet.mod
%attr(0755, root, bin) /usr/jetty/modules/servlets.mod
%attr(0755, root, bin) /usr/jetty/modules/setuid.mod
%attr(0755, root, bin) /usr/jetty/modules/spring.mod
%attr(0755, root, bin) /usr/jetty/modules/stats.mod
%attr(0755, root, bin) /usr/jetty/modules/threadlimit.mod
%attr(0755, root, bin) /usr/jetty/modules/webapp.mod
%attr(0755, root, bin) /usr/jetty/modules/websocket.mod

%dir %attr(0755, root, bin) /var/jetty
%dir %attr(0755, root, bin) /var/jetty/etc
%attr(0644, root, bin) /var/jetty/etc/README.spnego
%config %attr(0644, root, bin) /var/jetty/etc/example-quickstart.xml
%config %attr(0644, root, bin) /var/jetty/etc/gcloud-memcached-session-context.xml
%config %attr(0644, root, bin) /var/jetty/etc/gcloud-session-context.xml
%config %attr(0644, root, bin) /var/jetty/etc/hawtio.xml
%config %attr(0644, root, bin) /var/jetty/etc/home-base-warning.xml
%config %attr(0644, root, bin) /var/jetty/etc/jamon.xml
%config %attr(0644, root, bin) /var/jetty/etc/jdbcRealm.properties
%config %attr(0644, root, bin) /var/jetty/etc/jetty-alpn.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-annotations.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-cdi.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-debug.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-debuglog.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-deploy.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-gcloud-memcached-sessions.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-gcloud-session-idmgr.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-gcloud-sessions.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-gzip.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-http-forwarded.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-http.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-infinispan.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-ipaccess.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-jaas.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-jdbc-sessions.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-jmx-remote.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-jmx.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-logging.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-lowresources.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-monitor.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-nosql.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-plus.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-proxy-protocol.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-proxy.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-requestlog.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-rewrite-customizer.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-rewrite.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-setuid.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-spring.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-started.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-stats.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-threadlimit.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty.conf
%config %attr(0644, root, bin) /var/jetty/etc/jetty.xml
%config %attr(0644, root, bin) /var/jetty/etc/jminix.xml
%config %attr(0644, root, bin) /var/jetty/etc/jolokia.xml
%config %attr(0644, root, bin) /var/jetty/etc/keystore
%config %attr(0644, root, bin) /var/jetty/etc/krb5.ini
%config %attr(0644, root, bin) /var/jetty/etc/rewrite-compactpath.xml
%config %attr(0644, root, bin) /var/jetty/etc/spnego.conf
%config %attr(0644, root, bin) /var/jetty/etc/spnego.properties
%config %attr(0644, root, bin) /var/jetty/etc/webdefault.xml

%dir %attr(0755, root, bin) /var/jetty/start.d
%config %attr(0644, root, bin) /var/jetty/start.d/http.ini
%config %attr(0644, root, bin) /var/jetty/start.d/jsp.ini
%config %attr(0644, root, bin) /var/jetty/start.d/jstl.ini

%dir %attr(0755, root, bin) /var/jetty/webapps
%dir %attr(0755, webservd, webservd) /var/jetty/logs
%config %attr(0644, root, bin) /var/jetty/start.ini

%files ssl
%dir %attr(0755, root, sys) /usr
%dir %attr(0755, root, bin) /usr/jetty
%dir %attr(0755, root, bin) /usr/jetty/modules
%attr(0755, root, bin) /usr/jetty/modules/proxy-protocol-ssl.mod
%attr(0755, root, bin) /usr/jetty/modules/ssl.mod

%dir %attr(0755, root, bin) /var/jetty
%dir %attr(0755, root, bin) /var/jetty/etc
%config %attr(0644, root, bin) /var/jetty/etc/jetty-proxy-protocol-ssl.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-ssl-context.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-ssl.xml

%dir %attr(0755, root, bin) /var/jetty/start.d
%config %attr(0644, root, bin) /var/jetty/start.d/ssl.ini

%files https
%dir %attr(0755, root, sys) /usr
%dir %attr(0755, root, bin) /usr/jetty
%dir %attr(0755, root, bin) /usr/jetty/modules
%attr(0755, root, bin) /usr/jetty/modules/https.mod

%dir %attr(0755, root, bin) /var/jetty
%dir %attr(0755, root, bin) /var/jetty/etc
%config %attr(0644, root, bin) /var/jetty/etc/jetty-https.xml

%dir %attr(0755, root, bin) /var/jetty/start.d
%config %attr(0644, root, bin) /var/jetty/start.d/https.ini

%files http2
%dir %attr(0755, root, sys) /usr
%dir %attr(0755, root, bin) /usr/jetty
%dir %attr(0755, root, bin) /usr/jetty/modules
%attr(0755, root, bin) /usr/jetty/modules/http2.mod
%attr(0755, root, bin) /usr/jetty/modules/http2c.mod

%dir %attr(0755, root, bin) /var/jetty
%dir %attr(0755, root, bin) /var/jetty/etc
%config %attr(0644, root, bin) /var/jetty/etc/jetty-http2.xml
%config %attr(0644, root, bin) /var/jetty/etc/jetty-http2c.xml

%changelog
* Mon May 15 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update SMF manifest and add keystore
* Fri Apr 06 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.3.18.v20170406
* Thu Jun 23 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.3.10.v20160621
* Tue Feb 02 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- split package
* Sun Jan 17 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.3.6
* Fri Sep 25 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.3.3
* Sat Jun 20 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.3.0
* Wed Sep 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.2.3
* Wed Jul 25 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.2.2
* Wed Jun 11 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.2.1
* Fri Jun 06 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- specify required version of runtime/java/jre
* Wed May 28 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use /var/jetty
* Tue May 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
