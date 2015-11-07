%include Solaris.inc
%include default-depend.inc

%define gemname json
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin


Summary: This is a JSON implementation as a Ruby extension in C.
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/json
Version: 1.8.1
License: Ruby License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires: runtime/ruby-18

%description
This is a JSON implementation as a Ruby extension in C.

%package 19
IPS_package_name: library/ruby-19/json
Summary: This is a JSON implementation as a Ruby extension in C.
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%description 19
This is a JSON implementation as a Ruby extension in C.

%package 20
IPS_package_name: library/ruby-20/json
Summary: This is a JSON implementation as a Ruby extension in C.
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20

%description 20
This is a JSON implementation as a Ruby extension in C.

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
* Tue Oct 29 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.8.1
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.8.0
* Fri Oct 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
