%include Solaris.inc
%include default-depend.inc

%define build584 %( if [ -x /usr/perl5/5.8.4/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0

%define cpan_name ExtUtils-Constant
%define sfe_cpan_name extutils-constant

Summary:          generate XS code to import C header constants
Name:             SFEperl-%{sfe_cpan_name}
IPS_package_name: library/perl-5/%{sfe_cpan_name}
Version:          0.23
License:          unknown
URL:              https://metacpan.org/pod/ExtUtils::Constant
Source0:          http://cpan.metacpan.org/authors/id/N/NW/NWCLARK/ExtUtils-Constant-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
generate XS code to import C header constants

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          generate XS code to import C header constants
BuildRequires:    runtime/perl-584 = *
Requires:         runtime/perl-584 = *

%description 584
generate XS code to import C header constants
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          generate XS code to import C header constants
BuildRequires:    runtime/perl-512 = *
Requires:         runtime/perl-512 = *

%description 512
generate XS code to import C header constants
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          generate XS code to import C header constants
BuildRequires:    runtime/perl-516 = *
Requires:         runtime/perl-516 = *

%description 516
generate XS code to import C header constants
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          generate XS code to import C header constants
BuildRequires:    runtime/perl-520 = *
Requires:         runtime/perl-520 = *

%description 520
generate XS code to import C header constants
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
- fix IPS package names
- check existence of Makefile.PL and Build.PL instead of using variable
