%include Solaris.inc

%define build584 0
# build510 is for OpenIndiana,
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 1

%define cpan_name Net-Server
%define sfe_cpan_name net-server

Summary:               Extensible, general Perl server engine
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               2.008
IPS_component_version: 2.8
License:               unknown
URL:                   https://metacpan.org/pod/Net::Server
Source0:               http://cpan.metacpan.org/authors/id/R/RH/RHANDOM/Net-Server-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Extensible, general Perl server engine

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          Extensible, general Perl server engine
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/extutils-makemaker-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/io-socket-584
Requires:         library/perl-5/posix-584
Requires:         library/perl-5/socket-584
Requires:         library/perl-5/time-hires-584

%description 584
Extensible, general Perl server engine
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{sfe_cpan_name}-510
Summary:          Extensible, general Perl server engine
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/extutils-makemaker-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/io-socket-510
Requires:         library/perl-5/posix-510
Requires:         library/perl-5/socket-510
Requires:         library/perl-5/time-hires-510

%description 510
Extensible, general Perl server engine
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          Extensible, general Perl server engine
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/extutils-makemaker-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/io-socket-512
Requires:         library/perl-5/posix-512
Requires:         library/perl-5/socket-512
Requires:         library/perl-5/time-hires-512

%description 512
Extensible, general Perl server engine
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          Extensible, general Perl server engine
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/extutils-makemaker-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/io-socket-516
Requires:         library/perl-5/posix-516
Requires:         library/perl-5/socket-516
Requires:         library/perl-5/time-hires-516

%description 516
Extensible, general Perl server engine
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          Extensible, general Perl server engine
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/extutils-makemaker-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/io-socket-520
Requires:         library/perl-5/posix-520
Requires:         library/perl-5/socket-520
Requires:         library/perl-5/time-hires-520

%description 520
Extensible, general Perl server engine
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

%if %{build510}
%files 510
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.10
%if %{include_executable}
/usr/perl5/5.10
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
* Sat Nov 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packages for perl-516 and perl-520
* Sun Dec 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add '%include osdistro.inc' because %{osbuild} is defined in osdistro.inc
* Jul 21 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Bump up 2.008. Supported oi_151a9
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add %attr
* Sun Jan 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
