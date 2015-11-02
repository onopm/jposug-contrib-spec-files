%include Solaris.inc
%include default-depend.inc

%define gemname hiera-json
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin
%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

Summary: Store Hiera data in JSON
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/hiera/json
Version: 0.4.0
License: Apache License 2.0
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18
Requires:	library/ruby-18/json
Requires:	library/ruby-18/hiera

%description
Store Hiera data in JSON

%package 19
IPS_package_name: library/ruby-19/hiera/json
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
# Requires:	library/ruby-19/json
Requires:	library/ruby-19/hiera

%description 19
Store Hiera data in JSON

%prep
%setup -q -c -T
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}

%build
# export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

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

%install
rm -rf %{buildroot}

# ruby-18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Thu Jan 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix path in %define gemdir18 and gemdir19
* Thu Dec 20 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use full path in %define gemdir18 and gemdir19
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
