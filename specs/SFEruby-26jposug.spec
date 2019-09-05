%define version 2.6.4
%define major_version 2.6
%define unmangled_version 2.6.0
%define version_suffix 26jposug
%define patchlevel 0

%define jposug_prefix /opt/jposug
%define prefix %{jposug_prefix}/ruby/%{major_version}
%define bindir %{prefix}/bin
%define sbindir %{prefix}/sbin
%define libdir %{prefix}/lib
%define mandir %{prefix}/share/man
%define rubylib_prefix %{prefix}/lib/ruby

Name:                   SFEruby-%{version_suffix}
IPS_Package_Name:       jposug/runtime/ruby-%{version_suffix}
Summary:                An interpreter of object-oriented scripting language
Version:                %{version}
Release:                %{patchlevel}
IPS_component_version:  %{version}.%{patchlevel}
License:                2-clause BSDL
Source:                 https://cache.ruby-lang.org/pub/ruby/%{major_version}/ruby-%{version}.tar.xz
Source1:                rbconfig.sedscript.ruby26
Url:                    http://www.ruby-lang.org/


BuildRequires: jposug/library/text/yaml >= 0.1.7
BuildRequires: system/network/bpf
BuildRequires: system/library/libnet
Requires:      jposug/library/text/yaml >= 0.1.7
Requires:      jposug/library/ruby/bundler-26jposug

%description

%prep
# %setup -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}

%build
export CC=/usr/bin/gcc
%ifarch sparcv9
# export CFLAGS='-m64 -xO4 -D__sparc -mt -DFFI_NO_RAW_API -Kpic'
export CFLAGS='-m64 -g -O3 -fPIC -std=gnu99 -D__sparc'
%endif

%ifarch amd64
# export CFLAGS='-m64 -xO4 -Ui386 -U__i386 -D__amd64 -xregs=no%frameptr -mt -DFFI_NO_RAW_API'
export CFLAGS='-m64 -g -O3 -fPIC -std=gnu99 -Ui386 -U__i386 -D__amd64'
%endif

export LIBDIR=%{libdir}
export LDFLAGS="-m64 -L/opt/jposug/lib -L${LIBDIR} -R/opt/jposug/lib -R${LIBDIR}"
export PKG_CONFIG_PATH=/opt/jposug/lib/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
./configure \
    --prefix=%{prefix} \
    --bindir=%{bindir} \
    --sbindir=%{sbindir} \
    --libdir=%{libdir} \
    --mandir=%{mandir} \
    --with-rubylibprefix=%{rubylib_prefix} \
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
ln -s ../..%{bindir}/erb .
ln -s ../..%{bindir}/gem .
ln -s ../..%{bindir}/irb .
ln -s ../..%{bindir}/rake .
ln -s ../..%{bindir}/rdoc .
ln -s ../..%{bindir}/ri .
ln -s ../..%{bindir}/ruby .

ln -s ../..%{bindir}/erb erb%{version_suffix}
ln -s ../..%{bindir}/gem gem%{version_suffix}
ln -s ../..%{bindir}/irb irb%{version_suffix}
ln -s ../..%{bindir}/rake rake%{version_suffix}
ln -s ../..%{bindir}/rdoc rdoc%{version_suffix}
ln -s ../..%{bindir}/ri ri%{version_suffix}
ln -s ../..%{bindir}/ruby ruby%{version_suffix}
popd


arch=$(./miniruby --version|/usr/bin/sed -e 's/.*\[\(.*\)\].*/\1/')
/usr/bin/sed -e 's/RUBY_VER/%{major_version}/' \
    -e 's/RUBY_LIB_VER/%{unmangled_version}/' < %{SOURCE1} > rbconfig.sed
/usr/bin/sed -f rbconfig.sed < rbconfig.rb > $RPM_BUILD_ROOT%{libdir}/ruby/%{unmangled_version}/${arch}/rbconfig.rb


# bundler: use gem
rm $RPM_BUILD_ROOT/%{bindir}/bundle
# rm $RPM_BUILD_ROOT/%{bindir}/bundle_ruby
rm $RPM_BUILD_ROOT/%{bindir}/bundler
rm -r $RPM_BUILD_ROOT/opt/jposug/ruby/2.6/lib/ruby/2.6.0/bundler

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%ips_tag (mediator=ruby mediator-version=%{major_version} mediator-implementation=jposug)  /usr/bin/erb
%ips_tag (mediator=ruby mediator-version=%{major_version} mediator-implementation=jposug)  /usr/bin/gem
%ips_tag (mediator=ruby mediator-version=%{major_version} mediator-implementation=jposug)  /usr/bin/irb
%ips_tag (mediator=ruby mediator-version=%{major_version} mediator-implementation=jposug)  /usr/bin/rake
%ips_tag (mediator=ruby mediator-version=%{major_version} mediator-implementation=jposug)  /usr/bin/rdoc
%ips_tag (mediator=ruby mediator-version=%{major_version} mediator-implementation=jposug)  /usr/bin/ri
%ips_tag (mediator=ruby mediator-version=%{major_version} mediator-implementation=jposug)  /usr/bin/ruby
/usr/bin/*%{version_suffix}
%{prefix}

%changelog
* Thu Sep 05 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.6.4
* Fri Apr 19 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.6.3
* Thu Mar 14 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.6.2
* Fri Feb 08 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix source1
- initial commit
