%include Solaris.inc
%include default-depend.inc

%define gemname mocha
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin
%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

Summary: Mocking and stubbing library with JMock/SchMock syntax, which allows mocking and stubbing of methods on real (non-mock) classes.
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/mocha
Version: 0.13.3
License: Ruby
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18
Requires:       library/ruby-18/metaclass

%description
Mocking and stubbing library with JMock/SchMock syntax, which allows mocking and stubbing of methods on real (non-mock) classes.

%package 19
IPS_package_name: library/ruby-19/mocha
Summary: Mocking and stubbing library with JMock/SchMock syntax, which allows mocking and stubbing of methods on real (non-mock) classes.
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires:       library/ruby-19/metaclass

%description 19
Mocking and stubbing library with JMock/SchMock syntax, which allows mocking and stubbing of methods on real (non-mock) classes.

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

# mkdir -p %{buildroot}%{bindir18}
# cp -a .%{bindir18}/* \
#    %{buildroot}%{bindir18}/

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

# mkdir -p %{buildroot}%{bindir19}
# cp -a .%{bindir19}/* \
#    %{buildroot}%{bindir19}/

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

%changelog
* Tue Apr 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
