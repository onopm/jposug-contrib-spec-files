%include Solaris.inc
%include default-depend.inc

%define gemname pg
%define postgresql_ver 9.0

%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin

Summary: Pg is the Ruby interface to the PostgreSQL RDBMS
Name: SFEruby-%{gemname}-90
IPS_package_name:        library/ruby-18/pg-90
Version: 0.17.0
License: Ruby License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
BuildRequires:	database/postgres-90/developer
BuildRequires:	database/postgres-90/library
Requires:       runtime/ruby-18
Requires:	database/postgres-90/library

%description
Pg is the Ruby interface to the PostgreSQL RDBMS

%package 19
IPS_package_name: library/ruby-19/pg-90
Summary: Pg is the Ruby interface to the PostgreSQL RDBMS
BuildRequires:	runtime/ruby-19
BuildRequires:	database/postgres-90/developer
BuildRequires:	database/postgres-90/library
Requires:       runtime/ruby-19
Requires:	database/postgres-90/library

%description 19
Pg is the Ruby interface to the PostgreSQL RDBMS

# %package 20
# IPS_package_name: library/ruby-20/pg-90
# Summary: Pg is the Ruby interface to the PostgreSQL RDBMS
# BuildRequires:	runtime/ruby-20
# BuildRequires:	database/postgres-90/developer
# BuildRequires:	database/postgres-90/library
# Requires:       runtime/ruby-20
# Requires:	database/postgres-90/library

# %description 20
# Pg is the Ruby interface to the PostgreSQL RDBMS

%prep
%setup -q -c -T
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}
# mkdir -p .%{gemdir20}
# mkdir -p .%{bindir20}

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
    -- --with-pg-config=/usr/postgres/%{postgresql_ver}/bin/pg_config

# mv .%{gemdir18}/gems//mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir18}/gems//mysql2-%{version}/lib/mysql2/mysql2-55.so 

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0} \
    -- --with-pg-config=/usr/postgres/%{postgresql_ver}/bin/pg_config

# # ruby-20
# /usr/ruby/2.0/bin/gem install --local \
#     --install-dir .%{gemdir20} \
#     --bindir .%{bindir20} \
#     --no-ri \
#     --no-rdoc \
#     -V \
#     --force %{SOURCE0} \
#     -- --with-pg-config=/usr/postgres/%{postgresql_ver}/bin/pg_config

%install
rm -rf %{buildroot}

# ruby-18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

# # ruby-20
# mkdir -p %{buildroot}/%{gemdir20}
# cp -a .%{gemdir20}/* \
#     %{buildroot}/%{gemdir20}/

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
* Tue Oct 29 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
