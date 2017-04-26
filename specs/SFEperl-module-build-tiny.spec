%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name Module-Build-Tiny
%define sfe_cpan_name module-build-tiny
%define ips_cpan_name module-build-tiny

Summary:               A tiny replacement for Module::Build
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               0.039
IPS_component_version: 0.39
License:               perl_5
URL:                   https://metacpan.org/pod/Module::Build::Tiny
Source0:               http://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
A tiny replacement for Module::Build

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/carp-584
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/data-dumper-584
BuildRequires:    library/perl-5/exporter-584
BuildRequires:    library/perl-5/extutils-cbuilder-584
BuildRequires:    library/perl-5/extutils-config-584
BuildRequires:    library/perl-5/extutils-helpers-584
BuildRequires:    library/perl-5/extutils-install-584
BuildRequires:    library/perl-5/extutils-installpaths-584
BuildRequires:    library/perl-5/extutils-parsexs-584
BuildRequires:    library/perl-5/file-path-584
BuildRequires:    library/perl-5/file-sharedir-584
BuildRequires:    library/perl-5/file-temp-584
BuildRequires:    library/perl-5/getopt-long-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/json-pp-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/podlators-584
BuildRequires:    library/perl-5/test-harness-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/xsloader-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-584
Requires:         library/perl-5/cpan-meta-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/extutils-cbuilder-584
Requires:         library/perl-5/extutils-config-584
Requires:         library/perl-5/extutils-helpers-584
Requires:         library/perl-5/extutils-install-584
Requires:         library/perl-5/extutils-installpaths-584
Requires:         library/perl-5/extutils-parsexs-584
Requires:         library/perl-5/file-path-584
Requires:         library/perl-5/getopt-long-584
Requires:         library/perl-5/json-pp-584
Requires:         library/perl-5/local-lib-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/podlators-584
Requires:         library/perl-5/test-harness-584

%description 584
A tiny replacement for Module::Build
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/carp-510
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/data-dumper-510
BuildRequires:    library/perl-5/exporter-510
BuildRequires:    library/perl-5/extutils-cbuilder-510
BuildRequires:    library/perl-5/extutils-config-510
BuildRequires:    library/perl-5/extutils-helpers-510
BuildRequires:    library/perl-5/extutils-install-510
BuildRequires:    library/perl-5/extutils-installpaths-510
BuildRequires:    library/perl-5/extutils-parsexs-510
BuildRequires:    library/perl-5/file-path-510
BuildRequires:    library/perl-5/file-sharedir-510
BuildRequires:    library/perl-5/file-temp-510
BuildRequires:    library/perl-5/getopt-long-510
BuildRequires:    library/perl-5/io-510
BuildRequires:    library/perl-5/json-pp-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/podlators-510
BuildRequires:    library/perl-5/test-harness-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/xsloader-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-510
Requires:         library/perl-5/cpan-meta-510
Requires:         library/perl-5/exporter-510
Requires:         library/perl-5/extutils-cbuilder-510
Requires:         library/perl-5/extutils-config-510
Requires:         library/perl-5/extutils-helpers-510
Requires:         library/perl-5/extutils-install-510
Requires:         library/perl-5/extutils-installpaths-510
Requires:         library/perl-5/extutils-parsexs-510
Requires:         library/perl-5/file-path-510
Requires:         library/perl-5/getopt-long-510
Requires:         library/perl-5/json-pp-510
Requires:         library/perl-5/local-lib-510
Requires:         library/perl-5/pathtools-510
Requires:         library/perl-5/podlators-510
Requires:         library/perl-5/test-harness-510

%description 510
A tiny replacement for Module::Build
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/carp-512
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/data-dumper-512
BuildRequires:    library/perl-5/exporter-512
BuildRequires:    library/perl-5/extutils-cbuilder-512
BuildRequires:    library/perl-5/extutils-config-512
BuildRequires:    library/perl-5/extutils-helpers-512
BuildRequires:    library/perl-5/extutils-install-512
BuildRequires:    library/perl-5/extutils-installpaths-512
BuildRequires:    library/perl-5/extutils-parsexs-512
BuildRequires:    library/perl-5/file-path-512
BuildRequires:    library/perl-5/file-sharedir-512
BuildRequires:    library/perl-5/file-temp-512
BuildRequires:    library/perl-5/getopt-long-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/json-pp-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/podlators-512
BuildRequires:    library/perl-5/test-harness-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/xsloader-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-512
Requires:         library/perl-5/cpan-meta-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/extutils-cbuilder-512
Requires:         library/perl-5/extutils-config-512
Requires:         library/perl-5/extutils-helpers-512
Requires:         library/perl-5/extutils-install-512
Requires:         library/perl-5/extutils-installpaths-512
Requires:         library/perl-5/extutils-parsexs-512
Requires:         library/perl-5/file-path-512
Requires:         library/perl-5/getopt-long-512
Requires:         library/perl-5/json-pp-512
Requires:         library/perl-5/local-lib-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/podlators-512
Requires:         library/perl-5/test-harness-512

