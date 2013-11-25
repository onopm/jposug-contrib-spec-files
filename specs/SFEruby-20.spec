#
# spec file for package SFEruby-20
#

%define _name ruby
%define version 2.0.0
%define unmangled_version 2.0.0
%define patchlevel 353

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

Name: SFEruby-20
IPS_Package_Name:	runtime/ruby-20
Summary: An interpreter of object-oriented scripting language
Version: %{version}
Release: %{patchlevel}
IPS_component_version: %{version}.%{patchlevel}
License: GPL
Source: http://ftp.ruby-lang.org/pub/ruby/2.0/ruby-%{version}-p%{patchlevel}.tar.gz
Url: http://www.ruby-lang.org/

BuildRequires: library/text/yaml
Requires:      library/text/yaml

%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%define mimpure_text
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif

%description

%prep
# %setup -c -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}-p%{patchlevel}
%build
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags %gnu_lib_path"
export CFLAGS="%optflags"
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
./configure \
%if %( expr %{osbuild} '=' 175 )
%else
ac_cv_func_dl_iterate_phdr=no \
%endif
    --prefix=/usr/ruby/2.0 \
    --bindir=/usr/ruby/2.0/bin \
    --libdir=/usr/ruby/2.0/lib \
    --sbindir=/usr/ruby/2.0/sbin \
    --enable-dtrace \
    --enable-shared \
    --enable-install-doc \
    --disable-option-checking \
    --with-openssl \
    --with-tk-dir=/usr \
    --with-curses-dir=/usr \
    CC=/usr/bin/gcc \
    CXX=/usr/bin/g++
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../ruby/2.0/bin/erb erb20
ln -s ../ruby/2.0/bin/gem gem20
ln -s ../ruby/2.0/bin/irb irb20
ln -s ../ruby/2.0/bin/rake rake20
ln -s ../ruby/2.0/bin/rdoc rdoc20
ln -s ../ruby/2.0/bin/ri ri20
ln -s ../ruby/2.0/bin/ruby ruby20

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /usr
/usr/bin/*20
/usr/ruby/2.0

%changelog
* Mon Nov 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to patchlevel 353
* Sun Jun 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to patchlevel 247
* Wed May 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to patchlevel 195
* Sat Mar 09 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires and Requires because gem command requires library/text/yaml
* Thu Mar 07 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
