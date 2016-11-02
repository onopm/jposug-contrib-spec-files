%include Solaris.inc

%define build584 0
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name Module-Metadata
%define sfe_cpan_name module-metadata

Summary:               Gather package and POD information from perl module files
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               1.000027
IPS_component_version: 1.27
License:               perl_5
URL:                   https://metacpan.org/pod/Module::Metadata
Source0:               http://cpan.metacpan.org/authors/id/E/ET/ETHER/Module-Metadata-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Gather package and POD information from perl module files

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          Gather package and POD information from perl module files
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/data-dumper-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/file-path-584
BuildRequires:    library/perl-5/file-temp-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/test-simple-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/carp-584
Requires:         library/perl-5/fcntl-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/version-584

%description 584
Gather package and POD information from perl module files
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          Gather package and POD information from perl module files
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/data-dumper-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/file-path-512
BuildRequires:    library/perl-5/file-temp-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/test-simple-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/carp-512
Requires:         library/perl-5/fcntl-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/version-512

%description 512
Gather package and POD information from perl module files
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          Gather package and POD information from perl module files
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/data-dumper-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/file-path-516
BuildRequires:    library/perl-5/file-temp-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/test-simple-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/carp-516
Requires:         library/perl-5/fcntl-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/version-516

%description 516
Gather package and POD information from perl module files
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          Gather package and POD information from perl module files
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/cpan-meta-520
BuildRequires:    library/perl-5/data-dumper-520
BuildRequires:    library/perl-5/extutils-makemaker-520
BuildRequires:    library/perl-5/file-path-520
BuildRequires:    library/perl-5/file-temp-520
BuildRequires:    library/perl-5/io-520
BuildRequires:    library/perl-5/pathtools-520
BuildRequires:    library/perl-5/test-simple-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/carp-520
Requires:         library/perl-5/fcntl-520
Requires:         library/perl-5/pathtools-520
Requires:         library/perl-5/version-520

%description 520
Gather package and POD information from perl module files
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
* Tue Nov 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.000027 and build packages for perl-516 and perl-520
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512.
