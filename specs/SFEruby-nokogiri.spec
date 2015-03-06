%include Solaris.inc

%define gemname nokogiri
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

%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}

Summary:	  Nokogiri is an HTML, XML, SAX, and Reader parser.
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby-22/%{gemname}
Version:          1.6.6.2
License:          MIT License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-22
BuildRequires:  library/libxml2
Requires:       runtime/ruby-22
Requires:       library/ruby-22/mini_portile >= 0.6.0
Requires:       library/libxml2

%description
Nokogiri is an HTML, XML, SAX, and Reader parser.

%package 19
IPS_package_name: library/ruby-19/%{gemname}
Summary: Nokogiri is an HTML, XML, SAX, and Reader parser.
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
BuildRequires:  library/libxml2
Requires:       library/ruby-19/mini_portile >= 0.6.0
Requires:       library/libxml2

%description 19
Nokogiri is an HTML, XML, SAX, and Reader parser.

%package 20
IPS_package_name: library/ruby-20/%{gemname}
Summary: Nokogiri is an HTML, XML, SAX, and Reader parser.
BuildRequires:	runtime/ruby-20
BuildRequires:  library/libxml2
Requires:	runtime/ruby-20
Requires:       library/ruby-20/mini_portile
Requires:       library/libxml2

%description 20
Nokogiri is an HTML, XML, SAX, and Reader parser.

%package 21
IPS_package_name: library/ruby-21/%{gemname}
Summary: Nokogiri is an HTML, XML, SAX, and Reader parser.
BuildRequires:	runtime/ruby-21
BuildRequires:  library/libxml2
Requires:	runtime/ruby-21
Requires:       library/ruby-21/mini_portile
Requires:       library/libxml2

%description 21
Nokogiri is an HTML, XML, SAX, and Reader parser.

%prep
%setup -q -c -T

%build
export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes

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

# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
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

# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir22}
cp -a .%{bindir22}/* \
   %{buildroot}%{bindir22}/
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2

%files 19
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
* Sat Mar 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.6.2 and build package for ruby-22
* Tue Jul 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.1
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
