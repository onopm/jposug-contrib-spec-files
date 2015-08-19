#
# spec file for package SFEruby-21
#

%define _name ruby
%define version 2.2.3
%define major_version 2.2
%define unmangled_version 2.2.0
%define patchlevel 0

%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

Name:			SFEruby-22
IPS_Package_Name:	runtime/ruby-22
Summary:		An interpreter of object-oriented scripting language
Version:		%{version}
Release:		%{patchlevel}
IPS_component_version:	%{version}.%{patchlevel}
License: 		GPL
Source: http://cache.ruby-lang.org/pub/ruby/2.2/ruby-%{version}.tar.gz
Patch0:			ruby-22-ext-socket-option.patch
Url:			 http://www.ruby-lang.org/

BuildRequires: library/text/yaml >= 0.1.6
BuildRequires: system/network/bpf
BuildRequires: system/library/libnet
Requires:      library/text/yaml >= 0.1.6

%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-48
Requires:      system/library/gcc-48-runtime
%define mimpure_text
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif

%description

%prep
# %setup -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}

%patch0 -p1

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
    --prefix=/usr/ruby/%{major_version} \
    --bindir=/usr/ruby/%{major_version}/bin \
    --libdir=/usr/ruby/%{major_version}/lib/amd64 \
    --sbindir=/usr/ruby/%{major_version}/sbin \
    --mandir=/usr/ruby/%{major_version}/share/man \
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
ln -s ../ruby/%{major_version}/bin/erb .
ln -s ../ruby/%{major_version}/bin/gem .
ln -s ../ruby/%{major_version}/bin/irb .
ln -s ../ruby/%{major_version}/bin/rake .
ln -s ../ruby/%{major_version}/bin/rdoc .
ln -s ../ruby/%{major_version}/bin/ri .
ln -s ../ruby/%{major_version}/bin/ruby .

ln -s ../ruby/%{major_version}/bin/erb erb22
ln -s ../ruby/%{major_version}/bin/gem gem22
ln -s ../ruby/%{major_version}/bin/irb irb22
ln -s ../ruby/%{major_version}/bin/rake rake22
ln -s ../ruby/%{major_version}/bin/rdoc rdoc22
ln -s ../ruby/%{major_version}/bin/ri ri22
ln -s ../ruby/%{major_version}/bin/ruby ruby22

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
/usr/bin/*22
/usr/ruby/%{major_version}

%changelog
* Wed Aug 19 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.3
* Mon Mar 18 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.2
* Tue May 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.1
* Fri Dec 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- add BuildRequires
