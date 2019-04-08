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

%define cpan_name libwww-perl
%define sfe_cpan_name libwww-perl
%define ips_cpan_name lwp

Summary:               The World-Wide Web library for Perl
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               6.38
IPS_component_version: 6.38
License:               perl_5
URL:                   https://metacpan.org/pod/libwww::perl
Source0:               http://cpan.metacpan.org/authors/id/O/OA/OALDERS/libwww-perl-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
The World-Wide Web library for Perl

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          The World-Wide Web library for Perl
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/extutils-makemaker-584
BuildRequires:    library/perl-5/getopt-long-584
BuildRequires:    library/perl-5/json-pp-584
BuildRequires:    library/perl-5/pathtools-584
%if %{enable_test}
BuildRequires:    library/perl-5/test-fatal-584
BuildRequires:    library/perl-5/test-requiresinternet-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/authen-ntlm-584
BuildRequires:    library/perl-5/digest-md5-584
BuildRequires:    library/perl-5/encode-584
BuildRequires:    library/perl-5/encode-locale-584
BuildRequires:    library/perl-5/file-listing-584
BuildRequires:    library/perl-5/html-parser-584
BuildRequires:    library/perl-5/http-cookies-584
BuildRequires:    library/perl-5/http-daemon-584
BuildRequires:    library/perl-5/http-date-584
BuildRequires:    library/perl-5/http-message-584
BuildRequires:    library/perl-5/http-negotiate-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/io-select-584
BuildRequires:    library/perl-5/lwp-mediatypes-584
BuildRequires:    library/perl-5/lwp-protocol-https-584
BuildRequires:    library/perl-5/mime-base64-584
BuildRequires:    library/perl-5/net-ftp-584
BuildRequires:    library/perl-5/net-http-584
BuildRequires:    library/perl-5/scalar-list-utils-584
BuildRequires:    library/perl-5/try-tiny-584
BuildRequires:    library/perl-5/uri-584
BuildRequires:    library/perl-5/www-robotrules-584
%endif
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/authen-ntlm-584
Requires:         library/perl-5/digest-md5-584
Requires:         library/perl-5/encode-584
Requires:         library/perl-5/encode-locale-584
Requires:         library/perl-5/file-listing-584
Requires:         library/perl-5/html-parser-584
Requires:         library/perl-5/http-cookies-584
Requires:         library/perl-5/http-daemon-584
Requires:         library/perl-5/http-date-584
Requires:         library/perl-5/http-message-584
Requires:         library/perl-5/http-negotiate-584
Requires:         library/perl-5/io-584
Requires:         library/perl-5/io-select-584
Requires:         library/perl-5/lwp-mediatypes-584
Requires:         library/perl-5/lwp-protocol-https-584
Requires:         library/perl-5/mime-base64-584
Requires:         library/perl-5/net-ftp-584
Requires:         library/perl-5/net-http-584
Requires:         library/perl-5/scalar-list-utils-584
Requires:         library/perl-5/try-tiny-584
Requires:         library/perl-5/uri-584
Requires:         library/perl-5/www-robotrules-584

