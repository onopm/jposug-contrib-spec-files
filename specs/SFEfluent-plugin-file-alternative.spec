%include Solaris.inc
%include default-depend.inc

%define gemname fluent-plugin-file-alternative
%define generate_executable 0

%define gemdir21 %(/usr/ruby/2.1/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}
%define bindir21 /usr/ruby/2.1/bin

Summary:          alternative implementation of out_file, with various configurations
Name:             SFEfluent-plugin-file-alt
IPS_package_name: system/fluentd/plugins/file-alternative
Version:          0.1.5
License:          Apache License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-21
Requires:         runtime/ruby-21
Requires:         system/fluentd
Requires:         system/fluentd/plugins/mixin-plaintextformatter

%description
alternative implementation of out_file, with various configurations

%prep
%setup -q -c -T
mkdir -p .%{bindir18}

%build

# ruby-21
/usr/ruby/2.1/bin/gem install --local \
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
* Mon Jul 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.1.5 and use ruby-21 instead of ruby-19
* Mon Jul 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
