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

%define cpan_name Module-Build-Tiny
%define sfe_cpan_name module-build-tiny
%define ips_cpan_name module-build-tiny

Summary:               A tiny replacement for Module::Build
Name:                  perl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{ips_cpan_name}
Version:               0.039
IPS_component_version: 0.39
License:               perl_5
URL:                   https://metacpan.org/pod/Module::Build::Tiny
Source0:               http://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
A tiny replacement for Module::Build

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{ips_cpan_name}-584
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-584 = *
BuildRequires:    library/perl-5/carp-584
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/data-dumper-584
BuildRequires:    library/perl-5/exporter-584
BuildRequires:    library/perl-5/extutils-cbuilder-584
BuildRequires:    library/perl-5/extutils-config-584
BuildRequires:    library/perl-5/extutils-helpers-584
BuildRequires:    library/perl-5/extutils-install-584
BuildRequires:    library/perl-5/extutils-installpaths-584
BuildRequires:    library/perl-5/extutils-parsexs-584
BuildRequires:    library/perl-5/file-path-584
BuildRequires:    library/perl-5/file-sharedir-584
BuildRequires:    library/perl-5/file-temp-584
BuildRequires:    library/perl-5/getopt-long-584
BuildRequires:    library/perl-5/io-584
BuildRequires:    library/perl-5/json-pp-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/podlators-584
BuildRequires:    library/perl-5/test-harness-584
BuildRequires:    library/perl-5/test-simple-584
BuildRequires:    library/perl-5/xsloader-584
%if %{enable_test}
BuildRequires:    library/perl-5/constant-584
BuildRequires:    library/perl-5/cpan-meta-584
BuildRequires:    library/perl-5/exporter-584
BuildRequires:    library/perl-5/extutils-cbuilder-584
BuildRequires:    library/perl-5/extutils-config-584
BuildRequires:    library/perl-5/extutils-helpers-584
BuildRequires:    library/perl-5/extutils-install-584
BuildRequires:    library/perl-5/extutils-installpaths-584
BuildRequires:    library/perl-5/extutils-parsexs-584
BuildRequires:    library/perl-5/file-path-584
BuildRequires:    library/perl-5/getopt-long-584
BuildRequires:    library/perl-5/json-pp-584
BuildRequires:    library/perl-5/local-lib-584
BuildRequires:    library/perl-5/pathtools-584
BuildRequires:    library/perl-5/podlators-584
BuildRequires:    library/perl-5/test-harness-584
%endif
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-584
Requires:         library/perl-5/cpan-meta-584
Requires:         library/perl-5/exporter-584
Requires:         library/perl-5/extutils-cbuilder-584
Requires:         library/perl-5/extutils-config-584
Requires:         library/perl-5/extutils-helpers-584
Requires:         library/perl-5/extutils-install-584
Requires:         library/perl-5/extutils-installpaths-584
Requires:         library/perl-5/extutils-parsexs-584
Requires:         library/perl-5/file-path-584
Requires:         library/perl-5/getopt-long-584
Requires:         library/perl-5/json-pp-584
Requires:         library/perl-5/local-lib-584
Requires:         library/perl-5/pathtools-584
Requires:         library/perl-5/podlators-584
Requires:         library/perl-5/test-harness-584

%description 584
A tiny replacement for Module::Build
%endif

