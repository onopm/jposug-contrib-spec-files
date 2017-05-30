#
# spec file for package SFEruby-libv8-3-16-14
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%include base.inc
%include default-depend.inc
%define gemname libv8
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

Summary: A gem for distributing the v8 runtime libraries and headers.
%define majorver 3-16-14
Name: SFEruby-%{gemname}-%majorver
Version: 3.16.14.3
IPS_package_name:       library/ruby/%{gemname}-%majorver
SUNW_Copyright:   %name.copyright
License: MIT
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1: %{name}-%{gemname}.gemspec
#Patch0: %name-extconf.rb.patch
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
The goal of libv8 is two fold: provide a binary gem containing the a pre-compiled
libv8.a for as many platforms as possible while at the same time supporting for
an automated compilation for all others.
Not only does this drastically reduce gem install times, but it also reduces
dependencies on the local machine receiving the gem. It also opens the door for
supporting Windows.

%if %with_ruby18
%package 18
IPS_package_name: library/ruby-18/%{gemname}-%majorver
Summary: A gem for distributing the v8 runtime libraries and headers.
BuildRequires:  runtime/ruby-18
Requires:       runtime/ruby-18
Requires:	library/ruby/%{gemname}-%majorver

%description 18
The goal of libv8 is two fold: provide a binary gem containing the a pre-compiled
libv8.a for as many platforms as possible while at the same time supporting for
an automated compilation for all others.
Not only does this drastically reduce gem install times, but it also reduces
dependencies on the local machine receiving the gem. It also opens the door for
supporting Windows.

%endif

%package 19
IPS_package_name: library/ruby-19/%{gemname}-%majorver
Summary: A gem for distributing the v8 runtime libraries and headers.
Requires:	runtime/ruby-19
Requires:	library/ruby/%{gemname}-%majorver

%description 19
The goal of libv8 is two fold: provide a binary gem containing the a pre-compiled
libv8.a for as many platforms as possible while at the same time supporting for
an automated compilation for all others.
Not only does this drastically reduce gem install times, but it also reduces
dependencies on the local machine receiving the gem. It also opens the door for
supporting Windows.

%if %with_ruby20
#%package 20
#IPS_package_name: library/ruby-20/%{gemname}-%majorver
#Summary: A gem for distributing the v8 runtime libraries and headers.
#Requires:	runtime/ruby-20
#Requires:	library/ruby/%{gemname}-%majorver

#%description 20
#The goal of libv8 is two fold: provide a binary gem containing the a pre-compiled
#libv8.a for as many platforms as possible while at the same time supporting for
#an automated compilation for all others.
#Not only does this drastically reduce gem install times, but it also reduces
#dependencies on the local machine receiving the gem. It also opens the door for
#supporting Windows.
%endif

