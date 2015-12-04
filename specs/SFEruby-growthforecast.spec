%include Solaris.inc
%include default-depend.inc

%define gemname growthforecast

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}

%define tarball_name    growthforecast
%define tarball_version 0.0.4

Summary: %{gemname}
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-22/growthforecast
Version: 0.0.4
License: Apache License, Version 2.0
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-22
Requires:       runtime/ruby-22
Requires:       library/ruby-22/resolve-hostname

%description
Client library and tool to update values, create/edit/delete graphs of GrowthForecast

%package 19
IPS_package_name: library/ruby-19/growthforecast
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires:       library/ruby-19/resolve-hostname

%description 19
Client library and tool to update values, create/edit/delete graphs of GrowthForecast

%package 20
IPS_package_name: library/ruby-20/growthforecast
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
Requires:       library/ruby-20/resolve-hostname

%description 20
Client library and tool to update values, create/edit/delete graphs of GrowthForecast

%package 21
IPS_package_name: library/ruby-21/growthforecast
Summary: %{gemname}
BuildRequires:	runtime/ruby-21
Requires:	runtime/ruby-21
Requires:       library/ruby-21/resolve-hostname

%description 21
Client library and tool to update values, create/edit/delete graphs of GrowthForecast

%prep
%setup -q -c -T
%build
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    -V \
    --force %{SOURCE0}

# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

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

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/
mkdir -p %{buildroot}/%{bindir21}
cp -a .%{bindir21}/* \
    %{buildroot}/%{bindir21}

# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/
mkdir -p %{buildroot}/%{bindir22}
cp -a .%{bindir22}/* \
    %{buildroot}/%{bindir22}

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1

%changelog
* Fri Jan 30 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21 and ruby-22 instead of ruby-18
* Mon Feb 17 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix BuildRequires
* Mon Sep 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Fri Sep 27 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.4
* Thu Mar 07 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
