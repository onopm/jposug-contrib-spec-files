%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build526 %( if [ -x /usr/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build526jposug %( if [ -x /opt/jposug/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define enable_test %( if [ "x${PERL_DISABLE_TEST}" = 'xtrue' ]; then echo '0'; else echo '1'; fi )

%define include_executable 0
%define install_to_site_dir 0

%define cpan_name ExtUtils-MakeMaker
%define sfe_cpan_name extutils-mkmkr
%define ips_cpan_name extutils-makemaker

Summary:               Create a module Makefile
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               7.34
IPS_component_version: 7.34
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
%if %{enable_test}
BuildRequires:    library/perl-5/data-dumper-584
BuildRequires:    library/perl-5/encode-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/podlators-584
%endif
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
%if %{enable_test}
BuildRequires:    library/perl-5/data-dumper-512
BuildRequires:    library/perl-5/encode-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/podlators-512
%endif
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
%if %{enable_test}
BuildRequires:    library/perl-5/data-dumper-516
BuildRequires:    library/perl-5/encode-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/podlators-516
%endif
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
%if %{enable_test}
BuildRequires:    library/perl-5/data-dumper-522
BuildRequires:    library/perl-5/encode-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/podlators-522
%endif
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-522
Requires:         library/perl-5/encode-522
Requires:         library/perl-5/pathtools-522
Requires:         library/perl-5/podlators-522

%description 522
Create a module Makefile
%endif

%if %{build526}
%package 526
IPS_package_name: library/perl-5/%{ips_cpan_name}-526
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-526 = *
%if %{enable_test}
BuildRequires:    library/perl-5/data-dumper-526
BuildRequires:    library/perl-5/encode-526
BuildRequires:    library/perl-5/pathtools-526
BuildRequires:    library/perl-5/podlators-526
%endif
Requires:         runtime/perl-526 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-526
Requires:         library/perl-5/encode-526
Requires:         library/perl-5/pathtools-526
Requires:         library/perl-5/podlators-526

%description 526
Create a module Makefile
%endif

%if %{build526jposug}
%package 526jposug
IPS_package_name: library/perl-5/%{ips_cpan_name}-526jposug
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-526jposug = *
%if %{enable_test}
BuildRequires:    library/perl-5/data-dumper-526jposug
BuildRequires:    library/perl-5/encode-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/podlators-526jposug
%endif
Requires:         runtime/perl-526jposug = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/data-dumper-526jposug
Requires:         library/perl-5/encode-526jposug
Requires:         library/perl-5/pathtools-526jposug
Requires:         library/perl-5/podlators-526jposug

%description 526jposug
Create a module Makefile
%endif

%prep
%setup -q -n %{cpan_name}-%{version}
[ -d %{buildroot} ] && rm -rf %{buildroot}

%build
build_with_makefile.pl_for() {
    test=$2
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    perl_dir_prefix="${prefix}/perl5/${perl_ver}"
    bindir="${perl_dir_prefix}/bin"
    vendor_dir="${prefix}/perl5/vendor_perl/${perl_ver}"
    site_dir="${prefix}/perl5/site_perl/${perl_ver}"

    export PERL5LIB=${vendor_dir}
%if %{install_to_site_dir}
    perl_libdir="${site_dir}"
%else
    perl_libdir="${vendor_dir}"
%endif

    ${bindir}/perl Makefile.PL PREFIX=${prefix} \
                   DESTDIR=$RPM_BUILD_ROOT \
                   LIB=${perl_libdir}

    echo ${perl_ver} | egrep '5\.(84|12)' > /dev/null && bin64=0 || bin64=1
    if [ ${bin64} -eq 0 ]
    then
        export CC='cc -m32'
        export LD='cc -m32'
    else
        export CC='cc -m64'
        export LD='cc -m64'
    fi
    make CC="${CC}" LD="${LD}"
    [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || make test CC="${CC}" "LD=${LD}"
    make pure_install
}

build_with_build.pl_for() {
    test=$2
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    perl_dir_prefix="${prefix}/perl5/${perl_ver}"
    bindir="${perl_dir_prefix}/bin"
    vendor_dir="${prefix}/perl5/vendor_perl/${perl_ver}"
    site_dir="${prefix}/perl5/site_perl/${perl_ver}"

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
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    if [ -d $RPM_BUILD_ROOT/${prefix}/bin ]
    then
      [ -d ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver} ] || mkdir -p ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver}
      mv $RPM_BUILD_ROOT${prefix}/bin $RPM_BUILD_ROOT/${prefix}/perl5/${perl_ver}/bin
    fi
      
    if [ -d ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver}/bin ]
    then
        for i in ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver}/bin/*
        do
            sed -i.bak -e "s!/usr/bin/env perl!${prefix}/perl5/${perl_ver}/bin/perl!" ${i}
            [ -f ${i}.bak] || rm -f ${i}.bak
        done
    fi
}

modify_man_dir() {
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    if [ -d $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man ]
    then
        if [ -d $RPM_BUILD_ROOT%{_datadir}/man ]
        then
            rm -rf $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man
        else
            mkdir -p $RPM_BUILD_ROOT%{_datadir}
            mv $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man $RPM_BUILD_ROOT%{_datadir}/
            rm -rf $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man
        fi
        if [ %{include_executable} -eq 0 ]
        then
            rmdir $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}
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

%if %{build526jposug}
build_for 5.26jposug
%endif

%install
if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]
then
    mkdir -p $RPM_BUILD_ROOT%{_datadir}
    mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
fi

if [ -d $RPM_BUILD_ROOT/opt/jposug/man ]
then
    if [ -d $RPM_BUILD_ROOT%{_datadir}/man ]
    then
        rm -rf $RPM_BUILD_ROOT/opt/jposug/man
    else
        [ -d $RPM_BUILD_ROOT%{_datadir} ] || mkdir -p $RPM_BUILD_ROOT%{_datadir}
        mv $RPM_BUILD_ROOT/opt/jposug/man $RPM_BUILD_ROOT%{_datadir}
    fi
fi

if [ -d $RPM_BUILD_ROOT%{_datadir}/man/man3 ]
then
    mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl
fi

gfind $RPM_BUILD_ROOT -type f |egrep '(ExtUtils/(Install|Installed|Packlist).pm|ExtUtils::(Install|Installed|Packlist).3)' | \
    xargs rm

# to avoid conflict with executable files included in solaris/runtime/perl-5*
if [ $( expr %{build510} \| %{build512} \| %{build516} \| %{build522} \| %{build526} ) -ne 0 ]
then
  rm -rf ${RPM_BUILD_ROOT}/usr/perl5/5.*
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

%if %{build526jposug}
%files 526jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
%if %{install_to_site_dir}
/opt/jposug/perl5/site_perl/5.26
%else
/opt/jposug/perl5/vendor_perl/5.26
%endif
# %if %{include_executable}
/opt/jposug/perl5/5.26
# %endif
%endif

%changelog
* Tue Jun 05 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete some files to avoid conflict with files included in solaris/runtime/perl-5*
* Mon May 21 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete files to avoid conflict with ExtUtils-Install
* Thu May 17 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build package for perl-526jposug
* Fri May 11 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.34 and build package for perl-526
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
