%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name HTML-FillInForm-Lite
%define sfe_cpan_name html-fillinform-lite
%define ips_cpan_name html-fillinform-lite

Summary:               Lightweight FillInForm module in Pure Perl
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               1.13
IPS_component_version: 1.13
License:               perl_5
URL:                   https://metacpan.org/pod/HTML::FillInForm::Lite
Source0:               http://cpan.metacpan.org/authors/id/G/GF/GFUJI/HTML-FillInForm-Lite-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Lightweight FillInForm module in Pure Perl

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          Lightweight FillInForm module in Pure Perl
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cgi-584
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/module-build-584
BuildRequires:    library/perl-5/test-simple-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}

%description 584
Lightweight FillInForm module in Pure Perl
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Lightweight FillInForm module in Pure Perl
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/cgi-510
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/module-build-510
BuildRequires:    library/perl-5/test-simple-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}

%description 510
Lightweight FillInForm module in Pure Perl
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          Lightweight FillInForm module in Pure Perl
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cgi-512
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/module-build-512
BuildRequires:    library/perl-5/test-simple-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}

%description 512
Lightweight FillInForm module in Pure Perl
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          Lightweight FillInForm module in Pure Perl
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cgi-516
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/module-build-516
BuildRequires:    library/perl-5/test-simple-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}

%description 516
Lightweight FillInForm module in Pure Perl
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          Lightweight FillInForm module in Pure Perl
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/cgi-520
BuildRequires:    library/perl-5/cpan-meta-520
BuildRequires:    library/perl-5/extutils-makemaker-520
BuildRequires:    library/perl-5/module-build-520
BuildRequires:    library/perl-5/test-simple-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}

%description 520
Lightweight FillInForm module in Pure Perl
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
        rmdir $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
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
* Fri Nov 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.13 and build packages for perl-510, perl-516 and perl-520
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
