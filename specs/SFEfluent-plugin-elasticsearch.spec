%include Solaris.inc

%define gemname fluent-plugin-elasticsearch
%define generate_executable 0

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}


Name:             fluent-plugin-elasticsearch
IPS_package_name: system/fluentd/plugins/elasticsearch
Summary:          fluent plugin for elasticsearch
Version:          1.9.1
License:          MIT License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         system/fluentd >= 0.10.43
Requires:         library/ruby/elasticsearch-21 = *
Requires:         library/ruby/excon-21 = *

%description
fluent plugin for elasticsearch

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
rm -rf .%{gemdir21}/cache

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
* Wed Dec 21 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.1
* Mon Apr 18 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4.0
* Fri Jan 15 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Sun Dec 27 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1
* Sun Nov 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.1.0
* Tue Mar 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.0
* Sun Nov 02 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.0 and use ruby-21 instead of ruby-19
* Sun Apr 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.0
* Tue Feb 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not include default-depend.inc
* Mon Feb 03 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
