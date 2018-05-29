#
# spec file for package SFEruby-mysql2-02-51
# gem install mysql2 (0.2.x)
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%include base.inc
%include default-depend.inc
%define gemname mysql2
%define mysql_ver 5.1
%define with_ruby18 0
%define with_ruby20 0
%define skip_prep 0

%if %with_ruby18
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin
%endif

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

%if %with_ruby20
%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%define bindir20 /usr/ruby/2.0/bin
%endif

Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Name: SFEruby-%{gemname}-02-51
IPS_package_name:        library/ruby/mysql2-02/mysql-51
SUNW_Copyright:   %name.copyright
Version: 0.2.23
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1: %{name}-mysql2-0.2.23.gemspec
Patch0:  %{name}-0.2.23.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	%pnm_buildrequires_database_mysql_51
BuildRequires:	%pnm_buildrequires_mysql51lib
Requires:	%pnm_requires_mysql51lib
BuildRequires:  runtime/ruby-19
%if %cc_is_gcc
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc
Requires:      system/library/gcc-runtime
%endif
%endif

%description
A simple, fast Mysql library for Ruby, binding to libmysql

%if %with_ruby18
%package 18
IPS_package_name: library/ruby-18/mysql2-02/mysql-51
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
BuildRequires:  runtime/ruby-18
Requires:       runtime/ruby-18
Requires:       %pnm_requires_mysql51lib
Requires:	library/ruby/mysql2-02/mysql-51

%description 18
A simple, fast Mysql library for Ruby, binding to libmysql
%endif

%package 19
IPS_package_name: library/ruby-19/mysql2-02/mysql-51
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Requires:	runtime/ruby-19
Requires:       %pnm_requires_mysql51lib
Requires:	library/ruby/mysql2-02/mysql-51

%description 19
A simple, fast Mysql library for Ruby, binding to libmysql

%if %with_ruby20
#%package 20
#IPS_package_name: library/ruby-20/mysql2-02/mysql-51
#Summary: A simple, fast Mysql library for Ruby, binding to libmysql
#Requires:	runtime/ruby-20
#Requires:       %pnm_requires_mysql51lib
#Requires:	library/ruby/mysql2-02/mysql-51

#%description 20
#A simple, fast Mysql library for Ruby, binding to libmysql
%endif

%prep
gempath=%{S:0}
%if %{skip_prep}
%else
%setup -q -c -T
cp %{S:0} ${gempath##*/}
/usr/ruby/1.9/bin/gem unpack ${gempath##*/}
%patch0 -p0 -b .orig
cd %gemname-%version
cp %{S:1} %gemname.gemspec 
/usr/ruby/1.9/bin/gem build %gemname.gemspec
/bin/mv -f ${gempath##*/} ../
cd ..

%if %with_ruby18
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
%endif
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}
%endif

%build
%if %{skip_prep}
 cd %name-%version
%endif
gempath=%{S:0}
export PATH=/usr/mysql/%{mysql_ver}/bin:$PATH
# ruby-18
%if %with_ruby18
/usr/ruby/1.8/bin/gem install --local \
    --install-dir .%{gemdir18} \
    --bindir .%{bindir18} \
    --no-ri \
    --no-rdoc \
    -V \
    --force ${gempath##*/} \
    -- --with-mysql-config=/usr/mysql/%{mysql_ver}/bin/mysql_config

mv .%{gemdir18}/gems//mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir18}/gems//mysql2-%{version}/lib/mysql2/mysql2-51.so 
%endif

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force ${gempath##*/} \
    -- --with-mysql-config=/usr/mysql/%{mysql_ver}/bin/mysql_config 
mv .%{gemdir19}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir19}/gems/mysql2-%{version}/lib/mysql2/mysql2-51.so

# ruby-20
%if %with_ruby20
# /usr/ruby/2.0/bin/gem install --local \
#     --install-dir .%{gemdir20} \
#     --bindir .%{bindir20} \
#     --no-ri \
#     --no-rdoc \
#     -V \
#     --force ${gempath##*/} \
#     -- --with-mysql-config=/usr/mysql/%{mysql_ver}/bin/mysql_config

# mv .%{gemdir20}/gems/mysql2-%{version}/lib/mysql2/mysql2.so .%{gemdir20}/gems/mysql2-%{version}/lib/mysql2/mysql2-51.so
%endif

%install
rm -rf %{buildroot}

# ruby-18
%if %with_ruby18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

rm -rf %{buildroot}/%{gemdir18}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir18}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-51.so mysql2.so
popd
%endif

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

rm -rf %{buildroot}/%{gemdir19}/gems/mysql2-%{version}/ext
pushd %{buildroot}/%{gemdir19}/gems/mysql2-%{version}/lib/mysql2
ln -s mysql2-51.so mysql2.so
popd

# ruby-20
%if %with_ruby20
# mkdir -p %{buildroot}/%{gemdir20}
# cp -a .%{gemdir20}/* \
#     %{buildroot}/%{gemdir20}/

# rm -rf %{buildroot}/%{gemdir20}/gems/mysql2-%{version}/ext
# pushd %{buildroot}/%{gemdir20}/gems/mysql2-%{version}/lib/mysql2
# ln -s mysql2-51.so mysql2.so
# popd
%endif

%clean
rm -rf %{buildroot}

%if %with_ruby18
%files 18
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
%endif

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%if %with_ruby20
# %files 20
# %defattr(0755,root,bin,-)
# %dir %attr (0755, root, sys) /usr
# /usr/ruby/2.0
%endif

%changelog
* Sat Jun 7 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Change dependencies
* Fri Jun 6 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Change package name 
* Fri Jun 6 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- initial commit
