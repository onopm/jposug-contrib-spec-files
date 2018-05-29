%include Solaris.inc
%include default-depend.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name HTTP-Daemon
%define sfe_cpan_name http-daemon

Summary:               a simple http server class
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               6.01
IPS_component_version: 6.1
License:               perl_5
URL:                   https://metacpan.org/pod/HTTP::Daemon
Source0:               http://cpan.metacpan.org/authors/id/G/GA/GAAS/HTTP-Daemon-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
a simple http server class

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          a simple http server class
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/lwp-mediatypes-584
BuildRequires:    library/perl-5/http-message-584
BuildRequires:    library/perl-5/http-date-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/extutils-makemaker-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/lwp-mediatypes-584
Requires:         library/perl-5/http-message-584
Requires:         library/perl-5/http-date-584
Requires:         library/perl-5/io-584

%description 584
a simple http server class
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{sfe_cpan_name}-510
Summary:          a simple http server class
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/lwp-mediatypes-510
BuildRequires:    library/perl-5/http-message-510
BuildRequires:    library/perl-5/http-date-510
BuildRequires:    library/perl-5/io-510
BuildRequires:    library/perl-5/extutils-makemaker-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/lwp-mediatypes-510
Requires:         library/perl-5/http-message-510
Requires:         library/perl-5/http-date-510
Requires:         library/perl-5/io-510

%description 510
a simple http server class
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          a simple http server class
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/lwp-mediatypes-512
BuildRequires:    library/perl-5/http-message-512
BuildRequires:    library/perl-5/http-date-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/extutils-makemaker-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/lwp-mediatypes-512
Requires:         library/perl-5/http-message-512
Requires:         library/perl-5/http-date-512
Requires:         library/perl-5/io-512

%description 512
a simple http server class
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          a simple http server class
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/lwp-mediatypes-516
BuildRequires:    library/perl-5/http-message-516
BuildRequires:    library/perl-5/http-date-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/extutils-makemaker-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/lwp-mediatypes-516
Requires:         library/perl-5/http-message-516
Requires:         library/perl-5/http-date-516
Requires:         library/perl-5/io-516

%description 516
a simple http server class
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          a simple http server class
BuildRequires:    runtime/perl-520 = *
Buildrequires:    library/perl-5/lwp-mediatypes-520
Buildrequires:    library/perl-5/http-message-520
Buildrequires:    library/perl-5/http-date-520
Buildrequires:    library/perl-5/io-520
Buildrequires:    library/perl-5/extutils-makemaker-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/lwp-mediatypes-520
Requires:         library/perl-5/http-message-520
Requires:         library/perl-5/http-date-520
Requires:         library/perl-5/io-520

%description 520
a simple http server class
%endif


%prep
%setup -q -n %{cpan_name}-%{version}
rm -rf %{buildroot}

%build
build_with_makefile.pl_for() {
    perl_ver=$1
    bindir="/usr/perl5/${perl_ver}/bin"
    vendor_dir="/usr/perl5/vendor_perl/${perl_ver}"

    export PERL5LIB=${vendor_dir}
    ${bindir}/perl Makefile.PL PREFIX=%{_prefix} \
                   DESTDIR=$RPM_BUILD_ROOT \
                   LIB=${vendor_dir}
    make
    make test
    make pure_install
}

build_with_build.pl_for() {
    perl_ver=$1
    bindir="/usr/perl5/${perl_ver}/bin"
    vendor_dir="/usr/perl5/vendor_perl/${perl_ver}"

    export PERL5LIB=${vendor_dir}
    ${bindir}/perl Build.PL \
                   --installdirs vendor \
                   --destdir $RPM_BUILD_ROOT
    ${bindir}/perl ./Build
    ${bindir}/perl ./Build test
    ${bindir}/perl ./Build install --destdir $RPM_BUILD_ROOT
}

modify_bin_dir() {
  perl_ver=$1
  if [ -d $RPM_BUILD_ROOT/usr/bin ]
  then
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
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

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
* Fri Dec 18 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packages for perl-510, perl-516 and perl-520
* Mon Nov 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify spec file to make BuildRequires and Requires strict, and to build packages for perl-516 and perl-520
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
