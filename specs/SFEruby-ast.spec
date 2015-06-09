%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname ast

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

Summary:          A library for working with Abstract Syntax Trees.
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.0.0
License:          MIT
URL:              https://whitequark.github.io/ast/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
A library for working with Abstract Syntax Trees.

%if %{build19}
%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          A library for working with Abstract Syntax Trees.
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *

%description 19
A library for working with Abstract Syntax Trees.
%endif

%if %{build20}
%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          A library for working with Abstract Syntax Trees.
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *

%description 20
A library for working with Abstract Syntax Trees.
%endif

%if %{build21}
%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          A library for working with Abstract Syntax Trees.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *

%description 21
A library for working with Abstract Syntax Trees.
%endif

%if %{build22}
%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          A library for working with Abstract Syntax Trees.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *

%description 22
A library for working with Abstract Syntax Trees.
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

    mkdir -p %{buildroot}/${gemdir}
    cp -a .${gemdir}/* \
        %{buildroot}/${gemdir}/

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
* Wed Jun 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add function 'build_for' and 'install_for'
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
