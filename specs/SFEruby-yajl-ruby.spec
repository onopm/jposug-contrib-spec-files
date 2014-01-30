%include Solaris.inc
%include default-depend.inc

%define gemname yajl-ruby
%define gemdir19 %(ruby19 -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define tarball_name    yajl-ruby
%define tarball_version 1.2.0

Summary: %{gemname}
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-19/yajl-ruby
Version: 1.2.0
License: MIT
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
Source1: SFEruby-yajl-makefile
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library.

BuildRequires:	runtime/ruby-19
# BuildRequires:	library/ruby-19/rspec
# BuildRequires:	library/ruby-19/rake-compiler
Requires:	runtime/ruby-19

%prep
%setup -q -c -T

%build
# 1.9
mkdir -p .%{gemdir19}
/usr/ruby/1.9/bin/gem install --local --install-dir .%{gemdir19} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

# popd

%install
rm -rf %{buildroot}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Thu Jan 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.0
* Wed Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
