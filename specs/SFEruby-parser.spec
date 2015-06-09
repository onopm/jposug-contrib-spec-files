%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname parser

%if %{build19}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%endif

%if %{build20}
%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%endif

%if %{build21}
%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}
%endif

%if %{build22}
%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}
%endif

Summary:          A Ruby parser written in pure Ruby.
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.2.2.5
License:          MIT
URL:              https://github.com/whitequark/parser
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
A Ruby parser written in pure Ruby.

%if %{build19}
%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          A Ruby parser written in pure Ruby.
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# ast < 3.0, >= 1.1
Requires:         library/ruby/ast-19

%description 19
A Ruby parser written in pure Ruby.
%endif

%if %{build20}
%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          A Ruby parser written in pure Ruby.
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# ast < 3.0, >= 1.1
Requires:         library/ruby/ast-20

%description 20
A Ruby parser written in pure Ruby.
%endif

%if %{build21}
%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          A Ruby parser written in pure Ruby.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# ast < 3.0, >= 1.1
Requires:         library/ruby/ast-21

%description 21
A Ruby parser written in pure Ruby.
%endif

%if %{build22}
%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          A Ruby parser written in pure Ruby.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# ast < 3.0, >= 1.1
Requires:         library/ruby/ast-22

%description 22
A Ruby parser written in pure Ruby.
%endif

%prep
%setup -q -c -T

%build
%if %{build19}
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build20}
# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build21}
# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build22}
# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

%if %{build19}
# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}%{bindir19}/
%endif
%endif

%if %{build20}
# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
    %{buildroot}%{bindir20}/
%endif
%endif

%if %{build21}
# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
    %{buildroot}%{bindir21}/
%endif
%endif

%if %{build22}
# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

%if %{generate_executable}
mkdir -p %{buildroot}%{bindir22}
cp -a .%{bindir22}/* \
    %{buildroot}%{bindir22}/
%endif
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build19}
%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9
%endif

%if %{build20}
%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0
%endif

%if %{build21}
%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1
%endif

%if %{build22}
%files 22
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2
%endif

%changelog
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
