%include Solaris.inc
%include default-depend.inc

%define gemname rake
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin

Summary: A pluggable data store for rakercical data
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/rake
Version: 10.0.3
License: MIT-style
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
BuildRequires:	library/ruby-18/minitest
Requires:       runtime/ruby-18

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies arespecified in standard Ruby syntax.

%prep
%setup -q -c -T
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}

%build
# export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

# ruby-18
/usr/ruby/1.8/bin/gem install --local \
    --install-dir .%{gemdir18} \
    --bindir .%{bindir18} \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

mkdir -p %{buildroot}%{bindir18}
cp -a .%{bindir18}/* \
    %{buildroot}%{bindir18}/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8

%changelog
* Wed Jan 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
