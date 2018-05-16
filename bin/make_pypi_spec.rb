#!/usr/bin/ruby
# -*- coding: utf-8 -*-
=begin
make_pypi_spec.rb

pypi の API を使って Python 用の spec file を生成する。

usage: make_pypi_spec.rb python_package

=end

require 'open-uri'
require 'json'
require 'erb'
require 'pp'

def usage()
  puts "usage: #{File.basename($0)} gemname"
end

unless ARGV.size == 1
  usage
  exit 1
end

package_name = ARGV.shift

specfile = "SFEpython-#{package_name.downcase}.spec"
if File.exist?(specfile)
  STDERR.puts "file alerady exists. #{specfile}"
  exit 1
end

puts "get python package information: #{package_name}"
json = open("https://pypi.python.org/pypi/#{package_name.downcase}/json").read
data = JSON.load(json)['info']

puts "output: #{specfile}"
File.open(specfile, 'w').puts ERB.new(DATA.read, nil, '-').result(binding)

__END__
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define build26 1
%define build27 1
%define build34 0

%define tarball_index <%= data['name'][0] %>
%define tarball_name <%= data['name'] %>
%define tarball_version <%= data['version'] %>

Name:                    SFEpython-<%= data['name'].downcase %>
IPS_package_name:        library/python/<%= data['name'].downcase %>
Summary:                 <%= data['summary'] %>
<% url = data['home_page'].size > 0 ? data['home_page'] : data['package_url'] -%>
URL:                     <%= url %>
Version:                 %{tarball_version}
License:                 <%= data['license'] %>
Source:                  http://pypi.python.org/packages/source/%{tarball_index}/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
<%= data['summary'] %>

%if %{build26}
%package 26
IPS_package_name: library/python/<%= data['name'].downcase %>-26
Summary:          <%= data['summary'] %>
BuildRequires:    runtime/python-26
Requires:         runtime/python-26

%description 26
<%= data['summary'] %>
%endif

%if %{build27}
%package 27
IPS_package_name: library/python/<%= data['name'].downcase %>-27
Summary:          <%= data['summary'] %>
BuildRequires:    runtime/python-27
Requires:         runtime/python-27

%description 27
<%= data['summary'] %>
%endif

%if %{build34}
%package 34
IPS_package_name: library/python/<%= data['name'].downcase %>-34
Summary:          <%= data['summary'] %>
BuildRequires:    runtime/python-34
Requires:         runtime/python-34

%description 34
<%= data['summary'] %>
%endif


%prep
%setup -q -n %{tarball_name}-%{tarball_version}
if [ -d $RPM_BUILD_ROOT ]
then
    rm -rf $RPM_BUILD_ROOT
fi

%build
build_for () {
    python_version=$1

    /usr/bin/python${python_version} setup.py build
    /usr/bin/python${python_version} setup.py install \
        --skip-build \
        --root=$RPM_BUILD_ROOT

}

%if %{build26}
build_for 2.6
%endif

%if %{build27}
build_for 2.7
%endif

%if %{build34}
build_for 3.4
%endif

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
# %doc 

%if %{build26}
%files 26
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.6
%{_libdir}/python2.6/site-packages
%endif

%if %{build27}
%files 27
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python2.7
%{_libdir}/python2.7/site-packages
%endif

%if %{build34}
%files 34
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, bin) %{_libdir}/python3.4
%{_libdir}/python3.4/site-packages
%endif

%changelog
* <%= Time.now.strftime('%a %b %d %Y') %> - NAME <MAILADDR>
- initial commit
