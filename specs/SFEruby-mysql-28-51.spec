#
# spec file for package SFEruby-mysql-28-51
# gem install mysql (2.8.x)
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%include base.inc
%include default-depend.inc
%define gemname mysql
%define mysql_ver 5.1
# TODO: untested on ruby18
%define with_ruby18 0
# TODO: untested on ruby20
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
Name: SFEruby-%{gemname}-28-51
IPS_package_name:        library/ruby/mysql-28/mysql-51
SUNW_Copyright:   %name.copyright
Version: 2.8.1
License: GPL
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
Patch0: %{name}-2.8.1.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	%pnm_buildrequires_database_mysql_51
BuildRequires:	%pnm_buildrequires_mysql51lib
Requires:	%pnm_requires_mysql51lib
BuildRequires:  runtime/ruby-19
BuildRequires:  library/ruby-19/hoe
BuildRequires:  library/ruby-19/rake-compiler
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
IPS_package_name: library/ruby-18/mysql-28/mysql-51
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
BuildRequires:  runtime/ruby-18
Requires:       runtime/ruby-18
Requires:       %pnm_requires_mysql51lib
Requires:	library/ruby/mysql-28/mysql-51

%description 18
A simple, fast Mysql library for Ruby, binding to libmysql
%endif

%package 19
IPS_package_name: library/ruby-19/mysql-28/mysql-51
Summary: A simple, fast Mysql library for Ruby, binding to libmysql
Requires:	runtime/ruby-19
Requires:       %pnm_requires_mysql51lib
Requires:	library/ruby/mysql-28/mysql-51

%description 19
A simple, fast Mysql library for Ruby, binding to libmysql

%if %with_ruby20
#%package 20
#IPS_package_name: library/ruby-20/mysql-28/mysql-51
#Summary: A simple, fast Mysql library for Ruby, binding to libmysql
#Requires:	runtime/ruby-20
#Requires:       %pnm_requires_mysql51lib
#Requires:	library/ruby/mysql-28/mysql-51

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
sed -i '/self.rubyforge_name/d' tasks/gem.rake
/usr/ruby/1.9/bin/rake package
/bin/mv -f pkg/${gempath##*/} ../
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

#mv .%{gemdir18}/gems/mysql-%{version}/lib/mysql/mysql_api.so .%{gemdir18}/gems//mysql-%{version}/lib/mysql/mysql_api-51.so 
mv .%{gemdir18}/gems/mysql-%{version}/lib/mysql_api.so .%{gemdir18}/gems//mysql-%{version}/lib/mysql_api-51.so 
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
#mv .%{gemdir19}/gems/mysql-%{version}/lib/mysql/mysql_api.so .%{gemdir19}/gems/mysql-%{version}/lib/mysql/mysql_api-51.so
mv .%{gemdir19}/gems/mysql-%{version}/lib/mysql_api.so .%{gemdir19}/gems/mysql-%{version}/lib/mysql_api-51.so

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

## mv .%{gemdir20}/gems/mysql-%{version}/lib/mysql/mysql_api.so .%{gemdir20}/gems/mysql-%{version}/lib/mysql/mysql_api-51.so
# mv .%{gemdir20}/gems/mysql-%{version}/lib/mysql_api.so .%{gemdir20}/gems/mysql-%{version}/lib/mysql_api-51.so
%endif

%install
rm -rf %{buildroot}

# ruby-18
%if %with_ruby18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

rm -rf %{buildroot}/%{gemdir18}/gems/mysql-%{version}/ext
#pushd %{buildroot}/%{gemdir18}/gems/mysql-%{version}/lib/mysql
pushd %{buildroot}/%{gemdir18}/gems/mysql-%{version}/lib
ln -s mysql_api-51.so mysql_api.so
popd
%endif

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

rm -rf %{buildroot}/%{gemdir19}/gems/mysql-%{version}/ext
#pushd %{buildroot}/%{gemdir19}/gems/mysql-%{version}/lib/mysql
pushd %{buildroot}/%{gemdir19}/gems/mysql-%{version}/lib
ln -s mysql_api-51.so mysql_api.so
popd

# ruby-20
%if %with_ruby20
# mkdir -p %{buildroot}/%{gemdir20}
# cp -a .%{gemdir20}/* \
#     %{buildroot}/%{gemdir20}/

# rm -rf %{buildroot}/%{gemdir20}/gems/mysql-%{version}/ext
## pushd %{buildroot}/%{gemdir20}/gems/mysql-%{version}/lib/mysql
# pushd %{buildroot}/%{gemdir20}/gems/mysql-%{version}/lib
# ln -s mysql_api-51.so mysql_api.so
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
* Sat Jun 07 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial commit
