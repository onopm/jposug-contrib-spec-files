%include Solaris.inc

%define build584 0
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name Module-Build
%define sfe_cpan_name module-build

Summary:               Build and install Perl modules
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               0.4214
IPS_component_version: 0.4214
License:               perl_5
URL:                   https://metacpan.org/pod/Module::Build
Source0:               http://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Build and install Perl modules

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/cpan-meta-yaml-584
BuildRequires:    library/perl-5/file-temp-584
BuildRequires:    library/perl-5/module-metadata-584
BuildRequires:    library/perl-5/parse-cpan-meta-584
BuildRequires:    library/perl-5/perl-ostype-584
BuildRequires:    library/perl-5/test-harness-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/version-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/cpan-meta-584
Requires:         library/perl-5/data-dumper-584
Requires:         library/perl-5/extutils-cbuilder-584
Requires:         library/perl-5/extutils-install-584
Requires:         library/perl-5/extutils-manifest-584
Requires:         library/perl-5/extutils-mkbootstrap-584
Requires:         library/perl-5/extutils-parsexs-584
Requires:         library/perl-5/file-path-584
Requires:         library/perl-5/getopt-long-584
Requires:         library/perl-5/module-metadata-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/perl-ostype-584
Requires:         library/perl-5/podlators-584
Requires:         library/perl-5/test-harness-584
Requires:         library/perl-5/text-abbrev-584
Requires:         library/perl-5/text-parsewords-584
Requires:         library/perl-5/version-584

%description 584
Build and install Perl modules
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/cpan-meta-yaml-512
BuildRequires:    library/perl-5/file-temp-512
BuildRequires:    library/perl-5/module-metadata-512
BuildRequires:    library/perl-5/parse-cpan-meta-512
BuildRequires:    library/perl-5/perl-ostype-512
BuildRequires:    library/perl-5/test-harness-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/version-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/cpan-meta-512
Requires:         library/perl-5/data-dumper-512
Requires:         library/perl-5/extutils-cbuilder-512
Requires:         library/perl-5/extutils-install-512
Requires:         library/perl-5/extutils-manifest-512
Requires:         library/perl-5/extutils-mkbootstrap-512
Requires:         library/perl-5/extutils-parsexs-512
Requires:         library/perl-5/file-path-512
Requires:         library/perl-5/getopt-long-512
Requires:         library/perl-5/module-metadata-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/perl-ostype-512
Requires:         library/perl-5/podlators-512
Requires:         library/perl-5/test-harness-512
Requires:         library/perl-5/text-abbrev-512
Requires:         library/perl-5/text-parsewords-512
Requires:         library/perl-5/version-512

%description 512
Build and install Perl modules
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/cpan-meta-yaml-516
BuildRequires:    library/perl-5/file-temp-516
BuildRequires:    library/perl-5/module-metadata-516
BuildRequires:    library/perl-5/parse-cpan-meta-516
BuildRequires:    library/perl-5/perl-ostype-516
BuildRequires:    library/perl-5/test-harness-516
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/version-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/cpan-meta-516
Requires:         library/perl-5/data-dumper-516
Requires:         library/perl-5/extutils-cbuilder-516
Requires:         library/perl-5/extutils-install-516
Requires:         library/perl-5/extutils-manifest-516
Requires:         library/perl-5/extutils-mkbootstrap-516
Requires:         library/perl-5/extutils-parsexs-516
Requires:         library/perl-5/file-path-516
Requires:         library/perl-5/getopt-long-516
Requires:         library/perl-5/module-metadata-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/perl-ostype-516
Requires:         library/perl-5/podlators-516
Requires:         library/perl-5/test-harness-516
Requires:         library/perl-5/text-abbrev-516
Requires:         library/perl-5/text-parsewords-516
Requires:         library/perl-5/version-516

%description 516
Build and install Perl modules
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/cpan-meta-520
BuildRequires:    library/perl-5/cpan-meta-yaml-520
BuildRequires:    library/perl-5/file-temp-520
BuildRequires:    library/perl-5/module-metadata-520
BuildRequires:    library/perl-5/parse-cpan-meta-520
BuildRequires:    library/perl-5/perl-ostype-520
BuildRequires:    library/perl-5/test-harness-520
BuildRequires:    library/perl-5/test-simple-520
BuildRequires:    library/perl-5/version-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/cpan-meta-520
Requires:         library/perl-5/data-dumper-520
Requires:         library/perl-5/extutils-cbuilder-520
Requires:         library/perl-5/extutils-install-520
Requires:         library/perl-5/extutils-manifest-520
Requires:         library/perl-5/extutils-mkbootstrap-520
Requires:         library/perl-5/extutils-parsexs-520
Requires:         library/perl-5/file-path-520
Requires:         library/perl-5/getopt-long-520
Requires:         library/perl-5/module-metadata-520
Requires:         library/perl-5/pathtools-520
Requires:         library/perl-5/perl-ostype-520
Requires:         library/perl-5/podlators-520
Requires:         library/perl-5/test-harness-520
Requires:         library/perl-5/text-abbrev-520
Requires:         library/perl-5/text-parsewords-520
Requires:         library/perl-5/version-520

%description 520
Build and install Perl modules
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

# perl includes binary
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

  if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man ]
  then
      if [ -d $RPM_BUILD_ROOT%{_datadir} ]
      then
          rm -rf $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man
      else
          mkdir -p $RPM_BUILD_ROOT%{_datadir}
          mv $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man $RPM_BUILD_ROOT%{_datadir}
      fi
  fi
  rmdir $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
}

# To build without test, pass 'without_test' to build_for commaond.
# like 'build_for version without_test'
%if %{build584}
build_for 5.8.4
%endif

%if %{build512}
build_for 5.12 without_test
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
* Tue Nov 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4214 and build packages for perl-516 and perl-520
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Tue Jun 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-584
* Wed Jun 13 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- exclude executable files whitch conflict with perl-512
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify %attr
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use Build.PL instead of Makefile.PL
- stop to generate package for perl-584
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
