%define version 5.26.3
%define major_version 5.26
%define version_suffix 526jposug
%define patchlevel 0

%define jposug_prefix /opt/jposug
%define prefix %{jposug_prefix}/perl5/%{major_version}
%define bindir %{prefix}/bin
%define libdir %{prefix}/lib
%define site_dir %{jposug_prefix}/perl5/site_perl/%{major_version}
%define vendor_dir %{jposug_prefix}/perl5/vendor_perl/%{major_version}

Name:                   SFEperl-%{version_suffix}
IPS_Package_Name:       jposug/runtime/perl-%{version_suffix}
Summary:                Perl 5 is a highly capable, feature-rich programming language
Version:                %{version}
Release:                %{patchlevel}
IPS_Component_Version:  %{version}.%{patchlevel}
License:                GPL
Source:                 https://www.cpan.org/src/5.0/perl-%{version}.tar.gz
Url:                    https://www.perl.org/

%description
Perl 5 is a highly capable, feature-rich programming language with over 30 years of development.

Requires: library/perl-5/encode-526jposug
Requires: library/perl-5/podlators-526jposug
Requires: library/perl-5/extutils-makemaker-526jposug
Requires: library/perl-5/io-compress-526jposug
Requires: library/perl-5/json-pp-526jposug
Requires: library/perl-5/extutils-parsexs-526jposug
Requires: library/perl-5/pod-parser-526jposug

%package encode
IPS_Package_Name:       library/perl-5/encode-526jposug
IPS_Component_Version:  4.9
Summary:        perl encode module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description encode
perl encode module

%package podlators
IPS_Package_Name:       library/perl-5/podlators-526jposug
IPS_Component_Version:  2.88
Summary:        perl podlators module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description podlators
perl podlators module

%package ext-mm
IPS_Package_Name:       library/perl-5/extutils-makemaker-526jposug
IPS_Component_Version:  2.88
Summary:        perl extutils-makemaker module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description ext-mm
perl extutils-makemaker module

#
%package io-compress
IPS_Package_Name:       library/perl-5/io-compress-526jposug
IPS_Component_Version:  2.74
Summary:        perl io-compress module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description io-compress
perl io-compress module

#
%package json-pp
IPS_Package_Name:       library/perl-5/json-pp-526jposug
IPS_Component_Version:  2.274
Summary:        perl json-pp module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description json-pp
perl json-pp module

#
%package ext-parsexs
IPS_Package_Name:       library/perl-5/extutils-parsexs-526jposug
IPS_Component_Version:  3.34
Summary:        perl extutils-parsexs module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description ext-parsexs
perl extutils-parsexs module

#
%package pod-parser
IPS_Package_Name:       library/perl-5/pod-parser-526jposug
IPS_Component_Version:  1.63
Summary:        perl extutils-parsexs module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description pod-parser
perl pod-parser module

#

%prep
%setup -n perl-%{version}

%build
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi


export CFLAGS='-m64 -xO4 -KPIC'

./Configure -de \
-Ulocincpth= \
-Dbin=%{bindir} \
-Dcc="${CC}" \
-Dcf_by="perl-bugs" \
-Dlibperl=libperl.so \
-Dmyhostname="localhost" \
-Dperl_static_inline="static" \
-Dprefix=%{prefix} \
-Dprivlib=%{libdir} \
-Dsitelib=%{site_dir} \
-Dsiteprefix=%{prefix} \
-Dvendorlib=%{vendor_dir} \
-Dvendorprefix=%{prefix} \
-Duseshrplib \
-Dusedtrace \
-Duse64bitall \
-Dusethreads \
-Dlibpth="/lib/64 /usr/lib/64" \
-Doptimize="${CFLAGS}"

make -j$CPUS
make -j$CPUS test

