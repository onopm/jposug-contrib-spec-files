%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 1

%define cpan_name Kossy
%define sfe_cpan_name kossy
%define ips_cpan_name kossy

Summary:               Sinatra-ish Simple and Clear web application framework
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               0.38
IPS_component_version: 0.38
License:               perl_5
URL:                   https://metacpan.org/pod/Kossy
Source0:               http://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Kossy-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Sinatra-ish Simple and Clear web application framework

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          Sinatra-ish Simple and Clear web application framework
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/module-build-tiny-584
BuildRequires:    library/perl-5/test-simple-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/class-accessor-lite-584
Requires:         library/perl-5/cookie-baker-584
Requires:         library/perl-5/cookie-baker-xs-584
Requires:         library/perl-5/data-section-simple-584
Requires:         library/perl-5/file-sharedir-584
Requires:         library/perl-5/hash-multivalue-584
Requires:         library/perl-5/html-fillinform-lite-584
Requires:         library/perl-5/http-entity-parser-584
Requires:         library/perl-5/http-headers-fast-584
Requires:         library/perl-5/http-message-584
Requires:         library/perl-5/json-584
Requires:         library/perl-5/kossy-validator-584
Requires:         library/perl-5/number-format-584
Requires:         library/perl-5/parent-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/plack-584
Requires:         library/perl-5/plack-middleware-reverseproxy-584
Requires:         library/perl-5/router-boom-584
Requires:         library/perl-5/scalar-list-utils-584
Requires:         library/perl-5/test-simple-584
Requires:         library/perl-5/text-xslate-584
Requires:         library/perl-5/text-xslate-bridge-tt2like-584
Requires:         library/perl-5/try-tiny-584
Requires:         library/perl-5/www-form-urlencoded-584
Requires:         library/perl-5/www-form-urlencoded-xs-584

%description 584
Sinatra-ish Simple and Clear web application framework
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Sinatra-ish Simple and Clear web application framework
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/module-build-tiny-510
BuildRequires:    library/perl-5/test-simple-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/class-accessor-lite-510
Requires:         library/perl-5/cookie-baker-510
Requires:         library/perl-5/cookie-baker-xs-510
Requires:         library/perl-5/data-section-simple-510
Requires:         library/perl-5/file-sharedir-510
Requires:         library/perl-5/hash-multivalue-510
Requires:         library/perl-5/html-fillinform-lite-510
Requires:         library/perl-5/http-entity-parser-510
Requires:         library/perl-5/http-headers-fast-510
Requires:         library/perl-5/http-message-510
Requires:         library/perl-5/json-510
Requires:         library/perl-5/kossy-validator-510
Requires:         library/perl-5/number-format-510
Requires:         library/perl-5/parent-510
Requires:         library/perl-5/pathtools-510
Requires:         library/perl-5/plack-510
Requires:         library/perl-5/plack-middleware-reverseproxy-510
Requires:         library/perl-5/router-boom-510
Requires:         library/perl-5/scalar-list-utils-510
Requires:         library/perl-5/test-simple-510
Requires:         library/perl-5/text-xslate-510
Requires:         library/perl-5/text-xslate-bridge-tt2like-510
Requires:         library/perl-5/try-tiny-510
Requires:         library/perl-5/www-form-urlencoded-510
Requires:         library/perl-5/www-form-urlencoded-xs-510

