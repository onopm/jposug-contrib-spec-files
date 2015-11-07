%include Solaris.inc
%include default-depend.inc

%define gemname rdoc
%define gemdir18 %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define gemdir19 %(ruby19 -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define tarball_name    rdoc
%define tarball_version 3.12

Summary: %{gemname}
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/rdoc
Version: 3.12
License: GPL 2
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
Patch1:  SFEruby-rdoc-fix-test-01.patch
Patch2:  SFEruby-rdoc-fix-test-02.patch
Patch3:  SFEruby-rdoc-fix-test-03.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires: runtime/ruby-18
Requires:	library/ruby-18/json
BuildRequires:   runtime/ruby-18
BuildRequires:	library/ruby-18/racc
BuildRequires:	library/ruby-18/minitest
BuildRequires:	library/ruby-18/rake
BuildRequires:	library/ruby-18/json

%description


%package 19
IPS_package_name: library/ruby-19/rdoc
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
# BuildRequires:	library/ruby-19/racc
Requires:	runtime/ruby-19


%prep
%setup -q -c -T

tar xf %{SOURCE0}
tar zxvf data.tar.gz

# ruby 1.8
mkdir -p .%{gemdir18}/%{gemname}-%{version}
tar zxvf data.tar.gz -C .%{gemdir18}/%{gemname}-%{version}


mkdir -p .%{gemdir19}/%{gemname}-%{version}
tar zxvf data.tar.gz -C .%{gemdir19}/%{gemname}-%{version}

%build

# ruby-18
pushd .%{gemdir18}/%{gemname}-%{version}
%patch1 -p0
%patch2 -p0
%patch3 -p0

LANG=ja_JP.UTF-8 LC_ALL=ja_JP.UTF-8 /usr/ruby/1.8/bin/rake

popd

# ruby-19
pushd .%{gemdir19}/%{gemname}-%{version}
LANG=ja_JP.UTF-8 LC_ALL=ja_JP.UTF-8 /usr/ruby/1.9/bin/rake

%install
rm -rf %{buildroot}

# 1.8
mkdir -p %{buildroot}/usr/ruby/1.8/lib/ruby/site_ruby/1.8
cp -a .%{gemdir18}/%{gemname}-%{version}/lib/* \
    %{buildroot}/usr/ruby/1.8/lib/ruby/site_ruby/1.8

mkdir -p %{buildroot}%{bindir18}
cp -a .%{gemdir18}/%{gemname}-%{version}/bin/* \
    %{buildroot}%{bindir18}/

# 1.9
mkdir -p %{buildroot}/usr/ruby/1.9/lib/ruby/site_ruby/1.9.1/
cp -a .%{gemdir19}/%{gemname}-%{version}/lib/* \
    %{buildroot}/usr/ruby/1.9/lib/ruby/site_ruby/1.9.1/

mkdir -p %{buildroot}%{bindir19}
cp -a .%{gemdir19}/%{gemname}-%{version}/bin/* \
    %{buildroot}%{bindir19}/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
# %dir %attr (0755, root, sys) /var
# %attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Thu Jan 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify to pass test
* Wed Jan 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Fri Oct 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- patches to fix hash-order-dependent tests https://github.com/rdoc/rdoc/commit/2d606b3c
