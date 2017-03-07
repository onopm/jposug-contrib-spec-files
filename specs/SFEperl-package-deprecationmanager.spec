%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name Package-DeprecationManager
%define sfe_cpan_name pkg-depmanager
%define ips_cpan_name package-deprecationmanager

Summary:               Manage deprecation warnings for your distribution
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               0.17
IPS_component_version: 0.17
License:               artistic_2
URL:                   https://metacpan.org/pod/Package::DeprecationManager
Source0:               http://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Package-DeprecationManager-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Manage deprecation warnings for your distribution

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          Manage deprecation warnings for your distribution
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/exporter-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/test-fatal-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/test-warnings-584
BuildRequires:    library/perl-5/carp-584
BuildRequires:    library/perl-5/package-stash-584
BuildRequires:    library/perl-5/params-util-584
BuildRequires:    library/perl-5/scalar-list-utils-584
BuildRequires:    library/perl-5/sub-install-584
BuildRequires:    library/perl-5/sub-name-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-584
Requires:         library/perl-5/package-stash-584
Requires:         library/perl-5/params-util-584
Requires:         library/perl-5/scalar-list-utils-584
Requires:         library/perl-5/sub-install-584
Requires:         library/perl-5/sub-name-584

%description 584
Manage deprecation warnings for your distribution
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Manage deprecation warnings for your distribution
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/exporter-510
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/test-fatal-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/test-warnings-510
BuildRequires:    library/perl-5/carp-510
BuildRequires:    library/perl-5/package-stash-510
BuildRequires:    library/perl-5/params-util-510
BuildRequires:    library/perl-5/scalar-list-utils-510
BuildRequires:    library/perl-5/sub-install-510
BuildRequires:    library/perl-5/sub-name-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-510
Requires:         library/perl-5/package-stash-510
Requires:         library/perl-5/params-util-510
Requires:         library/perl-5/scalar-list-utils-510
Requires:         library/perl-5/sub-install-510
Requires:         library/perl-5/sub-name-510

%description 510
Manage deprecation warnings for your distribution
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          Manage deprecation warnings for your distribution
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/exporter-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/test-fatal-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/test-warnings-512
BuildRequires:    library/perl-5/carp-512
BuildRequires:    library/perl-5/package-stash-512
BuildRequires:    library/perl-5/params-util-512
BuildRequires:    library/perl-5/scalar-list-utils-512
BuildRequires:    library/perl-5/sub-install-512
BuildRequires:    library/perl-5/sub-name-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-512
Requires:         library/perl-5/package-stash-512
Requires:         library/perl-5/params-util-512
Requires:         library/perl-5/scalar-list-utils-512
Requires:         library/perl-5/sub-install-512
Requires:         library/perl-5/sub-name-512

%description 512
Manage deprecation warnings for your distribution
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          Manage deprecation warnings for your distribution
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/exporter-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/test-fatal-516
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/test-warnings-516
Requires:         library/perl-5/%{ips_cpan_name}
BuildRequires:    library/perl-5/carp-516
BuildRequires:    library/perl-5/package-stash-516
BuildRequires:    library/perl-5/params-util-516
BuildRequires:    library/perl-5/scalar-list-utils-516
BuildRequires:    library/perl-5/sub-install-516
BuildRequires:    library/perl-5/sub-name-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-516
Requires:         library/perl-5/package-stash-516
Requires:         library/perl-5/params-util-516
Requires:         library/perl-5/scalar-list-utils-516
Requires:         library/perl-5/sub-install-516
Requires:         library/perl-5/sub-name-516

%description 516
Manage deprecation warnings for your distribution
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          Manage deprecation warnings for your distribution
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/cpan-meta-520
BuildRequires:    library/perl-5/exporter-520
BuildRequires:    library/perl-5/extutils-makemaker-520
BuildRequires:    library/perl-5/pathtools-520
BuildRequires:    library/perl-5/test-fatal-520
BuildRequires:    library/perl-5/test-simple-520
BuildRequires:    library/perl-5/test-warnings-520
BuildRequires:    library/perl-5/carp-520
BuildRequires:    library/perl-5/package-stash-520
BuildRequires:    library/perl-5/params-util-520
BuildRequires:    library/perl-5/scalar-list-utils-520
BuildRequires:    library/perl-5/sub-install-520
BuildRequires:    library/perl-5/sub-name-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-520
Requires:         library/perl-5/package-stash-520
Requires:         library/perl-5/params-util-520
Requires:         library/perl-5/scalar-list-utils-520
Requires:         library/perl-5/sub-install-520
Requires:         library/perl-5/sub-name-520

%description 520
Manage deprecation warnings for your distribution
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          Manage deprecation warnings for your distribution
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/exporter-522
BuildRequires:    library/perl-5/extutils-makemaker-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/test-fatal-522
BuildRequires:    library/perl-5/test-simple-522
BuildRequires:    library/perl-5/test-warnings-522
BuildRequires:    library/perl-5/carp-522
BuildRequires:    library/perl-5/package-stash-522
BuildRequires:    library/perl-5/params-util-522
BuildRequires:    library/perl-5/scalar-list-utils-522
BuildRequires:    library/perl-5/sub-install-522
BuildRequires:    library/perl-5/sub-name-522
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-522
Requires:         library/perl-5/package-stash-522
Requires:         library/perl-5/params-util-522
Requires:         library/perl-5/scalar-list-utils-522
Requires:         library/perl-5/sub-install-522
Requires:         library/perl-5/sub-name-522

%description 522
Manage deprecation warnings for your distribution
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

    echo ${perl_ver} | egrep '5\.(84|12)' > /dev/null
    if [ $? -eq 0 ]
    then
        make CC='cc -m32' LD='cc -m32'
        [ "x${test}" = 'xwithout_test' ] || make test CC='cc -m32' LD='cc -m32'
    else
        make CC='cc -m64' LD='cc -m64'
        [ "x${test}" = 'xwithout_test' ] || make test CC='cc -m64' LD='cc -m64'
    fi

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
    [ "x${test}" = 'xwithout_test' ] || ${bindir}/perl ./Build test
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

%if %{build520}
%files 520
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.20
%if %{include_executable}
/usr/perl5/5.20
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
* Tue Mar 07 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.17
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
