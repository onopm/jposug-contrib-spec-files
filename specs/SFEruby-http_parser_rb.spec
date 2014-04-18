%include Solaris.inc
%include default-depend.inc

%define gemname http_parser.rb
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary: %{gemname}
Name: SFEruby-http-parser-rb
IPS_package_name:        library/ruby-19/http_parser.rb
Version: 0.5.3
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-19
Requires:       runtime/ruby-19

%description
Ruby bindings to http://github.com/ry/http-parser and http://github.com/a2800276/http-parser.java

%package 20
IPS_package_name: library/ruby-20/http_parser.rb
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20

%description 20
Ruby bindings to http://github.com/ry/http-parser and http://github.com/a2800276/http-parser.java

%package 21
IPS_package_name: library/ruby-21/http_parser.rb
Summary: %{gemname}
BuildRequires:	runtime/ruby-21
Requires:	runtime/ruby-21

%description 21
Ruby bindings to http://github.com/ry/http-parser and http://github.com/a2800276/http-parser.java

%prep
%setup -q -c -T
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}
mkdir -p .%{gemdir20}
mkdir -p .%{bindir20}
mkdir -p .%{gemdir21}
mkdir -p .%{bindir21}

%build
# export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

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

# rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1

%changelog
* Thu Jan 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for ruby-20 and ruby-21 instead of ruby-18
* Thu Jan 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %define gemdir18 and gemdir19
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
