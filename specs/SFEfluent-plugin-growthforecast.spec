%include Solaris.inc

%define gemname fluent-plugin-growthforecast
%define generate_executable 0

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Name:             fluent-plugin-growthforecast
IPS_package_name: system/fluentd/plugins/growthforecast
Summary:          fluent plugin for growthforecast
Version:          0.2.10
License:          APLv2
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-21
Requires:         runtime/ruby-21
Requires:         system/fluentd
Requires:         system/fluentd/mixin-config-placeholders
Requires:         library/ruby-21/resolve-hostname >= 0.0.4

%description
fluent plugin for growthforecast

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
* Thu Feb 25 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.10
* Sun Nov 02 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.8 and use ruby-21 instead of ruby-19
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.7
* Sat Feb 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not include default-depend.inc
* Fri Jan 31 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
