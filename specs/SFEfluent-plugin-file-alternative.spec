%include Solaris.inc
%include default-depend.inc

%define gemname fluent-plugin-file-alternative
%define generate_executable 0

%define gemdir23 %(/usr/ruby/2.3/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir23 %{gemdir23}/gems/%{gemname}-%{version}
%define bindir23 /usr/ruby/2.3/bin

Summary:          alternative implementation of out_file, with various configurations
Name:             SFEfluent-plugin-file-alt
IPS_package_name: system/fluentd/plugins/file-alternative
Version:          0.2.2
License:          Apache License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-23
Requires:         runtime/ruby-23
Requires:         system/fluentd >= 0.10.39
Requires:         system/fluentd/plugins/mixin-plaintextformatter

%description
alternative implementation of out_file, with various configurations

%prep
%setup -q -c -T
mkdir -p .%{bindir18}

%build

# ruby-23
/usr/ruby/2.3/bin/gem install --local \
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
- use ruby-23 instead of ruby-21
* Thu Feb 25 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.2
* Tue Mar 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.0
* Mon Jul 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.1.5 and use ruby-21 instead of ruby-19
* Mon Jul 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