%description 584
The World-Wide Web library for Perl
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          The World-Wide Web library for Perl
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/extutils-makemaker-510
BuildRequires:    library/perl-5/getopt-long-510
BuildRequires:    library/perl-5/json-pp-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/test-fatal-510
BuildRequires:    library/perl-5/test-requiresinternet-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/authen-ntlm-510
BuildRequires:    library/perl-5/digest-md5-510
BuildRequires:    library/perl-5/encode-510
BuildRequires:    library/perl-5/encode-locale-510
BuildRequires:    library/perl-5/file-listing-510
BuildRequires:    library/perl-5/html-parser-510
BuildRequires:    library/perl-5/http-cookies-510
BuildRequires:    library/perl-5/http-daemon-510
BuildRequires:    library/perl-5/http-date-510
BuildRequires:    library/perl-5/http-message-510
BuildRequires:    library/perl-5/http-negotiate-510
BuildRequires:    library/perl-5/io-510
BuildRequires:    library/perl-5/io-select-510
BuildRequires:    library/perl-5/lwp-mediatypes-510
BuildRequires:    library/perl-5/lwp-protocol-https-510
BuildRequires:    library/perl-5/mime-base64-510
BuildRequires:    library/perl-5/net-ftp-510
BuildRequires:    library/perl-5/net-http-510
BuildRequires:    library/perl-5/scalar-list-utils-510
BuildRequires:    library/perl-5/try-tiny-510
BuildRequires:    library/perl-5/uri-510
BuildRequires:    library/perl-5/www-robotrules-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/authen-ntlm-510
Requires:         library/perl-5/digest-md5-510
Requires:         library/perl-5/encode-510
Requires:         library/perl-5/encode-locale-510
Requires:         library/perl-5/file-listing-510
Requires:         library/perl-5/html-parser-510
Requires:         library/perl-5/http-cookies-510
Requires:         library/perl-5/http-daemon-510
Requires:         library/perl-5/http-date-510
Requires:         library/perl-5/http-message-510
Requires:         library/perl-5/http-negotiate-510
Requires:         library/perl-5/io-510
Requires:         library/perl-5/io-select-510
Requires:         library/perl-5/lwp-mediatypes-510
Requires:         library/perl-5/lwp-protocol-https-510
Requires:         library/perl-5/mime-base64-510
Requires:         library/perl-5/net-ftp-510
Requires:         library/perl-5/net-http-510
Requires:         library/perl-5/scalar-list-utils-510
Requires:         library/perl-5/try-tiny-510
Requires:         library/perl-5/uri-510
Requires:         library/perl-5/www-robotrules-510

%description 510
The World-Wide Web library for Perl
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          The World-Wide Web library for Perl
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/extutils-makemaker-512
BuildRequires:    library/perl-5/getopt-long-512
BuildRequires:    library/perl-5/json-pp-512
BuildRequires:    library/perl-5/pathtools-512
%if %{enable_test}
BuildRequires:    library/perl-5/test-fatal-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/authen-ntlm-512
BuildRequires:    library/perl-5/digest-md5-512
BuildRequires:    library/perl-5/encode-512
BuildRequires:    library/perl-5/encode-locale-512
BuildRequires:    library/perl-5/file-listing-512
BuildRequires:    library/perl-5/html-parser-512
BuildRequires:    library/perl-5/http-cookies-512
BuildRequires:    library/perl-5/http-daemon-512
BuildRequires:    library/perl-5/http-date-512
BuildRequires:    library/perl-5/http-message-512
BuildRequires:    library/perl-5/http-negotiate-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/io-select-512
BuildRequires:    library/perl-5/lwp-mediatypes-512
BuildRequires:    library/perl-5/lwp-protocol-https-512
BuildRequires:    library/perl-5/mime-base64-512
BuildRequires:    library/perl-5/net-ftp-512
BuildRequires:    library/perl-5/net-http-512
BuildRequires:    library/perl-5/scalar-list-utils-512
BuildRequires:    library/perl-5/try-tiny-512
BuildRequires:    library/perl-5/uri-512
BuildRequires:    library/perl-5/www-robotrules-512
%endif
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/authen-ntlm-512
Requires:         library/perl-5/digest-md5-512
Requires:         library/perl-5/encode-512
Requires:         library/perl-5/encode-locale-512
Requires:         library/perl-5/file-listing-512
Requires:         library/perl-5/html-parser-512
Requires:         library/perl-5/http-cookies-512
Requires:         library/perl-5/http-daemon-512
Requires:         library/perl-5/http-date-512
Requires:         library/perl-5/http-message-512
Requires:         library/perl-5/http-negotiate-512
Requires:         library/perl-5/io-512
Requires:         library/perl-5/io-select-512
Requires:         library/perl-5/lwp-mediatypes-512
Requires:         library/perl-5/lwp-protocol-https-512
Requires:         library/perl-5/mime-base64-512
Requires:         library/perl-5/net-ftp-512
Requires:         library/perl-5/net-http-512
Requires:         library/perl-5/scalar-list-utils-512
Requires:         library/perl-5/try-tiny-512
Requires:         library/perl-5/uri-512
Requires:         library/perl-5/www-robotrules-512

