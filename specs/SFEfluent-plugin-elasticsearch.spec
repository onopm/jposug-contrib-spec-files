%include Solaris.inc

%define gemname fluent-plugin-elasticsearch
%define generate_executable 0

%define bindir25 /opt/jposug/ruby/2.5/bin
%define gemdir25 %(%{bindir25}/ruby -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir25 %{gemdir25}/gems/%{gemname}-%{version}


Name:             fluent-plugin-elasticsearch
IPS_package_name: system/fluentd/plugins/elasticsearch
Summary:          fluent plugin for elasticsearch
Version:          2.4.1
License:          MIT License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
Requires:         system/fluentd >= 0.14.8
Requires:         library/ruby/elasticsearch-25jposug = *
Requires:         library/ruby/excon-25jposug = *

%description
fluent plugin for elasticsearch

%prep
%setup -q -c -T

%build

# ruby-25jposug
%{bindir25}/gem install --local \
    --install-dir .%{gemdir25} \
    --bindir .%{bindir25} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}
rm -rf .%{gemdir25}/cache

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{gemdir25}
cp -a .%{gemdir25}/* \
    %{buildroot}/%{gemdir25}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir25}
cp -a .%{bindir25}/* \
   %{buildroot}%{bindir25}/
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
%{gemdir25}

%changelog
* Mon Jan 15 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.1 and use ruby-25jposug
* Thu Apr 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.3 and use ruby-23 instead of ruby-21
* Tue Feb 14 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.2
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
