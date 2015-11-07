%include Solaris.inc
%include default-depend.inc

%define gemname timecop
%define gemdir18 %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin
%define gemdir19 %(ruby19 -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

Summary: A gem providing "time travel" and "time freezing" capabilities
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/timecop
Version: 0.5.3
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18

%description
A gem providing "time travel" and "time freezing" capabilities, making it dead simple to test time-dependent code. It provides a unified method to mock Time.now, Date.today, and DateTime.now in a single call.

%package 19
IPS_package_name: library/ruby-19/timecop
Summary: A gem providing "time travel" and "time freezing" capabilities
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%description 19
A gem providing "time travel" and "time freezing" capabilities, making it dead simple to test time-dependent code. It provides a unified method to mock Time.now, Date.today, and DateTime.now in a single call.

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
%dir %attr (0755, root, sys) /usr

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Wed Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
