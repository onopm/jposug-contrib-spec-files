%include Solaris.inc

%define gemname sigdump
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin

Summary:          Setup signal handler which dumps backtrace of running threads and number of allocated objects per class. 
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby-18/sigdump
Version:          0.2.2
License:          MIT
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18

%description
Setup signal handler which dumps backtrace of running threads and number of allocated objects per class. Require 'sigdump/setup', send SIGCONT, and see /tmp/sigdump-<pid>.log.

%package 19
IPS_package_name: library/ruby-19/sigdump
Summary:          Setup signal handler which dumps backtrace of running threads and number of allocated objects per class. 
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%description 19
extension for mysql2 to add client-side variable binding, by adding method Mysql2::Client#xquery

%package 20
IPS_package_name: library/ruby-20/sigdump
Summary:          Setup signal handler which dumps backtrace of running threads and number of allocated objects per class. 
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20

%description 20
extension for mysql2 to add client-side variable binding, by adding method Mysql2::Client#xquery

%prep
%setup -q -c -T
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}
mkdir -p .%{gemdir20}
mkdir -p .%{bindir20}

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

# mkdir -p %{buildroot}%{bindir18}
# cp -a .%{bindir18}/* \
#     %{buildroot}%{bindir18}/

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

# mkdir -p %{buildroot}%{bindir19}
# cp -a .%{bindir19}/* \
#     %{buildroot}%{bindir19}/

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

# mkdir -p %{buildroot}%{bindir20}
# cp -a .%{bindir20}/* \
#     %{buildroot}%{bindir20}/

rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
# /usr/ruby/1.8

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%changelog
* Sat Feb 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
