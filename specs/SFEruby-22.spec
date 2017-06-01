#
# spec file for package SFEruby-22
#

%define _name ruby
%define version 2.2.7
%define major_version 2.2
%define unmangled_version 2.2.0
%define patchlevel 0

%include Solaris.inc
%include packagenamemacros.inc
%include base.inc

Name:                   SFEruby-22
IPS_Package_Name:       runtime/ruby-22
Summary:                An interpreter of object-oriented scripting language
Version:                %{version}
Release:                %{patchlevel}
IPS_component_version:  %{version}.%{patchlevel}
License:                GPL
Source:                 http://cache.ruby-lang.org/pub/ruby/%{major_version}/ruby-%{version}.tar.gz
Source1:                https://hg.java.net/hg/solaris-userland~gate/raw-file/2062cde74e03/components/ruby/ruby-21/Solaris/rbconfig.sedscript
# Patch0:                 ruby-22-ext-socket-option.patch
Patch1:                 ruby-22-disable-ssl.patch
Url:                     http://www.ruby-lang.org/

BuildRequires: library/text/yaml >= 0.1.6
BuildRequires: system/network/bpf
BuildRequires: system/library/libnet
Requires:      library/text/yaml >= 0.1.6

%description

%prep
# %setup -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}

# %patch0 -p1
%patch1 -p0

%build
%ifarch sparcv9
export CFLAGS='-m64 -xO4 -D__sparc -mt -DFFI_NO_RAW_API -Kpic'
%endif

%ifarch amd64
export CFLAGS='-m64 -xO4 -Ui386 -U__i386 -D__amd64 -xregs=no%frameptr -mt -DFFI_NO_RAW_API'
%endif

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
    --libdir=/usr/ruby/%{major_version}/lib/%{_arch64} \
    --sbindir=/usr/ruby/%{major_version}/sbin \
    --mandir=/usr/ruby/%{major_version}/share/man \
    --enable-dtrace \
    --enable-shared \
    --enable-install-doc \
    --disable-option-checking \
    --with-openssl \
    --with-curses-dir=/usr \
    --disable-install-doc
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT/usr/bin
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
popd

arch=$(./miniruby --version|/usr/bin/sed -e 's/.*\[\(.*\)\].*/\1/')
/usr/bin/sed -e 's/RUBY_VER/%{major_version}/' -e 's/RUBY_LIB_VER/%{unmangled_version}/' < %{SOURCE1} > rbconfig.sed
/usr/bin/sed -f rbconfig.sed < rbconfig.rb > $RPM_BUILD_ROOT/usr/ruby/%{major_version}/lib/%{_arch64}/ruby/%{unmangled_version}/${arch}/rbconfig.rb

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
* Wed Mar 29 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.7
* Tue Mar 07 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add CFLAGS for SPARC
* Mon Dec 05 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use cc instead of gcc
* Thu Nov 17 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.6
* Mon May 02 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.5
* Wed Aug 19 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.3
* Mon Mar 18 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.2
* Tue May 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.1
* Fri Dec 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- add BuildRequires
