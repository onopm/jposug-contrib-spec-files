%include Solaris.inc
%include default-depend.inc

%define gemname puppet-lint

%define bindir19 /usr/ruby/1.9/bin
%define sbindir19 /usr/ruby/1.9/sbin
%define mandir19 /usr/ruby/1.9/share/man
%define siteruby19 /usr/ruby/1.9/lib/ruby/site_ruby/1.9.1
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define sbindir20 /usr/ruby/2.0/sbin
%define mandir20 /usr/ruby/2.0/share/man
%define siteruby20 /usr/ruby/2.0/lib/amd64/ruby/site_ruby/2.0.0
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define sbindir21 /usr/ruby/2.1/sbin
%define mandir21 /usr/ruby/2.1/share/man
%define siteruby21 /usr/ruby/2.1/lib/amd64/ruby/site_ruby/2.1.0
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

%define tarball_name    puppet-lint
%define tarball_version 1.1.0

Summary: %{gemname}
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-21/puppet-lint
Version: %{tarball_version}
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-21
Requires: runtime/ruby-21

%description
Checks your Puppet manifests against the Puppetlabs style guide and alerts you to any discrepancies.

%package 20
IPS_package_name: library/ruby-20/puppet-lint
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20

%description 20
Checks your Puppet manifests against the Puppetlabs style guide and alerts you to any discrepancies.

%package 19
IPS_package_name: library/ruby-19/puppet-lint
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%description 19
Checks your Puppet manifests against the Puppetlabs style guide and alerts you to any discrepancies.

%prep
%setup -q -c -T
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}

%build
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --no-env-shebang \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    -V \
    --no-env-shebang \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    -V \
    --no-env-shebang \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}%{bindir19}/

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
    %{buildroot}%{bindir20}/

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
    %{buildroot}%{bindir21}/


%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%changelog
* Wed Nov 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.1.0
* Thu Sep 11 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.1
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for ruby-19, ruby-20 and ruby-21
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
