%include Solaris.inc
%include default-depend.inc

%define gemname resolve-hostname
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin
%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin

%define tarball_name    resolve-hostname
%define tarball_version 0.0.4

Summary: %{gemname}
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/resolve-hostname
Version: 0.0.4
License: MIT
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires: runtime/ruby-18

%description
With caching, selector for IPv4/IPv6, and many other features

%package 19
IPS_package_name: library/ruby-19/resolve-hostname
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%description 19
With caching, selector for IPv4/IPv6, and many other features

%package 20
IPS_package_name: library/ruby-20/resolve-hostname
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20

%description 20
With caching, selector for IPv4/IPv6, and many other features

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
#mkdir -p %{buildroot}/%{bindir18}
#cp -a .%{bindir18}/* \
#    %{buildroot}/%{bindir18}


# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/
#mkdir -p %{buildroot}/%{bindir19}
#cp -a .%{bindir19}/* \
#    %{buildroot}/%{bindir19}

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/
#mkdir -p %{buildroot}/%{bindir20}
#cp -a .%{bindir20}/* \
#    %{buildroot}/%{bindir20}

rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
# /usr/ruby/1.8/bin

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
- initial commit