%install
[ -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /opt
%dir %attr (0755, root, bin) /opt/jposug
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/corelist
/opt/jposug/perl5/5.26/bin/cpan
/opt/jposug/perl5/5.26/bin/h2ph
/opt/jposug/perl5/5.26/bin/h2xs
/opt/jposug/perl5/5.26/bin/libnetcfg
/opt/jposug/perl5/5.26/bin/perl
/opt/jposug/perl5/5.26/bin/perl5.26.3
/opt/jposug/perl5/5.26/bin/perlbug
/opt/jposug/perl5/5.26/bin/perldoc
/opt/jposug/perl5/5.26/bin/perlivp
/opt/jposug/perl5/5.26/bin/perlthanks
/opt/jposug/perl5/5.26/bin/pl2pm
/opt/jposug/perl5/5.26/bin/pod2html
/opt/jposug/perl5/5.26/bin/pod2usage
/opt/jposug/perl5/5.26/bin/podchecker
/opt/jposug/perl5/5.26/bin/prove
/opt/jposug/perl5/5.26/bin/ptar
/opt/jposug/perl5/5.26/bin/ptardiff
/opt/jposug/perl5/5.26/bin/ptargrep
/opt/jposug/perl5/5.26/bin/shasum
/opt/jposug/perl5/5.26/bin/splain

%dir /opt/jposug/perl5/5.26/lib

/opt/jposug/perl5/5.26/lib/AnyDBM_File.pm
%dir /opt/jposug/perl5/5.26/lib/App
/opt/jposug/perl5/5.26/lib/App/*
%dir /opt/jposug/perl5/5.26/lib/Archive
/opt/jposug/perl5/5.26/lib/Archive/*
%dir /opt/jposug/perl5/5.26/lib/Attribute
/opt/jposug/perl5/5.26/lib/Attribute/*
/opt/jposug/perl5/5.26/lib/AutoLoader.pm
/opt/jposug/perl5/5.26/lib/AutoSplit.pm
%dir /opt/jposug/perl5/5.26/lib/B
/opt/jposug/perl5/5.26/lib/B/*
/opt/jposug/perl5/5.26/lib/Benchmark.pm
/opt/jposug/perl5/5.26/lib/CORE.pod
%dir /opt/jposug/perl5/5.26/lib/CPAN
/opt/jposug/perl5/5.26/lib/CPAN/*
/opt/jposug/perl5/5.26/lib/CPAN.pm
%dir /opt/jposug/perl5/5.26/lib/Carp
/opt/jposug/perl5/5.26/lib/Carp/*
/opt/jposug/perl5/5.26/lib/Carp.pm
%dir /opt/jposug/perl5/5.26/lib/Class
/opt/jposug/perl5/5.26/lib/Class/*
%dir /opt/jposug/perl5/5.26/lib/Config
/opt/jposug/perl5/5.26/lib/Config/*
/opt/jposug/perl5/5.26/lib/DB.pm
%dir /opt/jposug/perl5/5.26/lib/DBM_Filter
/opt/jposug/perl5/5.26/lib/DBM_Filter/*
/opt/jposug/perl5/5.26/lib/DBM_Filter.pm
%dir /opt/jposug/perl5/5.26/lib/Devel
/opt/jposug/perl5/5.26/lib/Devel/*
%dir /opt/jposug/perl5/5.26/lib/Digest
/opt/jposug/perl5/5.26/lib/Digest/*
/opt/jposug/perl5/5.26/lib/Digest.pm
/opt/jposug/perl5/5.26/lib/DirHandle.pm
/opt/jposug/perl5/5.26/lib/Dumpvalue.pm
/opt/jposug/perl5/5.26/lib/English.pm
/opt/jposug/perl5/5.26/lib/Env.pm
%dir /opt/jposug/perl5/5.26/lib/Exporter
/opt/jposug/perl5/5.26/lib/Exporter/*
/opt/jposug/perl5/5.26/lib/Exporter.pm

%dir /opt/jposug/perl5/5.26/lib/ExtUtils
%dir /opt/jposug/perl5/5.26/lib/ExtUtils/CBuilder
/opt/jposug/perl5/5.26/lib/ExtUtils/CBuilder/*
/opt/jposug/perl5/5.26/lib/ExtUtils/CBuilder.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Manifest.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Miniperl.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Packlist.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/typemap
%dir /opt/jposug/perl5/5.26/lib/ExtUtils/Constant
/opt/jposug/perl5/5.26/lib/ExtUtils/Constant/*
/opt/jposug/perl5/5.26/lib/ExtUtils/Constant.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Embed.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Install.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Installed.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/MANIFEST.SKIP
/opt/jposug/perl5/5.26/lib/Fatal.pm
%dir /opt/jposug/perl5/5.26/lib/File
/opt/jposug/perl5/5.26/lib/File/Basename.pm
/opt/jposug/perl5/5.26/lib/File/Compare.pm
/opt/jposug/perl5/5.26/lib/File/Copy.pm
/opt/jposug/perl5/5.26/lib/File/Fetch.pm
/opt/jposug/perl5/5.26/lib/File/Find.pm
/opt/jposug/perl5/5.26/lib/File/Path.pm
/opt/jposug/perl5/5.26/lib/File/Temp.pm
/opt/jposug/perl5/5.26/lib/File/stat.pm
/opt/jposug/perl5/5.26/lib/FileCache.pm
/opt/jposug/perl5/5.26/lib/FileHandle.pm
%dir /opt/jposug/perl5/5.26/lib/Filter
/opt/jposug/perl5/5.26/lib/Filter/*
/opt/jposug/perl5/5.26/lib/FindBin.pm
%dir /opt/jposug/perl5/5.26/lib/Getopt
/opt/jposug/perl5/5.26/lib/Getopt/*
%dir /opt/jposug/perl5/5.26/lib/HTTP
/opt/jposug/perl5/5.26/lib/HTTP/*
%dir /opt/jposug/perl5/5.26/lib/I18N
/opt/jposug/perl5/5.26/lib/I18N/*
%dir /opt/jposug/perl5/5.26/lib/IO
/opt/jposug/perl5/5.26/lib/IO/Zlib.pm
%dir /opt/jposug/perl5/5.26/lib/IO/Socket
/opt/jposug/perl5/5.26/lib/IO/Socket/IP.pm
%dir /opt/jposug/perl5/5.26/lib/IPC
/opt/jposug/perl5/5.26/lib/IPC/*
/opt/jposug/perl5/5.26/lib/Internals.pod
%dir /opt/jposug/perl5/5.26/lib/Locale
/opt/jposug/perl5/5.26/lib/Locale/*
%dir /opt/jposug/perl5/5.26/lib/Math
/opt/jposug/perl5/5.26/lib/Math/*
%dir /opt/jposug/perl5/5.26/lib/Memoize
/opt/jposug/perl5/5.26/lib/Memoize/*
/opt/jposug/perl5/5.26/lib/Memoize.pm
%dir /opt/jposug/perl5/5.26/lib/Module
/opt/jposug/perl5/5.26/lib/Module/*
/opt/jposug/perl5/5.26/lib/NEXT.pm
%dir /opt/jposug/perl5/5.26/lib/Net
/opt/jposug/perl5/5.26/lib/Net/*
%dir /opt/jposug/perl5/5.26/lib/Params
/opt/jposug/perl5/5.26/lib/Params/*
%dir /opt/jposug/perl5/5.26/lib/Parse
/opt/jposug/perl5/5.26/lib/Parse/*
%dir /opt/jposug/perl5/5.26/lib/Perl
/opt/jposug/perl5/5.26/lib/Perl/*
%dir /opt/jposug/perl5/5.26/lib/PerlIO
/opt/jposug/perl5/5.26/lib/PerlIO/*
/opt/jposug/perl5/5.26/lib/PerlIO.pm
%dir /opt/jposug/perl5/5.26/lib/Pod
/opt/jposug/perl5/5.26/lib/Pod/Checker.pm
/opt/jposug/perl5/5.26/lib/Pod/Escapes.pm
/opt/jposug/perl5/5.26/lib/Pod/Functions.pm
/opt/jposug/perl5/5.26/lib/Pod/Html.pm
%dir /opt/jposug/perl5/5.26/lib/Pod/Perldoc
/opt/jposug/perl5/5.26/lib/Pod/Perldoc/*
/opt/jposug/perl5/5.26/lib/Pod/Perldoc.pm
%dir /opt/jposug/perl5/5.26/lib/Pod/Simple
/opt/jposug/perl5/5.26/lib/Pod/Simple.pm
/opt/jposug/perl5/5.26/lib/Pod/Simple.pod
/opt/jposug/perl5/5.26/lib/Pod/Simple/*
%dir /opt/jposug/perl5/5.26/lib/Pod/Text
/opt/jposug/perl5/5.26/lib/Pod/Text/*
/opt/jposug/perl5/5.26/lib/Pod/Text.pm
/opt/jposug/perl5/5.26/lib/Pod/Usage.pm
/opt/jposug/perl5/5.26/lib/Safe.pm
%dir /opt/jposug/perl5/5.26/lib/Search
/opt/jposug/perl5/5.26/lib/Search/*
/opt/jposug/perl5/5.26/lib/SelectSaver.pm
/opt/jposug/perl5/5.26/lib/SelfLoader.pm
/opt/jposug/perl5/5.26/lib/Symbol.pm
%dir /opt/jposug/perl5/5.26/lib/TAP
/opt/jposug/perl5/5.26/lib/TAP/*
%dir /opt/jposug/perl5/5.26/lib/Term
/opt/jposug/perl5/5.26/lib/Term/*
%dir /opt/jposug/perl5/5.26/lib/Test
/opt/jposug/perl5/5.26/lib/Test/*
/opt/jposug/perl5/5.26/lib/Test.pm
%dir /opt/jposug/perl5/5.26/lib/Test2
/opt/jposug/perl5/5.26/lib/Test2/*
/opt/jposug/perl5/5.26/lib/Test2.pm
%dir /opt/jposug/perl5/5.26/lib/Text
/opt/jposug/perl5/5.26/lib/Text/*
%dir /opt/jposug/perl5/5.26/lib/Thread
/opt/jposug/perl5/5.26/lib/Thread/*
/opt/jposug/perl5/5.26/lib/Thread.pm
%dir /opt/jposug/perl5/5.26/lib/Tie
/opt/jposug/perl5/5.26/lib/Tie/*
%dir /opt/jposug/perl5/5.26/lib/Time
/opt/jposug/perl5/5.26/lib/Time/*
/opt/jposug/perl5/5.26/lib/UNIVERSAL.pm
%dir /opt/jposug/perl5/5.26/lib/Unicode
/opt/jposug/perl5/5.26/lib/Unicode/*
%dir /opt/jposug/perl5/5.26/lib/User
/opt/jposug/perl5/5.26/lib/User/*
/opt/jposug/perl5/5.26/lib/XSLoader.pm
/opt/jposug/perl5/5.26/lib/_charnames.pm
%dir /opt/jposug/perl5/5.26/lib/autodie
/opt/jposug/perl5/5.26/lib/autodie/*
/opt/jposug/perl5/5.26/lib/autodie.pm
/opt/jposug/perl5/5.26/lib/autouse.pm
/opt/jposug/perl5/5.26/lib/base.pm
/opt/jposug/perl5/5.26/lib/bigint.pm
/opt/jposug/perl5/5.26/lib/bignum.pm
/opt/jposug/perl5/5.26/lib/bigrat.pm
/opt/jposug/perl5/5.26/lib/blib.pm
/opt/jposug/perl5/5.26/lib/bytes.pm
/opt/jposug/perl5/5.26/lib/bytes_heavy.pl
/opt/jposug/perl5/5.26/lib/charnames.pm
/opt/jposug/perl5/5.26/lib/constant.pm
/opt/jposug/perl5/5.26/lib/deprecate.pm
/opt/jposug/perl5/5.26/lib/diagnostics.pm
/opt/jposug/perl5/5.26/lib/dumpvar.pl
%dir /opt/jposug/perl5/5.26/lib/encoding
/opt/jposug/perl5/5.26/lib/encoding/*
/opt/jposug/perl5/5.26/lib/experimental.pm
/opt/jposug/perl5/5.26/lib/feature.pm
/opt/jposug/perl5/5.26/lib/fields.pm
/opt/jposug/perl5/5.26/lib/filetest.pm
/opt/jposug/perl5/5.26/lib/if.pm
/opt/jposug/perl5/5.26/lib/integer.pm
/opt/jposug/perl5/5.26/lib/less.pm
/opt/jposug/perl5/5.26/lib/locale.pm
/opt/jposug/perl5/5.26/lib/meta_notation.pm
/opt/jposug/perl5/5.26/lib/ok.pm
/opt/jposug/perl5/5.26/lib/open.pm
/opt/jposug/perl5/5.26/lib/overload
/opt/jposug/perl5/5.26/lib/overload.pm
/opt/jposug/perl5/5.26/lib/overloading.pm
/opt/jposug/perl5/5.26/lib/parent.pm
/opt/jposug/perl5/5.26/lib/perl5db.pl
/opt/jposug/perl5/5.26/lib/perlfaq.pm
/opt/jposug/perl5/5.26/lib/pod
/opt/jposug/perl5/5.26/lib/sigtrap.pm
/opt/jposug/perl5/5.26/lib/sort.pm
/opt/jposug/perl5/5.26/lib/strict.pm
/opt/jposug/perl5/5.26/lib/subs.pm
/opt/jposug/perl5/5.26/lib/unicore
/opt/jposug/perl5/5.26/lib/utf8.pm
/opt/jposug/perl5/5.26/lib/utf8_heavy.pl
/opt/jposug/perl5/5.26/lib/vars.pm
%dir /opt/jposug/perl5/5.26/lib/version
/opt/jposug/perl5/5.26/lib/version/*
/opt/jposug/perl5/5.26/lib/version.pm
/opt/jposug/perl5/5.26/lib/version.pod
/opt/jposug/perl5/5.26/lib/vmsish.pm
%dir /opt/jposug/perl5/5.26/lib/warnings
/opt/jposug/perl5/5.26/lib/warnings/*
/opt/jposug/perl5/5.26/lib/warnings.pm


%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/.packlist
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/B
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/B/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/B.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/CORE
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/CORE/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Compress
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Compress/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Config.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Config.pod
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Config_git.pl
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Config_heavy.pl
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Cwd.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/DB_File.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Data
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Data/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Devel
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Devel/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Digest
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Digest/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/DynaLoader.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Errno.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Fcntl.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/File
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/File/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Filter
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Filter/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/GDBM_File.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Hash
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Hash/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/I18N
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/I18N/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/IO
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/IO/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/IO.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/IPC
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/IPC/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/List
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/List/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/MIME
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/MIME/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Math
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Math/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/NDBM_File.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/O.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/ODBM_File.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Opcode.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/POSIX.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/POSIX.pod
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/PerlIO
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/PerlIO/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/SDBM_File.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Scalar
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Scalar/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Socket.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Storable.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Sub
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Sub/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Sys
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Sys/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Tie
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Tie/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Time
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Time/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Unicode
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Unicode/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/arybase.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/attributes.pm
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/auto
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/auto/*
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/encoding.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/lib.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/mro.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/ops.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/re.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/threads
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/threads.pm

%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man1
/opt/jposug/perl5/5.26/man/man1/corelist.1
/opt/jposug/perl5/5.26/man/man1/cpan.1
/opt/jposug/perl5/5.26/man/man1/enc2xs.1
/opt/jposug/perl5/5.26/man/man1/encguess.1
/opt/jposug/perl5/5.26/man/man1/h2ph.1
/opt/jposug/perl5/5.26/man/man1/h2xs.1
/opt/jposug/perl5/5.26/man/man1/instmodsh.1
/opt/jposug/perl5/5.26/man/man1/libnetcfg.1
/opt/jposug/perl5/5.26/man/man1/perl.1
/opt/jposug/perl5/5.26/man/man1/perl5004delta.1
/opt/jposug/perl5/5.26/man/man1/perl5005delta.1
/opt/jposug/perl5/5.26/man/man1/perl5100delta.1
/opt/jposug/perl5/5.26/man/man1/perl5101delta.1
/opt/jposug/perl5/5.26/man/man1/perl5120delta.1
/opt/jposug/perl5/5.26/man/man1/perl5121delta.1
/opt/jposug/perl5/5.26/man/man1/perl5122delta.1
/opt/jposug/perl5/5.26/man/man1/perl5123delta.1
/opt/jposug/perl5/5.26/man/man1/perl5124delta.1
/opt/jposug/perl5/5.26/man/man1/perl5125delta.1
/opt/jposug/perl5/5.26/man/man1/perl5140delta.1
/opt/jposug/perl5/5.26/man/man1/perl5141delta.1
/opt/jposug/perl5/5.26/man/man1/perl5142delta.1
/opt/jposug/perl5/5.26/man/man1/perl5143delta.1
/opt/jposug/perl5/5.26/man/man1/perl5144delta.1
/opt/jposug/perl5/5.26/man/man1/perl5160delta.1
/opt/jposug/perl5/5.26/man/man1/perl5161delta.1
/opt/jposug/perl5/5.26/man/man1/perl5162delta.1
/opt/jposug/perl5/5.26/man/man1/perl5163delta.1
/opt/jposug/perl5/5.26/man/man1/perl5180delta.1
/opt/jposug/perl5/5.26/man/man1/perl5181delta.1
/opt/jposug/perl5/5.26/man/man1/perl5182delta.1
/opt/jposug/perl5/5.26/man/man1/perl5184delta.1
/opt/jposug/perl5/5.26/man/man1/perl5200delta.1
/opt/jposug/perl5/5.26/man/man1/perl5201delta.1
/opt/jposug/perl5/5.26/man/man1/perl5202delta.1
/opt/jposug/perl5/5.26/man/man1/perl5203delta.1
/opt/jposug/perl5/5.26/man/man1/perl5220delta.1
/opt/jposug/perl5/5.26/man/man1/perl5221delta.1
/opt/jposug/perl5/5.26/man/man1/perl5222delta.1
/opt/jposug/perl5/5.26/man/man1/perl5223delta.1
/opt/jposug/perl5/5.26/man/man1/perl5224delta.1
/opt/jposug/perl5/5.26/man/man1/perl5240delta.1
/opt/jposug/perl5/5.26/man/man1/perl5241delta.1
/opt/jposug/perl5/5.26/man/man1/perl5242delta.1
/opt/jposug/perl5/5.26/man/man1/perl5243delta.1
/opt/jposug/perl5/5.26/man/man1/perl5244delta.1
/opt/jposug/perl5/5.26/man/man1/perl5260delta.1
/opt/jposug/perl5/5.26/man/man1/perl5261delta.1
/opt/jposug/perl5/5.26/man/man1/perl5262delta.1
/opt/jposug/perl5/5.26/man/man1/perl5263delta.1
/opt/jposug/perl5/5.26/man/man1/perl5280delta.1
/opt/jposug/perl5/5.26/man/man1/perl561delta.1
/opt/jposug/perl5/5.26/man/man1/perl56delta.1
/opt/jposug/perl5/5.26/man/man1/perl581delta.1
/opt/jposug/perl5/5.26/man/man1/perl582delta.1
/opt/jposug/perl5/5.26/man/man1/perl583delta.1
/opt/jposug/perl5/5.26/man/man1/perl584delta.1
/opt/jposug/perl5/5.26/man/man1/perl585delta.1
/opt/jposug/perl5/5.26/man/man1/perl586delta.1
/opt/jposug/perl5/5.26/man/man1/perl587delta.1
/opt/jposug/perl5/5.26/man/man1/perl588delta.1
/opt/jposug/perl5/5.26/man/man1/perl589delta.1
/opt/jposug/perl5/5.26/man/man1/perl58delta.1
/opt/jposug/perl5/5.26/man/man1/perlaix.1
/opt/jposug/perl5/5.26/man/man1/perlamiga.1
/opt/jposug/perl5/5.26/man/man1/perlandroid.1
/opt/jposug/perl5/5.26/man/man1/perlapi.1
/opt/jposug/perl5/5.26/man/man1/perlapio.1
/opt/jposug/perl5/5.26/man/man1/perlartistic.1
/opt/jposug/perl5/5.26/man/man1/perlbook.1
/opt/jposug/perl5/5.26/man/man1/perlboot.1
/opt/jposug/perl5/5.26/man/man1/perlbot.1
/opt/jposug/perl5/5.26/man/man1/perlbs2000.1
/opt/jposug/perl5/5.26/man/man1/perlbug.1
/opt/jposug/perl5/5.26/man/man1/perlcall.1
/opt/jposug/perl5/5.26/man/man1/perlce.1
/opt/jposug/perl5/5.26/man/man1/perlcheat.1
/opt/jposug/perl5/5.26/man/man1/perlclib.1
/opt/jposug/perl5/5.26/man/man1/perlcn.1
/opt/jposug/perl5/5.26/man/man1/perlcommunity.1
/opt/jposug/perl5/5.26/man/man1/perlcygwin.1
/opt/jposug/perl5/5.26/man/man1/perldata.1
/opt/jposug/perl5/5.26/man/man1/perldbmfilter.1
/opt/jposug/perl5/5.26/man/man1/perldebguts.1
/opt/jposug/perl5/5.26/man/man1/perldebtut.1
/opt/jposug/perl5/5.26/man/man1/perldebug.1
/opt/jposug/perl5/5.26/man/man1/perldelta.1
/opt/jposug/perl5/5.26/man/man1/perldeprecation.1
/opt/jposug/perl5/5.26/man/man1/perldiag.1
/opt/jposug/perl5/5.26/man/man1/perldoc.1
/opt/jposug/perl5/5.26/man/man1/perldos.1
/opt/jposug/perl5/5.26/man/man1/perldsc.1
/opt/jposug/perl5/5.26/man/man1/perldtrace.1
/opt/jposug/perl5/5.26/man/man1/perlebcdic.1
/opt/jposug/perl5/5.26/man/man1/perlembed.1
/opt/jposug/perl5/5.26/man/man1/perlexperiment.1
/opt/jposug/perl5/5.26/man/man1/perlfaq.1
/opt/jposug/perl5/5.26/man/man1/perlfaq1.1
/opt/jposug/perl5/5.26/man/man1/perlfaq2.1
/opt/jposug/perl5/5.26/man/man1/perlfaq3.1
/opt/jposug/perl5/5.26/man/man1/perlfaq4.1
/opt/jposug/perl5/5.26/man/man1/perlfaq5.1
/opt/jposug/perl5/5.26/man/man1/perlfaq6.1
/opt/jposug/perl5/5.26/man/man1/perlfaq7.1
/opt/jposug/perl5/5.26/man/man1/perlfaq8.1
/opt/jposug/perl5/5.26/man/man1/perlfaq9.1
/opt/jposug/perl5/5.26/man/man1/perlfilter.1
/opt/jposug/perl5/5.26/man/man1/perlfork.1
/opt/jposug/perl5/5.26/man/man1/perlform.1
/opt/jposug/perl5/5.26/man/man1/perlfreebsd.1
/opt/jposug/perl5/5.26/man/man1/perlfunc.1
/opt/jposug/perl5/5.26/man/man1/perlgit.1
/opt/jposug/perl5/5.26/man/man1/perlglossary.1
/opt/jposug/perl5/5.26/man/man1/perlgpl.1
/opt/jposug/perl5/5.26/man/man1/perlguts.1
/opt/jposug/perl5/5.26/man/man1/perlhack.1
/opt/jposug/perl5/5.26/man/man1/perlhacktips.1
/opt/jposug/perl5/5.26/man/man1/perlhacktut.1
/opt/jposug/perl5/5.26/man/man1/perlhaiku.1
/opt/jposug/perl5/5.26/man/man1/perlhist.1
/opt/jposug/perl5/5.26/man/man1/perlhpux.1
/opt/jposug/perl5/5.26/man/man1/perlhurd.1
/opt/jposug/perl5/5.26/man/man1/perlintern.1
/opt/jposug/perl5/5.26/man/man1/perlinterp.1
/opt/jposug/perl5/5.26/man/man1/perlintro.1
/opt/jposug/perl5/5.26/man/man1/perliol.1
/opt/jposug/perl5/5.26/man/man1/perlipc.1
/opt/jposug/perl5/5.26/man/man1/perlirix.1
/opt/jposug/perl5/5.26/man/man1/perlivp.1
/opt/jposug/perl5/5.26/man/man1/perljp.1
/opt/jposug/perl5/5.26/man/man1/perlko.1
/opt/jposug/perl5/5.26/man/man1/perllexwarn.1
/opt/jposug/perl5/5.26/man/man1/perllinux.1
/opt/jposug/perl5/5.26/man/man1/perllocale.1
/opt/jposug/perl5/5.26/man/man1/perllol.1
/opt/jposug/perl5/5.26/man/man1/perlmacos.1
/opt/jposug/perl5/5.26/man/man1/perlmacosx.1
/opt/jposug/perl5/5.26/man/man1/perlmod.1
/opt/jposug/perl5/5.26/man/man1/perlmodinstall.1
/opt/jposug/perl5/5.26/man/man1/perlmodlib.1
/opt/jposug/perl5/5.26/man/man1/perlmodstyle.1
/opt/jposug/perl5/5.26/man/man1/perlmroapi.1
/opt/jposug/perl5/5.26/man/man1/perlnetware.1
/opt/jposug/perl5/5.26/man/man1/perlnewmod.1
/opt/jposug/perl5/5.26/man/man1/perlnumber.1
/opt/jposug/perl5/5.26/man/man1/perlobj.1
/opt/jposug/perl5/5.26/man/man1/perlootut.1
/opt/jposug/perl5/5.26/man/man1/perlop.1
/opt/jposug/perl5/5.26/man/man1/perlopenbsd.1
/opt/jposug/perl5/5.26/man/man1/perlopentut.1
/opt/jposug/perl5/5.26/man/man1/perlos2.1
/opt/jposug/perl5/5.26/man/man1/perlos390.1
/opt/jposug/perl5/5.26/man/man1/perlos400.1
/opt/jposug/perl5/5.26/man/man1/perlpacktut.1
/opt/jposug/perl5/5.26/man/man1/perlperf.1
/opt/jposug/perl5/5.26/man/man1/perlplan9.1
/opt/jposug/perl5/5.26/man/man1/perlpod.1
/opt/jposug/perl5/5.26/man/man1/perlpodspec.1
/opt/jposug/perl5/5.26/man/man1/perlpodstyle.1
/opt/jposug/perl5/5.26/man/man1/perlpolicy.1
/opt/jposug/perl5/5.26/man/man1/perlport.1
/opt/jposug/perl5/5.26/man/man1/perlpragma.1
/opt/jposug/perl5/5.26/man/man1/perlqnx.1
/opt/jposug/perl5/5.26/man/man1/perlre.1
/opt/jposug/perl5/5.26/man/man1/perlreapi.1
/opt/jposug/perl5/5.26/man/man1/perlrebackslash.1
/opt/jposug/perl5/5.26/man/man1/perlrecharclass.1
/opt/jposug/perl5/5.26/man/man1/perlref.1
/opt/jposug/perl5/5.26/man/man1/perlreftut.1
/opt/jposug/perl5/5.26/man/man1/perlreguts.1
/opt/jposug/perl5/5.26/man/man1/perlrepository.1
/opt/jposug/perl5/5.26/man/man1/perlrequick.1
/opt/jposug/perl5/5.26/man/man1/perlreref.1
/opt/jposug/perl5/5.26/man/man1/perlretut.1
/opt/jposug/perl5/5.26/man/man1/perlriscos.1
/opt/jposug/perl5/5.26/man/man1/perlrun.1
/opt/jposug/perl5/5.26/man/man1/perlsec.1
/opt/jposug/perl5/5.26/man/man1/perlsolaris.1
/opt/jposug/perl5/5.26/man/man1/perlsource.1
/opt/jposug/perl5/5.26/man/man1/perlstyle.1
/opt/jposug/perl5/5.26/man/man1/perlsub.1
/opt/jposug/perl5/5.26/man/man1/perlsymbian.1
/opt/jposug/perl5/5.26/man/man1/perlsyn.1
/opt/jposug/perl5/5.26/man/man1/perlsynology.1
/opt/jposug/perl5/5.26/man/man1/perlthanks.1
/opt/jposug/perl5/5.26/man/man1/perlthrtut.1
/opt/jposug/perl5/5.26/man/man1/perltie.1
/opt/jposug/perl5/5.26/man/man1/perltoc.1
/opt/jposug/perl5/5.26/man/man1/perltodo.1
/opt/jposug/perl5/5.26/man/man1/perltooc.1
/opt/jposug/perl5/5.26/man/man1/perltoot.1
/opt/jposug/perl5/5.26/man/man1/perltrap.1
/opt/jposug/perl5/5.26/man/man1/perltru64.1
/opt/jposug/perl5/5.26/man/man1/perltw.1
/opt/jposug/perl5/5.26/man/man1/perlunicode.1
/opt/jposug/perl5/5.26/man/man1/perlunicook.1
/opt/jposug/perl5/5.26/man/man1/perlunifaq.1
/opt/jposug/perl5/5.26/man/man1/perluniintro.1
/opt/jposug/perl5/5.26/man/man1/perluniprops.1
/opt/jposug/perl5/5.26/man/man1/perlunitut.1
/opt/jposug/perl5/5.26/man/man1/perlutil.1
/opt/jposug/perl5/5.26/man/man1/perlvar.1
/opt/jposug/perl5/5.26/man/man1/perlvms.1
/opt/jposug/perl5/5.26/man/man1/perlvos.1
/opt/jposug/perl5/5.26/man/man1/perlwin32.1
/opt/jposug/perl5/5.26/man/man1/perlxs.1
/opt/jposug/perl5/5.26/man/man1/perlxstut.1
/opt/jposug/perl5/5.26/man/man1/perlxstypemap.1
/opt/jposug/perl5/5.26/man/man1/piconv.1
/opt/jposug/perl5/5.26/man/man1/pl2pm.1
/opt/jposug/perl5/5.26/man/man1/pod2html.1
/opt/jposug/perl5/5.26/man/man1/pod2man.1
/opt/jposug/perl5/5.26/man/man1/pod2text.1
/opt/jposug/perl5/5.26/man/man1/pod2usage.1
/opt/jposug/perl5/5.26/man/man1/podchecker.1
/opt/jposug/perl5/5.26/man/man1/podselect.1
/opt/jposug/perl5/5.26/man/man1/prove.1
/opt/jposug/perl5/5.26/man/man1/ptar.1
/opt/jposug/perl5/5.26/man/man1/ptardiff.1
/opt/jposug/perl5/5.26/man/man1/ptargrep.1
/opt/jposug/perl5/5.26/man/man1/shasum.1
/opt/jposug/perl5/5.26/man/man1/splain.1
%dir /opt/jposug/perl5/5.26/man/man3
/opt/jposug/perl5/5.26/man/man3/AnyDBM_File.3
/opt/jposug/perl5/5.26/man/man3/App::Cpan.3
/opt/jposug/perl5/5.26/man/man3/App::Prove.3
/opt/jposug/perl5/5.26/man/man3/App::Prove::State.3
/opt/jposug/perl5/5.26/man/man3/App::Prove::State::Result.3
/opt/jposug/perl5/5.26/man/man3/App::Prove::State::Result::Test.3
/opt/jposug/perl5/5.26/man/man3/Archive::Tar.3
/opt/jposug/perl5/5.26/man/man3/Archive::Tar::File.3
/opt/jposug/perl5/5.26/man/man3/Attribute::Handlers.3
/opt/jposug/perl5/5.26/man/man3/AutoLoader.3
/opt/jposug/perl5/5.26/man/man3/AutoSplit.3
/opt/jposug/perl5/5.26/man/man3/B.3
/opt/jposug/perl5/5.26/man/man3/B::Concise.3
/opt/jposug/perl5/5.26/man/man3/B::Debug.3
/opt/jposug/perl5/5.26/man/man3/B::Deparse.3
/opt/jposug/perl5/5.26/man/man3/B::Op_private.3
/opt/jposug/perl5/5.26/man/man3/B::Showlex.3
/opt/jposug/perl5/5.26/man/man3/B::Terse.3
/opt/jposug/perl5/5.26/man/man3/B::Xref.3
/opt/jposug/perl5/5.26/man/man3/Benchmark.3
/opt/jposug/perl5/5.26/man/man3/CORE.3
/opt/jposug/perl5/5.26/man/man3/CPAN.3
/opt/jposug/perl5/5.26/man/man3/CPAN::API::HOWTO.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Debug.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Distroprefs.3
/opt/jposug/perl5/5.26/man/man3/CPAN::FirstTime.3
/opt/jposug/perl5/5.26/man/man3/CPAN::HandleConfig.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Kwalify.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::Converter.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::Feature.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::History.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::History::Meta_1_0.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::History::Meta_1_1.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::History::Meta_1_2.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::History::Meta_1_3.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::History::Meta_1_4.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::Merge.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::Prereqs.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::Requirements.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::Spec.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::Validator.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Meta::YAML.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Mirrors.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Nox.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Plugin.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Plugin::Specfile.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Queue.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Tarzip.3
/opt/jposug/perl5/5.26/man/man3/CPAN::Version.3
/opt/jposug/perl5/5.26/man/man3/Carp.3
/opt/jposug/perl5/5.26/man/man3/Class::Struct.3
/opt/jposug/perl5/5.26/man/man3/Compress::Raw::Bzip2.3
/opt/jposug/perl5/5.26/man/man3/Compress::Raw::Zlib.3
/opt/jposug/perl5/5.26/man/man3/Compress::Zlib.3
/opt/jposug/perl5/5.26/man/man3/Config.3
/opt/jposug/perl5/5.26/man/man3/Config::Extensions.3
/opt/jposug/perl5/5.26/man/man3/Config::Perl::V.3
/opt/jposug/perl5/5.26/man/man3/Cwd.3
/opt/jposug/perl5/5.26/man/man3/DB.3
/opt/jposug/perl5/5.26/man/man3/DBM_Filter.3
/opt/jposug/perl5/5.26/man/man3/DBM_Filter::compress.3
/opt/jposug/perl5/5.26/man/man3/DBM_Filter::encode.3
/opt/jposug/perl5/5.26/man/man3/DBM_Filter::int32.3
/opt/jposug/perl5/5.26/man/man3/DBM_Filter::null.3
/opt/jposug/perl5/5.26/man/man3/DBM_Filter::utf8.3
/opt/jposug/perl5/5.26/man/man3/DB_File.3
/opt/jposug/perl5/5.26/man/man3/Data::Dumper.3
/opt/jposug/perl5/5.26/man/man3/Devel::PPPort.3
/opt/jposug/perl5/5.26/man/man3/Devel::Peek.3
/opt/jposug/perl5/5.26/man/man3/Devel::SelfStubber.3
/opt/jposug/perl5/5.26/man/man3/Digest.3
/opt/jposug/perl5/5.26/man/man3/Digest::MD5.3
/opt/jposug/perl5/5.26/man/man3/Digest::SHA.3
/opt/jposug/perl5/5.26/man/man3/Digest::base.3
/opt/jposug/perl5/5.26/man/man3/Digest::file.3
/opt/jposug/perl5/5.26/man/man3/DirHandle.3
/opt/jposug/perl5/5.26/man/man3/Dumpvalue.3
/opt/jposug/perl5/5.26/man/man3/DynaLoader.3
/opt/jposug/perl5/5.26/man/man3/English.3
/opt/jposug/perl5/5.26/man/man3/Env.3
/opt/jposug/perl5/5.26/man/man3/Errno.3
/opt/jposug/perl5/5.26/man/man3/Exporter.3
/opt/jposug/perl5/5.26/man/man3/Exporter::Heavy.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Manifest.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Miniperl.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Mkbootstrap.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Mksymlists.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Packlist.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::XSSymSet.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::testlib.3
/opt/jposug/perl5/5.26/man/man3/Fatal.3
/opt/jposug/perl5/5.26/man/man3/Fcntl.3
/opt/jposug/perl5/5.26/man/man3/File::Basename.3
/opt/jposug/perl5/5.26/man/man3/File::Compare.3
/opt/jposug/perl5/5.26/man/man3/File::Copy.3
/opt/jposug/perl5/5.26/man/man3/File::DosGlob.3
/opt/jposug/perl5/5.26/man/man3/File::Fetch.3
/opt/jposug/perl5/5.26/man/man3/File::Find.3
/opt/jposug/perl5/5.26/man/man3/File::Glob.3
/opt/jposug/perl5/5.26/man/man3/File::GlobMapper.3
/opt/jposug/perl5/5.26/man/man3/File::Path.3
/opt/jposug/perl5/5.26/man/man3/File::Spec.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::AmigaOS.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::Cygwin.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::Epoc.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::Functions.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::Mac.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::OS2.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::Unix.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::VMS.3
/opt/jposug/perl5/5.26/man/man3/File::Spec::Win32.3
/opt/jposug/perl5/5.26/man/man3/File::Temp.3
/opt/jposug/perl5/5.26/man/man3/File::stat.3
/opt/jposug/perl5/5.26/man/man3/FileCache.3
/opt/jposug/perl5/5.26/man/man3/FileHandle.3
/opt/jposug/perl5/5.26/man/man3/Filter::Simple.3
/opt/jposug/perl5/5.26/man/man3/Filter::Util::Call.3
/opt/jposug/perl5/5.26/man/man3/FindBin.3
/opt/jposug/perl5/5.26/man/man3/GDBM_File.3
/opt/jposug/perl5/5.26/man/man3/Getopt::Long.3
/opt/jposug/perl5/5.26/man/man3/Getopt::Std.3
/opt/jposug/perl5/5.26/man/man3/HTTP::Tiny.3
/opt/jposug/perl5/5.26/man/man3/Hash::Util.3
/opt/jposug/perl5/5.26/man/man3/Hash::Util::FieldHash.3
/opt/jposug/perl5/5.26/man/man3/I18N::Collate.3
/opt/jposug/perl5/5.26/man/man3/I18N::LangTags.3
/opt/jposug/perl5/5.26/man/man3/I18N::LangTags::Detect.3
/opt/jposug/perl5/5.26/man/man3/I18N::LangTags::List.3
/opt/jposug/perl5/5.26/man/man3/I18N::Langinfo.3
/opt/jposug/perl5/5.26/man/man3/IO.3
/opt/jposug/perl5/5.26/man/man3/IO::Dir.3
/opt/jposug/perl5/5.26/man/man3/IO::File.3
/opt/jposug/perl5/5.26/man/man3/IO::Handle.3
/opt/jposug/perl5/5.26/man/man3/IO::Pipe.3
/opt/jposug/perl5/5.26/man/man3/IO::Poll.3
/opt/jposug/perl5/5.26/man/man3/IO::Seekable.3
/opt/jposug/perl5/5.26/man/man3/IO::Select.3
/opt/jposug/perl5/5.26/man/man3/IO::Socket.3
/opt/jposug/perl5/5.26/man/man3/IO::Socket::INET.3
/opt/jposug/perl5/5.26/man/man3/IO::Socket::IP.3
/opt/jposug/perl5/5.26/man/man3/IO::Socket::UNIX.3
/opt/jposug/perl5/5.26/man/man3/IO::Zlib.3
/opt/jposug/perl5/5.26/man/man3/IPC::Cmd.3
/opt/jposug/perl5/5.26/man/man3/IPC::Msg.3
/opt/jposug/perl5/5.26/man/man3/IPC::Open2.3
/opt/jposug/perl5/5.26/man/man3/IPC::Open3.3
/opt/jposug/perl5/5.26/man/man3/IPC::Semaphore.3
/opt/jposug/perl5/5.26/man/man3/IPC::SharedMem.3
/opt/jposug/perl5/5.26/man/man3/IPC::SysV.3
/opt/jposug/perl5/5.26/man/man3/Internals.3
/opt/jposug/perl5/5.26/man/man3/List::Util.3
/opt/jposug/perl5/5.26/man/man3/List::Util::XS.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::API.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::Changes.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::Country.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::Currency.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::LangExt.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::LangFam.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::LangVar.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::Language.3
/opt/jposug/perl5/5.26/man/man3/Locale::Codes::Script.3
/opt/jposug/perl5/5.26/man/man3/Locale::Country.3
/opt/jposug/perl5/5.26/man/man3/Locale::Currency.3
/opt/jposug/perl5/5.26/man/man3/Locale::Language.3
/opt/jposug/perl5/5.26/man/man3/Locale::Maketext.3
/opt/jposug/perl5/5.26/man/man3/Locale::Maketext::Cookbook.3
/opt/jposug/perl5/5.26/man/man3/Locale::Maketext::Guts.3
/opt/jposug/perl5/5.26/man/man3/Locale::Maketext::GutsLoader.3
/opt/jposug/perl5/5.26/man/man3/Locale::Maketext::Simple.3
/opt/jposug/perl5/5.26/man/man3/Locale::Maketext::TPJ13.3
/opt/jposug/perl5/5.26/man/man3/Locale::Script.3
/opt/jposug/perl5/5.26/man/man3/MIME::Base64.3
/opt/jposug/perl5/5.26/man/man3/MIME::QuotedPrint.3
/opt/jposug/perl5/5.26/man/man3/Math::BigFloat.3
/opt/jposug/perl5/5.26/man/man3/Math::BigInt.3
/opt/jposug/perl5/5.26/man/man3/Math::BigInt::Calc.3
/opt/jposug/perl5/5.26/man/man3/Math::BigInt::CalcEmu.3
/opt/jposug/perl5/5.26/man/man3/Math::BigInt::FastCalc.3
/opt/jposug/perl5/5.26/man/man3/Math::BigInt::Lib.3
/opt/jposug/perl5/5.26/man/man3/Math::BigRat.3
/opt/jposug/perl5/5.26/man/man3/Math::Complex.3
/opt/jposug/perl5/5.26/man/man3/Math::Trig.3
/opt/jposug/perl5/5.26/man/man3/Memoize.3
/opt/jposug/perl5/5.26/man/man3/Memoize::AnyDBM_File.3
/opt/jposug/perl5/5.26/man/man3/Memoize::Expire.3
/opt/jposug/perl5/5.26/man/man3/Memoize::ExpireFile.3
/opt/jposug/perl5/5.26/man/man3/Memoize::ExpireTest.3
/opt/jposug/perl5/5.26/man/man3/Memoize::NDBM_File.3
/opt/jposug/perl5/5.26/man/man3/Memoize::SDBM_File.3
/opt/jposug/perl5/5.26/man/man3/Memoize::Storable.3
/opt/jposug/perl5/5.26/man/man3/Module::CoreList.3
/opt/jposug/perl5/5.26/man/man3/Module::CoreList::Utils.3
/opt/jposug/perl5/5.26/man/man3/Module::Load.3
/opt/jposug/perl5/5.26/man/man3/Module::Load::Conditional.3
/opt/jposug/perl5/5.26/man/man3/Module::Loaded.3
/opt/jposug/perl5/5.26/man/man3/Module::Metadata.3
/opt/jposug/perl5/5.26/man/man3/NDBM_File.3
/opt/jposug/perl5/5.26/man/man3/NEXT.3
/opt/jposug/perl5/5.26/man/man3/Net::Cmd.3
/opt/jposug/perl5/5.26/man/man3/Net::Config.3
/opt/jposug/perl5/5.26/man/man3/Net::Domain.3
/opt/jposug/perl5/5.26/man/man3/Net::FTP.3
/opt/jposug/perl5/5.26/man/man3/Net::NNTP.3
/opt/jposug/perl5/5.26/man/man3/Net::Netrc.3
/opt/jposug/perl5/5.26/man/man3/Net::POP3.3
/opt/jposug/perl5/5.26/man/man3/Net::Ping.3
/opt/jposug/perl5/5.26/man/man3/Net::SMTP.3
/opt/jposug/perl5/5.26/man/man3/Net::Time.3
/opt/jposug/perl5/5.26/man/man3/Net::hostent.3
/opt/jposug/perl5/5.26/man/man3/Net::libnetFAQ.3
/opt/jposug/perl5/5.26/man/man3/Net::netent.3
/opt/jposug/perl5/5.26/man/man3/Net::protoent.3
/opt/jposug/perl5/5.26/man/man3/Net::servent.3
/opt/jposug/perl5/5.26/man/man3/O.3
/opt/jposug/perl5/5.26/man/man3/ODBM_File.3
/opt/jposug/perl5/5.26/man/man3/Opcode.3
/opt/jposug/perl5/5.26/man/man3/POSIX.3
/opt/jposug/perl5/5.26/man/man3/Params::Check.3
/opt/jposug/perl5/5.26/man/man3/Parse::CPAN::Meta.3
/opt/jposug/perl5/5.26/man/man3/Perl::OSType.3
/opt/jposug/perl5/5.26/man/man3/PerlIO.3
/opt/jposug/perl5/5.26/man/man3/PerlIO::encoding.3
/opt/jposug/perl5/5.26/man/man3/PerlIO::mmap.3
/opt/jposug/perl5/5.26/man/man3/PerlIO::scalar.3
/opt/jposug/perl5/5.26/man/man3/PerlIO::via.3
/opt/jposug/perl5/5.26/man/man3/PerlIO::via::QuotedPrint.3
/opt/jposug/perl5/5.26/man/man3/SDBM_File.3
/opt/jposug/perl5/5.26/man/man3/Safe.3
/opt/jposug/perl5/5.26/man/man3/Scalar::Util.3
/opt/jposug/perl5/5.26/man/man3/Search::Dict.3
/opt/jposug/perl5/5.26/man/man3/SelectSaver.3
/opt/jposug/perl5/5.26/man/man3/SelfLoader.3
/opt/jposug/perl5/5.26/man/man3/Socket.3
/opt/jposug/perl5/5.26/man/man3/Storable.3
/opt/jposug/perl5/5.26/man/man3/Sub::Util.3
/opt/jposug/perl5/5.26/man/man3/Symbol.3
/opt/jposug/perl5/5.26/man/man3/Sys::Hostname.3
/opt/jposug/perl5/5.26/man/man3/Sys::Syslog.3
/opt/jposug/perl5/5.26/man/man3/TAP::Base.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::Base.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::Color.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::Console.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::Console::ParallelSession.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::Console::Session.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::File.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::File::Session.3
/opt/jposug/perl5/5.26/man/man3/TAP::Formatter::Session.3
/opt/jposug/perl5/5.26/man/man3/TAP::Harness.3
/opt/jposug/perl5/5.26/man/man3/TAP::Harness::Beyond.3
/opt/jposug/perl5/5.26/man/man3/TAP::Harness::Env.3
/opt/jposug/perl5/5.26/man/man3/TAP::Object.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Aggregator.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Grammar.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Iterator.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Iterator::Array.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Iterator::Process.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Iterator::Stream.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::IteratorFactory.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Multiplexer.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::Bailout.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::Comment.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::Plan.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::Pragma.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::Test.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::Unknown.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::Version.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Result::YAML.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::ResultFactory.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Scheduler.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Scheduler::Job.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Scheduler::Spinner.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::Source.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::SourceHandler.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::SourceHandler::Executable.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::SourceHandler::File.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::SourceHandler::Handle.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::SourceHandler::Perl.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::SourceHandler::RawTAP.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::YAMLish::Reader.3
/opt/jposug/perl5/5.26/man/man3/TAP::Parser::YAMLish::Writer.3
/opt/jposug/perl5/5.26/man/man3/Term::ANSIColor.3
/opt/jposug/perl5/5.26/man/man3/Term::Cap.3
/opt/jposug/perl5/5.26/man/man3/Term::Complete.3
/opt/jposug/perl5/5.26/man/man3/Term::ReadLine.3
/opt/jposug/perl5/5.26/man/man3/Test.3
/opt/jposug/perl5/5.26/man/man3/Test2.3
/opt/jposug/perl5/5.26/man/man3/Test2::API.3
/opt/jposug/perl5/5.26/man/man3/Test2::API::Breakage.3
/opt/jposug/perl5/5.26/man/man3/Test2::API::Context.3
/opt/jposug/perl5/5.26/man/man3/Test2::API::Instance.3
/opt/jposug/perl5/5.26/man/man3/Test2::API::Stack.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Bail.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Diag.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Encoding.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Exception.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Generic.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Info.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Note.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Ok.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Plan.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Skip.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Subtest.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::TAP::Version.3
/opt/jposug/perl5/5.26/man/man3/Test2::Event::Waiting.3
/opt/jposug/perl5/5.26/man/man3/Test2::Formatter.3
/opt/jposug/perl5/5.26/man/man3/Test2::Formatter::TAP.3
/opt/jposug/perl5/5.26/man/man3/Test2::Hub.3
/opt/jposug/perl5/5.26/man/man3/Test2::Hub::Interceptor.3
/opt/jposug/perl5/5.26/man/man3/Test2::Hub::Interceptor::Terminator.3
/opt/jposug/perl5/5.26/man/man3/Test2::Hub::Subtest.3
/opt/jposug/perl5/5.26/man/man3/Test2::IPC.3
/opt/jposug/perl5/5.26/man/man3/Test2::IPC::Driver.3
/opt/jposug/perl5/5.26/man/man3/Test2::IPC::Driver::Files.3
/opt/jposug/perl5/5.26/man/man3/Test2::Tools::Tiny.3
/opt/jposug/perl5/5.26/man/man3/Test2::Transition.3
/opt/jposug/perl5/5.26/man/man3/Test2::Util.3
/opt/jposug/perl5/5.26/man/man3/Test2::Util::ExternalMeta.3
/opt/jposug/perl5/5.26/man/man3/Test2::Util::HashBase.3
/opt/jposug/perl5/5.26/man/man3/Test2::Util::Trace.3
/opt/jposug/perl5/5.26/man/man3/Test::Builder.3
/opt/jposug/perl5/5.26/man/man3/Test::Builder::Formatter.3
/opt/jposug/perl5/5.26/man/man3/Test::Builder::IO::Scalar.3
/opt/jposug/perl5/5.26/man/man3/Test::Builder::Module.3
/opt/jposug/perl5/5.26/man/man3/Test::Builder::Tester.3
/opt/jposug/perl5/5.26/man/man3/Test::Builder::Tester::Color.3
/opt/jposug/perl5/5.26/man/man3/Test::Builder::TodoDiag.3
/opt/jposug/perl5/5.26/man/man3/Test::Harness.3
/opt/jposug/perl5/5.26/man/man3/Test::More.3
/opt/jposug/perl5/5.26/man/man3/Test::Simple.3
/opt/jposug/perl5/5.26/man/man3/Test::Tester.3
/opt/jposug/perl5/5.26/man/man3/Test::Tester::Capture.3
/opt/jposug/perl5/5.26/man/man3/Test::Tester::CaptureRunner.3
/opt/jposug/perl5/5.26/man/man3/Test::Tutorial.3
/opt/jposug/perl5/5.26/man/man3/Test::use::ok.3
/opt/jposug/perl5/5.26/man/man3/Text::Abbrev.3
/opt/jposug/perl5/5.26/man/man3/Text::Balanced.3
/opt/jposug/perl5/5.26/man/man3/Text::ParseWords.3
/opt/jposug/perl5/5.26/man/man3/Text::Tabs.3
/opt/jposug/perl5/5.26/man/man3/Text::Wrap.3
/opt/jposug/perl5/5.26/man/man3/Thread.3
/opt/jposug/perl5/5.26/man/man3/Thread::Queue.3
/opt/jposug/perl5/5.26/man/man3/Thread::Semaphore.3
/opt/jposug/perl5/5.26/man/man3/Tie::Array.3
/opt/jposug/perl5/5.26/man/man3/Tie::File.3
/opt/jposug/perl5/5.26/man/man3/Tie::Handle.3
/opt/jposug/perl5/5.26/man/man3/Tie::Hash.3
/opt/jposug/perl5/5.26/man/man3/Tie::Hash::NamedCapture.3
/opt/jposug/perl5/5.26/man/man3/Tie::Memoize.3
/opt/jposug/perl5/5.26/man/man3/Tie::RefHash.3
/opt/jposug/perl5/5.26/man/man3/Tie::Scalar.3
/opt/jposug/perl5/5.26/man/man3/Tie::StdHandle.3
/opt/jposug/perl5/5.26/man/man3/Tie::SubstrHash.3
/opt/jposug/perl5/5.26/man/man3/Time::HiRes.3
/opt/jposug/perl5/5.26/man/man3/Time::Local.3
/opt/jposug/perl5/5.26/man/man3/Time::Piece.3
/opt/jposug/perl5/5.26/man/man3/Time::Seconds.3
/opt/jposug/perl5/5.26/man/man3/Time::gmtime.3
/opt/jposug/perl5/5.26/man/man3/Time::localtime.3
/opt/jposug/perl5/5.26/man/man3/Time::tm.3
/opt/jposug/perl5/5.26/man/man3/UNIVERSAL.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::CJK::Big5.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::CJK::GB2312.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::CJK::JISX0208.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::CJK::Korean.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::CJK::Pinyin.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::CJK::Stroke.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::CJK::Zhuyin.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Collate::Locale.3
/opt/jposug/perl5/5.26/man/man3/Unicode::Normalize.3
/opt/jposug/perl5/5.26/man/man3/Unicode::UCD.3
/opt/jposug/perl5/5.26/man/man3/User::grent.3
/opt/jposug/perl5/5.26/man/man3/User::pwent.3
/opt/jposug/perl5/5.26/man/man3/XSLoader.3
/opt/jposug/perl5/5.26/man/man3/arybase.3
/opt/jposug/perl5/5.26/man/man3/attributes.3
/opt/jposug/perl5/5.26/man/man3/autodie.3
/opt/jposug/perl5/5.26/man/man3/autodie::Scope::Guard.3
/opt/jposug/perl5/5.26/man/man3/autodie::Scope::GuardStack.3
/opt/jposug/perl5/5.26/man/man3/autodie::Util.3
/opt/jposug/perl5/5.26/man/man3/autodie::exception.3
/opt/jposug/perl5/5.26/man/man3/autodie::exception::system.3
/opt/jposug/perl5/5.26/man/man3/autodie::hints.3
/opt/jposug/perl5/5.26/man/man3/autodie::skip.3
/opt/jposug/perl5/5.26/man/man3/autouse.3
/opt/jposug/perl5/5.26/man/man3/base.3
/opt/jposug/perl5/5.26/man/man3/bigint.3
/opt/jposug/perl5/5.26/man/man3/bignum.3
/opt/jposug/perl5/5.26/man/man3/bigrat.3
/opt/jposug/perl5/5.26/man/man3/blib.3
/opt/jposug/perl5/5.26/man/man3/bytes.3
/opt/jposug/perl5/5.26/man/man3/charnames.3
/opt/jposug/perl5/5.26/man/man3/constant.3
/opt/jposug/perl5/5.26/man/man3/deprecate.3
/opt/jposug/perl5/5.26/man/man3/diagnostics.3
/opt/jposug/perl5/5.26/man/man3/encoding.3
/opt/jposug/perl5/5.26/man/man3/encoding::warnings.3
/opt/jposug/perl5/5.26/man/man3/experimental.3
/opt/jposug/perl5/5.26/man/man3/feature.3
/opt/jposug/perl5/5.26/man/man3/fields.3
/opt/jposug/perl5/5.26/man/man3/filetest.3
/opt/jposug/perl5/5.26/man/man3/if.3
/opt/jposug/perl5/5.26/man/man3/integer.3
/opt/jposug/perl5/5.26/man/man3/less.3
/opt/jposug/perl5/5.26/man/man3/lib.3
/opt/jposug/perl5/5.26/man/man3/locale.3
/opt/jposug/perl5/5.26/man/man3/mro.3
/opt/jposug/perl5/5.26/man/man3/ok.3
/opt/jposug/perl5/5.26/man/man3/open.3
/opt/jposug/perl5/5.26/man/man3/ops.3
/opt/jposug/perl5/5.26/man/man3/overload.3
/opt/jposug/perl5/5.26/man/man3/overloading.3
/opt/jposug/perl5/5.26/man/man3/parent.3
/opt/jposug/perl5/5.26/man/man3/re.3
/opt/jposug/perl5/5.26/man/man3/sigtrap.3
/opt/jposug/perl5/5.26/man/man3/sort.3
/opt/jposug/perl5/5.26/man/man3/strict.3
/opt/jposug/perl5/5.26/man/man3/subs.3
/opt/jposug/perl5/5.26/man/man3/threads.3
/opt/jposug/perl5/5.26/man/man3/threads::shared.3
/opt/jposug/perl5/5.26/man/man3/utf8.3
/opt/jposug/perl5/5.26/man/man3/vars.3
/opt/jposug/perl5/5.26/man/man3/version.3
/opt/jposug/perl5/5.26/man/man3/version::Internals.3
/opt/jposug/perl5/5.26/man/man3/vmsish.3
/opt/jposug/perl5/5.26/man/man3/warnings.3
/opt/jposug/perl5/5.26/man/man3/warnings::register.3
%dir /opt/jposug/perl5/site_perl
%dir /opt/jposug/perl5/site_perl/5.26
%dir /opt/jposug/perl5/site_perl/5.26/i86pc-solaris-thread-multi-64

%files encode
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/enc2xs
/opt/jposug/perl5/5.26/bin/encguess
/opt/jposug/perl5/5.26/bin/piconv
%dir /opt/jposug/perl5/5.26/lib
%dir /opt/jposug/perl5/5.26/lib/Encode
/opt/jposug/perl5/5.26/lib/Encode/*
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64
%dir /opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Encode
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Encode.pm
/opt/jposug/perl5/5.26/lib/i86pc-solaris-thread-multi-64/Encode/*
%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man3
/opt/jposug/perl5/5.26/man/man3/Encode.3
/opt/jposug/perl5/5.26/man/man3/Encode::Alias.3
/opt/jposug/perl5/5.26/man/man3/Encode::Byte.3
/opt/jposug/perl5/5.26/man/man3/Encode::CJKConstants.3
/opt/jposug/perl5/5.26/man/man3/Encode::CN.3
/opt/jposug/perl5/5.26/man/man3/Encode::CN::HZ.3
/opt/jposug/perl5/5.26/man/man3/Encode::Config.3
/opt/jposug/perl5/5.26/man/man3/Encode::EBCDIC.3
/opt/jposug/perl5/5.26/man/man3/Encode::Encoder.3
/opt/jposug/perl5/5.26/man/man3/Encode::Encoding.3
/opt/jposug/perl5/5.26/man/man3/Encode::GSM0338.3
/opt/jposug/perl5/5.26/man/man3/Encode::Guess.3
/opt/jposug/perl5/5.26/man/man3/Encode::JP.3
/opt/jposug/perl5/5.26/man/man3/Encode::JP::H2Z.3
/opt/jposug/perl5/5.26/man/man3/Encode::JP::JIS7.3
/opt/jposug/perl5/5.26/man/man3/Encode::KR.3
/opt/jposug/perl5/5.26/man/man3/Encode::KR::2022_KR.3
/opt/jposug/perl5/5.26/man/man3/Encode::MIME::Header.3
/opt/jposug/perl5/5.26/man/man3/Encode::MIME::Name.3
/opt/jposug/perl5/5.26/man/man3/Encode::PerlIO.3
/opt/jposug/perl5/5.26/man/man3/Encode::Supported.3
/opt/jposug/perl5/5.26/man/man3/Encode::Symbol.3
/opt/jposug/perl5/5.26/man/man3/Encode::TW.3
/opt/jposug/perl5/5.26/man/man3/Encode::Unicode.3
/opt/jposug/perl5/5.26/man/man3/Encode::Unicode::UTF7.3

%files podlators
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/pod2man
/opt/jposug/perl5/5.26/bin/pod2text

%dir /opt/jposug/perl5/5.26/lib/Pod
/opt/jposug/perl5/5.26/lib/Pod/Man.pm
/opt/jposug/perl5/5.26/lib/Pod/ParseUtils.pm
/opt/jposug/perl5/5.26/lib/Pod/ParseLink.pm
%dir /opt/jposug/perl5/5.26/lib/Pod/Text
/opt/jposug/perl5/5.26/lib/Pod/Text/*
%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man3
/opt/jposug/perl5/5.26/man/man3/Pod::Checker.3
/opt/jposug/perl5/5.26/man/man3/Pod::Escapes.3
/opt/jposug/perl5/5.26/man/man3/Pod::Find.3
/opt/jposug/perl5/5.26/man/man3/Pod::Html.3
/opt/jposug/perl5/5.26/man/man3/Pod::InputObjects.3
/opt/jposug/perl5/5.26/man/man3/Pod::Man.3
/opt/jposug/perl5/5.26/man/man3/Pod::ParseLink.3
/opt/jposug/perl5/5.26/man/man3/Pod::ParseUtils.3
/opt/jposug/perl5/5.26/man/man3/Pod::Parser.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::BaseTo.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::GetOptsOO.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToANSI.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToChecker.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToMan.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToNroff.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToPod.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToRtf.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToTerm.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToText.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToTk.3
/opt/jposug/perl5/5.26/man/man3/Pod::Perldoc::ToXml.3
/opt/jposug/perl5/5.26/man/man3/Pod::PlainText.3
/opt/jposug/perl5/5.26/man/man3/Pod::Select.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::Checker.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::Debug.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::DumpAsText.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::DumpAsXML.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::HTML.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::HTMLBatch.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::LinkSection.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::Methody.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::PullParser.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::PullParserEndToken.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::PullParserStartToken.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::PullParserTextToken.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::PullParserToken.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::RTF.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::Search.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::SimpleTree.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::Subclassing.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::Text.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::TextContent.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::XHTML.3
/opt/jposug/perl5/5.26/man/man3/Pod::Simple::XMLOutStream.3
/opt/jposug/perl5/5.26/man/man3/Pod::Text.3
/opt/jposug/perl5/5.26/man/man3/Pod::Text::Color.3
/opt/jposug/perl5/5.26/man/man3/Pod::Text::Overstrike.3
/opt/jposug/perl5/5.26/man/man3/Pod::Text::Termcap.3
/opt/jposug/perl5/5.26/man/man3/Pod::Usage.3


%files ext-mm
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/instmodsh
%dir /opt/jposug/perl5/5.26/lib/ExtUtils/Command
/opt/jposug/perl5/5.26/lib/ExtUtils/Command/*
/opt/jposug/perl5/5.26/lib/ExtUtils/Command.pm
%dir /opt/jposug/perl5/5.26/lib/ExtUtils/Liblist
/opt/jposug/perl5/5.26/lib/ExtUtils/Liblist/*
/opt/jposug/perl5/5.26/lib/ExtUtils/Liblist.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/MM.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/MM_*.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/MY.pm
%dir /opt/jposug/perl5/5.26/lib/ExtUtils/MakeMaker
/opt/jposug/perl5/5.26/lib/ExtUtils/MakeMaker/*
/opt/jposug/perl5/5.26/lib/ExtUtils/MakeMaker.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Mkbootstrap.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Mksymlists.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/testlib.pm
%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MakeMaker.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MakeMaker::Config.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MakeMaker::FAQ.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MakeMaker::Locale.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MakeMaker::Tutorial.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Liblist.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_AIX.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_Any.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_BeOS.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_Cygwin.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_DOS.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_Darwin.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_MacOS.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_NW5.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_OS2.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_QNX.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_UWIN.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_Unix.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_VMS.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_VOS.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_Win32.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MM_Win95.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::MY.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::CBuilder.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::CBuilder::Platform::Windows.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Command.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Command::MM.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Constant.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Constant::Base.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Constant::Utils.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Constant::XS.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Embed.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Install.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Installed.3


%files io-compress
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/zipdetails
%dir /opt/jposug/perl5/5.26/lib/Compress
/opt/jposug/perl5/5.26/lib/Compress/*
%dir /opt/jposug/perl5/5.26/lib/File
/opt/jposug/perl5/5.26/lib/File/GlobMapper.pm
%dir /opt/jposug/perl5/5.26/lib/IO
%dir /opt/jposug/perl5/5.26/lib/IO/Compress
/opt/jposug/perl5/5.26/lib/IO/Compress/*
%dir /opt/jposug/perl5/5.26/lib/IO/Uncompress
/opt/jposug/perl5/5.26/lib/IO/Uncompress/*

%dir /opt/jposug/perl5/5.26/man/man1
/opt/jposug/perl5/5.26/man/man1/zipdetails.1

%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man3
/opt/jposug/perl5/5.26/man/man3/IO::Compress::Base.3
/opt/jposug/perl5/5.26/man/man3/IO::Compress::Bzip2.3
/opt/jposug/perl5/5.26/man/man3/IO::Compress::Deflate.3
/opt/jposug/perl5/5.26/man/man3/IO::Compress::FAQ.3
/opt/jposug/perl5/5.26/man/man3/IO::Compress::Gzip.3
/opt/jposug/perl5/5.26/man/man3/IO::Compress::RawDeflate.3
/opt/jposug/perl5/5.26/man/man3/IO::Compress::Zip.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::AnyInflate.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::AnyUncompress.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::Base.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::Bunzip2.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::Gunzip.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::Inflate.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::RawInflate.3
/opt/jposug/perl5/5.26/man/man3/IO::Uncompress::Unzip.3

%files json-pp
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/json_pp
%dir /opt/jposug/perl5/5.26/lib/JSON
/opt/jposug/perl5/5.26/lib/JSON/*
%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man1
/opt/jposug/perl5/5.26/man/man1/json_pp.1
%dir /opt/jposug/perl5/5.26/man/man3
/opt/jposug/perl5/5.26/man/man3/JSON::PP.3
/opt/jposug/perl5/5.26/man/man3/JSON::PP::Boolean.3

%files ext-parsexs
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/xsubpp
%dir /opt/jposug/perl5/5.26/lib/ExtUtils
%dir /opt/jposug/perl5/5.26/lib/ExtUtils/ParseXS
/opt/jposug/perl5/5.26/lib/ExtUtils/ParseXS/*
/opt/jposug/perl5/5.26/lib/ExtUtils/ParseXS.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/ParseXS.pod
%dir /opt/jposug/perl5/5.26/lib/ExtUtils/Typemaps
/opt/jposug/perl5/5.26/lib/ExtUtils/Typemaps/*.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/Typemaps.pm
/opt/jposug/perl5/5.26/lib/ExtUtils/xsubpp
%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man1
/opt/jposug/perl5/5.26/man/man1/xsubpp.1
%dir /opt/jposug/perl5/5.26/man/man3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::ParseXS.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::ParseXS::Constants.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::ParseXS::Eval.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::ParseXS::Utilities.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Typemaps.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Typemaps::Cmd.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Typemaps::InputMap.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Typemaps::OutputMap.3
/opt/jposug/perl5/5.26/man/man3/ExtUtils::Typemaps::Type.3

%files pod-parser
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir /opt/jposug/perl5/5.26
%dir /opt/jposug/perl5/5.26/bin
/opt/jposug/perl5/5.26/bin/podselect
%dir /opt/jposug/perl5/5.26/lib
%dir /opt/jposug/perl5/5.26/lib/Pod
/opt/jposug/perl5/5.26/lib/Pod/Find.pm
/opt/jposug/perl5/5.26/lib/Pod/InputObjects.pm
/opt/jposug/perl5/5.26/lib/Pod/ParseUtils.pm
/opt/jposug/perl5/5.26/lib/Pod/Parser.pm
/opt/jposug/perl5/5.26/lib/Pod/PlainText.pm
/opt/jposug/perl5/5.26/lib/Pod/Select.pm
%dir /opt/jposug/perl5/5.26/man
%dir /opt/jposug/perl5/5.26/man/man1
%dir /opt/jposug/perl5/5.26/man/man3

%changelog
* Sun Dec 22 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files
* Fri Dec 20 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %files
* Mon Dec 16 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Split into multiple packages
* Fri Oct 18 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 5.26.3
* Wed May 16 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
