%include Solaris.inc
%include default-depend.inc

%define gemname growthforecast
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin
%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin

%define tarball_name    growthforecast
%define tarball_version 0.0.4

Summary: %{gemname}
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/growthforecast
Version: 0.0.4
License: Apache License, Version 2.0
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires: runtime/ruby-18
Requires:       scripts/library/ruby-18/resolve-hostname

%description
Client library and tool to update values, create/edit/delete graphs of GrowthForecast

%package 19
IPS_package_name: library/ruby-19/growthforecast
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires:       scripts/library/ruby-19/resolve-hostname

%description 19
Client library and tool to update values, create/edit/delete graphs of GrowthForecast

%package 20
IPS_package_name: library/ruby-20/growthforecast
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
Requires:       scripts/library/ruby-20/resolve-hostname

%description 20
Client library and tool to update values, create/edit/delete graphs of GrowthForecast

%prep
%setup -q -c -T
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}
mkdir -p .%{gemdir20}
mkdir -p .%{bindir20}

%build
# ruby-18
/usr/ruby/1.8/bin/gem install --local \
    --install-dir .%{gemdir18} \
    --bindir .%{bindir18} \
    -V \
    --force %{SOURCE0}

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --force %{SOURCE0}

# ruby-20
/usr/ruby/2.0/bin/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/
mkdir -p %{buildroot}/%{bindir18}
cp -a .%{bindir18}/* \
    %{buildroot}/%{bindir18}


# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/
mkdir -p %{buildroot}/%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}/%{bindir19}

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/
mkdir -p %{buildroot}/%{bindir20}
cp -a .%{bindir20}/* \
    %{buildroot}/%{bindir20}

rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
/usr/ruby/1.8/bin

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%changelog
* Mon Sep 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Fri Sep 27 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.4
* Thu Mar 07 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
