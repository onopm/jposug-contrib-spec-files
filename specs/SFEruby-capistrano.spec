%include Solaris.inc
%include default-depend.inc

%define gemname capistrano

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary: Capistrano is a utility and framework for executing commands in parallel on multiple remote machines, via SSH.
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-21/capistrano
Version: 2.15.4
License: as is
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-21
Requires:       runtime/ruby-21
Requires:       library/ruby-21/net-ssh
Requires:       library/ruby-21/net-ssh-gateway
Requires:       library/ruby-21/net-scp
Requires:       library/ruby-21/net-sftp
Requires:       library/ruby-21/highline

%description
Capistrano is a utility and framework for executing commands in parallel on multiple remote machines, via SSH.

%package 19
IPS_package_name: library/ruby-19/capistrano
Summary: Capistrano is a utility and framework for executing commands in parallel on multiple remote machines, via SSH.
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires:       library/ruby-19/net-ssh
Requires:       library/ruby-19/net-ssh-gateway
Requires:       library/ruby-19/net-scp
Requires:       library/ruby-19/net-sftp
Requires:       library/ruby-19/highline

%description 19
Capistrano is a utility and framework for executing commands in parallel on multiple remote machines, via SSH.

%package 20
IPS_package_name: library/ruby-20/capistrano
Summary: Capistrano is a utility and framework for executing commands in parallel on multiple remote machines, via SSH.
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
Requires:       library/ruby-20/net-ssh
Requires:       library/ruby-20/net-ssh-gateway
Requires:       library/ruby-20/net-scp
Requires:       library/ruby-20/net-sftp
Requires:       library/ruby-20/highline

%description 20
Capistrano is a utility and framework for executing commands in parallel on multiple remote machines, via SSH.

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
* Mon Jun 23 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for ruby-20 and ruby-21 instead of ruby-18
* Mon May 13 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.15.4
* Tue Apr 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
