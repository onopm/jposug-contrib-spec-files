%include Solaris.inc
%include default-depend.inc

%define bindir18 /usr/ruby/1.8/bin
%define gemname hiera-puppet
%define gemdir18 %(%{bindir18}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

Summary: Store and query Hiera data from Puppet
Name: SFEruby-hiera-puppet
IPS_package_name:        library/ruby-18/hiera/puppet
Version: 1.0.0
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18
Requires:       library/ruby-18/hiera

%description
Store and query Hiera data from Puppet

%package 19
IPS_package_name: library/ruby-19/hiera/puppet
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires:	library/ruby-19/hiera

%description 19
Store and query Hiera data from Puppet

%package 20
IPS_package_name: library/ruby-20/hiera/puppet
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
Requires:	library/ruby-20/hiera

%description 20
Store and query Hiera data from Puppet

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

# not install extlookup2hiera because it is provided by puppet3
# mkdir -p %{buildroot}%{bindir18}
# cp -a .%{bindir18}/* \
#    %{buildroot}%{bindir18}/

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

# not install extlookup2hiera because it is provided by puppet3
# mkdir -p %{buildroot}%{bindir19}
# cp -a .%{bindir19}/* \
#    %{buildroot}%{bindir19}/

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/


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

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%changelog
* Wed Jan 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-20
* Sun Dec 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete unnecessary string which causes syntax error
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
