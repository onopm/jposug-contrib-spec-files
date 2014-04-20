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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
/etc/elasticsearch
/usr/elasticsearch
/var/elasticsearch
/lib/svc/method
/var/svc/manifest/application

%changelog
* Sun Apr 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
