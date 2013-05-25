%include Solaris.inc
%include default-depend.inc

%define gemname sinatra
%define bindir18 /usr/ruby/1.8/bin
%define gemdir18 %(%{bindir18}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

Summary:          Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort.
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby-18/%{gemname}
Version:          1.4.2
License:          MIT License
# URL:              http://rubygems.org/gems/%{gemname}
URL:              http://www.sinatrarb.com/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	  runtime/ruby-18
Requires:         runtime/ruby-18
Requires:         library/ruby-18/rack >= 1.5.2
Requires:         library/ruby-18/rack-protection >= 1.4
Requires:         library/ruby-18/tilt >= 1.3.4

%description
Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort.

%package 19
IPS_package_name: library/ruby-19/%{gemname}
Summary:          Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort.
BuildRequires:	  runtime/ruby-19
Requires:	  runtime/ruby-19
Requires:         library/ruby-19/rack >= 1.5.2
Requires:         library/ruby-19/rack-protection >= 1.4
Requires:         library/ruby-19/tilt >= 1.3.4

%description 19
Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort.

%package 20
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort.
BuildRequires:	  runtime/ruby-20
Requires:	  runtime/ruby-20
Requires:         library/ruby-20/rack >= 1.5.2
Requires:         library/ruby-20/rack-protection >= 1.4
Requires:         library/ruby-20/tilt >= 1.3.4

%description 20
Sinatra is a DSL for quickly creating web applications in Ruby with minimal effort.

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
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

# ruby-20
/usr/ruby/2.0/bin/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
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

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

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
* Sat May 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
