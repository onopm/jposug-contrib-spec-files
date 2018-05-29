%include Solaris.inc

%define gemname fluent-plugin-datacounter
%define generate_executable 0

%define bindir23 /usr/ruby/2.3/bin
%define gemdir23 %(%{bindir23}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir23 %{gemdir23}/gems/%{gemname}-%{version}

Name:             SFEfluent-plugin-datacounter
IPS_package_name: system/fluentd/plugins/datacounter
Summary:          To count records with string fields by regexps (To count records with numbers, use numeric-counter)
Version:          1.0.0
License:          APLv2
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-23
Requires:         runtime/ruby-23
Requires:         system/fluentd >= 0.14.8

%description
To count records with string fields by regexps (To count records with numbers, use numeric-counter)

%prep
%setup -q -c -T

%build

# ruby-23
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
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.3

%changelog
* Thu Apr 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.0
* Thu Feb 25 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.5
* Sun Nov 02 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use ruby-21 instead of ruby-19
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.3
* Sat Feb 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not include default-depend.inc
* Fri Jan 31 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
