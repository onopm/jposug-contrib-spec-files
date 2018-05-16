%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name DBD-Pg
%define sfe_cpan_name dbd-pg93
%define ips_cpan_name dbd-pg93

Summary:               DBI PostgreSQL interface
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               3.5.3
IPS_component_version: 3.5.3
License:               perl_5
URL:                   https://metacpan.org/pod/DBD::Pg
Source0:               http://cpan.metacpan.org/authors/id/T/TU/TURNSTEP/DBD-Pg-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
DBI PostgreSQL interface

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          DBI PostgreSQL interface
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/dbi-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/time-hires-584
BuildRequires:    library/perl-5/version-584
BuildRequires:    database/postgres-93/developer
BuildRequires:    database/postgres-93/library
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/dbi-584
Requires:         library/perl-5/encode-584
Requires:         library/perl-5/file-temp-584
Requires:         library/perl-5/module-signature-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/version-584
Requires:         database/postgres-93/library

%description 584
DBI PostgreSQL interface
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          DBI PostgreSQL interface
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/dbi-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/time-hires-510
BuildRequires:    library/perl-5/version-510
BuildRequires:    database/postgres-93/developer
BuildRequires:    database/postgres-93/library
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/dbi-510
Requires:         library/perl-5/encode-510
Requires:         library/perl-5/file-temp-510
Requires:         library/perl-5/module-signature-510
Requires:         library/perl-5/pathtools-510
Requires:         library/perl-5/version-510
Requires:         database/postgres-93/library

%description 510
DBI PostgreSQL interface
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          DBI PostgreSQL interface
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/dbi-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/time-hires-512
BuildRequires:    library/perl-5/version-512
BuildRequires:    database/postgres-93/developer
BuildRequires:    database/postgres-93/library
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/dbi-512
Requires:         library/perl-5/encode-512
Requires:         library/perl-5/file-temp-512
Requires:         library/perl-5/module-signature-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/version-512
Requires:         database/postgres-93/library

%description 512
DBI PostgreSQL interface
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          DBI PostgreSQL interface
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/dbi-516
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/time-hires-516
BuildRequires:    library/perl-5/version-516
BuildRequires:    database/postgres-93/developer
BuildRequires:    database/postgres-93/library
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/dbi-516
Requires:         library/perl-5/encode-516
Requires:         library/perl-5/file-temp-516
Requires:         library/perl-5/module-signature-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/version-516
Requires:         database/postgres-93/library

%description 516
DBI PostgreSQL interface
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          DBI PostgreSQL interface
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/dbi-520
BuildRequires:    library/perl-5/test-simple-520
BuildRequires:    library/perl-5/time-hires-520
BuildRequires:    library/perl-5/version-520
BuildRequires:    database/postgres-93/developer
BuildRequires:    database/postgres-93/library
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/dbi-520
Requires:         library/perl-5/encode-520
Requires:         library/perl-5/file-temp-520
Requires:         library/perl-5/module-signature-520
Requires:         library/perl-5/pathtools-520
Requires:         library/perl-5/version-520
Requires:         database/postgres-93/library

%description 520
DBI PostgreSQL interface
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
  perl_ver=$1
  if [ $perl_ver = '5.16' -o $perl_ver = '5.20' ]
  then
     POSTGRES_LIB="/usr/postgres/9.3/lib/%{_arch64}/"; export POSTGRES_LIB
  else
     POSTGRES_LIB="/usr/postgres/9.3/lib/"; export POSTGRES_LIB
  fi
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
* Wed Dec 02 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
