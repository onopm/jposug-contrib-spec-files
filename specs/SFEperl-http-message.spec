%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build520 %( if [ -x /usr/perl5/5.20/bin/perl ]; then echo '1'; else echo '0'; fi)
%define include_executable 0

%define cpan_name HTTP-Message
%define sfe_cpan_name http-message
%define ips_cpan_name http-message

Summary:               HTTP style messages
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               6.11
IPS_component_version: 6.11
License:               perl_5
URL:                   https://metacpan.org/pod/HTTP::Message
Source0:               http://cpan.metacpan.org/authors/id/E/ET/ETHER/HTTP-Message-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
HTTP style messages

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          HTTP style messages
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/test-simple-584
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/compress-raw-zlib-584
Requires:         library/perl-5/encode-584
Requires:         library/perl-5/encode-locale-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/http-date-584
Requires:         library/perl-5/io-compress-bzip2-584
Requires:         library/perl-5/io-compress-deflate-584
Requires:         library/perl-5/io-compress-gzip-584
Requires:         library/perl-5/io-html-584
Requires:         library/perl-5/io-uncompress-bunzip2-584
Requires:         library/perl-5/io-uncompress-gunzip-584
Requires:         library/perl-5/io-uncompress-inflate-584
Requires:         library/perl-5/io-uncompress-rawinflate-584
Requires:         library/perl-5/lwp-mediatypes-584
Requires:         library/perl-5/mime-base64-584
Requires:         library/perl-5/mime-quotedprint-584
Requires:         library/perl-5/uri-584

%description 584
HTTP style messages
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          HTTP style messages
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/test-simple-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/compress-raw-zlib-510
Requires:         library/perl-5/encode-510
Requires:         library/perl-5/encode-locale-510
Requires:         library/perl-5/exporter-510
Requires:         library/perl-5/http-date-510
Requires:         library/perl-5/io-compress-bzip2-510
Requires:         library/perl-5/io-compress-deflate-510
Requires:         library/perl-5/io-compress-gzip-510
Requires:         library/perl-5/io-html-510
Requires:         library/perl-5/io-uncompress-bunzip2-510
Requires:         library/perl-5/io-uncompress-gunzip-510
Requires:         library/perl-5/io-uncompress-inflate-510
Requires:         library/perl-5/io-uncompress-rawinflate-510
Requires:         library/perl-5/lwp-mediatypes-510
Requires:         library/perl-5/mime-base64-510
Requires:         library/perl-5/mime-quotedprint-510
Requires:         library/perl-5/uri-510

%description 510
HTTP style messages
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          HTTP style messages
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/test-simple-512
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/compress-raw-zlib-512
Requires:         library/perl-5/encode-512
Requires:         library/perl-5/encode-locale-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/http-date-512
Requires:         library/perl-5/io-compress-bzip2-512
Requires:         library/perl-5/io-compress-deflate-512
Requires:         library/perl-5/io-compress-gzip-512
Requires:         library/perl-5/io-html-512
Requires:         library/perl-5/io-uncompress-bunzip2-512
Requires:         library/perl-5/io-uncompress-gunzip-512
Requires:         library/perl-5/io-uncompress-inflate-512
Requires:         library/perl-5/io-uncompress-rawinflate-512
Requires:         library/perl-5/lwp-mediatypes-512
Requires:         library/perl-5/mime-base64-512
Requires:         library/perl-5/mime-quotedprint-512
Requires:         library/perl-5/uri-512

%description 512
HTTP style messages
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          HTTP style messages
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/test-simple-516
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/compress-raw-zlib-516
Requires:         library/perl-5/encode-516
Requires:         library/perl-5/encode-locale-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/http-date-516
Requires:         library/perl-5/io-compress-bzip2-516
Requires:         library/perl-5/io-compress-deflate-516
Requires:         library/perl-5/io-compress-gzip-516
Requires:         library/perl-5/io-html-516
Requires:         library/perl-5/io-uncompress-bunzip2-516
Requires:         library/perl-5/io-uncompress-gunzip-516
Requires:         library/perl-5/io-uncompress-inflate-516
Requires:         library/perl-5/io-uncompress-rawinflate-516
Requires:         library/perl-5/lwp-mediatypes-516
Requires:         library/perl-5/mime-base64-516
Requires:         library/perl-5/mime-quotedprint-516
Requires:         library/perl-5/uri-516

%description 516
HTTP style messages
%endif

%if %{build520}
%package 520
IPS_package_name: library/perl-5/%{ips_cpan_name}-520
Summary:          HTTP style messages
BuildRequires:    runtime/perl-520 = *
BuildRequires:    library/perl-5/extutils-makemaker-520
BuildRequires:    library/perl-5/test-simple-520
Requires:         runtime/perl-520 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/compress-raw-zlib-520
Requires:         library/perl-5/encode-520
Requires:         library/perl-5/encode-locale-520
Requires:         library/perl-5/exporter-520
Requires:         library/perl-5/http-date-520
Requires:         library/perl-5/io-compress-bzip2-520
Requires:         library/perl-5/io-compress-deflate-520
Requires:         library/perl-5/io-compress-gzip-520
Requires:         library/perl-5/io-html-520
Requires:         library/perl-5/io-uncompress-bunzip2-520
Requires:         library/perl-5/io-uncompress-gunzip-520
Requires:         library/perl-5/io-uncompress-inflate-520
Requires:         library/perl-5/io-uncompress-rawinflate-520
Requires:         library/perl-5/lwp-mediatypes-520
Requires:         library/perl-5/mime-base64-520
Requires:         library/perl-5/mime-quotedprint-520
Requires:         library/perl-5/uri-520

%description 520
HTTP style messages
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
    [ x${test} = 'xwithout_test' ] || make test
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
    [ x${test} = 'xwithout_test' ] || ${bindir}/perl ./Build test
    ${bindir}/perl ./Build install --destdir $RPM_BUILD_ROOT
}

modify_bin_dir() {
    perl_ver=$1
    if [ -d $RPM_BUILD_ROOT/usr/bin ]
    then
      [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver} ] || mkdir -p $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
      mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/${perl_ver}/bin
    fi
      
    if [ -d $RPM_BUILD_ROOT/usr/perl5/${perl_ver}bin ]
    then
        for i in $RPM_BUILD_ROOT/usr/perl5/${perl_ver}bin/*
        do
            sed -ibak -e "s/\/usr\/bin\/env ruby/\/usr\/perl5\/${perl-ver}\/bin\/ruby/" ${I}
            [ -f ${i}.bak] || rm ${i}.bak
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
        rmdir $RPM_BUILD_ROOT/usr/perl5/${perl_ver}
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
build_for 5.16 without_test
%endif

%if %{build520}
build_for 5.20 without_test
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


%changelog
* Sat Nov 14 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packages for perl-510, perl-516 and perl-520
* Tue Nov 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.11
* Sun Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Thu Sep 27 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