%description 510
Sinatra-ish Simple and Clear web application framework
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          Sinatra-ish Simple and Clear web application framework
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/module-build-tiny-512
BuildRequires:    library/perl-5/test-simple-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/class-accessor-lite-512
Requires:         library/perl-5/cookie-baker-512
Requires:         library/perl-5/cookie-baker-xs-512
Requires:         library/perl-5/data-section-simple-512
Requires:         library/perl-5/file-sharedir-512
Requires:         library/perl-5/hash-multivalue-512
Requires:         library/perl-5/html-fillinform-lite-512
Requires:         library/perl-5/http-entity-parser-512
Requires:         library/perl-5/http-headers-fast-512
Requires:         library/perl-5/http-message-512
Requires:         library/perl-5/json-512
Requires:         library/perl-5/kossy-validator-512
Requires:         library/perl-5/number-format-512
Requires:         library/perl-5/parent-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/plack-512
Requires:         library/perl-5/plack-middleware-reverseproxy-512
Requires:         library/perl-5/router-boom-512
Requires:         library/perl-5/scalar-list-utils-512
Requires:         library/perl-5/test-simple-512
Requires:         library/perl-5/text-xslate-512
Requires:         library/perl-5/text-xslate-bridge-tt2like-512
Requires:         library/perl-5/try-tiny-512
Requires:         library/perl-5/www-form-urlencoded-512
Requires:         library/perl-5/www-form-urlencoded-xs-512

%description 512
Sinatra-ish Simple and Clear web application framework
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          Sinatra-ish Simple and Clear web application framework
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/module-build-tiny-516
BuildRequires:    library/perl-5/test-simple-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/class-accessor-lite-516
Requires:         library/perl-5/cookie-baker-516
Requires:         library/perl-5/cookie-baker-xs-516
Requires:         library/perl-5/data-section-simple-516
Requires:         library/perl-5/file-sharedir-516
Requires:         library/perl-5/hash-multivalue-516
Requires:         library/perl-5/html-fillinform-lite-516
Requires:         library/perl-5/http-entity-parser-516
Requires:         library/perl-5/http-headers-fast-516
Requires:         library/perl-5/http-message-516
Requires:         library/perl-5/json-516
Requires:         library/perl-5/kossy-validator-516
Requires:         library/perl-5/number-format-516
Requires:         library/perl-5/parent-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/plack-516
Requires:         library/perl-5/plack-middleware-reverseproxy-516
Requires:         library/perl-5/router-boom-516
Requires:         library/perl-5/scalar-list-utils-516
Requires:         library/perl-5/test-simple-516
Requires:         library/perl-5/text-xslate-516
Requires:         library/perl-5/text-xslate-bridge-tt2like-516
Requires:         library/perl-5/try-tiny-516
Requires:         library/perl-5/www-form-urlencoded-516
Requires:         library/perl-5/www-form-urlencoded-xs-516

%description 516
Sinatra-ish Simple and Clear web application framework
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          Sinatra-ish Simple and Clear web application framework
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/module-build-tiny-520
BuildRequires:    library/perl-5/test-simple-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/class-accessor-lite-520
Requires:         library/perl-5/cookie-baker-520
Requires:         library/perl-5/cookie-baker-xs-520
Requires:         library/perl-5/data-section-simple-520
Requires:         library/perl-5/file-sharedir-520
Requires:         library/perl-5/hash-multivalue-520
Requires:         library/perl-5/html-fillinform-lite-520
Requires:         library/perl-5/http-entity-parser-520
Requires:         library/perl-5/http-headers-fast-520
Requires:         library/perl-5/http-message-520
Requires:         library/perl-5/json-520
Requires:         library/perl-5/kossy-validator-520
Requires:         library/perl-5/number-format-520
Requires:         library/perl-5/parent-520
Requires:         library/perl-5/pathtools-520
Requires:         library/perl-5/plack-520
Requires:         library/perl-5/plack-middleware-reverseproxy-520
Requires:         library/perl-5/router-boom-520
Requires:         library/perl-5/scalar-list-utils-520
Requires:         library/perl-5/test-simple-520
Requires:         library/perl-5/text-xslate-520
Requires:         library/perl-5/text-xslate-bridge-tt2like-520
Requires:         library/perl-5/try-tiny-520
Requires:         library/perl-5/www-form-urlencoded-520
Requires:         library/perl-5/www-form-urlencoded-xs-520

%description 520
Sinatra-ish Simple and Clear web application framework
%endif


%prep
%setup -q -n %{cpan_name}-%{version}
rm -rf %{buildroot}