%prep
gempath=%{S:0}
%if %{skip_prep}
%else
%setup -q -c -T
cp %{S:0} ${gempath##*/}
/usr/ruby/1.9/bin/gem unpack ${gempath##*/}
cd %gemname-%version
#wget --no-check-certificate https://github.com/cowboyd/libv8/raw/master/%{gemname}.gemspec
cp %{S:1} %gemname.gemspec
#pushd ext/libv8
#/usr/ruby/1.9/bin/ruby extconf.rb
#popd
pushd vendor/v8 
sed -i -e 's/^ARCHES = .*/ARCHES = ia32/' -e 's/^DEFAULT_ARCHES = .*/DEFAULT_ARCHES = ia32/' Makefile
sed -i -e 's/-pthread/-lpthread/' -e 's/-Wall/-Wall -fPIC/' ./build/standalone.gypi
popd
sed -i -e 's/git ls-files/find/' %gemname.gemspec
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
mkdir -p %{buildroot}/%{gemdir18}/{cache,specifications}
cp -a ./%{gemdir18}/cache/* %{buildroot}/%{gemdir18}/cache
cp -a ./%{gemdir18}/specifications/* %{buildroot}/%{gemdir18}/specifications
mkdir -p %{buildroot}/%{geminstdir18}/lib/libv8
cp .%{geminstdir18}/lib/libv8.rb %{buildroot}/%{geminstdir18}/lib
cp .%{geminstdir18}/lib/libv8/version.rb %{buildroot}/%{geminstdir18}/lib/libv8/version.rb
mkdir -p %{buildroot}/%{geminstdir18}/vendor/v8/include
cp .%{geminstdir18}/vendor/v8/include/v8-debug.h  %{buildroot}/%{geminstdir18}/vendor/v8/include
cp .%{geminstdir18}/vendor/v8/include/v8stdint.h  %{buildroot}/%{geminstdir18}/vendor/v8/include
cp .%{geminstdir18}/vendor/v8/include/v8-preparser.h  %{buildroot}/%{geminstdir18}/vendor/v8/include
cp .%{geminstdir18}/vendor/v8/include/v8.h %{buildroot}/%{geminstdir18}/vendor/v8/include
cp .%{geminstdir18}/vendor/v8/include/v8-testing.h %{buildroot}/%{geminstdir18}/vendor/v8/include
cp .%{geminstdir18}/vendor/v8/include/v8-profiler.h %{buildroot}/%{geminstdir18}/vendor/v8/include
mkdir -p %{buildroot}/%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libpreparser_lib.a %{buildroot}/%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libv8_nosnapshot.a %{buildroot}/%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libv8_base.a %{buildroot}/%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libv8_snapshot.a %{buildroot}/%{geminstdir18}/vendor/v8/out/ia32.release/obj.target/tools/gyp
mkdir -p %{buildroot}/%{geminstdir18}/ext/libv8
cp .%{geminstdir18}/ext/libv8/paths.rb %{buildroot}/%{geminstdir18}/ext/libv8/
cp .%{geminstdir18}/ext/libv8/.location.yml %{buildroot}/%{geminstdir18}/ext/libv8/
cp .%{geminstdir18}/ext/libv8/arch.rb %{buildroot}/%{geminstdir18}/ext/libv8/
cp .%{geminstdir18}/ext/libv8/location.rb %{buildroot}/%{geminstdir18}/ext/libv8/
%endif

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}/{cache,specifications}
cp -a ./%{gemdir19}/cache/* %{buildroot}/%{gemdir19}/cache
cp -a ./%{gemdir19}/specifications/* %{buildroot}/%{gemdir19}/specifications
mkdir -p %{buildroot}/%{geminstdir19}/lib/libv8
cp .%{geminstdir19}/lib/libv8.rb %{buildroot}/%{geminstdir19}/lib
cp .%{geminstdir19}/lib/libv8/version.rb %{buildroot}/%{geminstdir19}/lib/libv8/version.rb
mkdir -p %{buildroot}/%{geminstdir19}/vendor/v8/include
cp .%{geminstdir19}/vendor/v8/include/v8-debug.h  %{buildroot}/%{geminstdir19}/vendor/v8/include
cp .%{geminstdir19}/vendor/v8/include/v8stdint.h  %{buildroot}/%{geminstdir19}/vendor/v8/include
cp .%{geminstdir19}/vendor/v8/include/v8-preparser.h  %{buildroot}/%{geminstdir19}/vendor/v8/include
cp .%{geminstdir19}/vendor/v8/include/v8.h %{buildroot}/%{geminstdir19}/vendor/v8/include
cp .%{geminstdir19}/vendor/v8/include/v8-testing.h %{buildroot}/%{geminstdir19}/vendor/v8/include
cp .%{geminstdir19}/vendor/v8/include/v8-profiler.h %{buildroot}/%{geminstdir19}/vendor/v8/include
mkdir -p %{buildroot}/%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libpreparser_lib.a %{buildroot}/%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libv8_nosnapshot.a %{buildroot}/%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libv8_base.a %{buildroot}/%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp
cp .%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp/libv8_snapshot.a %{buildroot}/%{geminstdir19}/vendor/v8/out/ia32.release/obj.target/tools/gyp
mkdir -p %{buildroot}/%{geminstdir19}/ext/libv8 
cp .%{geminstdir19}/ext/libv8/paths.rb %{buildroot}/%{geminstdir19}/ext/libv8/
cp .%{geminstdir19}/ext/libv8/.location.yml %{buildroot}/%{geminstdir19}/ext/libv8/
cp .%{geminstdir19}/ext/libv8/arch.rb %{buildroot}/%{geminstdir19}/ext/libv8/
cp .%{geminstdir19}/ext/libv8/location.rb %{buildroot}/%{geminstdir19}/ext/libv8/

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
