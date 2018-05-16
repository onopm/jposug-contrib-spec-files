%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)
%define enable_test %( if [ "x${PERL_DISABLE_TEST}" = 'xtrue' ]; then echo '0'; else echo '1'; fi )
%define include_executable 0

%define cpan_name Module-Build
%define sfe_cpan_name module-build
%define ips_cpan_name module-build

Summary:               Build and install Perl modules
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               0.4222
IPS_component_version: 0.4222
License:               perl_5
URL:                   https://metacpan.org/pod/Module::Build
Source0:               http://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Build and install Perl modules

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
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
%if %{enable_test}
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/data-dumper-584
BuildRequires:    library/perl-5/extutils-cbuilder-584
BuildRequires:    library/perl-5/extutils-install-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/extutils-manifest-584
BuildRequires:    library/perl-5/extutils-parsexs-584
BuildRequires:    library/perl-5/file-path-584
BuildRequires:    library/perl-5/getopt-long-584
BuildRequires:    library/perl-5/module-metadata-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/perl-ostype-584
BuildRequires:    library/perl-5/podlators-584
BuildRequires:    library/perl-5/test-harness-584
BuildRequires:    library/perl-5/text-abbrev-584
BuildRequires:    library/perl-5/text-parsewords-584
BuildRequires:    library/perl-5/version-584
%endif
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/cpan-meta-584
Requires:         library/perl-5/data-dumper-584
Requires:         library/perl-5/extutils-cbuilder-584
Requires:         library/perl-5/extutils-install-584
Requires:         library/perl-5/extutils-makemaker-584
Requires:         library/perl-5/extutils-manifest-584
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

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/cpan-meta-yaml-510
BuildRequires:    library/perl-5/file-temp-510
BuildRequires:    library/perl-5/module-metadata-510
BuildRequires:    library/perl-5/parse-cpan-meta-510
BuildRequires:    library/perl-5/perl-ostype-510
BuildRequires:    library/perl-5/test-harness-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/version-510
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/data-dumper-510
BuildRequires:    library/perl-5/extutils-cbuilder-510
BuildRequires:    library/perl-5/extutils-install-510
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/extutils-manifest-510
BuildRequires:    library/perl-5/extutils-parsexs-510
BuildRequires:    library/perl-5/file-path-510
BuildRequires:    library/perl-5/getopt-long-510
BuildRequires:    library/perl-5/module-metadata-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/perl-ostype-510
BuildRequires:    library/perl-5/podlators-510
BuildRequires:    library/perl-5/test-harness-510
BuildRequires:    library/perl-5/text-abbrev-510
BuildRequires:    library/perl-5/text-parsewords-510
BuildRequires:    library/perl-5/version-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/cpan-meta-510
Requires:         library/perl-5/data-dumper-510
Requires:         library/perl-5/extutils-cbuilder-510
Requires:         library/perl-5/extutils-install-510
Requires:         library/perl-5/extutils-makemaker-510
Requires:         library/perl-5/extutils-manifest-510
Requires:         library/perl-5/extutils-parsexs-510
Requires:         library/perl-5/file-path-510
Requires:         library/perl-5/getopt-long-510
Requires:         library/perl-5/module-metadata-510
Requires:         library/perl-5/pathtools-510
Requires:         library/perl-5/perl-ostype-510
Requires:         library/perl-5/podlators-510
Requires:         library/perl-5/test-harness-510
Requires:         library/perl-5/text-abbrev-510
Requires:         library/perl-5/text-parsewords-510
Requires:         library/perl-5/version-510

