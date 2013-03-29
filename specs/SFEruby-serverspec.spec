%include Solaris.inc
%include default-depend.inc

%define gemname serverspec
%define bindir18 /usr/ruby/1.8/bin
%define gemdir18 %(%{bindir18}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

Summary: RSpec tests for your provisioned servers
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/serverspec
Version: 0.0.17
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  runtime/ruby-18
Requires:       runtime/ruby-18
Requires:       library/ruby-18/net-ssh

%description
RSpec tests for your provisioned servers

%package 19
IPS_package_name: library/ruby-19/serverspec
Summary: RSpec tests for your provisioned servers
BuildRequires:  runtime/ruby-19
Requires:       runtime/ruby-19
Requires:       library/ruby-19/net-ssh

%description 19
RSpec tests for your provisioned servers

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

mkdir -p %{buildroot}/%{_bindir}
pushd %{buildroot}/%{_bindir}
ln -s ../../var/ruby1.8/gem_home/gems/%{gemname}-%{version}/bin/serverspec-init serverspec-init18
popd

mkdir -p %{buildroot}/%{bindir18}
pushd %{buildroot}/%{bindir18}
ln -s ../../../../var/ruby1.8/gem_home/gems/%{gemname}-%{version}/bin/serverspec-init .
popd

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

pushd %{buildroot}/%{_bindir}
ln -s ../ruby/1.9/lib/ruby/gems/1.9.1/gems/%{gemname}-%{version}/bin/serverspec-init serverspec-init19
popd

mkdir -p %{buildroot}/%{bindir19}
pushd %{buildroot}/%{bindir19}
ln -s ../lib/ruby/gems/1.9.1/gems/%{gemname}-%{version}/bin/serverspec-init .
popd

rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
/usr/bin/serverspec-init18
/usr/ruby/1.8/bin/serverspec-init

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/bin/serverspec-init19
/usr/ruby/1.9

%changelog
* Sat Mar 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.17
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
