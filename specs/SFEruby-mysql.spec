%include Solaris.inc
%include default-depend.inc

%define gemname mysql
%define gemdir18 %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define gemdir19 %(ruby19 -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define tarball_name    mysql-ruby
%define tarball_version 2.8.2

Summary: %{gemname}
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-18/mysql
Version: 2.8.2
License: Ruby License
#URL: http://rubygems.org/gems/%{gemname}
#Source0: http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
Source0: http://tmtm.org/downloads/mysql/ruby/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: runtime/ruby-18
BuildRequires: database/mysql-51
Requires:      runtime/ruby-18

%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby programs that the MySQL C API provides for C programs.

%package 19
IPS_package_name: library/ruby-19/mysql
Summary: %{gemname}
BuildRequires: runtime/ruby-19
BuildRequires: database/mysql-51
Requires:      runtime/ruby-19

%description 19
This is the MySQL API module for Ruby. It provides the same functions for Ruby programs that the MySQL C API provides for C programs.

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

# ruby 1.8
mkdir -p .%{gemdir18}/%{gemname}-%{version}
cp extconf.rb mysql.c .%{gemdir18}/%{gemname}-%{version}


mkdir -p .%{gemdir19}/%{gemname}-%{version}
cp extconf.rb mysql.c .%{gemdir19}/%{gemname}-%{version}

%build

# ruby-18
pushd .%{gemdir18}/%{gemname}-%{version}
/usr/ruby/1.8/bin/ruby extconf.rb --with-mysql-config=/usr/mysql/5.1/bin/mysql_config
make CC=/opt/solarisstudio12.3/bin/cc

popd

# ruby-19
pushd .%{gemdir19}/%{gemname}-%{version}
/usr/ruby/1.9/bin/ruby extconf.rb --with-mysql-config=/usr/mysql/5.1/bin/mysql_config
make CC=/opt/solarisstudio12.3/bin/cc

%install
rm -rf %{buildroot}

# 1.8
pushd .%{gemdir18}/%{gemname}-%{version}
make install DESTDIR=%{buildroot}
popd

# 1.9
pushd .%{gemdir19}/%{gemname}-%{version}
make install DESTDIR=%{buildroot}
popd

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
# %dir %attr (0755, root, sys) /var
# %attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Fri Dec 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Fri Oct 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
