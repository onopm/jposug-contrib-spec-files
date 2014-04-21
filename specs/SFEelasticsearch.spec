%include Solaris.inc
%include packagenamemacros.inc

Name:			SFEelasticsearch
IPS_package_name:       database/elasticsearch
Summary:		distributed restful search and analytics
Version:		1.1.1
# Source:		https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-%{version}.tar.gz
Source:		http://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.1.tar.gz
Source1:		svc-elasticsearch
Source2:		elasticsearch.xml
URL:			http://www.elasticsearch.org/
License:		Apache License 2.0

Requires:	runtime/java

%prep
%setup -q -n elasticsearch-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/elasticsearch
cp -r bin $RPM_BUILD_ROOT/usr/elasticsearch
cp -r lib $RPM_BUILD_ROOT/usr/elasticsearch

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
* Tue Apr 22 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add %config(noreplace) to config files
* Mon Apr 21 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files
* Sun Apr 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add %action
- initial commit
