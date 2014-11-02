%include Solaris.inc

%define gemname yajl-ruby
%define tarball_name    yajl-ruby
%define tarball_version 1.2.1

%define generate_executable 0

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary: Ruby C bindings to the excellent Yajl JSON stream-based parser library.
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-21/yajl-ruby
Version: 1.2.1
License: MIT
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
Source1: SFEruby-yajl-makefile
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ruby C bindings to the excellent Yajl JSON stream-based parser library.

BuildRequires:	runtime/ruby-21
Requires:	runtime/ruby-21

%package 19
IPS_package_name: library/ruby-19/%{gemname}
Summary:	  Ruby C bindings to the excellent Yajl JSON stream-based parser library.
BuildRequires:	  runtime/ruby-19
Requires:	  runtime/ruby-19

%description 19
Ruby C bindings to the excellent Yajl JSON stream-based parser library.

%package 20
IPS_package_name: library/ruby-20/%{gemname}
Summary:	  Ruby C bindings to the excellent Yajl JSON stream-based parser library.
BuildRequires:	  runtime/ruby-20
Requires:	  runtime/ruby-20

%description 20
Ruby C bindings to the excellent Yajl JSON stream-based parser library.


%prep
%setup -q -c -T

%build
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
   %{buildroot}%{bindir19}/
%endif

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
   %{buildroot}%{bindir20}/
%endif

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
   %{buildroot}%{bindir21}/
%endif

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
* Wed Apr 23 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1 and generate package for Ruby 1.9, 2.0 and 2.1
* Wed Apr 23 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete default-depend.inc
* Thu Jan 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.0
* Wed Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
