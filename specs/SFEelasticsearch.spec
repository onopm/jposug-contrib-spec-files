%include Solaris.inc
%include packagenamemacros.inc

Name:			SFEelasticsearch
IPS_package_name:       database/elasticsearch
Summary:		distributed restful search and analytics
Version:		2.2.1
Source:                 http://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-%{version}.zip
Source1:		svc-elasticsearch
Source2:		elasticsearch.xml
URL:			https://www.elastic.co
License:		Apache License 2.0

Requires:	runtime/java/jre = *

%prep
%setup -q -n elasticsearch-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/etc/elasticsearch
mkdir -p $RPM_BUILD_ROOT/etc/elasticsearch/scripts
mkdir -p $RPM_BUILD_ROOT/etc/elasticsearch/templates

mkdir -p $RPM_BUILD_ROOT/usr/elasticsearch
mkdir -p $RPM_BUILD_ROOT/usr/elasticsearch/plugins
cp -r bin $RPM_BUILD_ROOT/usr/elasticsearch
cp -r lib $RPM_BUILD_ROOT/usr/elasticsearch

pushd $RPM_BUILD_ROOT/usr/elasticsearch
ln -s ../../etc/elasticsearch config
popd

mkdir -p $RPM_BUILD_ROOT/etc/elasticsearch
cp config/* $RPM_BUILD_ROOT/etc/elasticsearch
mkdir -p $RPM_BUILD_ROOT/var/elasticsearch/data
mkdir -p $RPM_BUILD_ROOT/var/elasticsearch/logs

mkdir -p $RPM_BUILD_ROOT/lib/svc/method
install -m 0555 %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/application
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT/var/svc/manifest/application

%actions
group groupname="elasticsearch"
user username="elasticsearch" group="elasticsearch" password=NP gcos-field="Elasticsearch Reservd UID"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) /etc
%dir %attr(0755, root, bin) /etc/elasticsearch
%dir %attr(0755, root, bin) /etc/elasticsearch/scripts
%dir %attr(0755, root, bin) /etc/elasticsearch/templates
%attr(0755, root, bin) %config(noreplace) /etc/elasticsearch/elasticsearch.yml
%attr(0755, root, bin) %config(noreplace) /etc/elasticsearch/logging.yml
%dir %attr(0755, root, sys) /usr
/usr/elasticsearch
%dir %attr(0755, root, bin) /lib
%dir %attr(0755, root, bin) /lib/svc
%dir %attr(0755, root, bin) /lib/svc/method
%attr(0555, root, bin) /lib/svc/method/svc-elasticsearch
%dir %attr(0755, root, sys) /var
%dir %attr(0755, elasticsearch, elasticsearch) /var/elasticsearch
%dir %attr(0755, elasticsearch, elasticsearch) /var/elasticsearch/data
%dir %attr(0755, elasticsearch, elasticsearch) /var/elasticsearch/logs
%dir %attr(0755, root, sys) /var/svc
%dir %attr(0755, root, sys) /var/svc/manifest
%dir %attr(0755, root, sys) /var/svc/manifest/application
%attr(0755, root, sys) /var/svc/manifest/application/elasticsearch.xml

%changelog
* Wed Mar 16 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.1
* Wed Mar 09 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.0
* Mon Dec 14 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.0
* Mon Sep 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.1
* Tue Jun 02 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.2
* Sun Feb 15 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4.3
* Fri Nov 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.5
* Sat Oct 25 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.4
* Wed Sep 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.2
* Thu Jul 31 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.1
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1
* Tue Apr 22 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add %config(noreplace) to config files
- require any version of runtime/java
* Mon Apr 21 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files
* Sun Apr 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add %action
- initial commit