%if %{build510}
%package 510
IPS_package_name: library/perl-5/%{ips_cpan_name}-510
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-510 = *
BuildRequires:    library/perl-5/carp-510
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/data-dumper-510
BuildRequires:    library/perl-5/exporter-510
BuildRequires:    library/perl-5/extutils-cbuilder-510
BuildRequires:    library/perl-5/extutils-config-510
BuildRequires:    library/perl-5/extutils-helpers-510
BuildRequires:    library/perl-5/extutils-install-510
BuildRequires:    library/perl-5/extutils-installpaths-510
BuildRequires:    library/perl-5/extutils-parsexs-510
BuildRequires:    library/perl-5/file-path-510
BuildRequires:    library/perl-5/file-sharedir-510
BuildRequires:    library/perl-5/file-temp-510
BuildRequires:    library/perl-5/getopt-long-510
BuildRequires:    library/perl-5/io-510
BuildRequires:    library/perl-5/json-pp-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/podlators-510
BuildRequires:    library/perl-5/test-harness-510
BuildRequires:    library/perl-5/test-simple-510
BuildRequires:    library/perl-5/xsloader-510
BuildRequires:    library/perl-5/constant-510
BuildRequires:    library/perl-5/cpan-meta-510
BuildRequires:    library/perl-5/exporter-510
BuildRequires:    library/perl-5/extutils-cbuilder-510
BuildRequires:    library/perl-5/extutils-config-510
BuildRequires:    library/perl-5/extutils-helpers-510
BuildRequires:    library/perl-5/extutils-install-510
BuildRequires:    library/perl-5/extutils-installpaths-510
BuildRequires:    library/perl-5/extutils-parsexs-510
BuildRequires:    library/perl-5/file-path-510
BuildRequires:    library/perl-5/getopt-long-510
BuildRequires:    library/perl-5/json-pp-510
BuildRequires:    library/perl-5/local-lib-510
BuildRequires:    library/perl-5/pathtools-510
BuildRequires:    library/perl-5/podlators-510
BuildRequires:    library/perl-5/test-harness-510
Requires:         runtime/perl-510 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-510
Requires:         library/perl-5/cpan-meta-510
Requires:         library/perl-5/exporter-510
Requires:         library/perl-5/extutils-cbuilder-510
Requires:         library/perl-5/extutils-config-510
Requires:         library/perl-5/extutils-helpers-510
Requires:         library/perl-5/extutils-install-510
Requires:         library/perl-5/extutils-installpaths-510
Requires:         library/perl-5/extutils-parsexs-510
Requires:         library/perl-5/file-path-510
Requires:         library/perl-5/getopt-long-510
Requires:         library/perl-5/json-pp-510
Requires:         library/perl-5/local-lib-510
Requires:         library/perl-5/pathtools-510
Requires:         library/perl-5/podlators-510
Requires:         library/perl-5/test-harness-510

%description 510
A tiny replacement for Module::Build
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{ips_cpan_name}-512
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-512 = *
BuildRequires:    library/perl-5/carp-512
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/data-dumper-512
BuildRequires:    library/perl-5/exporter-512
BuildRequires:    library/perl-5/extutils-cbuilder-512
BuildRequires:    library/perl-5/extutils-config-512
BuildRequires:    library/perl-5/extutils-helpers-512
BuildRequires:    library/perl-5/extutils-install-512
BuildRequires:    library/perl-5/extutils-installpaths-512
BuildRequires:    library/perl-5/extutils-parsexs-512
BuildRequires:    library/perl-5/file-path-512
BuildRequires:    library/perl-5/file-sharedir-512
BuildRequires:    library/perl-5/file-temp-512
BuildRequires:    library/perl-5/getopt-long-512
BuildRequires:    library/perl-5/io-512
BuildRequires:    library/perl-5/json-pp-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/podlators-512
BuildRequires:    library/perl-5/test-harness-512
BuildRequires:    library/perl-5/test-simple-512
BuildRequires:    library/perl-5/xsloader-512
%if %{enable_test}
BuildRequires:    library/perl-5/constant-512
BuildRequires:    library/perl-5/cpan-meta-512
BuildRequires:    library/perl-5/exporter-512
BuildRequires:    library/perl-5/extutils-cbuilder-512
BuildRequires:    library/perl-5/extutils-config-512
BuildRequires:    library/perl-5/extutils-helpers-512
BuildRequires:    library/perl-5/extutils-install-512
BuildRequires:    library/perl-5/extutils-installpaths-512
BuildRequires:    library/perl-5/extutils-parsexs-512
BuildRequires:    library/perl-5/file-path-512
BuildRequires:    library/perl-5/getopt-long-512
BuildRequires:    library/perl-5/json-pp-512
BuildRequires:    library/perl-5/local-lib-512
BuildRequires:    library/perl-5/pathtools-512
BuildRequires:    library/perl-5/podlators-512
BuildRequires:    library/perl-5/test-harness-512
%endif
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-512
Requires:         library/perl-5/cpan-meta-512
Requires:         library/perl-5/exporter-512
Requires:         library/perl-5/extutils-cbuilder-512
Requires:         library/perl-5/extutils-config-512
Requires:         library/perl-5/extutils-helpers-512
Requires:         library/perl-5/extutils-install-512
Requires:         library/perl-5/extutils-installpaths-512
Requires:         library/perl-5/extutils-parsexs-512
Requires:         library/perl-5/file-path-512
Requires:         library/perl-5/getopt-long-512
Requires:         library/perl-5/json-pp-512
Requires:         library/perl-5/local-lib-512
Requires:         library/perl-5/pathtools-512
Requires:         library/perl-5/podlators-512
Requires:         library/perl-5/test-harness-512

