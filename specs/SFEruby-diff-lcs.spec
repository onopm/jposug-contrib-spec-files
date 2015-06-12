%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname diff-lcs
%define sfe_gemname diff-lcs

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

Summary:          Diff::LCS computes the difference between two Enumerable sequences
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          1.2.5
License:          MIT, Perl Artistic v2, GNU GPL v2
URL:              http://diff-lcs.rubyforge.org/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%if %{build19}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          Diff::LCS computes the difference between two Enumerable sequences
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19-old
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          Diff::LCS computes the difference between two Enumerable
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *

%description 19
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%endif

%if %{build20}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Diff::LCS computes the difference between two Enumerable
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20-old
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          Diff::LCS computes the difference between two Enumerable sequences
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *

%description 20
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%endif

%if %{build21}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Diff::LCS computes the difference between two Enumerable sequences
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Diff::LCS computes the difference between two Enumerable sequences
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *

%description 21
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%endif

%if %{build22}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Diff::LCS computes the difference between two Enumerable sequences
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Diff::LCS computes the difference between two Enumerable sequences
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *

%description 22
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

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

    pushd .${geminstdir}/bin
    for i in ldiff htmldiff
    do
        mv ${i} ${i}.bak
        sed -e "s!^\#\!ruby \-w\$!\#\!${bindir}/ruby -w!" < ${i}.bak > ${i}
        rm ${i}.bak
    done
    popd
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
- update specfile based on bin/make_rubygem_spec.rb
* Wed May 27 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix shebang to avoid failing dependency check
* Sat Feb 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-22
* Sun Dec 14 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18
* Wed Feb 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.5 and generate package for ruby-20 and ruby-21
* Sun Mar 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1
* Wed Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
