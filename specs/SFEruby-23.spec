%define version 2.3.0
%define major_version 2.3
%define unmangled_version 2.3.0
%define version_suffix 23
%define patchlevel 0

Name:			SFEruby-23
IPS_Package_Name:	runtime/ruby-23
Summary:		An interpreter of object-oriented scripting language
Version:		%{version}
Release:		%{patchlevel}
IPS_component_version:	%{version}.%{patchlevel}
License: 		GPL
Source: 		https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.0-preview1.tar.bz2
Patch0:                 ruby-23-disable-ssl.patch
Url:			 http://www.ruby-lang.org/

BuildRequires: library/text/yaml >= 0.1.6
BuildRequires: system/network/bpf
BuildRequires: system/library/libnet
Requires:      library/text/yaml >= 0.1.6

%description

%prep
# %setup -n ruby-%{version}-p%{patchlevel}
# %setup -n ruby-%{version}
%setup -n ruby-%{version}-preview1

%patch0 -p0

%build
export CFLAGS='-m64 -xO4 -Ui386 -U__i386 -D__amd64 -xregs=no%frameptr    -mt -DFFI_NO_RAW_API' 
# export CPPFLAGS="-m64 -D_POSIX_PTHREAD_SEMANTICS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I../CPPFLAGSTEST"
# export LDFLAGS="-m64 -L/lib/%{_arch64} -L/usr/lib/%{_arch64} -R/lib/%{_arch64} -R/usr/lib/%{_arch64}"

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
./configure \
    --prefix=/usr/ruby/%{major_version} \
    --bindir=/usr/ruby/%{major_version}/bin \
    --sbindir=/usr/ruby/%{major_version}/sbin \
    --libdir=/usr/ruby/%{major_version}/lib/amd64 \
    --mandir=/usr/ruby/%{major_version}/share/man \
    --with-rubylibprefix=/usr/ruby/%{major_version}/lib/ruby \
    --enable-dtrace \
    --enable-shared \
    --disable-install-doc \
    --with-openssl \
    --with-curses-dir=/usr \
    --with-setjmp-type=_setjmp \
    --with-tclConfig-file=/usr/lib/64/tclConfig.sh
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

ln -s ../ruby/%{major_version}/bin/erb erb%{version_suffix}
ln -s ../ruby/%{major_version}/bin/gem gem%{version_suffix}
ln -s ../ruby/%{major_version}/bin/irb irb%{version_suffix}
ln -s ../ruby/%{major_version}/bin/rake rake%{version_suffix}
ln -s ../ruby/%{major_version}/bin/rdoc rdoc%{version_suffix}
ln -s ../ruby/%{major_version}/bin/ri ri%{version_suffix}
ln -s ../ruby/%{major_version}/bin/ruby ruby%{version_suffix}

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
/usr/bin/*%{version_suffix}
/usr/ruby/%{major_version}

%changelog
* Mon Dec 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- gcc is not required to build because of compiling with SolarisStudio
* Tue Dec 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
