%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build526 %( if [ -x /usr/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define enable_test %( if [ "x${PERL_DISABLE_TEST}" = 'xtrue' ]; then echo '0'; else echo '1'; fi )

%define include_executable 0
%define install_to_site_dir 0

%define cpan_name YAML-Tiny
%define sfe_cpan_name yaml-tiny
%define ips_cpan_name yaml-tiny

Summary:               Read/Write YAML files with as little code as possible
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               1.73
IPS_component_version: 1.73
License:               perl_5
URL:                   https://metacpan.org/pod/YAML::Tiny
Source0:               http://cpan.metacpan.org/authors/id/E/ET/ETHER/YAML-Tiny-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Read/Write YAML files with as little code as possible

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          Read/Write YAML files with as little code as possible
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/file-temp-584
BuildRequires:    library/perl-5/getopt-long-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/json-maybexs-584
BuildRequires:    library/perl-5/json-pp-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/scalar-list-utils-584
BuildRequires:    library/perl-5/test-simple-584
%if %{enable_test}
BuildRequires:    library/perl-5/carp-584
BuildRequires:    library/perl-5/exporter-584
BuildRequires:    library/perl-5/scalar-list-utils-584
%endif
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/scalar-list-utils-584

%description 584
Read/Write YAML files with as little code as possible
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Read/Write YAML files with as little code as possible
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/file-temp-510
BuildRequires:    library/perl-5/getopt-long-510
BuildRequires:    library/perl-5/io-510
BuildRequires:    library/perl-5/json-maybexs-510
BuildRequires:    library/perl-5/json-pp-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/scalar-list-utils-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/carp-510
BuildRequires:    library/perl-5/exporter-510
BuildRequires:    library/perl-5/scalar-list-utils-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-510
Requires:         library/perl-5/exporter-510
Requires:         library/perl-5/scalar-list-utils-510

%description 510
Read/Write YAML files with as little code as possible
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          Read/Write YAML files with as little code as possible
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/file-temp-512
BuildRequires:    library/perl-5/getopt-long-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/json-maybexs-512
BuildRequires:    library/perl-5/json-pp-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/scalar-list-utils-512
BuildRequires:    library/perl-5/test-simple-512
%if %{enable_test}
BuildRequires:    library/perl-5/carp-512
BuildRequires:    library/perl-5/exporter-512
BuildRequires:    library/perl-5/scalar-list-utils-512
%endif
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/scalar-list-utils-512

%description 512
Read/Write YAML files with as little code as possible
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          Read/Write YAML files with as little code as possible
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/file-temp-516
BuildRequires:    library/perl-5/getopt-long-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/json-maybexs-516
BuildRequires:    library/perl-5/json-pp-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/scalar-list-utils-516
BuildRequires:    library/perl-5/test-simple-516
Requires:         library/perl-5/%{ips_cpan_name}
%if %{enable_test}
BuildRequires:    library/perl-5/carp-516
BuildRequires:    library/perl-5/exporter-516
BuildRequires:    library/perl-5/scalar-list-utils-516
%endif
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/scalar-list-utils-516

%description 516
Read/Write YAML files with as little code as possible
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          Read/Write YAML files with as little code as possible
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/extutils-makemaker-522
BuildRequires:    library/perl-5/file-temp-522
BuildRequires:    library/perl-5/getopt-long-522
BuildRequires:    library/perl-5/io-522
BuildRequires:    library/perl-5/json-maybexs-522
BuildRequires:    library/perl-5/json-pp-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/scalar-list-utils-522
BuildRequires:    library/perl-5/test-simple-522
%if %{enable_test}
BuildRequires:    library/perl-5/carp-522
BuildRequires:    library/perl-5/exporter-522
BuildRequires:    library/perl-5/scalar-list-utils-522
%endif
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-522
Requires:         library/perl-5/exporter-522
Requires:         library/perl-5/scalar-list-utils-522

%description 522
Read/Write YAML files with as little code as possible
%endif

%if %{build526}
%package 526
IPS_package_name: library/perl-5/%{ips_cpan_name}-526
Summary:          Read/Write YAML files with as little code as possible
BuildRequires:    runtime/perl-526 = *
BuildRequires:    library/perl-5/cpan-meta-526
BuildRequires:    library/perl-5/extutils-makemaker-526
BuildRequires:    library/perl-5/file-temp-526
BuildRequires:    library/perl-5/getopt-long-526
BuildRequires:    library/perl-5/io-526
BuildRequires:    library/perl-5/json-maybexs-526
BuildRequires:    library/perl-5/json-pp-526
BuildRequires:    library/perl-5/pathtools-526
BuildRequires:    library/perl-5/scalar-list-utils-526
BuildRequires:    library/perl-5/test-simple-526
%if %{enable_test}
BuildRequires:    library/perl-5/carp-526
BuildRequires:    library/perl-5/exporter-526
BuildRequires:    library/perl-5/scalar-list-utils-526
%endif
Requires:         runtime/perl-526 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-526
Requires:         library/perl-5/exporter-526
Requires:         library/perl-5/scalar-list-utils-526

%description 526
Read/Write YAML files with as little code as possible
%endif

%prep
%setup -q -n %{cpan_name}-%{version}
[ -d %{buildroot} ] && rm -rf %{buildroot}

%build
build_with_makefile.pl_for() {
    perl_ver=$1
    test=$2
    perl_dir_prefix="/usr/perl5/${perl_ver}"
    bindir="${perl_dir_prefix}/bin"
    vendor_dir="/usr/perl5/vendor_perl/${perl_ver}"
    site_dir="/usr/perl5/site_perl/${perl_ver}"

    export PERL5LIB=${vendor_dir}
%if %{install_to_site_dir}
    perl_libdir="${site_dir}"
%else
    perl_libdir="${vendor_dir}"
%endif

    ${bindir}/perl Makefile.PL PREFIX=%{_prefix} \
                   DESTDIR=$RPM_BUILD_ROOT \
                   LIB=${perl_libdir}

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
    perl_dir_prefix="/usr/perl5/${perl_ver}"
    bindir="${perl_dir_prefix}/bin"
    vendor_dir="/usr/perl5/vendor_perl/${perl_ver}"
    site_dir="/usr/perl5/site_perl/${perl_ver}"

%if %{install_to_site_dir}
    installdir='site'
%else
    installdir='vendor'
%endif
    export PERL5LIB=${vendor_dir}
    ${bindir}/perl Build.PL \
                   --installdirs ${installdir} \
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

%if %{build526}
build_for 5.26
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
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.8.4
%else
/usr/perl5/vendor_perl/5.8.4
%endif
%if %{include_executable}
/usr/perl5/5.8.4
%endif
%endif

%if %{build510}
%files 510
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.10
%else
/usr/perl5/vendor_perl/5.10
%endif
%if %{include_executable}
/usr/perl5/5.1.0
%endif
%endif

%if %{build512}
%files 512
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.12
%else
/usr/perl5/vendor_perl/5.12
%endif
%if %{include_executable}
/usr/perl5/5.12
%endif
%endif

%if %{build516}
%files 516
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.16
%else
/usr/perl5/vendor_perl/5.16
%endif
%if %{include_executable}
/usr/perl5/5.16
%endif
%endif

%if %{build522}
%files 522
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.22
%else
/usr/perl5/vendor_perl/5.22
%endif
%if %{include_executable}
/usr/perl5/5.22
%endif
%endif

%if %{build526}
%files 526
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.26
%else
/usr/perl5/vendor_perl/5.26
%endif
%if %{include_executable}
/usr/perl5/5.26
%endif
%endif

%changelog
* Sat Mar 17 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.73
* Sun Feb 03 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add summary
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
