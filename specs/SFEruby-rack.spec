%include Solaris.inc
%include default-depend.inc

%define gemname rack
%define generate_executable 0

%define bindir18 /usr/ruby/1.8/bin
%define gemdir18 %(%{bindir18}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}

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
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/rack
Version: 1.5.2
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires: runtime/ruby-18

%description
Rack provides a minimal, modular and adaptable interface for developing web applications in Ruby.

%package 19
IPS_package_name: library/ruby-19/rack
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%description 19
Rack provides a minimal, modular and adaptable interface for developing web applications in Ruby.

%package 20
IPS_package_name: library/ruby-20/rack
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20

%description 20
Rack provides a minimal, modular and adaptable interface for developing web applications in Ruby.

%package 21
IPS_package_name: library/ruby-21/rack
Summary: %{gemname}
BuildRequires:	runtime/ruby-21
Requires:	runtime/ruby-21

%description 21
Rack provides a minimal, modular and adaptable interface for developing web applications in Ruby.

%prep
%setup -q -c -T
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}
mkdir -p .%{gemdir20}
mkdir -p .%{bindir20}

%build
# export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

# ruby-18
/usr/ruby/1.8/bin/gem install --local \
    --install-dir .%{gemdir18} \
    --bindir .%{bindir18} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

# ruby-20
/usr/ruby/2.0/bin/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

mkdir -p %{buildroot}%{bindir18}
cp -a .%{bindir18}/* \
    %{buildroot}%{bindir18}/


pushd .%{bindir18}
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir18}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd

pushd .%{gemdir18}/gems/%{gemname}-%{version}/bin/
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir18}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd


# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}%{bindir19}/

pushd .%{bindir19}
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir19}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd

pushd .%{gemdir19}/gems/%{gemname}-%{version}/bin/
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir19}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
    %{buildroot}%{bindir20}/

pushd .%{bindir20}
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir20}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd

pushd .%{gemdir20}/gems/%{gemname}-%{version}/bin/
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir20}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
    %{buildroot}%{bindir21}/

pushd .%{bindir21}
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir21}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd

pushd .%{gemdir21}/gems/%{gemname}-%{version}/bin/
mv rackup rackup.bak
sed -e 's!/usr/bin/env ruby!%{bindir21}/ruby!' < rackup.bak > rackup
rm rackup.bak
popd

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8

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
* Tue Mar 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21 and modify shebang
* Tue May 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.2
* Fri Oct 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
