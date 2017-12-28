%define version 2.3.5
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
Source: 		https://cache.ruby-lang.org/pub/ruby/%{major_version}/ruby-%{version}.tar.bz2
Source1:		https://hg.java.net/hg/solaris-userland~gate/raw-file/2062cde74e03/components/ruby/ruby-21/Solaris/rbconfig.sedscript
Patch0:                 ruby-23-disable-ssl.patch
Url:			 http://www.ruby-lang.org/

BuildRequires: library/text/yaml >= 0.1.6
BuildRequires: system/network/bpf
BuildRequires: system/library/libnet
Requires:      library/text/yaml >= 0.1.6

%description

%prep
# %setup -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}

%patch0 -p0

%build
%ifarch sparcv9
export CFLAGS='-m64 -xO4 -D__sparc -mt -DFFI_NO_RAW_API -Kpic'
export LIBDIR="/usr/ruby/%{major_version}/lib/sparcv9"
%endif

%ifarch amd64
export CFLAGS='-m64 -xO4 -Ui386 -U__i386 -D__amd64 -xregs=no%frameptr -mt -DFFI_NO_RAW_API'
export LIBDIR="/usr/ruby/%{major_version}/lib/amd64"
%endif

export LDFLAGS="-m64 -L${LIBDIR} -R${LIBDIR}"

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

./configure \
    --prefix=/usr/ruby/%{major_version} \
    --bindir=/usr/ruby/%{major_version}/bin \
    --sbindir=/usr/ruby/%{major_version}/sbin \
    --libdir=${LIBDIR} \
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
pushd $RPM_BUILD_ROOT/usr/bin
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
popd


arch=$(./miniruby --version|/usr/bin/sed -e 's/.*\[\(.*\)\].*/\1/')
/usr/bin/sed -e 's/RUBY_VER/%{major_version}/' -e 's/RUBY_LIB_VER/%{unmangled_version}/' < %{SOURCE1} > rbconfig.sed
/usr/bin/sed -f rbconfig.sed < rbconfig.rb > $RPM_BUILD_ROOT/usr/ruby/%{major_version}/lib/ruby/%{unmangled_version}/${arch}/rbconfig.rb

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
* Wed Sep 20 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix libdir and add LDFLAGS
* Fri Sep 15 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.5
* Fri Mar 31 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.4
* Tue Mar 07 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add CFLAGS for SPARC
* Wed Nov 23 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.3
* Thu Nov 17 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.2
* Mon May 02 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.1
* Sun Dec 27 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.3.0
* Sun Dec 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to preview2
* Mon Dec 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- gcc is not required to build because of compiling with SolarisStudio
- delete commentouted CFLAGS and LDFLAGS
- modify rbconifg.rb to build gem which builds native modules with premise to use GCC (CFLAGS includes '-Wall' etc.)
- replace 'RUBY_VER' and 'RUBY_LIB_VER' in SOURCE1
* Tue Dec 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
