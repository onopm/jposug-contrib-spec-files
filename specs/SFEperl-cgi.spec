%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name CGI
%define sfe_cpan_name cgi
%define ips_cpan_name cgi

Summary:               Handle Common Gateway Interface requests and responses
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               4.35
IPS_component_version: 4.35
License:               perl_5
URL:                   https://metacpan.org/pod/CGI
Source0:               http://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Handle Common Gateway Interface requests and responses

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          Handle Common Gateway Interface requests and responses
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/test-deep-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/test-warn-584
BuildRequires:    library/perl-5/carp-584
BuildRequires:    library/perl-5/encode-584
BuildRequires:    library/perl-5/exporter-584
BuildRequires:    library/perl-5/file-temp-584
BuildRequires:    library/perl-5/html-parser-584
BuildRequires:    library/perl-5/parent-584
BuildRequires:    library/perl-5/pathtools-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-584
Requires:         library/perl-5/encode-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/file-temp-584
Requires:         library/perl-5/html-parser-584
Requires:         library/perl-5/parent-584
Requires:         library/perl-5/pathtools-584

%description 584
Handle Common Gateway Interface requests and responses
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          Handle Common Gateway Interface requests and responses
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/io-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/test-deep-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/test-warn-510
BuildRequires:    library/perl-5/carp-510
BuildRequires:    library/perl-5/encode-510
BuildRequires:    library/perl-5/exporter-510
BuildRequires:    library/perl-5/file-temp-510
BuildRequires:    library/perl-5/html-parser-510
BuildRequires:    library/perl-5/parent-510
BuildRequires:    library/perl-5/pathtools-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-510
Requires:         library/perl-5/encode-510
Requires:         library/perl-5/exporter-510
Requires:         library/perl-5/file-temp-510
Requires:         library/perl-5/html-parser-510
Requires:         library/perl-5/parent-510
Requires:         library/perl-5/pathtools-510

%description 510
Handle Common Gateway Interface requests and responses
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          Handle Common Gateway Interface requests and responses
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/test-deep-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/test-warn-512
BuildRequires:    library/perl-5/carp-512
BuildRequires:    library/perl-5/encode-512
BuildRequires:    library/perl-5/exporter-512
BuildRequires:    library/perl-5/file-temp-512
BuildRequires:    library/perl-5/html-parser-512
BuildRequires:    library/perl-5/parent-512
BuildRequires:    library/perl-5/pathtools-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-512
Requires:         library/perl-5/encode-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/file-temp-512
Requires:         library/perl-5/html-parser-512
Requires:         library/perl-5/parent-512
Requires:         library/perl-5/pathtools-512

%description 512
Handle Common Gateway Interface requests and responses
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          Handle Common Gateway Interface requests and responses
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/test-deep-516
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/test-warn-516
Requires:         library/perl-5/%{ips_cpan_name}
BuildRequires:    library/perl-5/carp-516
BuildRequires:    library/perl-5/encode-516
BuildRequires:    library/perl-5/exporter-516
BuildRequires:    library/perl-5/file-temp-516
BuildRequires:    library/perl-5/html-parser-516
BuildRequires:    library/perl-5/parent-516
BuildRequires:    library/perl-5/pathtools-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-516
Requires:         library/perl-5/encode-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/file-temp-516
Requires:         library/perl-5/html-parser-516
Requires:         library/perl-5/parent-516
Requires:         library/perl-5/pathtools-516

%description 516
Handle Common Gateway Interface requests and responses
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          Handle Common Gateway Interface requests and responses
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/extutils-makemaker-520
BuildRequires:    library/perl-5/io-520
BuildRequires:    library/perl-5/pathtools-520
BuildRequires:    library/perl-5/test-deep-520
BuildRequires:    library/perl-5/test-simple-520
BuildRequires:    library/perl-5/test-warn-520
BuildRequires:    library/perl-5/carp-520
BuildRequires:    library/perl-5/encode-520
BuildRequires:    library/perl-5/exporter-520
BuildRequires:    library/perl-5/file-temp-520
BuildRequires:    library/perl-5/html-parser-520
BuildRequires:    library/perl-5/parent-520
BuildRequires:    library/perl-5/pathtools-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-520
Requires:         library/perl-5/encode-520
Requires:         library/perl-5/exporter-520
Requires:         library/perl-5/file-temp-520
Requires:         library/perl-5/html-parser-520
Requires:         library/perl-5/parent-520
Requires:         library/perl-5/pathtools-520

%description 520
Handle Common Gateway Interface requests and responses
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          Handle Common Gateway Interface requests and responses
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/extutils-makemaker-522
BuildRequires:    library/perl-5/io-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/test-deep-522
BuildRequires:    library/perl-5/test-simple-522
BuildRequires:    library/perl-5/test-warn-522
BuildRequires:    library/perl-5/carp-522
BuildRequires:    library/perl-5/encode-522
BuildRequires:    library/perl-5/exporter-522
BuildRequires:    library/perl-5/file-temp-522
BuildRequires:    library/perl-5/html-parser-522
BuildRequires:    library/perl-5/parent-522
BuildRequires:    library/perl-5/pathtools-522
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-522
Requires:         library/perl-5/encode-522
Requires:         library/perl-5/exporter-522
Requires:         library/perl-5/file-temp-522
Requires:         library/perl-5/html-parser-522
Requires:         library/perl-5/parent-522
Requires:         library/perl-5/pathtools-522

%description 522
Handle Common Gateway Interface requests and responses
%endif


%prep
%setup -q -n %{cpan_name}-%{version}
[ -d %{buildroot} ] && rm -rf %{buildroot}

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

    echo ${perl_ver} | egrep '5\.(84|12)' > /dev/null
    if [ $? -eq 0 ]
    then
        make CC='cc -m32' LD='cc -m32'
        [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || make test CC='cc -m32' LD='cc -m32'
    else
        make CC='cc -m64' LD='cc -m64'
        [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || make test CC='cc -m64' LD='cc -m64'
    fi

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
    [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || ${bindir}/perl ./Build test
    ${bindir}/perl ./Build install --destdir $RPM_BUILD_ROOT
    ${bindir}/perl ./Build clean
}

modify_bin_dir() {
    perl_ver=$1
    if [ -d $RPM_BUILD_ROOT/usr/bin ]
    then
      [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver} ] || mkdir -p $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
      mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin
    fi
      
    if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin ]
    then
        for i in $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin/*
        do
            sed -i.bak -e "s/\/usr\/bin\/env ruby/\/usr\/perl5\/${perl-ver}\/bin\/ruby/" ${i}
            [ -f ${i}.bak] || rm -f ${i}.bak
        done
    fi
}

modify_man_dir() {
    perl_ver=$1
    if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man ]
    then
        if [ -d $RPM_BUILD_ROOT%{_datadir}/man ]
        then
            rm -rf $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man
        else
            mkdir -p $RPM_BUILD_ROOT%{_datadir}
            mv $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man $RPM_BUILD_ROOT%{_datadir}/
            rm -rf $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/man
        fi
        if [ %{include_executable} -eq 0 ]
        then
            rmdir $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
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

%if %{build522}
build_for 5.22
%endif

%install
if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]
then
    mkdir -p $RPM_BUILD_ROOT%{_datadir}
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

%if %{build522}
%files 522
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/perl5/vendor_perl/5.22
%if %{include_executable}
/usr/perl5/5.22
%endif
%endif

%changelog
* Fri Mar 17 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.35
* Fri Nov 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.22 and build packages for perl-510, perl-516 and perl-520
* Tue Jun 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
