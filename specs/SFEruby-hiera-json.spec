%include Solaris.inc
%include default-depend.inc

%define gemname hiera-json

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary: Store Hiera data in JSON
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-21/hiera/json
Version: 0.4.0
License: Apache License 2.0
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-21
Requires:       runtime/ruby-21
Requires:	library/ruby-21/json
Requires:	library/ruby-21/hiera

%description
Store Hiera data in JSON

%package 19
IPS_package_name: library/ruby-19/hiera/json
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
# Requires:	library/ruby-19/json
Requires:	library/ruby-19/hiera

%description 19
Store Hiera data in JSON

%package 20
IPS_package_name: library/ruby-20/hiera/json
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
# Requires:	library/ruby-20/json
Requires:	library/ruby-20/hiera

%description 20
Store Hiera data in JSON

%prep
%setup -q -c -T

%build
# export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --force %{SOURCE0}

# ruby-20
/usr/ruby/2.0/bin/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    -V \
    --force %{SOURCE0}

# ruby-21
/usr/ruby/2.1/bin/gem install --local \
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

rm -rf %{buildroot}%{geminstdir}/.yardoc/

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
* Tue Apr 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21 and stop to generate package for ruby-18
* Wed Jan 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-20
* Thu Jan 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix path in %define gemdir18 and gemdir19
* Thu Dec 20 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use full path in %define gemdir18 and gemdir19
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
