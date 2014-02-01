%include Solaris.inc

%define gemname fluent-plugin-growthforecast
%define generate_executable 0

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

Name:             fluent-plugin-growthforecast
IPS_package_name: system/fluentd/plugins/growthforecast
Summary:          fluent plugin for growthforecast
Version:          0.2.6
License:          APLv2
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-19
Requires:         runtime/ruby-19
Requires:         system/fluentd
Requires:         system/fluentd/mixin-config-placeholders
Requires:         library/ruby-19/resolve-hostname >= 0.0.4

%description
fluent plugin for growthforecast

%prep
%setup -q -c -T

%build

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
   %{buildroot}%{bindir19}/
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Sat Feb 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not include default-depend.inc
* Fri Jan 31 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