%description 512
The World-Wide Web library for Perl
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          The World-Wide Web library for Perl
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/extutils-makemaker-516
BuildRequires:    library/perl-5/getopt-long-516
BuildRequires:    library/perl-5/json-pp-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/test-fatal-516
BuildRequires:    library/perl-5/test-requiresinternet-516
BuildRequires:    library/perl-5/test-simple-516
Requires:         library/perl-5/%{ips_cpan_name}
%if %{enable_test}
BuildRequires:    library/perl-5/authen-ntlm-516
BuildRequires:    library/perl-5/digest-md5-516
BuildRequires:    library/perl-5/encode-516
BuildRequires:    library/perl-5/encode-locale-516
BuildRequires:    library/perl-5/file-listing-516
BuildRequires:    library/perl-5/html-parser-516
BuildRequires:    library/perl-5/http-cookies-516
BuildRequires:    library/perl-5/http-daemon-516
BuildRequires:    library/perl-5/http-date-516
BuildRequires:    library/perl-5/http-message-516
BuildRequires:    library/perl-5/http-negotiate-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/io-select-516
BuildRequires:    library/perl-5/lwp-mediatypes-516
BuildRequires:    library/perl-5/lwp-protocol-https-516
BuildRequires:    library/perl-5/mime-base64-516
BuildRequires:    library/perl-5/net-ftp-516
BuildRequires:    library/perl-5/net-http-516
BuildRequires:    library/perl-5/scalar-list-utils-516
BuildRequires:    library/perl-5/try-tiny-516
BuildRequires:    library/perl-5/uri-516
BuildRequires:    library/perl-5/www-robotrules-516
%endif
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/authen-ntlm-516
Requires:         library/perl-5/digest-md5-516
Requires:         library/perl-5/encode-516
Requires:         library/perl-5/encode-locale-516
Requires:         library/perl-5/file-listing-516
Requires:         library/perl-5/html-parser-516
Requires:         library/perl-5/http-cookies-516
Requires:         library/perl-5/http-daemon-516
Requires:         library/perl-5/http-date-516
Requires:         library/perl-5/http-message-516
Requires:         library/perl-5/http-negotiate-516
Requires:         library/perl-5/io-516
Requires:         library/perl-5/io-select-516
Requires:         library/perl-5/lwp-mediatypes-516
Requires:         library/perl-5/lwp-protocol-https-516
Requires:         library/perl-5/mime-base64-516
Requires:         library/perl-5/net-ftp-516
Requires:         library/perl-5/net-http-516
Requires:         library/perl-5/scalar-list-utils-516
Requires:         library/perl-5/try-tiny-516
Requires:         library/perl-5/uri-516
Requires:         library/perl-5/www-robotrules-516

%description 516
The World-Wide Web library for Perl
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          The World-Wide Web library for Perl
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/extutils-makemaker-522
BuildRequires:    library/perl-5/getopt-long-522
BuildRequires:    library/perl-5/json-pp-522
BuildRequires:    library/perl-5/pathtools-522
%if %{enable_test}
BuildRequires:    library/perl-5/test-fatal-522
BuildRequires:    library/perl-5/test-requiresinternet-522
BuildRequires:    library/perl-5/test-simple-522
BuildRequires:    library/perl-5/authen-ntlm-522
BuildRequires:    library/perl-5/digest-md5-522
BuildRequires:    library/perl-5/encode-522
BuildRequires:    library/perl-5/encode-locale-522
BuildRequires:    library/perl-5/file-listing-522
BuildRequires:    library/perl-5/html-parser-522
BuildRequires:    library/perl-5/http-cookies-522
BuildRequires:    library/perl-5/http-daemon-522
BuildRequires:    library/perl-5/http-date-522
BuildRequires:    library/perl-5/http-message-522
BuildRequires:    library/perl-5/http-negotiate-522
BuildRequires:    library/perl-5/io-522
BuildRequires:    library/perl-5/io-select-522
BuildRequires:    library/perl-5/lwp-mediatypes-522
BuildRequires:    library/perl-5/lwp-protocol-https-522
BuildRequires:    library/perl-5/mime-base64-522
BuildRequires:    library/perl-5/net-ftp-522
BuildRequires:    library/perl-5/net-http-522
BuildRequires:    library/perl-5/scalar-list-utils-522
BuildRequires:    library/perl-5/try-tiny-522
BuildRequires:    library/perl-5/uri-522
BuildRequires:    library/perl-5/www-robotrules-522
%endif
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/authen-ntlm-522
Requires:         library/perl-5/digest-md5-522
Requires:         library/perl-5/encode-522
Requires:         library/perl-5/encode-locale-522
Requires:         library/perl-5/file-listing-522
Requires:         library/perl-5/html-parser-522
Requires:         library/perl-5/http-cookies-522
Requires:         library/perl-5/http-daemon-522
Requires:         library/perl-5/http-date-522
Requires:         library/perl-5/http-message-522
Requires:         library/perl-5/http-negotiate-522
Requires:         library/perl-5/io-522
Requires:         library/perl-5/io-select-522
Requires:         library/perl-5/lwp-mediatypes-522
Requires:         library/perl-5/lwp-protocol-https-522
Requires:         library/perl-5/mime-base64-522
Requires:         library/perl-5/net-ftp-522
Requires:         library/perl-5/net-http-522
Requires:         library/perl-5/scalar-list-utils-522
Requires:         library/perl-5/try-tiny-522
Requires:         library/perl-5/uri-522
Requires:         library/perl-5/www-robotrules-522

