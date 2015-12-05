%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name Filesys-Notify-Simple
%define sfe_cpan_name filesys-notify-simple

Summary:               Simple and dumb file system watcher
Name:                  SFEperl-fs-notify-simple
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               0.12
IPS_component_version: 0.12
License:               perl_5
URL:                   https://metacpan.org/pod/Filesys::Notify::Simple
Source0:               http://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Filesys-Notify-Simple-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Simple and dumb file system watcher

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          Simple and dumb file system watcher
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/file-temp-584
BuildRequires:    library/perl-5/test-sharedfork-584
BuildRequires:    library/perl-5/test-simple-584
Requires:         runtime/perl-584 = *

%description 584
Simple and dumb file system watcher
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{sfe_cpan_name}-510
Summary:          Simple and dumb file system watcher
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/file-temp-510
BuildRequires:    library/perl-5/test-sharedfork-510
BuildRequires:    library/perl-5/test-simple-510
Requires:         runtime/perl-510 = *

%description 510
Simple and dumb file system watcher
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          Simple and dumb file system watcher
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/file-temp-512
BuildRequires:    library/perl-5/test-sharedfork-512
BuildRequires:    library/perl-5/test-simple-512
Requires:         runtime/perl-512 = *

%description 512
Simple and dumb file system watcher
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          Simple and dumb file system watcher
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/file-temp-516
BuildRequires:    library/perl-5/test-sharedfork-516
BuildRequires:    library/perl-5/test-simple-516
Requires:         runtime/perl-516 = *

%description 516
Simple and dumb file system watcher
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          Simple and dumb file system watcher
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/extutils-makemaker-520
BuildRequires:    library/perl-5/file-temp-520
BuildRequires:    library/perl-5/test-sharedfork-520
BuildRequires:    library/perl-5/test-simple-520
Requires:         runtime/perl-520 = *

%description 520
Simple and dumb file system watcher
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

build_for() {
  if [ -f Build.PL ];
  then
    build_with_build.pl_for $*
  elif [ -f Makefile.PL ];
  then
    build_with_makefile.pl_for $*
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
/usr/perl5/5.1.0
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
* Thu Nov 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.12 and build packages for perl-510, perl-516 and perl-520
* Sat Jun 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Name because old name is too long.
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
