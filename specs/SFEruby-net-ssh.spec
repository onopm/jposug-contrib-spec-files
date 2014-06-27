%include Solaris.inc
%include default-depend.inc

%define gemname net-ssh

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby-21/net-ssh
Version:          2.9.1
License:          MIT License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:       %{_tmppath}/%{name}-%{version}-build

BuildRequires:   runtime/ruby-21
Requires:        runtime/ruby-21

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%package 19
IPS_package_name: library/ruby-19/net-ssh
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-19
Requires:         runtime/ruby-19

%description 19
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%package 20
IPS_package_name: library/ruby-20/net-ssh
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-20
Requires:         runtime/ruby-20

%description 20
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.


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

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

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
* Thu Feb 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.9.1 and stop to generate package for ruby-18
* Thu Feb 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21
* Thu Feb 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.0
* Wed Jun 12 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-20
* Fri Apr 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.6.7
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
