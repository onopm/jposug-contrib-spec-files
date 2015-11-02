%include Solaris.inc
%include default-depend.inc

%define build584 0
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name ExtUtils-MakeMaker
%define sfe_cpan_name extutils-makemaker

Summary:               Create a module Makefile
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               7.10
IPS_component_version: 7.10
License:               perl_5
URL:                   https://metacpan.org/pod/ExtUtils::MakeMaker
Source0:               http://cpan.metacpan.org/authors/id/B/BI/BINGOS/ExtUtils-MakeMaker-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Create a module Makefile

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/data-dumper-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/pod-man-584
Requires:         library/perl-5/encode-584
Requires:         library/perl-5/file-spec-584
Requires:         library/perl-5/file-basename-584
Requires:         library/perl-5/dirhandle-584

%description 584
Create a module Makefile
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/data-dumper-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/pod-man-512
Requires:         library/perl-5/encode-512
Requires:         library/perl-5/file-spec-512
Requires:         library/perl-5/file-basename-512
Requires:         library/perl-5/dirhandle-512

%description 512
Create a module Makefile
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/data-dumper-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/pod-man-516
Requires:         library/perl-5/encode-516
Requires:         library/perl-5/file-spec-516
Requires:         library/perl-5/file-basename-516
Requires:         library/perl-5/dirhandle-516

%description 516
Create a module Makefile
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{sfe_cpan_name}-520
Summary:          Create a module Makefile
BuildRequires:    runtime/perl-520 = *
Buildrequires:    library/perl-5/data-dumper-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/pod-man-520
Requires:         library/perl-5/encode-520
Requires:         library/perl-5/file-spec-520
Requires:         library/perl-5/file-basename-520
Requires:         library/perl-5/dirhandle-520

%description 520
Create a module Makefile
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
    # make test
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

  # modify_bin_dir $*
  rm -rf $RPM_BUILD_ROOT/usr/bin
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
%{_datadir}/man/man1
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
- bump to 7.10 and modify specfile to build packages for perl-516 and perl-520
* Mon Nov 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.64
* Thu Nov 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete man to avoid conflict
- add Requires and BuildRequires
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete some files to avoid confilict with SFEperl-cpan-meta
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete Manifest.pm to avoid conflit with SFEperl-extutils-manifest
- delete some files which conflict with SFEperl-file-copy-recursive
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add library/perl-5/parse-cpan-meta to BuildRequire
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires and BuildRequires
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires to avoid confilict with file-copy-recursive
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires library/perl-5/extutils-install
- export PERL5LIB to adjust @inc
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
