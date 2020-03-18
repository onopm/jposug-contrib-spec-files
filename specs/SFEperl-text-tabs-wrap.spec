%include Solaris.inc

%define build526 %( if [ -x /opt/jposug/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build530 %( if [ -x /opt/jposug/perl5/5.30/bin/perl ]; then echo '1'; else echo '0'; fi)
%define enable_test %( if [ "x${PERL_DISABLE_TEST}" = 'xtrue' ]; then echo '0'; else echo '1'; fi )

%define include_executable 0
%define install_to_site_dir 0

%define cpan_name Text-Tabs+Wrap
%define sfe_cpan_name text-tabs-wrap
%define ips_cpan_name text-tabs-wrap

Summary:               Expand tabs and do simple line wrapping
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      jposug/library/perl-5/%{ips_cpan_name}
Version:               2013.0523
IPS_component_version: 2013.523
License:               unknown
URL:                   https://metacpan.org/pod/Text::Tabs+Wrap
Source0:               http://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/Text-Tabs+Wrap-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Expand tabs and do simple line wrapping

%if %{build526}
%package 526jposug
IPS_package_name: library/perl-5/%{ips_cpan_name}-526jposug
Summary:          Expand tabs and do simple line wrapping
BuildRequires:    runtime/perl-526jposug = *
BuildRequires:    library/perl-5/extutils-makemaker-526jposug
%if %{enable_test}
%endif
Requires:         runtime/perl-526jposug = *
# Requires:         library/perl-5/%{ips_cpan_name}

%description 526jposug
Expand tabs and do simple line wrapping
%endif

%if %{build530}
%package 530jposug
IPS_package_name: jposug/library/perl-5/%{ips_cpan_name}-530jposug
Summary:          Expand tabs and do simple line wrapping
BuildRequires:    runtime/perl-530jposug = *
BuildRequires:    jposug/library/perl-5/extutils-makemaker-530jposug
%if %{enable_test}
%endif
Requires:         runtime/perl-530jposug = *
# Requires:         jposug/library/perl-5/%{ips_cpan_name}

%description 530jposug
Expand tabs and do simple line wrapping
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
* Wed Mar 11 2020 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- only build for JPOSUG perl packages
* Tue May 29 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add package for perl-526jposug
* Fri May 11 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packge for perl-526
* Thu Apr 27 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