%description 512
A tiny replacement for Module::Build
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{ips_cpan_name}-516
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-516 = *
BuildRequires:    library/perl-5/carp-516
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/data-dumper-516
BuildRequires:    library/perl-5/exporter-516
BuildRequires:    library/perl-5/extutils-cbuilder-516
BuildRequires:    library/perl-5/extutils-config-516
BuildRequires:    library/perl-5/extutils-helpers-516
BuildRequires:    library/perl-5/extutils-install-516
BuildRequires:    library/perl-5/extutils-installpaths-516
BuildRequires:    library/perl-5/extutils-parsexs-516
BuildRequires:    library/perl-5/file-path-516
BuildRequires:    library/perl-5/file-sharedir-516
BuildRequires:    library/perl-5/file-temp-516
BuildRequires:    library/perl-5/getopt-long-516
BuildRequires:    library/perl-5/io-516
BuildRequires:    library/perl-5/json-pp-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/podlators-516
BuildRequires:    library/perl-5/test-harness-516
BuildRequires:    library/perl-5/test-simple-516
BuildRequires:    library/perl-5/xsloader-516
Requires:         library/perl-5/%{ips_cpan_name}
%if %{enable_test}
BuildRequires:    library/perl-5/constant-516
BuildRequires:    library/perl-5/cpan-meta-516
BuildRequires:    library/perl-5/exporter-516
BuildRequires:    library/perl-5/extutils-cbuilder-516
BuildRequires:    library/perl-5/extutils-config-516
BuildRequires:    library/perl-5/extutils-helpers-516
BuildRequires:    library/perl-5/extutils-install-516
BuildRequires:    library/perl-5/extutils-installpaths-516
BuildRequires:    library/perl-5/extutils-parsexs-516
BuildRequires:    library/perl-5/file-path-516
BuildRequires:    library/perl-5/getopt-long-516
BuildRequires:    library/perl-5/json-pp-516
BuildRequires:    library/perl-5/local-lib-516
BuildRequires:    library/perl-5/pathtools-516
BuildRequires:    library/perl-5/podlators-516
BuildRequires:    library/perl-5/test-harness-516
%endif
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-516
Requires:         library/perl-5/cpan-meta-516
Requires:         library/perl-5/exporter-516
Requires:         library/perl-5/extutils-cbuilder-516
Requires:         library/perl-5/extutils-config-516
Requires:         library/perl-5/extutils-helpers-516
Requires:         library/perl-5/extutils-install-516
Requires:         library/perl-5/extutils-installpaths-516
Requires:         library/perl-5/extutils-parsexs-516
Requires:         library/perl-5/file-path-516
Requires:         library/perl-5/getopt-long-516
Requires:         library/perl-5/json-pp-516
Requires:         library/perl-5/local-lib-516
Requires:         library/perl-5/pathtools-516
Requires:         library/perl-5/podlators-516
Requires:         library/perl-5/test-harness-516

