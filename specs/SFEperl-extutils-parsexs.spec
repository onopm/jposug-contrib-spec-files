%include Solaris.inc

%define build584 0
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name ExtUtils-ParseXS
%define sfe_cpan_name extutils-parsexs

Summary:               converts Perl XS code into C code
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               3.30
IPS_component_version: 3.30
License:               unknown
URL:                   https://metacpan.org/pod/ExtUtils::ParseXS
Source0:               http://cpan.metacpan.org/authors/id/S/SM/SMUELLER/ExtUtils-ParseXS-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
converts Perl XS code into C code

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          converts Perl XS code into C code
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/extutils-makemaker-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/carp-584
Requires:         library/perl-5/dynaloader-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/extutils-cbuilder-584
Requires:         library/perl-5/extutils-makemaker-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/symbol-584
Requires:         library/perl-5/test-simple-584

%description 584
converts Perl XS code into C code
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          converts Perl XS code into C code
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/extutils-makemaker-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/carp-512
Requires:         library/perl-5/dynaloader-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/extutils-cbuilder-512
Requires:         library/perl-5/extutils-makemaker-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/symbol-512
Requires:         library/perl-5/test-simple-512

%description 512
converts Perl XS code into C code
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          converts Perl XS code into C code
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/extutils-makemaker-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/carp-516
Requires:         library/perl-5/dynaloader-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/extutils-cbuilder-516
Requires:         library/perl-5/extutils-makemaker-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/symbol-516
Requires:         library/perl-5/test-simple-516

%description 516
converts Perl XS code into C code
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          converts Perl XS code into C code
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/extutils-makemaker-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/carp-520
Requires:         library/perl-5/dynaloader-520
Requires:         library/perl-5/exporter-520
Requires:         library/perl-5/extutils-cbuilder-520
Requires:         library/perl-5/extutils-makemaker-520
Requires:         library/perl-5/pathtools-520
Requires:         library/perl-5/symbol-520
Requires:         library/perl-5/test-simple-520

%description 520
converts Perl XS code into C code
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
    [ ${test} = 'without_test' ] || make test
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
    [ ${test} = 'without_test' ] || ${bindir}/perl ./Build test
    ${bindir}/perl ./Build install --destdir $RPM_BUILD_ROOT
}

modify_bin_dir() {
  perl_ver=$1
  if [ -d $RPM_BUILD_ROOT/usr/bin ]
  then
      rm -rf $RPM_BUILD_ROOT/usr/bin
  fi

  if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin ]
  then
      rm -rf $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin
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
}

# To build without test, pass 'without_test' to build_for commaond.
# like 'build_for version without_test'
%if %{build584}
build_for 5.8.4
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}
if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]
then
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
* Wed Nov 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.30 and build packages for perl-516 and perl-520
* Tue Nov 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.22
* Tue Feb 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequire to %package 584
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