%description 512
A tiny replacement for Module::Build
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/carp-516
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/data-dumper-516
BuildRequires:    library/perl-5/exporter-516
BuildRequires:    library/perl-5/extutils-cbuilder-516
BuildRequires:    library/perl-5/extutils-config-516
BuildRequires:    library/perl-5/extutils-helpers-516
BuildRequires:    library/perl-5/extutils-install-516
BuildRequires:    library/perl-5/extutils-installpaths-516
BuildRequires:    library/perl-5/extutils-parsexs-516
BuildRequires:    library/perl-5/file-path-516
BuildRequires:    library/perl-5/file-sharedir-516
BuildRequires:    library/perl-5/file-temp-516
BuildRequires:    library/perl-5/getopt-long-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/json-pp-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/podlators-516
BuildRequires:    library/perl-5/test-harness-516
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/xsloader-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-516
Requires:         library/perl-5/cpan-meta-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/extutils-cbuilder-516
Requires:         library/perl-5/extutils-config-516
Requires:         library/perl-5/extutils-helpers-516
Requires:         library/perl-5/extutils-install-516
Requires:         library/perl-5/extutils-installpaths-516
Requires:         library/perl-5/extutils-parsexs-516
Requires:         library/perl-5/file-path-516
Requires:         library/perl-5/getopt-long-516
Requires:         library/perl-5/json-pp-516
Requires:         library/perl-5/local-lib-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/podlators-516
Requires:         library/perl-5/test-harness-516

%description 516
A tiny replacement for Module::Build
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/carp-520
BuildRequires:    library/perl-5/cpan-meta-520
BuildRequires:    library/perl-5/data-dumper-520
BuildRequires:    library/perl-5/exporter-520
BuildRequires:    library/perl-5/extutils-cbuilder-520
BuildRequires:    library/perl-5/extutils-config-520
BuildRequires:    library/perl-5/extutils-helpers-520
BuildRequires:    library/perl-5/extutils-install-520
BuildRequires:    library/perl-5/extutils-installpaths-520
BuildRequires:    library/perl-5/extutils-parsexs-520
BuildRequires:    library/perl-5/file-path-520
BuildRequires:    library/perl-5/file-sharedir-520
BuildRequires:    library/perl-5/file-temp-520
BuildRequires:    library/perl-5/getopt-long-520
BuildRequires:    library/perl-5/io-520
BuildRequires:    library/perl-5/json-pp-520
BuildRequires:    library/perl-5/pathtools-520
BuildRequires:    library/perl-5/podlators-520
BuildRequires:    library/perl-5/test-harness-520
BuildRequires:    library/perl-5/test-simple-520
BuildRequires:    library/perl-5/xsloader-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-520
Requires:         library/perl-5/cpan-meta-520
Requires:         library/perl-5/exporter-520
Requires:         library/perl-5/extutils-cbuilder-520
Requires:         library/perl-5/extutils-config-520
Requires:         library/perl-5/extutils-helpers-520
Requires:         library/perl-5/extutils-install-520
Requires:         library/perl-5/extutils-installpaths-520
Requires:         library/perl-5/extutils-parsexs-520
Requires:         library/perl-5/file-path-520
Requires:         library/perl-5/getopt-long-520
Requires:         library/perl-5/json-pp-520
Requires:         library/perl-5/local-lib-520
Requires:         library/perl-5/pathtools-520
Requires:         library/perl-5/podlators-520
Requires:         library/perl-5/test-harness-520

%description 520
A tiny replacement for Module::Build
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
}

modify_bin_dir() {
    perl_ver=$1
    if [ -d $RPM_BUILD_ROOT/usr/bin ]
    then
      [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver} ] || mkdir -p $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
      mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin
    fi
      
    if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}bin ]
    then
        for i in $RPM_BUILD_ROOT/usr/perl5/${perl_ver}bin/*
        do
            sed -ibak -e "s/\/usr\/bin\/env ruby/\/usr\/perl5\/${perl-ver}\/bin\/ruby/" ${I}
            [ -f ${i}.bak] || rm ${i}.bak
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
* Sun Nov 15 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
