%include Solaris.inc
%include packagenamemacros.inc
%include base.inc
%define cc_is_gcc 0

%define module_name puppetlabs-stdlib
%define module_version 4.3.2

Name:           puppet-modules-stdlib
IPS_package_name:        system/management/puppet3/modules/puppetlabs/stdlib
Version:        %{module_version}
Summary:        Puppet Module Standard Library
Group:		Applications/System
# License:        ASL 2.0
URL:            https://github.com/puppetlabs/puppetlabs-stdlib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: system/management/puppet3
Requires:      system/management/puppet3

%description
Puppet Module Standard Library

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
* Tue Oct 28 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.3.2
* Fri May 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete unnecessary lines
* Thu Sep 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix URL
* Mon Jul 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