%description 516
A tiny replacement for Module::Build
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{ips_cpan_name}-522
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-522 = *
BuildRequires:    library/perl-5/carp-522
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/data-dumper-522
BuildRequires:    library/perl-5/exporter-522
BuildRequires:    library/perl-5/extutils-cbuilder-522
BuildRequires:    library/perl-5/extutils-config-522
BuildRequires:    library/perl-5/extutils-helpers-522
BuildRequires:    library/perl-5/extutils-install-522
BuildRequires:    library/perl-5/extutils-installpaths-522
BuildRequires:    library/perl-5/extutils-parsexs-522
BuildRequires:    library/perl-5/file-path-522
BuildRequires:    library/perl-5/file-sharedir-522
BuildRequires:    library/perl-5/file-temp-522
BuildRequires:    library/perl-5/getopt-long-522
BuildRequires:    library/perl-5/io-522
BuildRequires:    library/perl-5/json-pp-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/podlators-522
BuildRequires:    library/perl-5/test-harness-522
BuildRequires:    library/perl-5/test-simple-522
BuildRequires:    library/perl-5/xsloader-522
%if %{enable_test}
BuildRequires:    library/perl-5/constant-522
BuildRequires:    library/perl-5/cpan-meta-522
BuildRequires:    library/perl-5/exporter-522
BuildRequires:    library/perl-5/extutils-cbuilder-522
BuildRequires:    library/perl-5/extutils-config-522
BuildRequires:    library/perl-5/extutils-helpers-522
BuildRequires:    library/perl-5/extutils-install-522
BuildRequires:    library/perl-5/extutils-installpaths-522
BuildRequires:    library/perl-5/extutils-parsexs-522
BuildRequires:    library/perl-5/file-path-522
BuildRequires:    library/perl-5/getopt-long-522
BuildRequires:    library/perl-5/json-pp-522
BuildRequires:    library/perl-5/local-lib-522
BuildRequires:    library/perl-5/pathtools-522
BuildRequires:    library/perl-5/podlators-522
BuildRequires:    library/perl-5/test-harness-522
%endif
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-522
Requires:         library/perl-5/cpan-meta-522
Requires:         library/perl-5/exporter-522
Requires:         library/perl-5/extutils-cbuilder-522
Requires:         library/perl-5/extutils-config-522
Requires:         library/perl-5/extutils-helpers-522
Requires:         library/perl-5/extutils-install-522
Requires:         library/perl-5/extutils-installpaths-522
Requires:         library/perl-5/extutils-parsexs-522
Requires:         library/perl-5/file-path-522
Requires:         library/perl-5/getopt-long-522
Requires:         library/perl-5/json-pp-522
Requires:         library/perl-5/local-lib-522
Requires:         library/perl-5/pathtools-522
Requires:         library/perl-5/podlators-522
Requires:         library/perl-5/test-harness-522

%description 522
A tiny replacement for Module::Build
%endif

%if %{build526}
%package 526
IPS_package_name: library/perl-5/%{ips_cpan_name}-526
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-526 = *
BuildRequires:    library/perl-5/carp-526
BuildRequires:    library/perl-5/cpan-meta-526
BuildRequires:    library/perl-5/data-dumper-526
BuildRequires:    library/perl-5/exporter-526
BuildRequires:    library/perl-5/extutils-cbuilder-526
BuildRequires:    library/perl-5/extutils-config-526
BuildRequires:    library/perl-5/extutils-helpers-526
BuildRequires:    library/perl-5/extutils-install-526
BuildRequires:    library/perl-5/extutils-installpaths-526
BuildRequires:    library/perl-5/extutils-parsexs-526
BuildRequires:    library/perl-5/file-path-526
BuildRequires:    library/perl-5/file-sharedir-526
BuildRequires:    library/perl-5/file-temp-526
BuildRequires:    library/perl-5/getopt-long-526
BuildRequires:    library/perl-5/io-526
BuildRequires:    library/perl-5/json-pp-526
BuildRequires:    library/perl-5/pathtools-526
BuildRequires:    library/perl-5/podlators-526
BuildRequires:    library/perl-5/test-harness-526
BuildRequires:    library/perl-5/test-simple-526
BuildRequires:    library/perl-5/xsloader-526
%if %{enable_test}
BuildRequires:    library/perl-5/constant-526
BuildRequires:    library/perl-5/cpan-meta-526
BuildRequires:    library/perl-5/exporter-526
BuildRequires:    library/perl-5/extutils-cbuilder-526
BuildRequires:    library/perl-5/extutils-config-526
BuildRequires:    library/perl-5/extutils-helpers-526
BuildRequires:    library/perl-5/extutils-install-526
BuildRequires:    library/perl-5/extutils-installpaths-526
BuildRequires:    library/perl-5/extutils-parsexs-526
BuildRequires:    library/perl-5/file-path-526
BuildRequires:    library/perl-5/getopt-long-526
BuildRequires:    library/perl-5/json-pp-526
BuildRequires:    library/perl-5/local-lib-526
BuildRequires:    library/perl-5/pathtools-526
BuildRequires:    library/perl-5/podlators-526
BuildRequires:    library/perl-5/test-harness-526
%endif
Requires:         runtime/perl-526 = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-526
Requires:         library/perl-5/cpan-meta-526
Requires:         library/perl-5/exporter-526
Requires:         library/perl-5/extutils-cbuilder-526
Requires:         library/perl-5/extutils-config-526
Requires:         library/perl-5/extutils-helpers-526
Requires:         library/perl-5/extutils-install-526
Requires:         library/perl-5/extutils-installpaths-526
Requires:         library/perl-5/extutils-parsexs-526
Requires:         library/perl-5/file-path-526
Requires:         library/perl-5/getopt-long-526
Requires:         library/perl-5/json-pp-526
Requires:         library/perl-5/local-lib-526
Requires:         library/perl-5/pathtools-526
Requires:         library/perl-5/podlators-526
Requires:         library/perl-5/test-harness-526

