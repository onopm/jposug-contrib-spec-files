#!/usr/bin/ruby
# -*- coding: utf-8 -*-
=begin
make_rubygem_spec.rb

rubygem 用の spec file を生成する。

usage: make_rubygem_spec.rb gemname

=end

require 'open-uri'
require 'json'
require 'erb'

API_ENDPOINT = 'https://rubygems.org/api/v1/gems'

def usage()
  puts "usage: #{File.basename($0)} gemname"
end

unless ARGV.size == 1
  usage
  exit 1
end

gemname = ARGV.shift

specfile = "SFEruby-#{gemname}.spec"
if File.exist?(specfile)
  STDERR.puts "file alerady exists. #{specfile}"
  exit 1
end

puts "get gem information: #{gemname}"
json = open("#{API_ENDPOINT}/#{gemname}").read
data = JSON.load(json)

puts "output: #{specfile}"
File.open(specfile, 'w').puts ERB.new(DATA.read, nil, '-').result(binding)

__END__
%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname <%= data['name'] %>

%if %{build19}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%endif

%if %{build20}
%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%endif

%if %{build21}
%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}
%endif

%if %{build22}
%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}
%endif

Summary:          <%= data['info'] %>
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          <%= data['version'] %>
License:          <%= data['licenses'].join(', ') unless data['licenses'].nil? %>
<% url = data['homepage_uri'].length > 0 ? data['homepage_uri'] : data['project_uri'] -%>
URL:              <%= url %>
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
<%= data['info'] %>

%if %{build19}
%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          <%= data['info'] %>
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
<% data['dependencies']['runtime'].each do |req| -%>
# <%= req['name'] %> <%= req['requirements'] %>
Requires:         library/ruby/<%= req['name'] %>-19
<% end -%>

%description 19
<%= data['info'] %>
%endif

%if %{build20}
%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          <%= data['info'] %>
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
<% data['dependencies']['runtime'].each do |req| -%>
# <%= req['name'] %> <%= req['requirements'] %>
Requires:         library/ruby/<%= req['name'] %>-20
<% end -%>

%description 20
<%= data['info'] %>
%endif

%if %{build21}
%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          <%= data['info'] %>
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
<% data['dependencies']['runtime'].each do |req| -%>
# <%= req['name'] %> <%= req['requirements'] %>
Requires:         library/ruby/<%= req['name'] %>-21
<% end -%>

%description 21
<%= data['info'] %>
%endif

%if %{build22}
%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          <%= data['info'] %>
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
<% data['dependencies']['runtime'].each do |req| -%>
# <%= req['name'] %> <%= req['requirements'] %>
Requires:         library/ruby/<%= req['name'] %>-22
<% end -%>

%description 22
<%= data['info'] %>
%endif

%prep
%setup -q -c -T

%build
%if %{build19}
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build20}
# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build21}
# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build22}
# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

%if %{build19}
# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}%{bindir19}/
%endif
%endif

%if %{build20}
# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
    %{buildroot}%{bindir20}/
%endif
%endif

%if %{build21}
# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
    %{buildroot}%{bindir21}/
%endif
%endif

%if %{build22}
# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir22}
cp -a .%{bindir22}/* \
    %{buildroot}%{bindir22}/
%endif
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build19}
%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9
%endif

%if %{build20}
%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0
%endif

%if %{build21}
%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1
%endif

%if %{build22}
%files 22
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2
%endif

%changelog
* <%= Time.now.strftime('%a %b %d %Y') %> - NAME <MAILADDR>
- initial commit
