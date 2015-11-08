%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname rspec-its
%define sfe_gemname rspec-its

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

Summary:          RSpec extension gem for attribute matching
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          1.2.0
License:          MIT
URL:              https://github.com/rspec/rspec-its
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
RSpec extension gem for attribute matching

%if %{build19}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19-old
RSpec extension gem for attribute matching

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# rspec-core >= 3.0.0
Requires:         library/ruby/rspec-core-19
# rspec-expectations >= 3.0.0
Requires:         library/ruby/rspec-expectations-19

%description 19
RSpec extension gem for attribute matching
%endif

%if %{build20}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20-old
RSpec extension gem for attribute matching

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# rspec-core >= 3.0.0
Requires:         library/ruby/rspec-core-20
# rspec-expectations >= 3.0.0
Requires:         library/ruby/rspec-expectations-20

%description 20
RSpec extension gem for attribute matching
%endif

%if %{build21}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
RSpec extension gem for attribute matching

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# rspec-core >= 3.0.0
Requires:         library/ruby/rspec-core-21
# rspec-expectations >= 3.0.0
Requires:         library/ruby/rspec-expectations-21

%description 21
RSpec extension gem for attribute matching
%endif

%if %{build22}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
RSpec extension gem for attribute matching

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          RSpec extension gem for attribute matching
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# rspec-core >= 3.0.0
Requires:         library/ruby/rspec-core-22
# rspec-expectations >= 3.0.0
Requires:         library/ruby/rspec-expectations-22

%description 22
RSpec extension gem for attribute matching
%endif

%prep
%setup -q -c -T

%build
build_for() {
    ruby_ver=$1
    bindir="/usr/ruby/${ruby_ver}/bin"
    gemdir="$(${bindir}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    ${bindir}/gem install --local \
        --no-env-shebang \
        --install-dir .${gemdir} \
        --bindir .${bindir} \
        --no-ri \
        --no-rdoc \
        -V \
        --force %{SOURCE0}
}

%if %{build19}
# ruby-19
build_for 1.9
%endif

%if %{build20}
# ruby-20
build_for 2.0
%endif

%if %{build21}
# ruby-21
build_for 2.1
%endif

%if %{build22}
# ruby-22
build_for 2.2
%endif

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

install_for() {
    ruby_ver=$1
    bindir="/usr/ruby/${ruby_ver}/bin"
    gemdir="$(${bindir}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    mkdir -p %{buildroot}/usr/ruby/${ruby_var}
    cp -a ./usr/ruby/${ruby_var}/* \
        %{buildroot}/usr/ruby/${ruby_var}/

%if %{generate_executable}
    mkdir -p %{buildroot}${bindir}
    cp -a .${bindir}/* \
        %{buildroot}${bindir}/
%endif
}

%if %{build19}
# ruby-19
install_for 1.9
%endif

%if %{build20}
install_for 2.0
%endif

%if %{build21}
# ruby-21
install_for 2.1
%endif

%if %{build22}
install_for 2.2
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build19}
%files 19-old
%defattr(0755,root,bin,-)

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9
%endif

%if %{build20}
%files 20-old
%defattr(0755,root,bin,-)

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0
%endif

%if %{build21}
%files 21-old
%defattr(0755,root,bin,-)

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1
%endif

%if %{build22}
%files 22-old
%defattr(0755,root,bin,-)

%files 22
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2
%endif

%changelog
* Fri Jun 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.0
* Sat Dec 13 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
