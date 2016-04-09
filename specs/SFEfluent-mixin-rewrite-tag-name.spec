%include Solaris.inc

%define gemname fluent-mixin-rewrite-tag-name
%define generate_executable 0

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}


Name:             fluent-mixin-rw-tag-name
IPS_package_name: system/fluentd/mixin-rewrite-tag-name
Summary:          Fluentd mixin plugin to provides placeholder function for rewriting tag
Version:          0.1.0
License:          Apache License, Version 2.0
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         system/fluentd >= 0.10.43

%description
Fluentd mixin plugin to provides placeholder function for rewriting tag for your any plugins as like fluent-plugin-rewrite-tag-filter. It will let you get easy to implement tag placeholder for your own plugins.

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
* Sat Jan 16 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
