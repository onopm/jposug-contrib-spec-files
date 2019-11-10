%define version 5.26.3
%define major_version 5.26
%define version_suffix 526jposug
%define patchlevel 0

%define jposug_prefix /opt/jposug
%define prefix %{jposug_prefix}/perl5/%{major_version}
%define bindir %{prefix}/bin
%define libdir %{prefix}/lib
%define site_dir %{jposug_prefix}/perl5/site_perl/%{major_version}
%define vendor_dir %{jposug_prefix}/perl5/vendor_perl/%{major_version}

Name:                   SFEperl-%{version_suffix}
IPS_Package_Name:       jposug/runtime/perl-%{version_suffix}
Summary:                Perl 5 is a highly capable, feature-rich programming language
Version:                %{version}
Release:                %{patchlevel}
IPS_component_version:  %{version}.%{patchlevel}
License:                GPL
Source:                 https://www.cpan.org/src/5.0/perl-%{version}.tar.gz
Url:                    https://www.perl.org/

%description
Perl 5 is a highly capable, feature-rich programming language with over 30 years of development.

%prep
%setup -n perl-%{version}

%build
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi


export CFLAGS='-m64 -xO4 -KPIC'

./Configure -de \
-Ulocincpth= \
-Dbin=%{bindir} \
-Dcc="${CC}" \
-Dcf_by="perl-bugs" \
-Dlibperl=libperl.so \
-Dmyhostname="localhost" \
-Dperl_static_inline="static" \
-Dprefix=%{prefix} \
-Dprivlib=%{libdir} \
-Dsitelib=%{site_dir} \
-Dsiteprefix=%{prefix} \
-Dvendorlib=%{vendor_dir} \
-Dvendorprefix=%{prefix} \
-Duseshrplib \
-Dusedtrace \
-Duse64bitall \
-Dusethreads \
-Dlibpth="/lib/64 /usr/lib/64" \
-Doptimize="${CFLAGS}"

make -j$CPUS
make -j$CPUS test

%install
[ -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
/opt/jposug/perl5

%changelog
* Fri Oct 18 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
* bump to 5.26.3
* Wed May 16 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
