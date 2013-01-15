%include Solaris.inc
%include default-depend.inc

%define gemname jeweler
%define gemdir18 %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define gemdir19 %(ruby19 -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define tarball_name    jeweler
%define tarball_version 1.8.4

Summary: jeweler
Name: SFEruby-jeweler
IPS_package_name:        library/ruby-18/jeweler
Version: 1.8.4
License: MIT
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: runtime/ruby-18
Requires: runtime/ruby-18
Requires: library/ruby-18/bundler
Requires: library/ruby-18/git
Requires: library/ruby-18/rake
Requires: library/ruby-18/rdoc

%description
Simple and opinionated helper for creating Rubygem projects on GitHub

%package 19
IPS_package_name: library/ruby-19/jeweler
Summary: jeweler
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires: library/ruby-19/bundler
Requires: library/ruby-19/git

%prep
%setup -q -c -T

tar xvf %{SOURCE0}
tar zxvf data.tar.gz


# ruby 1.8
mkdir -p .%{gemdir18}
mkdir -p ./usr/ruby/1.8/bin

gem install --local --install-dir .%{gemdir18} \
            --bindir ./usr/ruby/1.8/bin \
            --force %{SOURCE0}

mkdir -p .%{gemdir19}
mkdir -p ./usr/ruby/1.9/bin

gem19 install --local --install-dir .%{gemdir19} \
            --bindir ./usr/ruby/1.9/bin \
            --force %{SOURCE0}

%build

%install
rm -rf %{buildroot}

# 1.8
mkdir -p %{buildroot}%{gemdir18}
mkdir -p %{buildroot}/usr/ruby/1.8/bin
cp -a .%{gemdir18}/* \
        %{buildroot}%{gemdir18}/

rm -rf %{buildroot}%{geminstdir18}/.yardoc/
rm -rf %{buildroot}%{gemdir18}/doc

# 1.9
mkdir -p %{buildroot}%{gemdir19}
mkdir -p %{buildroot}/usr/ruby/1.9/bin
cp -a .%{gemdir19}/* \
        %{buildroot}%{gemdir19}/

rm -rf %{buildroot}%{geminstdir19}/.yardoc/
rm -rf %{buildroot}%{gemdir19}/doc

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Wed Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
