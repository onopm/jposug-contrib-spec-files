%include Solaris.inc

%define gemname fluent-plugin-geoip
%define generate_executable 0

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}


Name:             fluent-plugin-geoip
IPS_package_name: system/fluentd/plugins/geoip
Summary:          Fluentd Output plugin to add information about geographical location of IP addresses with Maxmind GeoIP databases.
Version:          0.5.1
License:          MIT License
License:          Apache-2.0
URL:              https://github.com/y-ken/fluent-plugin-geoip
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-21 = *
BuildRequires:    library/GeoIP/devel
Requires:         runtime/ruby-21 = *
Requires:         system/fluentd >= 0.10.43
Requires:         library/GeoIP
Requires:         library/ruby/excon-21 = *

%description
Fluentd Output plugin to add information about geographical location of IP addresses with Maxmind GeoIP databases.

%prep
%setup -q -c -T

%build

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
   %{buildroot}%{bindir21}/
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1

%changelog
* Fri Jan 15 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
