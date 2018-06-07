%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name Test-MockObject
%define sfe_cpan_name test-mockobject
%define ips_cpan_name test-mockobject

Summary:               Perl extension for emulating troublesome interfaces
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               1.20150527
IPS_component_version: 1.20150527
License:               perl_5
URL:                   https://metacpan.org/pod/Test::MockObject
Source0:               http://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/Test-MockObject-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Perl extension for emulating troublesome interfaces

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          Perl extension for emulating troublesome interfaces
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cgi-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/base-584
BuildRequires:    library/perl-5/test-exception-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/test-warn-584
BuildRequires:    library/perl-5/universal-can-584
BuildRequires:    library/perl-5/universal-isa-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-584
Requires:         library/perl-5/constant-584
Requires:         library/perl-5/scalar-list-utils-584
Requires:         library/perl-5/test-simple-584
Requires:         library/perl-5/universal-can-584
Requires:         library/perl-5/universal-isa-584

%description 584
Perl extension for emulating troublesome interfaces
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Perl extension for emulating troublesome interfaces
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/cgi-510
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/base-510
BuildRequires:    library/perl-5/test-exception-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/test-warn-510
BuildRequires:    library/perl-5/universal-can-510
BuildRequires:    library/perl-5/universal-isa-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-510
Requires:         library/perl-5/constant-510
Requires:         library/perl-5/scalar-list-utils-510
Requires:         library/perl-5/test-simple-510
Requires:         library/perl-5/universal-can-510
Requires:         library/perl-5/universal-isa-510

%description 510
Perl extension for emulating troublesome interfaces
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          Perl extension for emulating troublesome interfaces
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cgi-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/base-512
BuildRequires:    library/perl-5/test-exception-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/test-warn-512
BuildRequires:    library/perl-5/universal-can-512
BuildRequires:    library/perl-5/universal-isa-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-512
Requires:         library/perl-5/constant-512
Requires:         library/perl-5/scalar-list-utils-512
Requires:         library/perl-5/test-simple-512
Requires:         library/perl-5/universal-can-512
Requires:         library/perl-5/universal-isa-512

%description 512
Perl extension for emulating troublesome interfaces
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          Perl extension for emulating troublesome interfaces
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cgi-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/base-516
BuildRequires:    library/perl-5/test-exception-516
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/test-warn-516
BuildRequires:    library/perl-5/universal-can-516
BuildRequires:    library/perl-5/universal-isa-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-516
Requires:         library/perl-5/constant-516
Requires:         library/perl-5/scalar-list-utils-516
Requires:         library/perl-5/test-simple-516
Requires:         library/perl-5/universal-can-516
Requires:         library/perl-5/universal-isa-516

%description 516
Perl extension for emulating troublesome interfaces
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          Perl extension for emulating troublesome interfaces
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/cgi-520
BuildRequires:    library/perl-5/extutils-makemaker-520
BuildRequires:    library/perl-5/base-520
BuildRequires:    library/perl-5/test-exception-520
BuildRequires:    library/perl-5/test-simple-520
BuildRequires:    library/perl-5/test-warn-520
BuildRequires:    library/perl-5/universal-can-520
BuildRequires:    library/perl-5/universal-isa-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-520
Requires:         library/perl-5/constant-520
Requires:         library/perl-5/scalar-list-utils-520
Requires:         library/perl-5/test-simple-520
Requires:         library/perl-5/universal-can-520
Requires:         library/perl-5/universal-isa-520

%description 520
Perl extension for emulating troublesome interfaces
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
* Sun Dec 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.20150527
* Sat Dec 23 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sun Jun 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
