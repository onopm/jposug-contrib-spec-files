%include Solaris.inc

%{!?ruby_sitelibdir19: %define ruby19_sitelibdir %(/usr/ruby/1.9/bin/ruby -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')}

%define gemname fluentd
%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define tarball_name    fluentd
%define tarball_version 0.10.33

Name:             SFEfluentd
IPS_package_name: system/fluentd
Summary:          Fluentd is a log collector daemon written in Ruby. 
Version:          0.10.33
License:          Apache License, Version 2.0
URL:              http://fluentd.org/
Source0:          http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Fluentd is a log collector daemon written in Ruby. Fluentd receives logs as JSON streams, buffers them, and sends them to other systems like MySQL, MongoDB, or even other instances of Fluentd.

BuildRequires:	runtime/ruby-19
BuildRequires:	library/ruby-19/jeweler
BuildRequires:	library/ruby-19/rr
BuildRequires:	library/ruby-19/timecop
BuildRequires:	library/text/yaml
Requires:	runtime/ruby-19
Requires:	library/ruby-19/cool.io
Requires:	library/ruby-19/http_parser.rb
Requires:	library/ruby-19/json
Requires:	library/ruby-19/msgpack
Requires:	library/ruby-19/yajl-ruby

%prep
%setup -q -c -T

mkdir -p .%{gemdir19}
/usr/ruby/1.9/bin/gem install --local --install-dir .%{gemdir19} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gemdir19}
cp -a .%{gemdir19}/* \
        %{buildroot}%{gemdir19}/

rm -rf %{buildroot}%{geminstdir19}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
# %dir %{geminstdir18}
%dir %attr(0755, root, sys) /usr
%{gemdir19}

%changelog
* Sat Mar 30 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.33
* Sat Feb 02 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.31
* Wed Dec 12 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.30
* Wed Dec 05 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.29
* Wed Nov 21 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Name and IPS_package_name
* Wed Nov 14 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
