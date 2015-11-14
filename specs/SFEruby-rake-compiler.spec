#
# spec file for package SFEruby-rake-compiler
#
%include Solaris.inc
%include packagenamemacros.inc
%include base.inc
%include default-depend.inc
%define gemname rake-compiler
#TODO: untested on ruby18 
%define with_ruby18 0
#TODO: untested on ruby20
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

Summary: Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.
Name: SFEruby-%{gemname}
IPS_package_name:       library/ruby/%{gemname}
SUNW_Copyright:   %name.copyright
Version: 0.8.3
License: Luis Lavena
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  runtime/ruby-19

%description
Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.

%if %with_ruby18
%package 18
IPS_package_name: library/ruby-18/%{gemname}
Summary: Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.
BuildRequires:  runtime/ruby-18
Requires:       runtime/ruby-18

%description 18
Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.
%endif

%package 19
IPS_package_name: library/ruby-19/%{gemname}
Summary: Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.
Requires:	runtime/ruby-19

%description 19
Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.

%if %with_ruby20
#%package 20
#IPS_package_name: library/ruby-20/%{gemname}
#Summary: Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.
#BuildRequires: runtime/ruby-18
#Requires:	runtime/ruby-20

#%description 20
#Provide a standard and simplified way to build and package Ruby extensions (C, Java) using Rake as glue.
%endif

%prep
gempath=%{S:0}
%if %{skip_prep}
%else
%setup -q -c -T
cp %{S:0} ${gempath##*/}
/usr/ruby/1.9/bin/gem unpack ${gempath##*/}
#cd %gemname-%version
#cp %{S:1} %gemname.gemspec 
#/usr/ruby/1.9/bin/gem build %gemname.gemspec
#/bin/mv -f ${gempath##*/} ../
#cd ..

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
# ruby-18
%if %with_ruby18
/usr/ruby/1.8/bin/gem install --local \
    --install-dir .%{gemdir18} \
    --bindir .%{bindir18} \
    --no-ri \
    --no-rdoc \
    -V \
    --force ${gempath##*/} \
%endif

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force ${gempath##*/} \

# ruby-20
%if %with_ruby20
# /usr/ruby/2.0/bin/gem install --local \
#     --install-dir .%{gemdir20} \
#     --bindir .%{bindir20} \
#     --no-ri \
#     --no-rdoc \
#     -V \
#     --force ${gempath##*/} \
%endif

%install
rm -rf %{buildroot}

# ruby-18
%if %with_ruby18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/
rm -rf %{buildroot}/%{gemdir18}/gems/%{gemname}-%{version}/ext
%endif

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/
rm -rf %{buildroot}/%{gemdir19}/gems/%{gemname}-%{version}/ext

# ruby-20
%if %with_ruby20
#mkdir -p %{buildroot}/%{gemdir20}
#cp -a .%{gemdir20}/* \
#    %{buildroot}/%{gemdir20}/

#rm -rf %{buildroot}/%{gemdir20}/gems/%{gemname}-%{version}/ext
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
- initial commit