%description 526
A tiny replacement for Module::Build
%endif

%if %{build526jposug}
%package 526jposug
IPS_package_name: library/perl-5/%{ips_cpan_name}-526jposug
Summary:          A tiny replacement for Module::Build
BuildRequires:    runtime/perl-526jposug = *
BuildRequires:    library/perl-5/carp-526jposug
BuildRequires:    library/perl-5/cpan-meta-526jposug
BuildRequires:    library/perl-5/data-dumper-526jposug
BuildRequires:    library/perl-5/exporter-526jposug
BuildRequires:    library/perl-5/extutils-cbuilder-526jposug
BuildRequires:    library/perl-5/extutils-config-526jposug
BuildRequires:    library/perl-5/extutils-helpers-526jposug
BuildRequires:    library/perl-5/extutils-install-526jposug
BuildRequires:    library/perl-5/extutils-installpaths-526jposug
BuildRequires:    library/perl-5/extutils-parsexs-526jposug
BuildRequires:    library/perl-5/file-path-526jposug
BuildRequires:    library/perl-5/file-sharedir-526jposug
BuildRequires:    library/perl-5/file-temp-526jposug
BuildRequires:    library/perl-5/getopt-long-526jposug
BuildRequires:    library/perl-5/io-526jposug
BuildRequires:    library/perl-5/json-pp-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/podlators-526jposug
BuildRequires:    library/perl-5/test-harness-526jposug
BuildRequires:    library/perl-5/test-simple-526jposug
BuildRequires:    library/perl-5/xsloader-526jposug
%if %{enable_test}
BuildRequires:    library/perl-5/constant-526jposug
BuildRequires:    library/perl-5/cpan-meta-526jposug
BuildRequires:    library/perl-5/exporter-526jposug
BuildRequires:    library/perl-5/extutils-cbuilder-526jposug
BuildRequires:    library/perl-5/extutils-config-526jposug
BuildRequires:    library/perl-5/extutils-helpers-526jposug
BuildRequires:    library/perl-5/extutils-install-526jposug
BuildRequires:    library/perl-5/extutils-installpaths-526jposug
BuildRequires:    library/perl-5/extutils-parsexs-526jposug
BuildRequires:    library/perl-5/file-path-526jposug
BuildRequires:    library/perl-5/getopt-long-526jposug
BuildRequires:    library/perl-5/json-pp-526jposug
BuildRequires:    library/perl-5/local-lib-526jposug
BuildRequires:    library/perl-5/pathtools-526jposug
BuildRequires:    library/perl-5/podlators-526jposug
BuildRequires:    library/perl-5/test-harness-526jposug
%endif
Requires:         runtime/perl-526jposug = *
Requires:         library/perl-5/%{ips_cpan_name}
Requires:         library/perl-5/constant-526jposug
Requires:         library/perl-5/cpan-meta-526jposug
Requires:         library/perl-5/exporter-526jposug
Requires:         library/perl-5/extutils-cbuilder-526jposug
Requires:         library/perl-5/extutils-config-526jposug
Requires:         library/perl-5/extutils-helpers-526jposug
Requires:         library/perl-5/extutils-install-526jposug
Requires:         library/perl-5/extutils-installpaths-526jposug
Requires:         library/perl-5/extutils-parsexs-526jposug
Requires:         library/perl-5/file-path-526jposug
Requires:         library/perl-5/getopt-long-526jposug
Requires:         library/perl-5/json-pp-526jposug
Requires:         library/perl-5/local-lib-526jposug
Requires:         library/perl-5/pathtools-526jposug
Requires:         library/perl-5/podlators-526jposug
Requires:         library/perl-5/test-harness-526jposug

%description 526jposug
A tiny replacement for Module::Build
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
* Thu May 24 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add packages for perl-526{,jposug}
* Mon Jun 05 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build package for perl-522
* Sun Nov 15 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
