%include Solaris.inc

%define build584 0
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 1

%define cpan_name Net-SNMP
%define sfe_cpan_name net-snmp

Summary:               Object oriented interface to SNMP
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               6.0.1
IPS_component_version: 6.0.1
License:               perl_5
URL:                   https://metacpan.org/pod/Net::SNMP
Source0:               http://cpan.metacpan.org/authors/id/D/DT/DTOWN/Net-SNMP-v%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Object oriented interface to SNMP

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          Object oriented interface to SNMP
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/module-build-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/carp-584
Requires:         library/perl-5/crypt-des-584
Requires:         library/perl-5/crypt-rijndael-584
Requires:         library/perl-5/digest-hmac-584
Requires:         library/perl-5/digest-md5-584
Requires:         library/perl-5/digest-sha1-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/io-socket-584
Requires:         library/perl-5/math-bigint-584
Requires:         library/perl-5/socket6-584

%description 584
Object oriented interface to SNMP
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          Object oriented interface to SNMP
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/module-build-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/carp-512
Requires:         library/perl-5/crypt-des-512
Requires:         library/perl-5/crypt-rijndael-512
Requires:         library/perl-5/digest-hmac-512
Requires:         library/perl-5/digest-md5-512
Requires:         library/perl-5/digest-sha1-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/io-socket-512
Requires:         library/perl-5/math-bigint-512
Requires:         library/perl-5/socket6-512

%description 512
Object oriented interface to SNMP
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          Object oriented interface to SNMP
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/module-build-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/carp-516
Requires:         library/perl-5/crypt-des-516
Requires:         library/perl-5/crypt-rijndael-516
Requires:         library/perl-5/digest-hmac-516
Requires:         library/perl-5/digest-md5-516
Requires:         library/perl-5/digest-sha1-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/io-socket-516
Requires:         library/perl-5/math-bigint-516
Requires:         library/perl-5/socket6-516

%description 516
Object oriented interface to SNMP
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          Object oriented interface to SNMP
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/module-build-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/carp-520
Requires:         library/perl-5/crypt-des-520
Requires:         library/perl-5/crypt-rijndael-520
Requires:         library/perl-5/digest-hmac-520
Requires:         library/perl-5/digest-md5-520
Requires:         library/perl-5/digest-sha1-520
Requires:         library/perl-5/exporter-520
Requires:         library/perl-5/io-socket-520
Requires:         library/perl-5/math-bigint-520
Requires:         library/perl-5/socket6-520

%description 520
Object oriented interface to SNMP
%endif


%prep
%setup -q -n %{cpan_name}-v%{version}
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
    [ ${test} = 'without_test' ] || make test
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
    [ ${test} = 'without_test' ] || ${bindir}/perl ./Build test
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

modify_man_dir() {
  perl_ver=$1
  if [ -d $RPM_BUILD_ROOT/usr/perl/${perl_ver}/man ]
  then
      if [ -d $RPM_BUILD_ROOT%{_datadir}/man ]
      then
	  mkdir -p $RPM_BUILD_ROOT%{_datadir}/man
	  mv $RPM_BUILD_ROOT/usr/perl/${perl_ver}/man/* $RPM_BUILD_ROOT%{_datadir}/man
      else
	  rm -rf $RPM_BUILD_ROOT%{_datadir}/man
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
# mkdir -p $RPM_BUILD_ROOT%{_datadir}
# if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]
# then
#     mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
# fi
# if [ -d $RPM_BUILD_ROOT%{_datadir}/man/man3 ]
# then
#     mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl
# fi

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

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
* Wed Nov 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packages for perl-516 and perl-520
* Mon Feb 11 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix version
* Sun Feb 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add %attr
* Sun Jan 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
