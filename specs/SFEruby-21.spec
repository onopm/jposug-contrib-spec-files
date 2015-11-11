#
# spec file for package SFEruby-21
#

%define _name ruby
%define version 2.1.5
%define major_version 2.1
%define unmangled_version 2.1.0
%define patchlevel 0

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

Name: SFEruby-21
IPS_Package_Name:	runtime/ruby-21
Summary: An interpreter of object-oriented scripting language
Version: %{version}
Release: %{patchlevel}
IPS_component_version: %{version}.%{patchlevel}
License: GPL
Source: http://cache.ruby-lang.org/pub/ruby/2.1/ruby-%{version}.tar.gz
# Source: http://cache.ruby-lang.org/pub/ruby/2.1/ruby-%{version}-p%{patchlevel}.tar.gz
Url: http://www.ruby-lang.org/

BuildRequires: library/text/yaml >= 0.1.6
BuildRequires: system/network/bpf
Requires:      library/text/yaml >= 0.1.6

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
# %setup -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}
%build
export CFLAGS='-m64 -std=gnu99 -I/usr/gcc/include'
export CPPFLAGS="-m64 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
export LDFLAGS="-m64 -L/lib/%{_arch64} -L/usr/lib/%{_arch64} -R/lib/%{_arch64} -R/usr/lib/%{_arch64}"

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
./configure \
%if %( expr %{osbuild} '=' 175 )
%else
ac_cv_func_dl_iterate_phdr=no \
%endif
    --prefix=/usr/ruby/2.1 \
    --bindir=/usr/ruby/2.1/bin \
    --libdir=/usr/ruby/2.1/lib/amd64 \
    --sbindir=/usr/ruby/2.1/sbin \
    --mandir=/usr/ruby/2.1/share/man \
    --enable-dtrace \
    --enable-shared \
    --enable-install-doc \
    --disable-option-checking \
    --with-openssl \
    --with-curses-dir=/usr \
    --disable-install-doc \
    CC=/usr/bin/gcc \
    CXX=/usr/bin/g++
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../ruby/2.1/bin/erb .
ln -s ../ruby/2.1/bin/gem .
ln -s ../ruby/2.1/bin/irb .
ln -s ../ruby/2.1/bin/rake .
ln -s ../ruby/2.1/bin/rdoc .
ln -s ../ruby/2.1/bin/ri .
ln -s ../ruby/2.1/bin/ruby .

ln -s ../ruby/2.1/bin/erb erb21
ln -s ../ruby/2.1/bin/gem gem21
ln -s ../ruby/2.1/bin/irb irb21
ln -s ../ruby/2.1/bin/rake rake21
ln -s ../ruby/2.1/bin/rdoc rdoc21
ln -s ../ruby/2.1/bin/ri ri21
ln -s ../ruby/2.1/bin/ruby ruby21

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%ips_tag (mediator=ruby mediator-version=%{major_version})  /usr/bin/erb
%ips_tag (mediator=ruby mediator-version=%{major_version})  /usr/bin/gem
%ips_tag (mediator=ruby mediator-version=%{major_version})  /usr/bin/irb
%ips_tag (mediator=ruby mediator-version=%{major_version})  /usr/bin/rake
%ips_tag (mediator=ruby mediator-version=%{major_version})  /usr/bin/rdoc
%ips_tag (mediator=ruby mediator-version=%{major_version})  /usr/bin/ri
%ips_tag (mediator=ruby mediator-version=%{major_version})  /usr/bin/ruby
/usr/bin/*21
/usr/ruby/2.1

%changelog
* Fri Nov 14 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.5
* Wed Oct 28 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.4
* Mon Sep 22 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.3
* Fri May 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.2
* Wed Apr 02 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- specify required version of library/text/yaml (CVE-2014-2525)
* Tue Feb 25 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- use mediator
