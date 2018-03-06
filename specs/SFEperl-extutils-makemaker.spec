%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name ExtUtils-MakeMaker
%define sfe_cpan_name extutils-makemaker
%define ips_cpan_name extutils-makemaker

Summary:               Create a module Makefile
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               7.24
IPS_component_version: 7.24
License:               perl_5
URL:                   https://metacpan.org/pod/ExtUtils::MakeMaker
Source0:               http://cpan.metacpan.org/authors/id/B/BI/BINGOS/ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Create a module Makefile

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/data-dumper-584
BuildRequires:    library/perl-5/encode-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/podlators-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-584
Requires:         library/perl-5/encode-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/podlators-584

%description 584
Create a module Makefile
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/data-dumper-510
BuildRequires:    library/perl-5/encode-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/podlators-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-510
Requires:         library/perl-5/encode-510
Requires:         library/perl-5/pathtools-510
Requires:         library/perl-5/podlators-510

%description 510
Create a module Makefile
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/data-dumper-512
BuildRequires:    library/perl-5/encode-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/podlators-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-512
Requires:         library/perl-5/encode-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/podlators-512

%description 512
Create a module Makefile
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
BuildRequires:    library/perl-5/data-dumper-516
BuildRequires:    library/perl-5/encode-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/podlators-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-516
Requires:         library/perl-5/encode-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/podlators-516

%description 516
Create a module Makefile
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/data-dumper-522
BuildRequires:    library/perl-5/encode-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/podlators-522
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-522
Requires:         library/perl-5/encode-522
Requires:         library/perl-5/pathtools-522
Requires:         library/perl-5/podlators-522

%description 522
Create a module Makefile
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
  modify_man_dir $*
}

export BUILDING_AS_PACKAGE=true

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

# instmodsh conflict with instmodsh included in perl-5XX
rm -rf ${RPM_BUILD_ROOT}/usr/perl5/5.*

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
* Wed Apr 26 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.24 and add packages for perl-510 and perl-522
- not include instmodsh because it conflicts with instmodsh included in perl-5XX
* Tue Nov 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.10 and modify specfile to build packages for perl-516 and perl-520
- use BUILDING_AS_PACKAGE to avoid including bundled modules
* Mon Nov 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.64
* Thu Nov 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete man to avoid conflict
- add Requires and BuildRequires
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete some files to avoid confilict with SFEperl-cpan-meta
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete Manifest.pm to avoid conflit with SFEperl-extutils-manifest
- delete some files which conflict with SFEperl-file-copy-recursive
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add library/perl-5/parse-cpan-meta to BuildRequire
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires and BuildRequires
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires to avoid confilict with file-copy-recursive
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires library/perl-5/extutils-install
- export PERL5LIB to adjust @inc
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
