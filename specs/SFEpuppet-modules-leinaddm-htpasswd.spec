%include Solaris.inc
%include packagenamemacros.inc
%include base.inc
%define cc_is_gcc 0

%define module_name leinaddm-htpasswd
%define module_version 0.0.3

Name:           puppet-modules-htpasswd
IPS_package_name:        system/management/puppet3/modules/leinaddm/htpasswd
Version:        %{module_version}
Summary:        htpasswd module for Puppet
Group:		Applications/System
License:        Apache Version 2.0
URL:            https://github.com/puppetlabs/puppetlabs-stdlib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: system/management/puppet3 = *
Requires:      system/management/puppet3 = *

%description
Puppet module to manage htpasswd and htgroup files

%prep
mkdir %{module_name}-%{module_version}

%setup -T -c -n %{module_name}-%{module_version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/puppet/modules
puppet module install %{module_name} \
    --force \
    --ignore-dependencies \
    --version %{module_version} \
    --target-dir %{buildroot}%{_datadir}/puppet/modules

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin, 0755)
/usr/share/puppet/modules


%changelog
* Fri Mar 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- specify required puppet3 version
* Thu Mar 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
