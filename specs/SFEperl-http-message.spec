%include Solaris.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build526 %( if [ -x /usr/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build526jposug %( if [ -x /opt/jposug/perl5/5.26/bin/perl ]; then echo '1'; else echo '0'; fi)
%define enable_test %( if [ "x${PERL_DISABLE_TEST}" = 'xtrue' ]; then echo '0'; else echo '1'; fi )

%define include_executable 0
%define install_to_site_dir 0

%define cpan_name HTTP-Message
%define sfe_cpan_name http-message
%define ips_cpan_name http-message

Summary:               HTTP style message (base class)
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               6.18
IPS_component_version: 6.18
License:               perl_5
URL:                   https://metacpan.org/pod/HTTP::Message
Source0:               http://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Message-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
HTTP style message (base class)

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          HTTP style message (base class)
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/json-pp-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/time-local-584
BuildRequires:    library/perl-5/try-tiny-584
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/carp-584
BuildRequires:    library/perl-5/compress-raw-zlib-584
BuildRequires:    library/perl-5/encode-584
BuildRequires:    library/perl-5/encode-locale-584
BuildRequires:    library/perl-5/exporter-584
BuildRequires:    library/perl-5/http-date-584
BuildRequires:    library/perl-5/io-compress-bzip2-584
BuildRequires:    library/perl-5/io-compress-deflate-584
BuildRequires:    library/perl-5/io-compress-gzip-584
BuildRequires:    library/perl-5/io-html-584
BuildRequires:    library/perl-5/io-uncompress-bunzip2-584
BuildRequires:    library/perl-5/io-uncompress-gunzip-584
BuildRequires:    library/perl-5/io-uncompress-inflate-584
BuildRequires:    library/perl-5/io-uncompress-rawinflate-584
BuildRequires:    library/perl-5/lwp-mediatypes-584
BuildRequires:    library/perl-5/mime-base64-584
BuildRequires:    library/perl-5/mime-quotedprint-584
BuildRequires:    library/perl-5/storable-584
BuildRequires:    library/perl-5/uri-584
%endif
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-584
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
Requires:         library/perl-5/storable-584
Requires:         library/perl-5/uri-584

%description 584
HTTP style message (base class)
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          HTTP style message (base class)
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/json-pp-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/time-local-510
BuildRequires:    library/perl-5/try-tiny-510
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/carp-510
BuildRequires:    library/perl-5/compress-raw-zlib-510
BuildRequires:    library/perl-5/encode-510
BuildRequires:    library/perl-5/encode-locale-510
BuildRequires:    library/perl-5/exporter-510
BuildRequires:    library/perl-5/http-date-510
BuildRequires:    library/perl-5/io-compress-bzip2-510
BuildRequires:    library/perl-5/io-compress-deflate-510
BuildRequires:    library/perl-5/io-compress-gzip-510
BuildRequires:    library/perl-5/io-html-510
BuildRequires:    library/perl-5/io-uncompress-bunzip2-510
BuildRequires:    library/perl-5/io-uncompress-gunzip-510
BuildRequires:    library/perl-5/io-uncompress-inflate-510
BuildRequires:    library/perl-5/io-uncompress-rawinflate-510
BuildRequires:    library/perl-5/lwp-mediatypes-510
BuildRequires:    library/perl-5/mime-base64-510
BuildRequires:    library/perl-5/mime-quotedprint-510
BuildRequires:    library/perl-5/storable-510
BuildRequires:    library/perl-5/uri-510
%endif
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-510
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
Requires:         library/perl-5/storable-510
Requires:         library/perl-5/uri-510

%description 510
HTTP style message (base class)
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          HTTP style message (base class)
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/json-pp-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/time-local-512
BuildRequires:    library/perl-5/try-tiny-512
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/carp-512
BuildRequires:    library/perl-5/compress-raw-zlib-512
BuildRequires:    library/perl-5/encode-512
BuildRequires:    library/perl-5/encode-locale-512
BuildRequires:    library/perl-5/exporter-512
BuildRequires:    library/perl-5/http-date-512
BuildRequires:    library/perl-5/io-compress-bzip2-512
BuildRequires:    library/perl-5/io-compress-deflate-512
BuildRequires:    library/perl-5/io-compress-gzip-512
BuildRequires:    library/perl-5/io-html-512
BuildRequires:    library/perl-5/io-uncompress-bunzip2-512
BuildRequires:    library/perl-5/io-uncompress-gunzip-512
BuildRequires:    library/perl-5/io-uncompress-inflate-512
BuildRequires:    library/perl-5/io-uncompress-rawinflate-512
BuildRequires:    library/perl-5/lwp-mediatypes-512
BuildRequires:    library/perl-5/mime-base64-512
BuildRequires:    library/perl-5/mime-quotedprint-512
BuildRequires:    library/perl-5/storable-512
BuildRequires:    library/perl-5/uri-512
%endif
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-512
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
Requires:         library/perl-5/storable-512
Requires:         library/perl-5/uri-512

%description 512
HTTP style message (base class)
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          HTTP style message (base class)
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/json-pp-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/time-local-516
BuildRequires:    library/perl-5/try-tiny-516
Requires:         library/perl-5/%{ips_cpan_name}
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/carp-516
BuildRequires:    library/perl-5/compress-raw-zlib-516
BuildRequires:    library/perl-5/encode-516
BuildRequires:    library/perl-5/encode-locale-516
BuildRequires:    library/perl-5/exporter-516
BuildRequires:    library/perl-5/http-date-516
BuildRequires:    library/perl-5/io-compress-bzip2-516
BuildRequires:    library/perl-5/io-compress-deflate-516
BuildRequires:    library/perl-5/io-compress-gzip-516
BuildRequires:    library/perl-5/io-html-516
BuildRequires:    library/perl-5/io-uncompress-bunzip2-516
BuildRequires:    library/perl-5/io-uncompress-gunzip-516
BuildRequires:    library/perl-5/io-uncompress-inflate-516
BuildRequires:    library/perl-5/io-uncompress-rawinflate-516
BuildRequires:    library/perl-5/lwp-mediatypes-516
BuildRequires:    library/perl-5/mime-base64-516
BuildRequires:    library/perl-5/mime-quotedprint-516
BuildRequires:    library/perl-5/storable-516
BuildRequires:    library/perl-5/uri-516
%endif
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-516
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
Requires:         library/perl-5/storable-516
Requires:         library/perl-5/uri-516

%description 516
HTTP style message (base class)
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          HTTP style message (base class)
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/extutils-makemaker-522
BuildRequires:    library/perl-5/json-pp-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/time-local-522
BuildRequires:    library/perl-5/try-tiny-522
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-522
BuildRequires:    library/perl-5/carp-522
BuildRequires:    library/perl-5/compress-raw-zlib-522
BuildRequires:    library/perl-5/encode-522
BuildRequires:    library/perl-5/encode-locale-522
BuildRequires:    library/perl-5/exporter-522
BuildRequires:    library/perl-5/http-date-522
BuildRequires:    library/perl-5/io-compress-bzip2-522
BuildRequires:    library/perl-5/io-compress-deflate-522
BuildRequires:    library/perl-5/io-compress-gzip-522
BuildRequires:    library/perl-5/io-html-522
BuildRequires:    library/perl-5/io-uncompress-bunzip2-522
BuildRequires:    library/perl-5/io-uncompress-gunzip-522
BuildRequires:    library/perl-5/io-uncompress-inflate-522
BuildRequires:    library/perl-5/io-uncompress-rawinflate-522
BuildRequires:    library/perl-5/lwp-mediatypes-522
BuildRequires:    library/perl-5/mime-base64-522
BuildRequires:    library/perl-5/mime-quotedprint-522
BuildRequires:    library/perl-5/storable-522
BuildRequires:    library/perl-5/uri-522
%endif
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-522
Requires:         library/perl-5/compress-raw-zlib-522
Requires:         library/perl-5/encode-522
Requires:         library/perl-5/encode-locale-522
Requires:         library/perl-5/exporter-522
Requires:         library/perl-5/http-date-522
Requires:         library/perl-5/io-compress-bzip2-522
Requires:         library/perl-5/io-compress-deflate-522
Requires:         library/perl-5/io-compress-gzip-522
Requires:         library/perl-5/io-html-522
Requires:         library/perl-5/io-uncompress-bunzip2-522
Requires:         library/perl-5/io-uncompress-gunzip-522
Requires:         library/perl-5/io-uncompress-inflate-522
Requires:         library/perl-5/io-uncompress-rawinflate-522
Requires:         library/perl-5/lwp-mediatypes-522
Requires:         library/perl-5/mime-base64-522
Requires:         library/perl-5/mime-quotedprint-522
Requires:         library/perl-5/storable-522
Requires:         library/perl-5/uri-522

%description 522
HTTP style message (base class)
%endif

%if %{build526}
%package 526
IPS_package_name: library/perl-5/%{ips_cpan_name}-526
Summary:          HTTP style message (base class)
BuildRequires:    runtime/perl-526 = *
BuildRequires:    library/perl-5/cpan-meta-526
BuildRequires:    library/perl-5/extutils-makemaker-526
BuildRequires:    library/perl-5/json-pp-526
BuildRequires:    library/perl-5/pathtools-526
BuildRequires:    library/perl-5/time-local-526
BuildRequires:    library/perl-5/try-tiny-526
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-526
BuildRequires:    library/perl-5/carp-526
BuildRequires:    library/perl-5/compress-raw-zlib-526
BuildRequires:    library/perl-5/encode-526
BuildRequires:    library/perl-5/encode-locale-526
BuildRequires:    library/perl-5/exporter-526
BuildRequires:    library/perl-5/http-date-526
BuildRequires:    library/perl-5/io-compress-bzip2-526
BuildRequires:    library/perl-5/io-compress-deflate-526
BuildRequires:    library/perl-5/io-compress-gzip-526
BuildRequires:    library/perl-5/io-html-526
BuildRequires:    library/perl-5/io-uncompress-bunzip2-526
BuildRequires:    library/perl-5/io-uncompress-gunzip-526
BuildRequires:    library/perl-5/io-uncompress-inflate-526
BuildRequires:    library/perl-5/io-uncompress-rawinflate-526
BuildRequires:    library/perl-5/lwp-mediatypes-526
BuildRequires:    library/perl-5/mime-base64-526
BuildRequires:    library/perl-5/mime-quotedprint-526
BuildRequires:    library/perl-5/storable-526
BuildRequires:    library/perl-5/uri-526
%endif
Requires:         runtime/perl-526 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-526
Requires:         library/perl-5/compress-raw-zlib-526
Requires:         library/perl-5/encode-526
Requires:         library/perl-5/encode-locale-526
Requires:         library/perl-5/exporter-526
Requires:         library/perl-5/http-date-526
Requires:         library/perl-5/io-compress-bzip2-526
Requires:         library/perl-5/io-compress-deflate-526
Requires:         library/perl-5/io-compress-gzip-526
Requires:         library/perl-5/io-html-526
Requires:         library/perl-5/io-uncompress-bunzip2-526
Requires:         library/perl-5/io-uncompress-gunzip-526
Requires:         library/perl-5/io-uncompress-inflate-526
Requires:         library/perl-5/io-uncompress-rawinflate-526
Requires:         library/perl-5/lwp-mediatypes-526
Requires:         library/perl-5/mime-base64-526
Requires:         library/perl-5/mime-quotedprint-526
Requires:         library/perl-5/storable-526
Requires:         library/perl-5/uri-526

%description 526
HTTP style message (base class)
%endif

%if %{build526jposug}
%package 526jposug
IPS_package_name: library/perl-5/%{ips_cpan_name}-526jposug
Summary:          HTTP style message (base class)
BuildRequires:    runtime/perl-526jposug = *
BuildRequires:    library/perl-5/cpan-meta-526jposug
BuildRequires:    library/perl-5/extutils-makemaker-526jposug
BuildRequires:    library/perl-5/json-pp-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/time-local-526jposug
BuildRequires:    library/perl-5/try-tiny-526jposug
%if %{enable_test}
BuildRequires:    library/perl-5/test-simple-526jposug
BuildRequires:    library/perl-5/carp-526jposug
BuildRequires:    library/perl-5/compress-raw-zlib-526jposug
BuildRequires:    library/perl-5/encode-526jposug
BuildRequires:    library/perl-5/encode-locale-526jposug
BuildRequires:    library/perl-5/exporter-526jposug
BuildRequires:    library/perl-5/http-date-526jposug
BuildRequires:    library/perl-5/io-compress-bzip2-526jposug
BuildRequires:    library/perl-5/io-compress-deflate-526jposug
BuildRequires:    library/perl-5/io-compress-gzip-526jposug
BuildRequires:    library/perl-5/io-html-526jposug
BuildRequires:    library/perl-5/io-uncompress-bunzip2-526jposug
BuildRequires:    library/perl-5/io-uncompress-gunzip-526jposug
BuildRequires:    library/perl-5/io-uncompress-inflate-526jposug
BuildRequires:    library/perl-5/io-uncompress-rawinflate-526jposug
BuildRequires:    library/perl-5/lwp-mediatypes-526jposug
BuildRequires:    library/perl-5/mime-base64-526jposug
BuildRequires:    library/perl-5/mime-quotedprint-526jposug
BuildRequires:    library/perl-5/storable-526jposug
BuildRequires:    library/perl-5/uri-526jposug
%endif
Requires:         runtime/perl-526jposug = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/carp-526jposug
Requires:         library/perl-5/compress-raw-zlib-526jposug
Requires:         library/perl-5/encode-526jposug
Requires:         library/perl-5/encode-locale-526jposug
Requires:         library/perl-5/exporter-526jposug
Requires:         library/perl-5/http-date-526jposug
Requires:         library/perl-5/io-compress-bzip2-526jposug
Requires:         library/perl-5/io-compress-deflate-526jposug
Requires:         library/perl-5/io-compress-gzip-526jposug
Requires:         library/perl-5/io-html-526jposug
Requires:         library/perl-5/io-uncompress-bunzip2-526jposug
Requires:         library/perl-5/io-uncompress-gunzip-526jposug
Requires:         library/perl-5/io-uncompress-inflate-526jposug
Requires:         library/perl-5/io-uncompress-rawinflate-526jposug
Requires:         library/perl-5/lwp-mediatypes-526jposug
Requires:         library/perl-5/mime-base64-526jposug
Requires:         library/perl-5/mime-quotedprint-526jposug
Requires:         library/perl-5/storable-526jposug
Requires:         library/perl-5/uri-526jposug

%description 526jposug
HTTP style message (base class)
%endif

%prep
%setup -q -n %{cpan_name}-%{version}
[ -d %{buildroot} ] && rm -rf %{buildroot}

%build
build_with_makefile.pl_for() {
    test=$2
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    perl_dir_prefix="${prefix}/perl5/${perl_ver}"
    bindir="${perl_dir_prefix}/bin"
    vendor_dir="${prefix}/perl5/vendor_perl/${perl_ver}"
    site_dir="${prefix}/perl5/site_perl/${perl_ver}"

    export PERL5LIB=${vendor_dir}
%if %{install_to_site_dir}
    perl_libdir="${site_dir}"
%else
    perl_libdir="${vendor_dir}"
%endif

    ${bindir}/perl Makefile.PL PREFIX=${prefix} \
                   DESTDIR=$RPM_BUILD_ROOT \
                   LIB=${perl_libdir}

    echo ${perl_ver} | egrep '5\.(84|12)' > /dev/null && bin64=0 || bin64=1
    if [ ${bin64} -eq 0 ]
    then
        export CC='cc -m32'
        export LD='cc -m32'
    else
        export CC='cc -m64'
        export LD='cc -m64'
    fi
    make CC="${CC}" LD="${LD}"
    [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || make test CC="${CC}" "LD=${LD}"
    make pure_install
}

build_with_build.pl_for() {
    test=$2
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    perl_dir_prefix="${prefix}/perl5/${perl_ver}"
    bindir="${perl_dir_prefix}/bin"
    vendor_dir="${prefix}/perl5/vendor_perl/${perl_ver}"
    site_dir="${prefix}/perl5/site_perl/${perl_ver}"

%if %{install_to_site_dir}
    installdir='site'
%else
    installdir='vendor'
%endif
    export PERL5LIB=${vendor_dir}
    ${bindir}/perl Build.PL \
                   --installdirs ${installdir} \
                   --destdir $RPM_BUILD_ROOT
    ${bindir}/perl ./Build
    [ "x${PERL_DISABLE_TEST}" = 'xtrue' ] || [ "x${test}" = 'xwithout_test' ] || ${bindir}/perl ./Build test
    ${bindir}/perl ./Build install --destdir $RPM_BUILD_ROOT
    ${bindir}/perl ./Build clean
}

modify_bin_dir() {
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    if [ -d $RPM_BUILD_ROOT/${prefix}/bin ]
    then
      [ -d ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver} ] || mkdir -p ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver}
      mv $RPM_BUILD_ROOT${prefix}/bin $RPM_BUILD_ROOT/${prefix}/perl5/${perl_ver}/bin
    fi
      
    if [ -d ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver}/bin ]
    then
        for i in ${RPM_BUILD_ROOT}${prefix}/perl5/${perl_ver}/bin/*
        do
            sed -i.bak -e "s!/usr/bin/env perl!${prefix}/perl5/${perl_ver}/bin/perl!" ${i}
            [ -f ${i}.bak] || rm -f ${i}.bak
        done
    fi
}

modify_man_dir() {
    if [ "x${1}" = 'x5.26jposug' ]
    then
        perl_ver=$(echo $1 | sed -e 's/jposug//')
        prefix=/opt/jposug
    else
        perl_ver=$1
        prefix=/usr
    fi

    if [ -d $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man ]
    then
        if [ -d $RPM_BUILD_ROOT%{_datadir}/man ]
        then
            rm -rf $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man
        else
            mkdir -p $RPM_BUILD_ROOT%{_datadir}
            mv $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man $RPM_BUILD_ROOT%{_datadir}/
            rm -rf $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}/man
        fi
        if [ %{include_executable} -eq 0 ]
        then
            rmdir $RPM_BUILD_ROOT${prefix}/perl5/${perl_ver}
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

%if %{build522}
build_for 5.22
%endif

%if %{build526}
build_for 5.26
%endif

%if %{build526jposug}
build_for 5.26jposug
%endif

%install
if [ -d $RPM_BUILD_ROOT%{_prefix}/man ]
then
    mkdir -p $RPM_BUILD_ROOT%{_datadir}
    mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
fi

if [ -d $RPM_BUILD_ROOT/opt/jposug/man ]
then
    if [ -d $RPM_BUILD_ROOT%{_datadir}/man ]
    then
        rm -rf $RPM_BUILD_ROOT/opt/jposug/man
    else
        [ -d $RPM_BUILD_ROOT%{_datadir} ] || mkdir -p $RPM_BUILD_ROOT%{_datadir}
        mv $RPM_BUILD_ROOT/opt/jposug/man $RPM_BUILD_ROOT%{_datadir}
    fi
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
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.8.4
%else
/usr/perl5/vendor_perl/5.8.4
%endif
%if %{include_executable}
/usr/perl5/5.8.4
%endif
%endif

%if %{build510}
%files 510
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.10
%else
/usr/perl5/vendor_perl/5.10
%endif
%if %{include_executable}
/usr/perl5/5.1.0
%endif
%endif

%if %{build512}
%files 512
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.12
%else
/usr/perl5/vendor_perl/5.12
%endif
%if %{include_executable}
/usr/perl5/5.12
%endif
%endif

%if %{build516}
%files 516
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.16
%else
/usr/perl5/vendor_perl/5.16
%endif
%if %{include_executable}
/usr/perl5/5.16
%endif
%endif

%if %{build522}
%files 522
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.22
%else
/usr/perl5/vendor_perl/5.22
%endif
%if %{include_executable}
/usr/perl5/5.22
%endif
%endif

%if %{build526}
%files 526
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %{install_to_site_dir}
/usr/perl5/site_perl/5.26
%else
/usr/perl5/vendor_perl/5.26
%endif
%if %{include_executable}
/usr/perl5/5.26
%endif
%endif

%if %{build526jposug}
%files 526jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
%if %{install_to_site_dir}
/opt/jposug/perl5/site_perl/5.26
%else
/opt/jposug/perl5/vendor_perl/5.26
%endif
%if %{include_executable}
/opt/jposug/perl5/5.26
%endif
%endif

%changelog
* Wed Jun 06 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.18 and add packages for perl-5{22,26{,jposug}}
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
