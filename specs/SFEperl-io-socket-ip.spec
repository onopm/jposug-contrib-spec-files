%include Solaris.inc
%include default-depend.inc

%define build584 %( if [ -x /usr/perl5/5.8.4/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0

%define build_with_makefile_pl 1
%define build_with_build_pl 0

%define cpan_name IO-Socket-IP
%define sfe_cpan_name io-socket-ip

Summary:               Family-neutral IP socket supporting both IPv4 and IPv6
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl/%{sfe_cpan_name}
Version:               0.37
IPS_component_version: 0.37
License:               perl_5
URL:                   https://metacpan.org/pod/IO::Socket::IP
Source0:               http://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Family-neutral IP socket supporting both IPv4 and IPv6

%if %{build584}
%package 584
IPS_package_name: library/perl/%{sfe_cpan_name}-584
Summary:          Family-neutral IP socket supporting both IPv4 and IPv6
BuildRequires:    runtime/perl-584 = *
Requires:         library/perl/test-more-584
Requires:         runtime/perl-584 = *
Requires:         library/perl/socket-584
Requires:         library/perl/io-socket-584

%description 584
Family-neutral IP socket supporting both IPv4 and IPv6
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl/%{sfe_cpan_name}-512
Summary:          Family-neutral IP socket supporting both IPv4 and IPv6
BuildRequires:    runtime/perl-512 = *
Requires:         library/perl/test-more-512
Requires:         runtime/perl-512 = *
Requires:         library/perl/socket-512
Requires:         library/perl/io-socket-512

%description 512
Family-neutral IP socket supporting both IPv4 and IPv6
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl/%{sfe_cpan_name}-516
Summary:          Family-neutral IP socket supporting both IPv4 and IPv6
BuildRequires:    runtime/perl-516 = *
Requires:         library/perl/test-more-516
Requires:         runtime/perl-516 = *
Requires:         library/perl/socket-516
Requires:         library/perl/io-socket-516

%description 516
Family-neutral IP socket supporting both IPv4 and IPv6
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl/%{sfe_cpan_name}-520
Summary:          Family-neutral IP socket supporting both IPv4 and IPv6
BuildRequires:    runtime/perl-520 = *
Requires:         library/perl/test-more-520
Requires:         runtime/perl-520 = *
Requires:         library/perl/socket-520
Requires:         library/perl/io-socket-520

%description 520
Family-neutral IP socket supporting both IPv4 and IPv6
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
%if %{build_with_makefile_pl}
build_with_makefile.pl_for $*
%endif

%if %{build_with_build_pl}
build_with_build.pl_for $*
%endif

%if %{generate_executable}
modify_bin_dir $*
%endif
}


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
%if %{generate_executable}
/usr/perl5/5.8.4
%endif
%endif

%if %{build512}
%files 512
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.12
%if %{generate_executable}
/usr/perl5/5.12
%endif
%endif

%if %{build516}
%files 516
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.16
%if %{generate_executable}
/usr/perl5/5.16
%endif
%endif

%if %{build520}
%files 520
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.20
%if %{generate_executable}
/usr/perl5/5.20
%endif
%endif


%changelog
* Mon Nov 02 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
