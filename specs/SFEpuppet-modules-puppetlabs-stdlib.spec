%include Solaris.inc
%include packagenamemacros.inc
%include base.inc
%define cc_is_gcc 0

%define _bindir /usr/ruby/1.8/bin
%define _sbindir /usr/ruby/1.8/sbin
%define _mandir /usr/ruby/1.8/share/man

%define module_name puppetlabs-stdlib
%define module_version 4.1.0

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%define confdir conf/solaris

Name:           puppet-modules-stdlib
IPS_package_name:        system/management/puppet3/modules/puppetlabs/stdlib
Version:        %{module_version}
Summary:        Puppet Module Standard Library
Group:		Applications/System
# License:        ASL 2.0
URL:            http://www.bolthole.com
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
# cp -r ppbrown-svcprop-%{version}/* %{buildroot}%{_datadir}/puppet/modules/svcprop
puppet module install %{module_name} \
    --force \
    --ignore-dependencies \
    --version %{module_version} \
    --target-dir %{buildroot}%{_datadir}/puppet/modules

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin, 0755)
# %doc README
/usr/share/puppet/modules


%changelog
* Mon Jul 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
