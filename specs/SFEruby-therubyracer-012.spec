#
# spec file for package SFEruby-therubyracer-012
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%include base.inc
%include default-depend.inc
%define gemname therubyracer
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

Summary: Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code and manipulate Ruby objects from JavaScript.
%define majorver 012
Name: SFEruby-%{gemname}-%majorver
Version: 0.12.1 
IPS_package_name:       library/ruby/%{gemname}-%majorver
SUNW_Copyright:   %name.copyright
License: MIT
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1: %{name}-%{gemname}.gemspec
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
BuildRequires:  %{pnm_buildrequires_library_openldap}
Requires:       %{pnm_requires_library_openldap}

%description
The Ruby Racer is designed to let you evaluate JavaScript as safely as possible
unless you tell it to do something more dangerous. The default context is
a hermetically sealed JavaScript environment with only the standard JavaScript
objects and functions. Nothing from the Ruby world is accessible at all.

%if %with_ruby18
%package 18
IPS_package_name: library/ruby-18/%{gemname}-%majorver
Summary: Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code and manipulate Ruby objects from JavaScript.
BuildRequires:  runtime/ruby-18
Requires:       runtime/ruby-18
Requires:	library/ruby/%{gemname}-%majorver
BuildRequires:	library/ruby-18/libv8-3-16-14
Requires:	library/ruby-18/libv8-3-16-14

%description 18
The Ruby Racer is designed to let you evaluate JavaScript as safely as possible
unless you tell it to do something more dangerous. The default context is
a hermetically sealed JavaScript environment with only the standard JavaScript
objects and functions. Nothing from the Ruby world is accessible at all.

%endif

%package 19
IPS_package_name: library/ruby-19/%{gemname}-%majorver
Summary: Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code and manipulate Ruby objects from JavaScript.
Requires:	runtime/ruby-19
Requires:	library/ruby/%{gemname}-%majorver
BuildRequires:	library/ruby-19/libv8-3-16-14
Requires:	library/ruby-19/libv8-3-16-14


%description 19
The Ruby Racer is designed to let you evaluate JavaScript as safely as possible
unless you tell it to do something more dangerous. The default context is
a hermetically sealed JavaScript environment with only the standard JavaScript
objects and functions. Nothing from the Ruby world is accessible at all.

%if %with_ruby20
#%package 20
#IPS_package_name: library/ruby-20/%{gemname}-%majorver
#Summary: Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code and manipulate Ruby objects from JavaScript.
#Requires:	runtime/ruby-20
#Requires:	library/ruby/%{gemname}-%majorver
#BuildRequires:	library/ruby-20/libv8-3-16-14
#Requires:	library/ruby-20/libv8-3-16-14

#%description 20
#The Ruby Racer is designed to let you evaluate JavaScript as safely as possible
#unless you tell it to do something more dangerous. The default context is
#a hermetically sealed JavaScript environment with only the standard JavaScript
#objects and functions. Nothing from the Ruby world is accessible at all.
%endif

%prep
gempath=%{S:0}
%if %{skip_prep}
%else
%setup -q -c -T
cp %{S:0} ${gempath##*/}
/usr/ruby/1.9/bin/gem unpack ${gempath##*/}
cd %gemname-%version
cp %{S:1} %gemname.gemspec
sed -i -e '/gem.executables/d' -e '/gem.test_files/d' -e 's/git ls-files/find/' %gemname.gemspec
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
%if %( expr %{osbuild} '=' 175 )
export CC=gcc
export CXX=g++
%else
export CC=/usr/gcc/4.6/bin/gcc
export CXX=/usr/gcc/4.6/bin/g++
%endif
export CFLAGS="%optflags -fno-strict-aliasing -Wno-pointer-sign"
export CPPFLAGS=""
export LDFLAGS="%{_ldflags}"
gempath=%{S:0}
# ruby-18
%if %with_ruby18
/usr/ruby/1.9/bin/gem install --local \
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
#    --install-dir .%{gemdir20} \
#    --bindir .%{bindir20} \
#    --no-ri \
#    --no-rdoc \
#    -V \
#    --force ${gempath##*/} \
%endif

%install
rm -rf %{buildroot}
# ruby-18
%if %with_ruby18
/bin/rm -rf ./%{geminstdir18}/ext/v8/*.o
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/
%endif

# ruby-19
/bin/rm -rf ./%{geminstdir19}/ext/v8/*.o
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

# ruby-20
%if %with_ruby20
#mkdir -p %{buildroot}/%{gemdir20}
#cp -a .%{gemdir20}/* \
#    %{buildroot}/%{gemdir20}/
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
* Sun Aug 9 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- initial commit
