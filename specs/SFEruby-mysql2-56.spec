%include Solaris.inc
%include default-depend.inc

%define gemname mysql2
%define mysql_ver 5.6

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}

Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Name: SFEruby-%{gemname}-56
IPS_package_name:        library/ruby-22/mysql2-56
Version: 0.3.15
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-22
BuildRequires:	database/mysql-56
BuildRequires:	database/mysql-56/library
Requires:       runtime/ruby-22
Requires:	database/mysql-56/library

%description
A simple, fast Mysql library for Ruby, binding to libmysql

%package 19
IPS_package_name: library/ruby-19/mysql2-56
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
BuildRequires:	runtime/ruby-19
BuildRequires:	database/mysql-56
BuildRequires:	database/mysql-56/library
Requires:	runtime/ruby-19
Requires:	database/mysql-56/library

%description 19
A simple, fast Mysql library for Ruby, binding to libmysql

%package 20
IPS_package_name: library/ruby-20/mysql2-56
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
BuildRequires:	runtime/ruby-20
BuildRequires:	database/mysql-56
BuildRequires:	database/mysql-56/library
Requires:	runtime/ruby-20
Requires:	database/mysql-56/library

%description 20
A simple, fast Mysql library for Ruby, binding to libmysql

%package 21
IPS_package_name: library/ruby-21/mysql2-56
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
BuildRequires:	runtime/ruby-21
BuildRequires:	database/mysql-56
BuildRequires:	database/mysql-56/library
Requires:	runtime/ruby-21
Requires:	database/mysql-56/library

%description 21
A simple, fast Mysql library for Ruby, binding to libmysql

%prep
%setup -q -c -T

%build
export PATH=/usr/mysql/5.6/bin:$PATH

# ruby-19
export CFLAGS='-m64'
export LDFLAGS='-L/usr/mysql/5.6/lib/%{_arch64}:/lib/%{_arch64}:/usr/lib/%{_arch64} -R/usr/mysql/5.6/lib/%{_arch64}:/lib/%{_arch64}:/usr/lib/%{_arch64}'

/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0} \
    -- --with-mysql-config=/usr/mysql/5.6/bin/%{_arch64}/mysql_config

mv .%{gemdir19}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir19}/gems/mysql2-%{version}/lib/mysql2/mysql2-56.so

# ruby-20
/usr/ruby/2.0/bin/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0} \
    -- --with-mysql-config=/usr/mysql/5.6/bin/%{_arch64}/mysql_config

mv .%{gemdir20}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir20}/gems/mysql2-%{version}/lib/mysql2/mysql2-56.so

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0} \
    -- --with-mysql-config=/usr/mysql/5.6/bin/%{_arch64}/mysql_config

mv .%{gemdir21}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir21}/gems/mysql2-%{version}/lib/mysql2/mysql2-56.so

# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0} \
    -- --with-mysql-config=/usr/mysql/5.6/bin/%{_arch64}/mysql_config

mv .%{gemdir22}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir22}/gems/mysql2-%{version}/lib/mysql2/mysql2-56.so


%install
rm -rf %{buildroot}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

rm -rf %{buildroot}/%{gemdir19}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir19}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-56.so mysql2.so
popd

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

rm -rf %{buildroot}/%{gemdir20}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir20}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-56.so mysql2.so
popd

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

rm -rf %{buildroot}/%{gemdir21}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir21}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-56.so mysql2.so
popd

# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

rm -rf %{buildroot}/%{gemdir22}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir22}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-56.so mysql2.so
popd

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
* Wed Jan 14 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-22 instead of ruby-18
* Mon Mar 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21
* Fri Jan 31 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.15
* Tue May 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
