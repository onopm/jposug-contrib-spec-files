%include Solaris.inc
%include default-depend.inc

%define build584 0
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 0
%define build520 0
%define include_executable 0

%define cpan_name Try-Tiny
%define sfe_cpan_name try-tiny

Summary:               minimal try/catch with proper preservation of $@
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               0.22
IPS_component_version: 0.22
License:               mit
URL:                   https://metacpan.org/pod/Try::Tiny
Source0:               http://cpan.metacpan.org/authors/id/D/DO/DOY/Try-Tiny-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
minimal try/catch with proper preservation of $@

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          minimal try/catch with proper preservation of $@
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/if-584
BuildRequires:    library/perl-5/capture-tiny-584
BuildRequires:    library/perl-5/sub-name-584
BuildRequires:    library/perl-5/extutils-makemaker-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/warnings-584
Requires:         library/perl-5/strict-584
Requires:         library/perl-5/constant-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/carp-584

%description 584
minimal try/catch with proper preservation of $@
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          minimal try/catch with proper preservation of $@
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/pathtools-512
#BuildRequires:    library/perl-5/if-512
BuildRequires:    library/perl-5/capture-tiny-512
BuildRequires:    library/perl-5/sub-name-512
BuildRequires:    library/perl-5/extutils-makemaker-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/warnings-512
Requires:         library/perl-5/strict-512
Requires:         library/perl-5/constant-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/carp-512

%description 512
minimal try/catch with proper preservation of $@
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          minimal try/catch with proper preservation of $@
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/if-516
BuildRequires:    library/perl-5/capture-tiny-516
BuildRequires:    library/perl-5/sub-name-516
BuildRequires:    library/perl-5/extutils-makemaker-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/warnings-516
Requires:         library/perl-5/strict-516
Requires:         library/perl-5/constant-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/carp-516

%description 516
minimal try/catch with proper preservation of $@
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          minimal try/catch with proper preservation of $@
BuildRequires:    runtime/perl-520 = *
Buildrequires:    library/perl-5/test-simple-520
Buildrequires:    library/perl-5/io-520
Buildrequires:    library/perl-5/pathtools-520
Buildrequires:    library/perl-5/if-520
Buildrequires:    library/perl-5/capture-tiny-520
Buildrequires:    library/perl-5/sub-name-520
Buildrequires:    library/perl-5/extutils-makemaker-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/warnings-520
Requires:         library/perl-5/strict-520
Requires:         library/perl-5/constant-520
Requires:         library/perl-5/exporter-520
Requires:         library/perl-5/carp-520

%description 520
minimal try/catch with proper preservation of $@
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
    [ ${test} == 'without_test' ] || make test
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
    [ ${test} == 'without_test' ] || ${bindir}/perl ./Build test
    ${bindir}/perl ./Build install --destdir $RPM_BUILD_ROOT
}

modify_bin_dir() {
  perl_ver=$1
  if [ -d $RPM_BUILD_ROOT/usr/bin ]
  then
    [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver} ] || mkdir -p $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
    mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin
  fi
}

build_for() {
  if [ -f Makefile.PL ];
  then
    build_with_makefile.pl_for $*
  elif [ -f Build.PL ];
  then
    build_with_build.pl_for $*
  fi

    modify_bin_dir $*
}

# To build without test, pass 'without_test' to build_for commaond.
# like 'build_for version without_test'
%if %{build584}
build_for 5.8.4
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}
if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]
then
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
%{_datadir}/man/man3perl

%if %{build584}
%files 584
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.8.4
%if %{include_executable}
/usr/perl5/5.8.4
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
* Tue Nov 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.22 and modify spec file to build packages for perl-516 and perl-520
* Thu Nov 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.18
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Sat 16 Jun 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-584
* Sat 09 Jun 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit.