%description 522
The World-Wide Web library for Perl
%endif

%if %{build526}
%package 526
IPS_package_name: library/perl-5/%{ips_cpan_name}-526
Summary:          The World-Wide Web library for Perl
BuildRequires:    runtime/perl-526 = *
BuildRequires:    library/perl-5/cpan-meta-526
BuildRequires:    library/perl-5/extutils-makemaker-526
BuildRequires:    library/perl-5/getopt-long-526
BuildRequires:    library/perl-5/json-pp-526
BuildRequires:    library/perl-5/pathtools-526
BuildRequires:    library/perl-5/test-fatal-526
BuildRequires:    library/perl-5/test-requiresinternet-526
BuildRequires:    library/perl-5/test-simple-526
%if %{enable_test}
BuildRequires:    library/perl-5/authen-ntlm-526
BuildRequires:    library/perl-5/digest-md5-526
BuildRequires:    library/perl-5/encode-526
BuildRequires:    library/perl-5/encode-locale-526
BuildRequires:    library/perl-5/file-listing-526
BuildRequires:    library/perl-5/html-parser-526
BuildRequires:    library/perl-5/http-cookies-526
BuildRequires:    library/perl-5/http-daemon-526
BuildRequires:    library/perl-5/http-date-526
BuildRequires:    library/perl-5/http-message-526
BuildRequires:    library/perl-5/http-negotiate-526
BuildRequires:    library/perl-5/io-526
BuildRequires:    library/perl-5/io-select-526
BuildRequires:    library/perl-5/lwp-mediatypes-526
BuildRequires:    library/perl-5/lwp-protocol-https-526
BuildRequires:    library/perl-5/mime-base64-526
BuildRequires:    library/perl-5/net-ftp-526
BuildRequires:    library/perl-5/net-http-526
BuildRequires:    library/perl-5/scalar-list-utils-526
BuildRequires:    library/perl-5/try-tiny-526
BuildRequires:    library/perl-5/uri-526
BuildRequires:    library/perl-5/www-robotrules-526
%endif
Requires:         runtime/perl-526 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/authen-ntlm-526
Requires:         library/perl-5/digest-md5-526
Requires:         library/perl-5/encode-526
Requires:         library/perl-5/encode-locale-526
Requires:         library/perl-5/file-listing-526
Requires:         library/perl-5/html-parser-526
Requires:         library/perl-5/http-cookies-526
Requires:         library/perl-5/http-daemon-526
Requires:         library/perl-5/http-date-526
Requires:         library/perl-5/http-message-526
Requires:         library/perl-5/http-negotiate-526
Requires:         library/perl-5/io-526
Requires:         library/perl-5/io-select-526
Requires:         library/perl-5/lwp-mediatypes-526
Requires:         library/perl-5/lwp-protocol-https-526
Requires:         library/perl-5/mime-base64-526
Requires:         library/perl-5/net-ftp-526
Requires:         library/perl-5/net-http-526
Requires:         library/perl-5/scalar-list-utils-526
Requires:         library/perl-5/try-tiny-526
Requires:         library/perl-5/uri-526
Requires:         library/perl-5/www-robotrules-526

