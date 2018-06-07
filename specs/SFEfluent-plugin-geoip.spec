%include Solaris.inc

%define gemname fluent-plugin-geoip
%define generate_executable 0

%define bindir23 /opt/jposug/ruby/2.3/bin
%define gemdir23 %(%{bindir23}/ruby -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir23 %{gemdir23}/gems/%{gemname}-%{version}

Name:             fluent-plugin-geoip
IPS_package_name: system/fluentd/plugins/geoip
Summary:          Fluentd Output plugin to add information about geographical location of IP addresses with Maxmind GeoIP databases.
Version:          0.7.0
License:          Apache-2.0
URL:              https://github.com/y-ken/fluent-plugin-geoip
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:    runtime/ruby-23jposug = *
BuildRequires:    library/GeoIP/devel
Requires:         runtime/ruby-23jposug = *
Requires:         system/fluentd >= 0.10.43
Requires:         system/fluent/mixin-rewrite-tag-name
Requires:         library/ruby/geoip-c-23jposug = *
Requires:         library/ruby/dig_rb-23jposug = *

%description
Fluentd Output plugin to add information about geographical location of IP addresses with Maxmind GeoIP databases.

%prep
%setup -q -c -T

%build

# ruby-23jposug
%{bindir23}/gem install --local \
    --install-dir .%{gemdir23} \
    --bindir .%{bindir23} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{gemdir23}
cp -a .%{gemdir23}/* \
    %{buildroot}/%{gemdir23}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir23}
cp -a .%{bindir23}/* \
   %{buildroot}%{bindir23}/
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
/opt/jposug/ruby

%changelog
* Fri May 11 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use ruby-23jposug instead of ruby-23
* Thu Apr 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.0 and use ruby-23 instead of ruby-21
* Sat Jan 16 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix Requires
* Fri Jan 15 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
