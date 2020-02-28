%include Solaris.inc

%define build526 %( if [ -x /opt/jposug/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build530 %( if [ -x /opt/jposug/perl5/5.30/bin/perl ]; then echo '1'; else echo '0'; fi)
%define enable_test %( if [ "x${PERL_DISABLE_TEST}" = 'xtrue' ]; then echo '0'; else echo '1'; fi )

%define include_executable 0
%define install_to_site_dir 0

%define cpan_name CPAN-Meta
%define sfe_cpan_name cpan-meta
%define ips_cpan_name cpan-meta

Summary:               the distribution metadata for a CPAN dist
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      jposug/library/perl-5/%{ips_cpan_name}
Version:               2.150010
IPS_component_version: 2.150010
License:               perl_5
URL:                   https://metacpan.org/pod/CPAN::Meta
Source0:               http://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
the distribution metadata for a CPAN dist

%if %{build526}
%package 526jposug
IPS_package_name: library/perl-5/%{ips_cpan_name}-526jposug
Summary:          the distribution metadata for a CPAN dist
BuildRequires:    runtime/perl-526jposug = *
BuildRequires:    library/perl-5/cpan-meta-526jposug
BuildRequires:    library/perl-5/data-dumper-526jposug
BuildRequires:    library/perl-5/extutils-makemaker-526jposug
BuildRequires:    library/perl-5/file-temp-526jposug
BuildRequires:    library/perl-5/io-526jposug
BuildRequires:    library/perl-5/json-pp-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/storable-526jposug
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-526jposug
BuildRequires:    library/perl-5/carp-526jposug
BuildRequires:    library/perl-5/cpan-meta-requirements-526jposug
BuildRequires:    library/perl-5/cpan-meta-yaml-526jposug
BuildRequires:    library/perl-5/encode-526jposug
BuildRequires:    library/perl-5/exporter-526jposug
BuildRequires:    library/perl-5/json-pp-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/scalar-list-utils-526jposug
BuildRequires:    library/perl-5/version-526jposug
%endif
Requires:         runtime/perl-526jposug = *
# Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-526jposug
Requires:         library/perl-5/cpan-meta-requirements-526jposug
Requires:         library/perl-5/cpan-meta-yaml-526jposug
Requires:         library/perl-5/encode-526jposug
Requires:         library/perl-5/exporter-526jposug
Requires:         library/perl-5/json-pp-526jposug
Requires:         library/perl-5/pathtools-526jposug
Requires:         library/perl-5/scalar-list-utils-526jposug
Requires:         library/perl-5/version-526jposug

%description 526jposug
the distribution metadata for a CPAN dist
%endif

%if %{build530}
%package 530jposug
IPS_package_name: jposug/library/perl-5/%{ips_cpan_name}-530jposug
Summary:          the distribution metadata for a CPAN dist
BuildRequires:    runtime/perl-530jposug = *
BuildRequires:    jposug/library/perl-5/cpan-meta-530jposug
BuildRequires:    jposug/library/perl-5/data-dumper-530jposug
BuildRequires:    jposug/library/perl-5/extutils-makemaker-530jposug
BuildRequires:    jposug/library/perl-5/file-temp-530jposug
BuildRequires:    jposug/library/perl-5/io-530jposug
BuildRequires:    jposug/library/perl-5/json-pp-530jposug
BuildRequires:    jposug/library/perl-5/pathtools-530jposug
BuildRequires:    jposug/library/perl-5/storable-530jposug
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-530jposug
BuildRequires:    jposug/library/perl-5/carp-530jposug
BuildRequires:    jposug/library/perl-5/cpan-meta-requirements-530jposug
BuildRequires:    jposug/library/perl-5/cpan-meta-yaml-530jposug
BuildRequires:    jposug/library/perl-5/encode-530jposug
BuildRequires:    jposug/library/perl-5/exporter-530jposug
BuildRequires:    jposug/library/perl-5/json-pp-530jposug
BuildRequires:    jposug/library/perl-5/pathtools-530jposug
BuildRequires:    jposug/library/perl-5/scalar-list-utils-530jposug
BuildRequires:    jposug/library/perl-5/version-530jposug
%endif
Requires:         runtime/perl-530jposug = *
# Requires:         jposug/library/perl-5/%{ips_cpan_name}
Requires:         jposug/library/perl-5/carp-530jposug
Requires:         jposug/library/perl-5/cpan-meta-requirements-530jposug
Requires:         jposug/library/perl-5/cpan-meta-yaml-530jposug
Requires:         jposug/library/perl-5/encode-530jposug
Requires:         jposug/library/perl-5/exporter-530jposug
Requires:         jposug/library/perl-5/json-pp-530jposug
Requires:         jposug/library/perl-5/pathtools-530jposug
Requires:         jposug/library/perl-5/scalar-list-utils-530jposug
Requires:         jposug/library/perl-5/version-530jposug

%description 530jposug
the distribution metadata for a CPAN dist
%endif


%prep
%setup -q -n %{cpan_name}-%{version}
[ -d %{buildroot} ] && rm -rf %{buildroot}

%build
build_with_makefile.pl_for() {
    [ -f xdefine ] && rm -f xdefine
    [ -d blib ] && rm -rf blib
    perl_ver=$1
    test=$2
    prefix=/opt/jposug

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

    export CC='cc -m64'
    export LD='cc -m64'
    make CC="${CC}" LD="${LD}"
    [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || make test CC="${CC}" "LD=${LD}"
    make pure_install
}

build_with_build.pl_for() {
    test=$2
    perl_ver=$1
    prefix=/opt/jposug

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
    perl_ver=$1
    prefix=/opt/jposug

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
    perl_ver=$1
    prefix=/opt/jposug

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
%if %{build526}
build_for 5.26
%endif

%if %{build530}
build_for 5.30
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

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%{_datadir}/man

%if %{build526}
%files 526jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
%if %{install_to_site_dir}
/opt/jposug/perl5/site_perl/5.26
%else
/opt/jposug/perl5/vendor_perl/5.26
%endif
%if %{include_executable}
/opt/jposug/perl5/5.26
%endif
%endif

%if %{build530}
%files 530jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
%if %{install_to_site_dir}
/opt/jposug/perl5/site_perl/5.30
%else
/opt/jposug/perl5/vendor_perl/5.30
%endif
%if %{include_executable}
/opt/jposug/perl5/5.30
%endif
%endif

%changelog
* Thu Feb 27 2020 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build only for JPOSUG Perl packages
* Wed May 23 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add packages for perl-526{,jposug}
* Thu Jun 01 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.150010
* Sun Nov 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bumpt to 2.150005 and build packages for perl-516 and perl-520
- add BuildRequires
* Mon Sep 09 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.132510
* Tue Jun 12 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-584 and perl-512
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-584 and perl-512
- initial commit