%description 510
Build and install Perl modules
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
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
%if %{enable_test}
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/data-dumper-512
BuildRequires:    library/perl-5/extutils-cbuilder-512
BuildRequires:    library/perl-5/extutils-install-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/extutils-manifest-512
BuildRequires:    library/perl-5/extutils-parsexs-512
BuildRequires:    library/perl-5/file-path-512
BuildRequires:    library/perl-5/getopt-long-512
BuildRequires:    library/perl-5/module-metadata-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/perl-ostype-512
BuildRequires:    library/perl-5/podlators-512
BuildRequires:    library/perl-5/test-harness-512
BuildRequires:    library/perl-5/text-abbrev-512
BuildRequires:    library/perl-5/text-parsewords-512
BuildRequires:    library/perl-5/version-512
%endif
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/cpan-meta-512
Requires:         library/perl-5/data-dumper-512
Requires:         library/perl-5/extutils-cbuilder-512
Requires:         library/perl-5/extutils-install-512
Requires:         library/perl-5/extutils-makemaker-512
Requires:         library/perl-5/extutils-manifest-512
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
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
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
Requires:         library/perl-5/%{ips_cpan_name}
%if %{enable_test}
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/data-dumper-516
BuildRequires:    library/perl-5/extutils-cbuilder-516
BuildRequires:    library/perl-5/extutils-install-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/extutils-manifest-516
BuildRequires:    library/perl-5/extutils-parsexs-516
BuildRequires:    library/perl-5/file-path-516
BuildRequires:    library/perl-5/getopt-long-516
BuildRequires:    library/perl-5/module-metadata-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/perl-ostype-516
BuildRequires:    library/perl-5/podlators-516
BuildRequires:    library/perl-5/test-harness-516
BuildRequires:    library/perl-5/text-abbrev-516
BuildRequires:    library/perl-5/text-parsewords-516
BuildRequires:    library/perl-5/version-516
%endif
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/cpan-meta-516
Requires:         library/perl-5/data-dumper-516
Requires:         library/perl-5/extutils-cbuilder-516
Requires:         library/perl-5/extutils-install-516
Requires:         library/perl-5/extutils-makemaker-516
Requires:         library/perl-5/extutils-manifest-516
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

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/cpan-meta-yaml-522
BuildRequires:    library/perl-5/file-temp-522
BuildRequires:    library/perl-5/module-metadata-522
BuildRequires:    library/perl-5/parse-cpan-meta-522
BuildRequires:    library/perl-5/perl-ostype-522
BuildRequires:    library/perl-5/test-harness-522
BuildRequires:    library/perl-5/test-simple-522
BuildRequires:    library/perl-5/version-522
%if %{enable_test}
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/data-dumper-522
BuildRequires:    library/perl-5/extutils-cbuilder-522
BuildRequires:    library/perl-5/extutils-install-522
BuildRequires:    library/perl-5/extutils-makemaker-522
BuildRequires:    library/perl-5/extutils-manifest-522
BuildRequires:    library/perl-5/extutils-parsexs-522
BuildRequires:    library/perl-5/file-path-522
BuildRequires:    library/perl-5/getopt-long-522
BuildRequires:    library/perl-5/module-metadata-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/perl-ostype-522
BuildRequires:    library/perl-5/podlators-522
BuildRequires:    library/perl-5/test-harness-522
BuildRequires:    library/perl-5/text-abbrev-522
BuildRequires:    library/perl-5/text-parsewords-522
BuildRequires:    library/perl-5/version-522
%endif
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/cpan-meta-522
Requires:         library/perl-5/data-dumper-522
Requires:         library/perl-5/extutils-cbuilder-522
Requires:         library/perl-5/extutils-install-522
Requires:         library/perl-5/extutils-makemaker-522
Requires:         library/perl-5/extutils-manifest-522
Requires:         library/perl-5/extutils-parsexs-522
Requires:         library/perl-5/file-path-522
Requires:         library/perl-5/getopt-long-522
Requires:         library/perl-5/module-metadata-522
Requires:         library/perl-5/pathtools-522
Requires:         library/perl-5/perl-ostype-522
Requires:         library/perl-5/podlators-522
Requires:         library/perl-5/test-harness-522
Requires:         library/perl-5/text-abbrev-522
Requires:         library/perl-5/text-parsewords-522
Requires:         library/perl-5/version-522

%description 522
Build and install Perl modules
%endif


%prep
%setup -q -n %{cpan_name}-%{version}
[ -d %{buildroot} ] && rm -rf %{buildroot}

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

    export CC='cc -m32'
    export LD='cc -m32'
    echo ${perl_ver} | egrep '5\.(84|12)' > /dev/null || (export CC='cc -m64'; export LD='cc -m64')
    make CC="${CC}" LD="${LD}"
    [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || make test CC="${CC}" "LD=${LD}"
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
    [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || ${bindir}/perl ./Build test
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
            sed -i.bak -e "s!/usr/bin/env perl!/usr/perl5/${perl-ver}/bin/perl!" ${i}
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

  # config_data conflicts with file included in runtime/perl-*
  rm -rf $RPM_BUILD_ROOT/usr/perl5/$*/bin

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

%if %{build522}
build_for 5.22
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

%if %{build522}
%files 522
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.22
%if %{include_executable}
/usr/perl5/5.22
%endif
%endif

%changelog
* Thu Apr 27 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix build
* Wed Apr 05 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4222 and package for perl-522 is added, for perl-520 is obsolete
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