%description 526
The World-Wide Web library for Perl
%endif

%if %{build526jposug}
%package 526jposug
IPS_package_name: library/perl-5/%{ips_cpan_name}-526jposug
Summary:          The World-Wide Web library for Perl
BuildRequires:    runtime/perl-526jposug = *
BuildRequires:    library/perl-5/cpan-meta-526jposug
BuildRequires:    library/perl-5/extutils-makemaker-526jposug
BuildRequires:    library/perl-5/getopt-long-526jposug
BuildRequires:    library/perl-5/json-pp-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
%if %{enable_test}
BuildRequires:    library/perl-5/test-fatal-526jposug
BuildRequires:    library/perl-5/test-requiresinternet-526jposug
BuildRequires:    library/perl-5/test-simple-526jposug
BuildRequires:    library/perl-5/authen-ntlm-526jposug
BuildRequires:    library/perl-5/digest-md5-526jposug
BuildRequires:    library/perl-5/encode-526jposug
BuildRequires:    library/perl-5/encode-locale-526jposug
BuildRequires:    library/perl-5/file-listing-526jposug
BuildRequires:    library/perl-5/html-parser-526jposug
BuildRequires:    library/perl-5/http-cookies-526jposug
BuildRequires:    library/perl-5/http-daemon-526jposug
BuildRequires:    library/perl-5/http-date-526jposug
BuildRequires:    library/perl-5/http-message-526jposug
BuildRequires:    library/perl-5/http-negotiate-526jposug
BuildRequires:    library/perl-5/io-526jposug
BuildRequires:    library/perl-5/io-select-526jposug
BuildRequires:    library/perl-5/lwp-mediatypes-526jposug
BuildRequires:    library/perl-5/lwp-protocol-https-526jposug
BuildRequires:    library/perl-5/mime-base64-526jposug
BuildRequires:    library/perl-5/net-ftp-526jposug
BuildRequires:    library/perl-5/net-http-526jposug
BuildRequires:    library/perl-5/scalar-list-utils-526jposug
BuildRequires:    library/perl-5/try-tiny-526jposug
BuildRequires:    library/perl-5/uri-526jposug
BuildRequires:    library/perl-5/www-robotrules-526jposug
%endif
Requires:         runtime/perl-526jposug = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/authen-ntlm-526jposug
Requires:         library/perl-5/digest-md5-526jposug
Requires:         library/perl-5/encode-526jposug
Requires:         library/perl-5/encode-locale-526jposug
Requires:         library/perl-5/file-listing-526jposug
Requires:         library/perl-5/html-parser-526jposug
Requires:         library/perl-5/http-cookies-526jposug
Requires:         library/perl-5/http-daemon-526jposug
Requires:         library/perl-5/http-date-526jposug
Requires:         library/perl-5/http-message-526jposug
Requires:         library/perl-5/http-negotiate-526jposug
Requires:         library/perl-5/io-526jposug
Requires:         library/perl-5/io-select-526jposug
Requires:         library/perl-5/lwp-mediatypes-526jposug
Requires:         library/perl-5/lwp-protocol-https-526jposug
Requires:         library/perl-5/mime-base64-526jposug
Requires:         library/perl-5/net-ftp-526jposug
Requires:         library/perl-5/net-http-526jposug
Requires:         library/perl-5/scalar-list-utils-526jposug
Requires:         library/perl-5/try-tiny-526jposug
Requires:         library/perl-5/uri-526jposug
Requires:         library/perl-5/www-robotrules-526jposug

%description 526jposug
The World-Wide Web library for Perl
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
* Mon Apr 08 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.38
* Fri May 25 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.33 and build packages for perl-5{22,26{,jposug}}
* Sun Nov 15 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build packages for perl-510, perl-516 and perl-520
* Tue Nov 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.13
* Wed Jan 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Mon Dec 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Fri Sep 28 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Wed Sep 26 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