%build
build_with_makefile.pl_for() {
    perl_ver=$1
    test=$2
    bindir="/usr/perl5/${perl_ver}/bin"
    vendor_dir="/usr/perl5/vendor_perl/${perl_ver}"

    export PERL5LIB=${vendor_dir}
    ${bindir}/perl Makefile.PL PREFIX=%{_prefix} \
                   DESTDIR=$RPM_BUILD_ROOT \
                   LIB=${vendor_dir}
    make
    [ x${test} = 'xwithout_test' ] || make test
    make pure_install
}

build_with_build.pl_for() {
    perl_ver=$1
    test=$2
    bindir="/usr/perl5/${perl_ver}/bin"
    vendor_dir="/usr/perl5/vendor_perl/${perl_ver}"

    export PERL5LIB=${vendor_dir}
    ${bindir}/perl Build.PL \
                   --installdirs vendor \
                   --destdir $RPM_BUILD_ROOT
    ${bindir}/perl ./Build
    [ x${test} = 'xwithout_test' ] || ${bindir}/perl ./Build test
    ${bindir}/perl ./Build install --destdir $RPM_BUILD_ROOT
    ${bindir}/perl ./Build clean
}

modify_bin_dir() {
    perl_ver=$1
    if [ -d $RPM_BUILD_ROOT/usr/bin ]
    then
      [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver} ] || mkdir -p $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
      mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin
    fi
      
    if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin ]
    then
        for i in $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin/*
        do
            sed -i.bak -e "s/\/usr\/bin\/env ruby/\/usr\/perl5\/${perl-ver}\/bin\/ruby/" ${i}
            [ -f ${i}.bak] || rm -f ${i}.bak
        done
    fi
}

modify_man_dir() {
    perl_ver=$1
    if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man ]
    then
        if [ -d $RPM_BUILD_ROOT%{_datadir}/man ]
        then
            rm -rf $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man
        else
            mkdir -p $RPM_BUILD_ROOT%{_datadir}
            mv $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man $RPM_BUILD_ROOT%{_datadir}/
            rm -rf $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man
        fi
        if [ %{include_executable} -eq 0 ]
        then
            rmdir $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
        fi
    fi
}

build_for() {
  if [ -f Build.PL ];
  then
    build_with_build.pl_for $*
  elif [ -f Makefile.PL ];
  then
    build_with_makefile.pl_for $*
  fi

  modify_bin_dir $*
  modify_man_dir $*
}

# To build without test, pass 'without_test' to build_for commaond.
# like 'build_for version without_test'
%if %{build584}
build_for 5.8.4
%endif

%if %{build510}
build_for 5.10
%endif

%if %{build512}
build_for 5.12
%endif

%if %{build516}
build_for 5.16
%endif

%if %{build520}
build_for 5.20
%endif

%install
if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]
then
    mkdir -p $RPM_BUILD_ROOT%{_datadir}
    mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
fi
if [ -d $RPM_BUILD_ROOT%{_datadir}/man/man3 ]
then
    mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl
fi

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%{_datadir}/man

%if %{build584}
%files 584
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.8.4
%if %{include_executable}
/usr/perl5/5.8.4
%endif
%endif

%if %{build510}
%files 510
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.10
%if %{include_executable}
/usr/perl5/5.1.0
%endif
%endif

%if %{build512}
%files 512
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.12
%if %{include_executable}
/usr/perl5/5.12
%endif
%endif

%if %{build516}
%files 516
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.16
%if %{include_executable}
/usr/perl5/5.16
%endif
%endif

%if %{build520}
%files 520
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.20
%if %{include_executable}
/usr/perl5/5.20
%endif
%endif


%changelog
* Sat Nov 14 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.38 and build packages for perl-510, perl-516 and perl-520
* Thu Nov 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Mon Feb 11 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
- bump to 0.13
* Sun Feb 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Thu Jun 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 0.10
* Sat Jun 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
