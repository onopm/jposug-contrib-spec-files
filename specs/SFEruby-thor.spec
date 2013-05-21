%include Solaris.inc
%include default-depend.inc

%define gemname thor
%define generate_executable 1

%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin

Summary: A scripting framework that replaces rake, sake and rubigen
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/%{gemname}
Version: 0.18.1
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18
Requires:       library/ruby-18/mime-types

%description
A scripting framework that replaces rake, sake and rubigen

%package 19
IPS_package_name: library/ruby-19/%{gemname}
Summary:          A scripting framework that replaces rake, sake and rubigen
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires:       library/ruby-19/mime-types

%description 19
A scripting framework that replaces rake, sake and rubigen

%package 20
IPS_package_name: library/ruby-20/%{gemname}
Summary:          A scripting framework that replaces rake, sake and rubigen
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
Requires:       library/ruby-20/mime-types

%description 20
A scripting framework that replaces rake, sake and rubigen

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
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-20
/usr/ruby/2.0/bin/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# delete spec test.
# because some file names include space and symbols.
# And I do not know how to package them.
rm -rf .%{gemdir18}/gems/thor-%{version}/spec
rm -rf .%{gemdir19}/gems/thor-%{version}/spec
rm -rf .%{gemdir20}/gems/thor-%{version}/spec

# ruby-18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir18}
cp -a .%{bindir18}/* \
   %{buildroot}%{bindir18}/
%endif

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

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /%{gemdir18}
%dir %attr (0755, root, bin) %{bindir18}
%{bindir18}/thor

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%attr (0755, root, bin) /usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%attr (0755, root, bin) /usr/ruby/2.0

%changelog
* Tue May 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
