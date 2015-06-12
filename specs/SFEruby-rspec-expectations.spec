%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname rspec-expectations
%define sfe_gemname rspec-expectations

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

Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
Name:             ruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          3.2.1
License:          MIT
URL:              http://github.com/rspec/rspec-expectations
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build


%description
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.

%if %{build19}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19-old
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         library/ruby/diff-lcs-19
# rspec-support ~> 3.2.0
Requires:         library/ruby/rspec-support-19 >= 3.2.2

%description 19
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%if %{build20}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20-old
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         library/ruby/diff-lcs-20
# rspec-support ~> 3.2.0
Requires:         library/ruby/rspec-support-20 >= 3.2.2

%description 20
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%if %{build21}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         library/ruby/diff-lcs-21
# rspec-support ~> 3.2.0
Requires:         library/ruby/rspec-support-21 >= 3.2.2

%description 21
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%if %{build22}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         library/ruby/diff-lcs-22
# rspec-support ~> 3.2.0
Requires:         library/ruby/rspec-support-22 >= 3.2.2

%description 22
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
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
- bump to 3.2.1
* Mon Oct 06 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.1.2
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.99.1 and stop to generate package for ruby-18
* Wed Feb 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.14.5 and generate package for ruby-21
* Mon Sep 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.14.3
* Sun Mar 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.13.0
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
