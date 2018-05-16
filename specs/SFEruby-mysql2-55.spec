%include Solaris.inc
%include default-depend.inc

%define gemname mysql2
%define mysql_ver 5.5

%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin

Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Name: SFEruby-%{gemname}-55
IPS_package_name:        library/ruby-18/mysql2-55
Version: 0.3.11
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
BuildRequires:	database/mysql-55
BuildRequires:	database/mysql-55/devel
BuildRequires:	database/mysql-55/library
Requires:       runtime/ruby-18
Requires:	database/mysql-55/library

%description
A simple, fast Mysql library for Ruby, binding to libmysql

%package 19
IPS_package_name: library/ruby-19/mysql2-55
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
BuildRequires:	runtime/ruby-19
BuildRequires:	database/mysql-55
BuildRequires:	database/mysql-55/library
Requires:	runtime/ruby-19

%description 19
A simple, fast Mysql library for Ruby, binding to libmysql

# %package 20
# IPS_package_name: library/ruby-20/mysql2-55
# Summary: A simple, fast Mysql library for Ruby, binding to libmysql
# BuildRequires:	runtime/ruby-20
# BuildRequires:	database/mysql-55
# BuildRequires:	database/mysql-55/library
# Requires:	runtime/ruby-20

# %description 20
# A simple, fast Mysql library for Ruby, binding to libmysql

%prep
%setup -q -c -T
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}

%build
export PATH=/usr/mysql/%{mysql_ver}/bin:$PATH

# ruby-18
/usr/ruby/1.8/bin/gem install --local \
    --install-dir .%{gemdir18} \
    --bindir .%{bindir18} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0} \
    -- --with-mysql-config=/usr/mysql/%{mysql_ver}/bin/mysql_config

mv .%{gemdir18}/gems//mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir18}/gems//mysql2-%{version}/lib/mysql2/mysql2-55.so 

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0} \
    -- --with-mysql-config=/usr/mysql/%{mysql_ver}/bin/mysql_config

mv .%{gemdir19}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir19}/gems/mysql2-%{version}/lib/mysql2/mysql2-55.so

# # ruby-20
# /usr/ruby/2.0/bin/gem install --local \
#     --install-dir .%{gemdir20} \
#     --bindir .%{bindir20} \
#     --no-ri \
#     --no-rdoc \
#     -V \
#     --force %{SOURCE0} \
#     -- --with-mysql-config=/usr/mysql/%{mysql_ver}/bin/mysql_config

# mv .%{gemdir20}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir20}/gems/mysql2-%{version}/lib/mysql2/mysql2-55.so

%install
rm -rf %{buildroot}

# ruby-18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

rm -rf %{buildroot}/%{gemdir18}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir18}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-55.so mysql2.so
popd

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

rm -rf %{buildroot}/%{gemdir19}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir19}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-55.so mysql2.so
popd

# # ruby-20
# mkdir -p %{buildroot}/%{gemdir20}
# cp -a .%{gemdir20}/* \
#     %{buildroot}/%{gemdir20}/

# rm -rf %{buildroot}/%{gemdir20}/gems/mysql2-%{version}/ext
# pushd %{buildroot}/%{gemdir20}/gems/mysql2-%{version}/lib/mysql2
# ln -s mysql2-55.so mysql2.so
# popd

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

# %files 20
# %defattr(0755,root,bin,-)
# %dir %attr (0755, root, sys) /usr
# /usr/ruby/2.0

%changelog
* Mon Jun 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
