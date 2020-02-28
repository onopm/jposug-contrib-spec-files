%include Solaris.inc

%define build526 %( if [ -x /opt/jposug/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build530 %( if [ -x /opt/jposug/perl5/5.30/bin/perl ]; then echo '1'; else echo '0'; fi)
%define enable_test %( if [ "x${PERL_DISABLE_TEST}" = 'xtrue' ]; then echo '0'; else echo '1'; fi )

%define include_executable 1
%define install_to_site_dir 0

%define cpan_name Module-Build
%define sfe_cpan_name module-build
%define ips_cpan_name module-build

Summary:               Build and install Perl modules
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      jposug/library/perl-5/%{ips_cpan_name}
Version:               0.4231
IPS_component_version: 0.4231
License:               perl_5
URL:                   https://metacpan.org/pod/Module::Build
Source0:               http://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Build and install Perl modules

%if %{build526}
%package 526jposug
IPS_package_name: library/perl-5/%{ips_cpan_name}-526jposug
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-526jposug = *
BuildRequires:    library/perl-5/cpan-meta-526jposug
BuildRequires:    library/perl-5/cpan-meta-yaml-526jposug
BuildRequires:    library/perl-5/file-path-526jposug
BuildRequires:    library/perl-5/file-temp-526jposug
BuildRequires:    library/perl-5/module-metadata-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/perl-ostype-526jposug
BuildRequires:    library/perl-5/version-526jposug
%if %{enable_test}
BuildRequires:    library/perl-5/test-harness-526jposug
BuildRequires:    library/perl-5/test-simple-526jposug
BuildRequires:    library/perl-5/cpan-meta-526jposug
BuildRequires:    library/perl-5/data-dumper-526jposug
BuildRequires:    library/perl-5/extutils-cbuilder-526jposug
BuildRequires:    library/perl-5/extutils-install-526jposug
BuildRequires:    library/perl-5/extutils-makemaker-526jposug
BuildRequires:    library/perl-5/extutils-manifest-526jposug
BuildRequires:    library/perl-5/extutils-parsexs-526jposug
BuildRequires:    library/perl-5/file-path-526jposug
BuildRequires:    library/perl-5/getopt-long-526jposug
BuildRequires:    library/perl-5/module-metadata-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/perl-ostype-526jposug
BuildRequires:    library/perl-5/podlators-526jposug
BuildRequires:    library/perl-5/test-harness-526jposug
BuildRequires:    library/perl-5/text-abbrev-526jposug
BuildRequires:    library/perl-5/text-parsewords-526jposug
BuildRequires:    library/perl-5/version-526jposug
%endif
Requires:         runtime/perl-526jposug = *
# Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/cpan-meta-526jposug
Requires:         library/perl-5/data-dumper-526jposug
Requires:         library/perl-5/extutils-cbuilder-526jposug
Requires:         library/perl-5/extutils-install-526jposug
Requires:         library/perl-5/extutils-makemaker-526jposug
Requires:         library/perl-5/extutils-manifest-526jposug
Requires:         library/perl-5/extutils-parsexs-526jposug
Requires:         library/perl-5/file-path-526jposug
Requires:         library/perl-5/getopt-long-526jposug
Requires:         library/perl-5/module-metadata-526jposug
Requires:         library/perl-5/pathtools-526jposug
Requires:         library/perl-5/perl-ostype-526jposug
Requires:         library/perl-5/podlators-526jposug
Requires:         library/perl-5/test-harness-526jposug
Requires:         library/perl-5/text-abbrev-526jposug
Requires:         library/perl-5/text-parsewords-526jposug
Requires:         library/perl-5/version-526jposug

%description 526jposug
Build and install Perl modules
%endif

%if %{build530}
%package 530jposug
IPS_package_name: jposug/library/perl-5/%{ips_cpan_name}-530jposug
Summary:          Build and install Perl modules
BuildRequires:    runtime/perl-530jposug = *
BuildRequires:    jposug/library/perl-5/cpan-meta-530jposug
BuildRequires:    jposug/library/perl-5/cpan-meta-yaml-530jposug
BuildRequires:    jposug/library/perl-5/file-path-530jposug
BuildRequires:    jposug/library/perl-5/file-temp-530jposug
BuildRequires:    jposug/library/perl-5/module-metadata-530jposug
BuildRequires:    jposug/library/perl-5/pathtools-530jposug
BuildRequires:    jposug/library/perl-5/perl-ostype-530jposug
BuildRequires:    jposug/library/perl-5/version-530jposug
%if %{enable_test}
BuildRequires:    library/perl-5/test-harness-530jposug
BuildRequires:    library/perl-5/test-simple-530jposug
BuildRequires:    jposug/library/perl-5/cpan-meta-530jposug
BuildRequires:    jposug/library/perl-5/data-dumper-530jposug
BuildRequires:    jposug/library/perl-5/extutils-cbuilder-530jposug
BuildRequires:    jposug/library/perl-5/extutils-install-530jposug
BuildRequires:    jposug/library/perl-5/extutils-makemaker-530jposug
BuildRequires:    jposug/library/perl-5/extutils-manifest-530jposug
BuildRequires:    jposug/library/perl-5/extutils-parsexs-530jposug
BuildRequires:    jposug/library/perl-5/file-path-530jposug
BuildRequires:    jposug/library/perl-5/getopt-long-530jposug
BuildRequires:    jposug/library/perl-5/module-metadata-530jposug
BuildRequires:    jposug/library/perl-5/pathtools-530jposug
BuildRequires:    jposug/library/perl-5/perl-ostype-530jposug
BuildRequires:    jposug/library/perl-5/podlators-530jposug
BuildRequires:    jposug/library/perl-5/test-harness-530jposug
BuildRequires:    jposug/library/perl-5/text-abbrev-530jposug
BuildRequires:    jposug/library/perl-5/text-parsewords-530jposug
BuildRequires:    jposug/library/perl-5/version-530jposug
%endif
Requires:         runtime/perl-530jposug = *
# Requires:         jposug/library/perl-5/%{ips_cpan_name}
Requires:         jposug/library/perl-5/cpan-meta-530jposug
Requires:         jposug/library/perl-5/data-dumper-530jposug
Requires:         jposug/library/perl-5/extutils-cbuilder-530jposug
Requires:         jposug/library/perl-5/extutils-install-530jposug
Requires:         jposug/library/perl-5/extutils-makemaker-530jposug
Requires:         jposug/library/perl-5/extutils-manifest-530jposug
Requires:         jposug/library/perl-5/extutils-parsexs-530jposug
Requires:         jposug/library/perl-5/file-path-530jposug
Requires:         jposug/library/perl-5/getopt-long-530jposug
Requires:         jposug/library/perl-5/module-metadata-530jposug
Requires:         jposug/library/perl-5/pathtools-530jposug
Requires:         jposug/library/perl-5/perl-ostype-530jposug
Requires:         jposug/library/perl-5/podlators-530jposug
Requires:         jposug/library/perl-5/test-harness-530jposug
Requires:         jposug/library/perl-5/text-abbrev-530jposug
Requires:         jposug/library/perl-5/text-parsewords-530jposug
Requires:         jposug/library/perl-5/version-530jposug

%description 530jposug
Build and install Perl modules
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
* Fri Feb 28 2020 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4231 and build only for JPOSUG Perl packages
* Fri May 25 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4224 and add packages for perl-526{,jposug}
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
- initial commit
