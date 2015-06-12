%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname net-ssh
%define sfe_gemname net-ssh

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

Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          2.9.2
License:          MIT
URL:              https://github.com/net-ssh/net-ssh
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%if %{build19}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/%{gemname}-19

%description 19-old
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *

%description 19
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.
%endif

%if %{build20}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/%{gemname}-20

%description 20-old
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *

%description 20
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.
%endif

%if %{build21}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/%{gemname}-21

%description 21-old
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *

%description 21
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.
%endif

%if %{build22}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/%{gemname}-22

%description 22-old
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.
BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *

%description 22
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.
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

    pushd .${geminstdir}
    mv support/ssh_tunnel_bug.rb support/ssh_tunnel_bug.rb.bak
    sed -e "s!^\#\!/usr/bin/ruby\$!\#\!${bindir}/ruby!" < support/ssh_tunnel_bug.rb.bak > support/ssh_tunnel_bug.rb
    rm support/ssh_tunnel_bug.rb.bak
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
- modify shebang to avoid dependency detection problem
* Wed Jul 23 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- specify required ruby version
* Thu Feb 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.9.1 and stop to generate package for ruby-18
* Thu Feb 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21
* Thu Feb 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.0
* Wed Jun 12 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-20
* Fri Apr 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.6.7
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
