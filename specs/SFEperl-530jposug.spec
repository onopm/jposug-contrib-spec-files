%define version 5.30.1
%define major_version 5.30
%define version_suffix 530jposug
%define patchlevel 0

%define jposug_prefix /opt/jposug
%define prefix %{jposug_prefix}/perl5/%{major_version}
%define bindir %{prefix}/bin
%define libdir %{prefix}/lib
%define site_dir %{jposug_prefix}/perl5/site_perl/%{major_version}
%define vendor_dir %{jposug_prefix}/perl5/vendor_perl/%{major_version}

%ifarch sparc
%define perl_dir sun4-solaris-thread-multi-64
%else
%define perl_dir i86pc-solaris-thread-multi-64
%endif

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

Requires: library/perl-5/encode-530jposug
Requires: library/perl-5/podlators-530jposug
Requires: library/perl-5/extutils-makemaker-530jposug
Requires: library/perl-5/io-compress-530jposug
Requires: library/perl-5/json-pp-530jposug
Requires: library/perl-5/extutils-parsexs-530jposug
Requires: library/perl-5/pod-parser-530jposug

%package encode
IPS_Package_Name:       library/perl-5/encode-530jposug
IPS_Component_Version:  2.88
Summary:        perl encode module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description encode
perl encode module

%package podlators
IPS_Package_Name:       library/perl-5/podlators-530jposug
IPS_Component_Version:  4.09
Summary:        perl podlators module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description podlators
perl podlators module

%package ext-mm
IPS_Package_Name:       library/perl-5/extutils-makemaker-530jposug
IPS_Component_Version:  7.24
Summary:        perl extutils-makemaker module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description ext-mm
perl extutils-makemaker module

#
%package io-compress
IPS_Package_Name:       library/perl-5/io-compress-530jposug
IPS_Component_Version:  2.74
Summary:        perl io-compress module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description io-compress
perl io-compress module

#
%package json-pp
IPS_Package_Name:       library/perl-5/json-pp-530jposug
IPS_Component_Version:  2.274
Summary:        perl json-pp module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description json-pp
perl json-pp module

#
%package ext-parsexs
IPS_Package_Name:       library/perl-5/extutils-parsexs-530jposug
IPS_Component_Version:  3.34
Summary:        perl extutils-parsexs module
SUNW_BaseDir:   /opt/jposug
Requires:       jposug/runtime/perl-%{version_suffix}

%description ext-parsexs
perl extutils-parsexs module

#
%package pod-parser
IPS_Package_Name:       library/perl-5/pod-parser-530jposug
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
# make -j$CPUS test

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
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/corelist
%{prefix}/bin/cpan
%{prefix}/bin/h2ph
%{prefix}/bin/h2xs
%{prefix}/bin/libnetcfg
%{prefix}/bin/perl
%{prefix}/bin/perl5.30.1
%{prefix}/bin/perlbug
%{prefix}/bin/perldoc
%{prefix}/bin/perlivp
%{prefix}/bin/perlthanks
%{prefix}/bin/pl2pm
%{prefix}/bin/pod2html
%{prefix}/bin/pod2usage
%{prefix}/bin/podchecker
%{prefix}/bin/prove
%{prefix}/bin/ptar
%{prefix}/bin/ptardiff
%{prefix}/bin/ptargrep
%{prefix}/bin/shasum
%{prefix}/bin/splain

%dir %{prefix}/lib

%{prefix}/lib/AnyDBM_File.pm
%dir %{prefix}/lib/App
%{prefix}/lib/App/*
%dir %{prefix}/lib/Archive
%{prefix}/lib/Archive/*
%dir %{prefix}/lib/Attribute
%{prefix}/lib/Attribute/*
%{prefix}/lib/AutoLoader.pm
%{prefix}/lib/AutoSplit.pm
%dir %{prefix}/lib/B
%{prefix}/lib/B/*
%{prefix}/lib/Benchmark.pm
%{prefix}/lib/CORE.pod
%dir %{prefix}/lib/CPAN
%{prefix}/lib/CPAN/*
%{prefix}/lib/CPAN.pm
%dir %{prefix}/lib/Carp
%{prefix}/lib/Carp/*
%{prefix}/lib/Carp.pm
%dir %{prefix}/lib/Class
%{prefix}/lib/Class/*
%dir %{prefix}/lib/Config
%{prefix}/lib/Config/*
%{prefix}/lib/DB.pm
%dir %{prefix}/lib/DBM_Filter
%{prefix}/lib/DBM_Filter/*
%{prefix}/lib/DBM_Filter.pm
%dir %{prefix}/lib/Devel
%{prefix}/lib/Devel/*
%dir %{prefix}/lib/Digest
%{prefix}/lib/Digest/*
%{prefix}/lib/Digest.pm
%{prefix}/lib/DirHandle.pm
%{prefix}/lib/Dumpvalue.pm
%{prefix}/lib/English.pm
%{prefix}/lib/Env.pm
%dir %{prefix}/lib/Exporter
%{prefix}/lib/Exporter/*
%{prefix}/lib/Exporter.pm

%dir %{prefix}/lib/ExtUtils
%dir %{prefix}/lib/ExtUtils/CBuilder
%{prefix}/lib/ExtUtils/CBuilder/*
%{prefix}/lib/ExtUtils/CBuilder.pm
%{prefix}/lib/ExtUtils/Manifest.pm
%{prefix}/lib/ExtUtils/Miniperl.pm
%{prefix}/lib/ExtUtils/Packlist.pm
%{prefix}/lib/ExtUtils/typemap
%dir %{prefix}/lib/ExtUtils/Constant
%{prefix}/lib/ExtUtils/Constant/*
%{prefix}/lib/ExtUtils/Constant.pm
%{prefix}/lib/ExtUtils/Embed.pm
%{prefix}/lib/ExtUtils/Install.pm
%{prefix}/lib/ExtUtils/Installed.pm
%{prefix}/lib/ExtUtils/MANIFEST.SKIP
%{prefix}/lib/Fatal.pm
%dir %{prefix}/lib/File
%{prefix}/lib/File/Basename.pm
%{prefix}/lib/File/Compare.pm
%{prefix}/lib/File/Copy.pm
%{prefix}/lib/File/Fetch.pm
%{prefix}/lib/File/Find.pm
%{prefix}/lib/File/Path.pm
%{prefix}/lib/File/Temp.pm
%{prefix}/lib/File/stat.pm
%{prefix}/lib/FileCache.pm
%{prefix}/lib/FileHandle.pm
%dir %{prefix}/lib/Filter
%{prefix}/lib/Filter/*
%{prefix}/lib/FindBin.pm
%dir %{prefix}/lib/Getopt
%{prefix}/lib/Getopt/*
%dir %{prefix}/lib/HTTP
%{prefix}/lib/HTTP/*
%dir %{prefix}/lib/I18N
%{prefix}/lib/I18N/*
%dir %{prefix}/lib/IO
%{prefix}/lib/IO/Zlib.pm
%dir %{prefix}/lib/IO/Socket
%{prefix}/lib/IO/Socket/IP.pm
%dir %{prefix}/lib/IPC
%{prefix}/lib/IPC/*
%{prefix}/lib/Internals.pod
%dir %{prefix}/lib/Locale
%{prefix}/lib/Locale/*
%dir %{prefix}/lib/Math
%{prefix}/lib/Math/*
%dir %{prefix}/lib/Memoize
%{prefix}/lib/Memoize/*
%{prefix}/lib/Memoize.pm
%dir %{prefix}/lib/Module
%{prefix}/lib/Module/*
%{prefix}/lib/NEXT.pm
%dir %{prefix}/lib/Net
%{prefix}/lib/Net/*
%dir %{prefix}/lib/Params
%{prefix}/lib/Params/*
%dir %{prefix}/lib/Parse
%{prefix}/lib/Parse/*
%dir %{prefix}/lib/Perl
%{prefix}/lib/Perl/*
%dir %{prefix}/lib/PerlIO
%{prefix}/lib/PerlIO/*
%{prefix}/lib/PerlIO.pm
%dir %{prefix}/lib/Pod
%{prefix}/lib/Pod/Checker.pm
%{prefix}/lib/Pod/Escapes.pm
%{prefix}/lib/Pod/Functions.pm
%{prefix}/lib/Pod/Html.pm
%dir %{prefix}/lib/Pod/Perldoc
%{prefix}/lib/Pod/Perldoc/*
%{prefix}/lib/Pod/Perldoc.pm
%dir %{prefix}/lib/Pod/Simple
%{prefix}/lib/Pod/Simple.pm
%{prefix}/lib/Pod/Simple.pod
%{prefix}/lib/Pod/Simple/*
%{prefix}/lib/Pod/Text.pm
%{prefix}/lib/Pod/Usage.pm
%{prefix}/lib/Safe.pm
%dir %{prefix}/lib/Search
%{prefix}/lib/Search/*
%{prefix}/lib/SelectSaver.pm
%{prefix}/lib/SelfLoader.pm
%{prefix}/lib/Symbol.pm
%dir %{prefix}/lib/TAP
%{prefix}/lib/TAP/*
%dir %{prefix}/lib/Term
%{prefix}/lib/Term/*
%dir %{prefix}/lib/Test
%{prefix}/lib/Test/*
%{prefix}/lib/Test.pm
%dir %{prefix}/lib/Test2
%{prefix}/lib/Test2/*
%{prefix}/lib/Test2.pm
%dir %{prefix}/lib/Text
%{prefix}/lib/Text/*
%dir %{prefix}/lib/Thread
%{prefix}/lib/Thread/*
%{prefix}/lib/Thread.pm
%dir %{prefix}/lib/Tie
%{prefix}/lib/Tie/*
%dir %{prefix}/lib/Time
%{prefix}/lib/Time/*
%{prefix}/lib/UNIVERSAL.pm
%dir %{prefix}/lib/Unicode
%{prefix}/lib/Unicode/*
%dir %{prefix}/lib/User
%{prefix}/lib/User/*
%{prefix}/lib/XSLoader.pm
%{prefix}/lib/_charnames.pm
%dir %{prefix}/lib/autodie
%{prefix}/lib/autodie/*
%{prefix}/lib/autodie.pm
%{prefix}/lib/autouse.pm
%{prefix}/lib/base.pm
%{prefix}/lib/bigint.pm
%{prefix}/lib/bignum.pm
%{prefix}/lib/bigrat.pm
%{prefix}/lib/blib.pm
%{prefix}/lib/bytes.pm
%{prefix}/lib/bytes_heavy.pl
%{prefix}/lib/charnames.pm
%{prefix}/lib/constant.pm
%{prefix}/lib/deprecate.pm
%{prefix}/lib/diagnostics.pm
%{prefix}/lib/dumpvar.pl
%dir %{prefix}/lib/encoding
%{prefix}/lib/encoding/*
%{prefix}/lib/experimental.pm
%{prefix}/lib/feature.pm
%{prefix}/lib/fields.pm
%{prefix}/lib/filetest.pm
%{prefix}/lib/if.pm
%{prefix}/lib/integer.pm
%{prefix}/lib/less.pm
%{prefix}/lib/locale.pm
%{prefix}/lib/meta_notation.pm
%{prefix}/lib/ok.pm
%{prefix}/lib/open.pm
%{prefix}/lib/overload
%{prefix}/lib/overload.pm
%{prefix}/lib/overloading.pm
%{prefix}/lib/parent.pm
%{prefix}/lib/perl5db.pl
%{prefix}/lib/perlfaq.pm
%{prefix}/lib/pod
%{prefix}/lib/sigtrap.pm
%{prefix}/lib/sort.pm
%{prefix}/lib/strict.pm
%{prefix}/lib/subs.pm
%{prefix}/lib/unicore
%{prefix}/lib/utf8.pm
%{prefix}/lib/utf8_heavy.pl
%{prefix}/lib/vars.pm
%dir %{prefix}/lib/version
%{prefix}/lib/version/*
%{prefix}/lib/version.pm
%{prefix}/lib/version.pod
%{prefix}/lib/vmsish.pm
%dir %{prefix}/lib/warnings
%{prefix}/lib/warnings/*
%{prefix}/lib/warnings.pm


%dir %{prefix}/lib/%{perl_dir}
%{prefix}/lib/%{perl_dir}/.packlist
%dir %{prefix}/lib/%{perl_dir}/B
%{prefix}/lib/%{perl_dir}/B/*
%{prefix}/lib/%{perl_dir}/B.pm
%dir %{prefix}/lib/%{perl_dir}/CORE
%{prefix}/lib/%{perl_dir}/CORE/*
%dir %{prefix}/lib/%{perl_dir}/Compress
%{prefix}/lib/%{perl_dir}/Compress/*
%{prefix}/lib/%{perl_dir}/Config.pm
%{prefix}/lib/%{perl_dir}/Config.pod
%{prefix}/lib/%{perl_dir}/Config_git.pl
%{prefix}/lib/%{perl_dir}/Config_heavy.pl
%{prefix}/lib/%{perl_dir}/Cwd.pm
%{prefix}/lib/%{perl_dir}/DB_File.pm
%dir %{prefix}/lib/%{perl_dir}/Data
%{prefix}/lib/%{perl_dir}/Data/*
%dir %{prefix}/lib/%{perl_dir}/Devel
%{prefix}/lib/%{perl_dir}/Devel/*
%dir %{prefix}/lib/%{perl_dir}/Digest
%{prefix}/lib/%{perl_dir}/Digest/*
%{prefix}/lib/%{perl_dir}/DynaLoader.pm
%{prefix}/lib/%{perl_dir}/Errno.pm
%{prefix}/lib/%{perl_dir}/Fcntl.pm
%dir %{prefix}/lib/%{perl_dir}/File
%{prefix}/lib/%{perl_dir}/File/*
%dir %{prefix}/lib/%{perl_dir}/Filter
%{prefix}/lib/%{perl_dir}/Filter/*
%{prefix}/lib/%{perl_dir}/GDBM_File.pm
%dir %{prefix}/lib/%{perl_dir}/Hash
%{prefix}/lib/%{perl_dir}/Hash/*
%dir %{prefix}/lib/%{perl_dir}/I18N
%{prefix}/lib/%{perl_dir}/I18N/*
%dir %{prefix}/lib/%{perl_dir}/IO
%{prefix}/lib/%{perl_dir}/IO/*
%{prefix}/lib/%{perl_dir}/IO.pm
%dir %{prefix}/lib/%{perl_dir}/IPC
%{prefix}/lib/%{perl_dir}/IPC/*
%dir %{prefix}/lib/%{perl_dir}/List
%{prefix}/lib/%{perl_dir}/List/*
%dir %{prefix}/lib/%{perl_dir}/MIME
%{prefix}/lib/%{perl_dir}/MIME/*
%dir %{prefix}/lib/%{perl_dir}/Math
%{prefix}/lib/%{perl_dir}/Math/*
%{prefix}/lib/%{perl_dir}/NDBM_File.pm
%{prefix}/lib/%{perl_dir}/O.pm
%{prefix}/lib/%{perl_dir}/ODBM_File.pm
%{prefix}/lib/%{perl_dir}/Opcode.pm
%{prefix}/lib/%{perl_dir}/POSIX.pm
%{prefix}/lib/%{perl_dir}/POSIX.pod
%dir %{prefix}/lib/%{perl_dir}/PerlIO
%{prefix}/lib/%{perl_dir}/PerlIO/*
%{prefix}/lib/%{perl_dir}/SDBM_File.pm
%dir %{prefix}/lib/%{perl_dir}/Scalar
%{prefix}/lib/%{perl_dir}/Scalar/*
%{prefix}/lib/%{perl_dir}/Socket.pm
%{prefix}/lib/%{perl_dir}/Storable.pm
%dir %{prefix}/lib/%{perl_dir}/Sub
%{prefix}/lib/%{perl_dir}/Sub/*
%dir %{prefix}/lib/%{perl_dir}/Sys
%{prefix}/lib/%{perl_dir}/Sys/*
%dir %{prefix}/lib/%{perl_dir}/Tie
%{prefix}/lib/%{perl_dir}/Tie/*
%dir %{prefix}/lib/%{perl_dir}/Time
%{prefix}/lib/%{perl_dir}/Time/*
%dir %{prefix}/lib/%{perl_dir}/Unicode
%{prefix}/lib/%{perl_dir}/Unicode/*
# %{prefix}/lib/%{perl_dir}/arybase.pm
%{prefix}/lib/%{perl_dir}/attributes.pm
%dir %{prefix}/lib/%{perl_dir}/auto
%{prefix}/lib/%{perl_dir}/auto/*
%{prefix}/lib/%{perl_dir}/encoding.pm
%{prefix}/lib/%{perl_dir}/lib.pm
%{prefix}/lib/%{perl_dir}/mro.pm
%{prefix}/lib/%{perl_dir}/ops.pm
%{prefix}/lib/%{perl_dir}/re.pm
%{prefix}/lib/%{perl_dir}/threads
%{prefix}/lib/%{perl_dir}/threads.pm

%dir %{prefix}/man
%dir %{prefix}/man/man1
%{prefix}/man/man1/corelist.1
%{prefix}/man/man1/cpan.1
%{prefix}/man/man1/enc2xs.1
%{prefix}/man/man1/encguess.1
%{prefix}/man/man1/h2ph.1
%{prefix}/man/man1/h2xs.1
%{prefix}/man/man1/instmodsh.1
%{prefix}/man/man1/libnetcfg.1
%{prefix}/man/man1/perl.1
%{prefix}/man/man1/perl*delta.1
%{prefix}/man/man1/perlaix.1
%{prefix}/man/man1/perlamiga.1
%{prefix}/man/man1/perlandroid.1
%{prefix}/man/man1/perlapi.1
%{prefix}/man/man1/perlapio.1
%{prefix}/man/man1/perlartistic.1
%{prefix}/man/man1/perlbook.1
%{prefix}/man/man1/perlboot.1
%{prefix}/man/man1/perlbot.1
%{prefix}/man/man1/perlbs2000.1
%{prefix}/man/man1/perlbug.1
%{prefix}/man/man1/perlcall.1
%{prefix}/man/man1/perlce.1
%{prefix}/man/man1/perlcheat.1
%{prefix}/man/man1/perlclib.1
%{prefix}/man/man1/perlcn.1
%{prefix}/man/man1/perlcommunity.1
%{prefix}/man/man1/perlcygwin.1
%{prefix}/man/man1/perldata.1
%{prefix}/man/man1/perldbmfilter.1
%{prefix}/man/man1/perldebguts.1
%{prefix}/man/man1/perldebtut.1
%{prefix}/man/man1/perldebug.1
# %{prefix}/man/man1/perldelta.1
%{prefix}/man/man1/perldeprecation.1
%{prefix}/man/man1/perldiag.1
%{prefix}/man/man1/perldoc.1
%{prefix}/man/man1/perldos.1
%{prefix}/man/man1/perldsc.1
%{prefix}/man/man1/perldtrace.1
%{prefix}/man/man1/perlebcdic.1
%{prefix}/man/man1/perlembed.1
%{prefix}/man/man1/perlexperiment.1
%{prefix}/man/man1/perlfaq.1
%{prefix}/man/man1/perlfaq1.1
%{prefix}/man/man1/perlfaq2.1
%{prefix}/man/man1/perlfaq3.1
%{prefix}/man/man1/perlfaq4.1
%{prefix}/man/man1/perlfaq5.1
%{prefix}/man/man1/perlfaq6.1
%{prefix}/man/man1/perlfaq7.1
%{prefix}/man/man1/perlfaq8.1
%{prefix}/man/man1/perlfaq9.1
%{prefix}/man/man1/perlfilter.1
%{prefix}/man/man1/perlfork.1
%{prefix}/man/man1/perlform.1
%{prefix}/man/man1/perlfreebsd.1
%{prefix}/man/man1/perlfunc.1
%{prefix}/man/man1/perlgit.1
%{prefix}/man/man1/perlglossary.1
%{prefix}/man/man1/perlgpl.1
%{prefix}/man/man1/perlguts.1
%{prefix}/man/man1/perlhack.1
%{prefix}/man/man1/perlhacktips.1
%{prefix}/man/man1/perlhacktut.1
%{prefix}/man/man1/perlhaiku.1
%{prefix}/man/man1/perlhist.1
%{prefix}/man/man1/perlhpux.1
%{prefix}/man/man1/perlhurd.1
%{prefix}/man/man1/perlintern.1
%{prefix}/man/man1/perlinterp.1
%{prefix}/man/man1/perlintro.1
%{prefix}/man/man1/perliol.1
%{prefix}/man/man1/perlipc.1
%{prefix}/man/man1/perlirix.1
%{prefix}/man/man1/perlivp.1
%{prefix}/man/man1/perljp.1
%{prefix}/man/man1/perlko.1
%{prefix}/man/man1/perllexwarn.1
%{prefix}/man/man1/perllinux.1
%{prefix}/man/man1/perllocale.1
%{prefix}/man/man1/perllol.1
%{prefix}/man/man1/perlmacos.1
%{prefix}/man/man1/perlmacosx.1
%{prefix}/man/man1/perlmod.1
%{prefix}/man/man1/perlmodinstall.1
%{prefix}/man/man1/perlmodlib.1
%{prefix}/man/man1/perlmodstyle.1
%{prefix}/man/man1/perlmroapi.1
%{prefix}/man/man1/perlnetware.1
%{prefix}/man/man1/perlnewmod.1
%{prefix}/man/man1/perlnumber.1
%{prefix}/man/man1/perlobj.1
%{prefix}/man/man1/perlootut.1
%{prefix}/man/man1/perlop.1
%{prefix}/man/man1/perlopenbsd.1
%{prefix}/man/man1/perlopentut.1
%{prefix}/man/man1/perlos2.1
%{prefix}/man/man1/perlos390.1
%{prefix}/man/man1/perlos400.1
%{prefix}/man/man1/perlpacktut.1
%{prefix}/man/man1/perlperf.1
%{prefix}/man/man1/perlplan9.1
%{prefix}/man/man1/perlpod.1
%{prefix}/man/man1/perlpodspec.1
%{prefix}/man/man1/perlpodstyle.1
%{prefix}/man/man1/perlpolicy.1
%{prefix}/man/man1/perlport.1
%{prefix}/man/man1/perlpragma.1
%{prefix}/man/man1/perlqnx.1
%{prefix}/man/man1/perlre.1
%{prefix}/man/man1/perlreapi.1
%{prefix}/man/man1/perlrebackslash.1
%{prefix}/man/man1/perlrecharclass.1
%{prefix}/man/man1/perlref.1
%{prefix}/man/man1/perlreftut.1
%{prefix}/man/man1/perlreguts.1
%{prefix}/man/man1/perlrepository.1
%{prefix}/man/man1/perlrequick.1
%{prefix}/man/man1/perlreref.1
%{prefix}/man/man1/perlretut.1
%{prefix}/man/man1/perlriscos.1
%{prefix}/man/man1/perlrun.1
%{prefix}/man/man1/perlsec.1
%{prefix}/man/man1/perlsolaris.1
%{prefix}/man/man1/perlsource.1
%{prefix}/man/man1/perlstyle.1
%{prefix}/man/man1/perlsub.1
%{prefix}/man/man1/perlsymbian.1
%{prefix}/man/man1/perlsyn.1
%{prefix}/man/man1/perlsynology.1
%{prefix}/man/man1/perlthanks.1
%{prefix}/man/man1/perlthrtut.1
%{prefix}/man/man1/perltie.1
%{prefix}/man/man1/perltoc.1
%{prefix}/man/man1/perltodo.1
%{prefix}/man/man1/perltooc.1
%{prefix}/man/man1/perltoot.1
%{prefix}/man/man1/perltrap.1
%{prefix}/man/man1/perltru64.1
%{prefix}/man/man1/perltw.1
%{prefix}/man/man1/perlunicode.1
%{prefix}/man/man1/perlunicook.1
%{prefix}/man/man1/perlunifaq.1
%{prefix}/man/man1/perluniintro.1
%{prefix}/man/man1/perluniprops.1
%{prefix}/man/man1/perlunitut.1
%{prefix}/man/man1/perlutil.1
%{prefix}/man/man1/perlvar.1
%{prefix}/man/man1/perlvms.1
%{prefix}/man/man1/perlvos.1
%{prefix}/man/man1/perlwin32.1
%{prefix}/man/man1/perlxs.1
%{prefix}/man/man1/perlxstut.1
%{prefix}/man/man1/perlxstypemap.1
%{prefix}/man/man1/piconv.1
%{prefix}/man/man1/pl2pm.1
%{prefix}/man/man1/pod2html.1
%{prefix}/man/man1/pod2man.1
%{prefix}/man/man1/pod2text.1
%{prefix}/man/man1/pod2usage.1
%{prefix}/man/man1/podchecker.1
%{prefix}/man/man1/podselect.1
%{prefix}/man/man1/prove.1
%{prefix}/man/man1/ptar.1
%{prefix}/man/man1/ptardiff.1
%{prefix}/man/man1/ptargrep.1
%{prefix}/man/man1/shasum.1
%{prefix}/man/man1/splain.1
%dir %{prefix}/man/man3
%{prefix}/man/man3/AnyDBM_File.3
%{prefix}/man/man3/App::Cpan.3
%{prefix}/man/man3/App::Prove.3
%{prefix}/man/man3/App::Prove::State.3
%{prefix}/man/man3/App::Prove::State::Result.3
%{prefix}/man/man3/App::Prove::State::Result::Test.3
%{prefix}/man/man3/Archive::Tar.3
%{prefix}/man/man3/Archive::Tar::File.3
%{prefix}/man/man3/Attribute::Handlers.3
%{prefix}/man/man3/AutoLoader.3
%{prefix}/man/man3/AutoSplit.3
%{prefix}/man/man3/B.3
%{prefix}/man/man3/B::Concise.3
# %{prefix}/man/man3/B::Debug.3
%{prefix}/man/man3/B::Deparse.3
%{prefix}/man/man3/B::Op_private.3
%{prefix}/man/man3/B::Showlex.3
%{prefix}/man/man3/B::Terse.3
%{prefix}/man/man3/B::Xref.3
%{prefix}/man/man3/Benchmark.3
%{prefix}/man/man3/CORE.3
%{prefix}/man/man3/CPAN.3
%{prefix}/man/man3/CPAN::API::HOWTO.3
%{prefix}/man/man3/CPAN::Debug.3
%{prefix}/man/man3/CPAN::Distroprefs.3
%{prefix}/man/man3/CPAN::FirstTime.3
%{prefix}/man/man3/CPAN::HandleConfig.3
%{prefix}/man/man3/CPAN::Kwalify.3
%{prefix}/man/man3/CPAN::Meta.3
%{prefix}/man/man3/CPAN::Meta::Converter.3
%{prefix}/man/man3/CPAN::Meta::Feature.3
%{prefix}/man/man3/CPAN::Meta::History.3
%{prefix}/man/man3/CPAN::Meta::History::Meta_1_0.3
%{prefix}/man/man3/CPAN::Meta::History::Meta_1_1.3
%{prefix}/man/man3/CPAN::Meta::History::Meta_1_2.3
%{prefix}/man/man3/CPAN::Meta::History::Meta_1_3.3
%{prefix}/man/man3/CPAN::Meta::History::Meta_1_4.3
%{prefix}/man/man3/CPAN::Meta::Merge.3
%{prefix}/man/man3/CPAN::Meta::Prereqs.3
%{prefix}/man/man3/CPAN::Meta::Requirements.3
%{prefix}/man/man3/CPAN::Meta::Spec.3
%{prefix}/man/man3/CPAN::Meta::Validator.3
%{prefix}/man/man3/CPAN::Meta::YAML.3
%{prefix}/man/man3/CPAN::Mirrors.3
%{prefix}/man/man3/CPAN::Nox.3
%{prefix}/man/man3/CPAN::Plugin.3
%{prefix}/man/man3/CPAN::Plugin::Specfile.3
%{prefix}/man/man3/CPAN::Queue.3
%{prefix}/man/man3/CPAN::Tarzip.3
%{prefix}/man/man3/CPAN::Version.3
%{prefix}/man/man3/Carp.3
%{prefix}/man/man3/Class::Struct.3
%{prefix}/man/man3/Compress::Raw::Bzip2.3
%{prefix}/man/man3/Compress::Raw::Zlib.3
%{prefix}/man/man3/Compress::Zlib.3
%{prefix}/man/man3/Config.3
%{prefix}/man/man3/Config::Extensions.3
%{prefix}/man/man3/Config::Perl::V.3
%{prefix}/man/man3/Cwd.3
%{prefix}/man/man3/DB.3
%{prefix}/man/man3/DBM_Filter.3
%{prefix}/man/man3/DBM_Filter::compress.3
%{prefix}/man/man3/DBM_Filter::encode.3
%{prefix}/man/man3/DBM_Filter::int32.3
%{prefix}/man/man3/DBM_Filter::null.3
%{prefix}/man/man3/DBM_Filter::utf8.3
%{prefix}/man/man3/DB_File.3
%{prefix}/man/man3/Data::Dumper.3
%{prefix}/man/man3/Devel::PPPort.3
%{prefix}/man/man3/Devel::Peek.3
%{prefix}/man/man3/Devel::SelfStubber.3
%{prefix}/man/man3/Digest.3
%{prefix}/man/man3/Digest::MD5.3
%{prefix}/man/man3/Digest::SHA.3
%{prefix}/man/man3/Digest::base.3
%{prefix}/man/man3/Digest::file.3
%{prefix}/man/man3/DirHandle.3
%{prefix}/man/man3/Dumpvalue.3
%{prefix}/man/man3/DynaLoader.3
%{prefix}/man/man3/English.3
%{prefix}/man/man3/Env.3
%{prefix}/man/man3/Errno.3
%{prefix}/man/man3/Exporter.3
%{prefix}/man/man3/Exporter::Heavy.3
%{prefix}/man/man3/ExtUtils::Manifest.3
%{prefix}/man/man3/ExtUtils::Miniperl.3
%{prefix}/man/man3/ExtUtils::Mkbootstrap.3
%{prefix}/man/man3/ExtUtils::Mksymlists.3
%{prefix}/man/man3/ExtUtils::Packlist.3
%{prefix}/man/man3/ExtUtils::XSSymSet.3
%{prefix}/man/man3/ExtUtils::testlib.3
%{prefix}/man/man3/Fatal.3
%{prefix}/man/man3/Fcntl.3
%{prefix}/man/man3/File::Basename.3
%{prefix}/man/man3/File::Compare.3
%{prefix}/man/man3/File::Copy.3
%{prefix}/man/man3/File::DosGlob.3
%{prefix}/man/man3/File::Fetch.3
%{prefix}/man/man3/File::Find.3
%{prefix}/man/man3/File::Glob.3
%{prefix}/man/man3/File::GlobMapper.3
%{prefix}/man/man3/File::Path.3
%{prefix}/man/man3/File::Spec.3
%{prefix}/man/man3/File::Spec::AmigaOS.3
%{prefix}/man/man3/File::Spec::Cygwin.3
%{prefix}/man/man3/File::Spec::Epoc.3
%{prefix}/man/man3/File::Spec::Functions.3
%{prefix}/man/man3/File::Spec::Mac.3
%{prefix}/man/man3/File::Spec::OS2.3
%{prefix}/man/man3/File::Spec::Unix.3
%{prefix}/man/man3/File::Spec::VMS.3
%{prefix}/man/man3/File::Spec::Win32.3
%{prefix}/man/man3/File::Temp.3
%{prefix}/man/man3/File::stat.3
%{prefix}/man/man3/FileCache.3
%{prefix}/man/man3/FileHandle.3
%{prefix}/man/man3/Filter::Simple.3
%{prefix}/man/man3/Filter::Util::Call.3
%{prefix}/man/man3/FindBin.3
%{prefix}/man/man3/GDBM_File.3
%{prefix}/man/man3/Getopt::Long.3
%{prefix}/man/man3/Getopt::Std.3
%{prefix}/man/man3/HTTP::Tiny.3
%{prefix}/man/man3/Hash::Util.3
%{prefix}/man/man3/Hash::Util::FieldHash.3
%{prefix}/man/man3/I18N::Collate.3
%{prefix}/man/man3/I18N::LangTags.3
%{prefix}/man/man3/I18N::LangTags::Detect.3
%{prefix}/man/man3/I18N::LangTags::List.3
%{prefix}/man/man3/I18N::Langinfo.3
%{prefix}/man/man3/IO.3
%{prefix}/man/man3/IO::Dir.3
%{prefix}/man/man3/IO::File.3
%{prefix}/man/man3/IO::Handle.3
%{prefix}/man/man3/IO::Pipe.3
%{prefix}/man/man3/IO::Poll.3
%{prefix}/man/man3/IO::Seekable.3
%{prefix}/man/man3/IO::Select.3
%{prefix}/man/man3/IO::Socket.3
%{prefix}/man/man3/IO::Socket::INET.3
%{prefix}/man/man3/IO::Socket::IP.3
%{prefix}/man/man3/IO::Socket::UNIX.3
%{prefix}/man/man3/IO::Zlib.3
%{prefix}/man/man3/IPC::Cmd.3
%{prefix}/man/man3/IPC::Msg.3
%{prefix}/man/man3/IPC::Open2.3
%{prefix}/man/man3/IPC::Open3.3
%{prefix}/man/man3/IPC::Semaphore.3
%{prefix}/man/man3/IPC::SharedMem.3
%{prefix}/man/man3/IPC::SysV.3
%{prefix}/man/man3/Internals.3
%{prefix}/man/man3/List::Util.3
%{prefix}/man/man3/List::Util::XS.3
# %{prefix}/man/man3/Locale::Codes.3
# %{prefix}/man/man3/Locale::Codes::API.3
# %{prefix}/man/man3/Locale::Codes::Changes.3
# %{prefix}/man/man3/Locale::Codes::Country.3
# %{prefix}/man/man3/Locale::Codes::Currency.3
# %{prefix}/man/man3/Locale::Codes::LangExt.3
# %{prefix}/man/man3/Locale::Codes::LangFam.3
# %{prefix}/man/man3/Locale::Codes::LangVar.3
# %{prefix}/man/man3/Locale::Codes::Language.3
# %{prefix}/man/man3/Locale::Codes::Script.3
# %{prefix}/man/man3/Locale::Country.3
# %{prefix}/man/man3/Locale::Currency.3
# %{prefix}/man/man3/Locale::Language.3
%{prefix}/man/man3/Locale::Maketext.3
%{prefix}/man/man3/Locale::Maketext::Cookbook.3
%{prefix}/man/man3/Locale::Maketext::Guts.3
%{prefix}/man/man3/Locale::Maketext::GutsLoader.3
%{prefix}/man/man3/Locale::Maketext::Simple.3
%{prefix}/man/man3/Locale::Maketext::TPJ13.3
# %{prefix}/man/man3/Locale::Script.3
%{prefix}/man/man3/MIME::Base64.3
%{prefix}/man/man3/MIME::QuotedPrint.3
%{prefix}/man/man3/Math::BigFloat.3
%{prefix}/man/man3/Math::BigInt.3
%{prefix}/man/man3/Math::BigInt::Calc.3
# %{prefix}/man/man3/Math::BigInt::CalcEmu.3
%{prefix}/man/man3/Math::BigInt::FastCalc.3
%{prefix}/man/man3/Math::BigInt::Lib.3
%{prefix}/man/man3/Math::BigRat.3
%{prefix}/man/man3/Math::Complex.3
%{prefix}/man/man3/Math::Trig.3
%{prefix}/man/man3/Memoize.3
%{prefix}/man/man3/Memoize::AnyDBM_File.3
%{prefix}/man/man3/Memoize::Expire.3
%{prefix}/man/man3/Memoize::ExpireFile.3
%{prefix}/man/man3/Memoize::ExpireTest.3
%{prefix}/man/man3/Memoize::NDBM_File.3
%{prefix}/man/man3/Memoize::SDBM_File.3
%{prefix}/man/man3/Memoize::Storable.3
%{prefix}/man/man3/Module::CoreList.3
%{prefix}/man/man3/Module::CoreList::Utils.3
%{prefix}/man/man3/Module::Load.3
%{prefix}/man/man3/Module::Load::Conditional.3
%{prefix}/man/man3/Module::Loaded.3
%{prefix}/man/man3/Module::Metadata.3
%{prefix}/man/man3/NDBM_File.3
%{prefix}/man/man3/NEXT.3
%{prefix}/man/man3/Net::Cmd.3
%{prefix}/man/man3/Net::Config.3
%{prefix}/man/man3/Net::Domain.3
%{prefix}/man/man3/Net::FTP.3
%{prefix}/man/man3/Net::NNTP.3
%{prefix}/man/man3/Net::Netrc.3
%{prefix}/man/man3/Net::POP3.3
%{prefix}/man/man3/Net::Ping.3
%{prefix}/man/man3/Net::SMTP.3
%{prefix}/man/man3/Net::Time.3
%{prefix}/man/man3/Net::hostent.3
%{prefix}/man/man3/Net::libnetFAQ.3
%{prefix}/man/man3/Net::netent.3
%{prefix}/man/man3/Net::protoent.3
%{prefix}/man/man3/Net::servent.3
%{prefix}/man/man3/O.3
%{prefix}/man/man3/ODBM_File.3
%{prefix}/man/man3/Opcode.3
%{prefix}/man/man3/POSIX.3
%{prefix}/man/man3/Params::Check.3
%{prefix}/man/man3/Parse::CPAN::Meta.3
%{prefix}/man/man3/Perl::OSType.3
%{prefix}/man/man3/PerlIO.3
%{prefix}/man/man3/PerlIO::encoding.3
%{prefix}/man/man3/PerlIO::mmap.3
%{prefix}/man/man3/PerlIO::scalar.3
%{prefix}/man/man3/PerlIO::via.3
%{prefix}/man/man3/PerlIO::via::QuotedPrint.3
%{prefix}/man/man3/SDBM_File.3
%{prefix}/man/man3/Safe.3
%{prefix}/man/man3/Scalar::Util.3
%{prefix}/man/man3/Search::Dict.3
%{prefix}/man/man3/SelectSaver.3
%{prefix}/man/man3/SelfLoader.3
%{prefix}/man/man3/Socket.3
%{prefix}/man/man3/Storable.3
%{prefix}/man/man3/Sub::Util.3
%{prefix}/man/man3/Symbol.3
%{prefix}/man/man3/Sys::Hostname.3
%{prefix}/man/man3/Sys::Syslog.3
%{prefix}/man/man3/TAP::Base.3
%{prefix}/man/man3/TAP::Formatter::Base.3
%{prefix}/man/man3/TAP::Formatter::Color.3
%{prefix}/man/man3/TAP::Formatter::Console.3
%{prefix}/man/man3/TAP::Formatter::Console::ParallelSession.3
%{prefix}/man/man3/TAP::Formatter::Console::Session.3
%{prefix}/man/man3/TAP::Formatter::File.3
%{prefix}/man/man3/TAP::Formatter::File::Session.3
%{prefix}/man/man3/TAP::Formatter::Session.3
%{prefix}/man/man3/TAP::Harness.3
%{prefix}/man/man3/TAP::Harness::Beyond.3
%{prefix}/man/man3/TAP::Harness::Env.3
%{prefix}/man/man3/TAP::Object.3
%{prefix}/man/man3/TAP::Parser.3
%{prefix}/man/man3/TAP::Parser::Aggregator.3
%{prefix}/man/man3/TAP::Parser::Grammar.3
%{prefix}/man/man3/TAP::Parser::Iterator.3
%{prefix}/man/man3/TAP::Parser::Iterator::Array.3
%{prefix}/man/man3/TAP::Parser::Iterator::Process.3
%{prefix}/man/man3/TAP::Parser::Iterator::Stream.3
%{prefix}/man/man3/TAP::Parser::IteratorFactory.3
%{prefix}/man/man3/TAP::Parser::Multiplexer.3
%{prefix}/man/man3/TAP::Parser::Result.3
%{prefix}/man/man3/TAP::Parser::Result::Bailout.3
%{prefix}/man/man3/TAP::Parser::Result::Comment.3
%{prefix}/man/man3/TAP::Parser::Result::Plan.3
%{prefix}/man/man3/TAP::Parser::Result::Pragma.3
%{prefix}/man/man3/TAP::Parser::Result::Test.3
%{prefix}/man/man3/TAP::Parser::Result::Unknown.3
%{prefix}/man/man3/TAP::Parser::Result::Version.3
%{prefix}/man/man3/TAP::Parser::Result::YAML.3
%{prefix}/man/man3/TAP::Parser::ResultFactory.3
%{prefix}/man/man3/TAP::Parser::Scheduler.3
%{prefix}/man/man3/TAP::Parser::Scheduler::Job.3
%{prefix}/man/man3/TAP::Parser::Scheduler::Spinner.3
%{prefix}/man/man3/TAP::Parser::Source.3
%{prefix}/man/man3/TAP::Parser::SourceHandler.3
%{prefix}/man/man3/TAP::Parser::SourceHandler::Executable.3
%{prefix}/man/man3/TAP::Parser::SourceHandler::File.3
%{prefix}/man/man3/TAP::Parser::SourceHandler::Handle.3
%{prefix}/man/man3/TAP::Parser::SourceHandler::Perl.3
%{prefix}/man/man3/TAP::Parser::SourceHandler::RawTAP.3
%{prefix}/man/man3/TAP::Parser::YAMLish::Reader.3
%{prefix}/man/man3/TAP::Parser::YAMLish::Writer.3
%{prefix}/man/man3/Term::ANSIColor.3
%{prefix}/man/man3/Term::Cap.3
%{prefix}/man/man3/Term::Complete.3
%{prefix}/man/man3/Term::ReadLine.3
%{prefix}/man/man3/Test.3
%{prefix}/man/man3/Test2.3
# %{prefix}/man/man3/Test2::Event::Info.3
%{prefix}/man/man3/Test2::API.3
%{prefix}/man/man3/Test2::API::Breakage.3
%{prefix}/man/man3/Test2::API::Context.3
%{prefix}/man/man3/Test2::API::Instance.3
%{prefix}/man/man3/Test2::API::Stack.3
%{prefix}/man/man3/Test2::Event.3
%{prefix}/man/man3/Test2::Event::Bail.3
%{prefix}/man/man3/Test2::Event::Diag.3
%{prefix}/man/man3/Test2::Event::Encoding.3
%{prefix}/man/man3/Test2::Event::Exception.3
%{prefix}/man/man3/Test2::Event::Fail.3
%{prefix}/man/man3/Test2::Event::Generic.3
%{prefix}/man/man3/Test2::Event::Note.3
%{prefix}/man/man3/Test2::Event::Ok.3
%{prefix}/man/man3/Test2::Event::Pass.3
%{prefix}/man/man3/Test2::Event::Plan.3
%{prefix}/man/man3/Test2::Event::Skip.3
%{prefix}/man/man3/Test2::Event::Subtest.3
%{prefix}/man/man3/Test2::Event::TAP::Version.3
%{prefix}/man/man3/Test2::Event::V2.3
%{prefix}/man/man3/Test2::Event::Waiting.3
%{prefix}/man/man3/Test2::EventFacet.3
%{prefix}/man/man3/Test2::EventFacet::About.3
%{prefix}/man/man3/Test2::EventFacet::Amnesty.3
%{prefix}/man/man3/Test2::EventFacet::Assert.3
%{prefix}/man/man3/Test2::EventFacet::Control.3
%{prefix}/man/man3/Test2::EventFacet::Error.3
%{prefix}/man/man3/Test2::EventFacet::Hub.3
%{prefix}/man/man3/Test2::EventFacet::Info.3
%{prefix}/man/man3/Test2::EventFacet::Info::Table.3
%{prefix}/man/man3/Test2::EventFacet::Meta.3
%{prefix}/man/man3/Test2::EventFacet::Parent.3
%{prefix}/man/man3/Test2::EventFacet::Plan.3
%{prefix}/man/man3/Test2::EventFacet::Render.3
%{prefix}/man/man3/Test2::EventFacet::Trace.3
%{prefix}/man/man3/Test2::Formatter.3
%{prefix}/man/man3/Test2::Formatter::TAP.3
%{prefix}/man/man3/Test2::Hub.3
%{prefix}/man/man3/Test2::Hub::Interceptor.3
%{prefix}/man/man3/Test2::Hub::Interceptor::Terminator.3
%{prefix}/man/man3/Test2::Hub::Subtest.3
%{prefix}/man/man3/Test2::IPC.3
%{prefix}/man/man3/Test2::IPC::Driver.3
%{prefix}/man/man3/Test2::IPC::Driver::Files.3
%{prefix}/man/man3/Test2::Tools::Tiny.3
%{prefix}/man/man3/Test2::Transition.3
%{prefix}/man/man3/Test2::Util.3
%{prefix}/man/man3/Test2::Util::ExternalMeta.3
%{prefix}/man/man3/Test2::Util::Facets2Legacy.3
%{prefix}/man/man3/Test2::Util::HashBase.3
%{prefix}/man/man3/Test2::Util::Trace.3
%{prefix}/man/man3/Test::Builder.3
%{prefix}/man/man3/Test::Builder::Formatter.3
%{prefix}/man/man3/Test::Builder::IO::Scalar.3
%{prefix}/man/man3/Test::Builder::Module.3
%{prefix}/man/man3/Test::Builder::Tester.3
%{prefix}/man/man3/Test::Builder::Tester::Color.3
%{prefix}/man/man3/Test::Builder::TodoDiag.3
%{prefix}/man/man3/Test::Harness.3
%{prefix}/man/man3/Test::More.3
%{prefix}/man/man3/Test::Simple.3
%{prefix}/man/man3/Test::Tester.3
%{prefix}/man/man3/Test::Tester::Capture.3
%{prefix}/man/man3/Test::Tester::CaptureRunner.3
%{prefix}/man/man3/Test::Tutorial.3
%{prefix}/man/man3/Test::use::ok.3
%{prefix}/man/man3/Text::Abbrev.3
%{prefix}/man/man3/Text::Balanced.3
%{prefix}/man/man3/Text::ParseWords.3
%{prefix}/man/man3/Text::Tabs.3
%{prefix}/man/man3/Text::Wrap.3
%{prefix}/man/man3/Thread.3
%{prefix}/man/man3/Thread::Queue.3
%{prefix}/man/man3/Thread::Semaphore.3
%{prefix}/man/man3/Tie::Array.3
%{prefix}/man/man3/Tie::File.3
%{prefix}/man/man3/Tie::Handle.3
%{prefix}/man/man3/Tie::Hash.3
%{prefix}/man/man3/Tie::Hash::NamedCapture.3
%{prefix}/man/man3/Tie::Memoize.3
%{prefix}/man/man3/Tie::RefHash.3
%{prefix}/man/man3/Tie::Scalar.3
%{prefix}/man/man3/Tie::StdHandle.3
%{prefix}/man/man3/Tie::SubstrHash.3
%{prefix}/man/man3/Time::HiRes.3
%{prefix}/man/man3/Time::Local.3
%{prefix}/man/man3/Time::Piece.3
%{prefix}/man/man3/Time::Seconds.3
%{prefix}/man/man3/Time::gmtime.3
%{prefix}/man/man3/Time::localtime.3
%{prefix}/man/man3/Time::tm.3
%{prefix}/man/man3/UNIVERSAL.3
%{prefix}/man/man3/Unicode::Collate.3
%{prefix}/man/man3/Unicode::Collate::CJK::Big5.3
%{prefix}/man/man3/Unicode::Collate::CJK::GB2312.3
%{prefix}/man/man3/Unicode::Collate::CJK::JISX0208.3
%{prefix}/man/man3/Unicode::Collate::CJK::Korean.3
%{prefix}/man/man3/Unicode::Collate::CJK::Pinyin.3
%{prefix}/man/man3/Unicode::Collate::CJK::Stroke.3
%{prefix}/man/man3/Unicode::Collate::CJK::Zhuyin.3
%{prefix}/man/man3/Unicode::Collate::Locale.3
%{prefix}/man/man3/Unicode::Normalize.3
%{prefix}/man/man3/Unicode::UCD.3
%{prefix}/man/man3/User::grent.3
%{prefix}/man/man3/User::pwent.3
%{prefix}/man/man3/XSLoader.3
# %{prefix}/man/man3/arybase.3
%{prefix}/man/man3/attributes.3
%{prefix}/man/man3/autodie.3
%{prefix}/man/man3/autodie::Scope::Guard.3
%{prefix}/man/man3/autodie::Scope::GuardStack.3
%{prefix}/man/man3/autodie::Util.3
%{prefix}/man/man3/autodie::exception.3
%{prefix}/man/man3/autodie::exception::system.3
%{prefix}/man/man3/autodie::hints.3
%{prefix}/man/man3/autodie::skip.3
%{prefix}/man/man3/autouse.3
%{prefix}/man/man3/base.3
%{prefix}/man/man3/bigint.3
%{prefix}/man/man3/bignum.3
%{prefix}/man/man3/bigrat.3
%{prefix}/man/man3/blib.3
%{prefix}/man/man3/bytes.3
%{prefix}/man/man3/charnames.3
%{prefix}/man/man3/constant.3
%{prefix}/man/man3/deprecate.3
%{prefix}/man/man3/diagnostics.3
%{prefix}/man/man3/encoding.3
%{prefix}/man/man3/encoding::warnings.3
%{prefix}/man/man3/experimental.3
%{prefix}/man/man3/feature.3
%{prefix}/man/man3/fields.3
%{prefix}/man/man3/filetest.3
%{prefix}/man/man3/if.3
%{prefix}/man/man3/integer.3
%{prefix}/man/man3/less.3
%{prefix}/man/man3/lib.3
%{prefix}/man/man3/locale.3
%{prefix}/man/man3/mro.3
%{prefix}/man/man3/ok.3
%{prefix}/man/man3/open.3
%{prefix}/man/man3/ops.3
%{prefix}/man/man3/overload.3
%{prefix}/man/man3/overloading.3
%{prefix}/man/man3/parent.3
%{prefix}/man/man3/re.3
%{prefix}/man/man3/sigtrap.3
%{prefix}/man/man3/sort.3
%{prefix}/man/man3/strict.3
%{prefix}/man/man3/subs.3
%{prefix}/man/man3/threads.3
%{prefix}/man/man3/threads::shared.3
%{prefix}/man/man3/utf8.3
%{prefix}/man/man3/vars.3
%{prefix}/man/man3/version.3
%{prefix}/man/man3/version::Internals.3
%{prefix}/man/man3/vmsish.3
%{prefix}/man/man3/warnings.3
%{prefix}/man/man3/warnings::register.3
%dir /opt/jposug/perl5/site_perl
%dir /opt/jposug/perl5/site_perl/5.30
%dir /opt/jposug/perl5/site_perl/5.30/%{perl_dir}

%files encode
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/enc2xs
%{prefix}/bin/encguess
%{prefix}/bin/piconv
%dir %{prefix}/lib
%dir %{prefix}/lib/Encode
%{prefix}/lib/Encode/*
%dir %{prefix}/lib/%{perl_dir}
%dir %{prefix}/lib/%{perl_dir}/Encode
%{prefix}/lib/%{perl_dir}/Encode.pm
%{prefix}/lib/%{perl_dir}/Encode/*
%dir %{prefix}/man
%dir %{prefix}/man/man3
%{prefix}/man/man3/Encode.3
%{prefix}/man/man3/Encode::Alias.3
%{prefix}/man/man3/Encode::Byte.3
%{prefix}/man/man3/Encode::CJKConstants.3
%{prefix}/man/man3/Encode::CN.3
%{prefix}/man/man3/Encode::CN::HZ.3
%{prefix}/man/man3/Encode::Config.3
%{prefix}/man/man3/Encode::EBCDIC.3
%{prefix}/man/man3/Encode::Encoder.3
%{prefix}/man/man3/Encode::Encoding.3
%{prefix}/man/man3/Encode::GSM0338.3
%{prefix}/man/man3/Encode::Guess.3
%{prefix}/man/man3/Encode::JP.3
%{prefix}/man/man3/Encode::JP::H2Z.3
%{prefix}/man/man3/Encode::JP::JIS7.3
%{prefix}/man/man3/Encode::KR.3
%{prefix}/man/man3/Encode::KR::2022_KR.3
%{prefix}/man/man3/Encode::MIME::Header.3
%{prefix}/man/man3/Encode::MIME::Name.3
%{prefix}/man/man3/Encode::PerlIO.3
%{prefix}/man/man3/Encode::Supported.3
%{prefix}/man/man3/Encode::Symbol.3
%{prefix}/man/man3/Encode::TW.3
%{prefix}/man/man3/Encode::Unicode.3
%{prefix}/man/man3/Encode::Unicode::UTF7.3

%files podlators
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/pod2man
%{prefix}/bin/pod2text

%dir %{prefix}/lib/Pod
%{prefix}/lib/Pod/Man.pm
%{prefix}/lib/Pod/ParseLink.pm
%dir %{prefix}/lib/Pod/Text
%{prefix}/lib/Pod/Text/*
%dir %{prefix}/man
%dir %{prefix}/man/man3
%{prefix}/man/man3/Pod::Checker.3
%{prefix}/man/man3/Pod::Escapes.3
%{prefix}/man/man3/Pod::Find.3
%{prefix}/man/man3/Pod::Html.3
%{prefix}/man/man3/Pod::InputObjects.3
%{prefix}/man/man3/Pod::Man.3
%{prefix}/man/man3/Pod::ParseLink.3
%{prefix}/man/man3/Pod::Parser.3
%{prefix}/man/man3/Pod::Perldoc.3
%{prefix}/man/man3/Pod::Perldoc::BaseTo.3
%{prefix}/man/man3/Pod::Perldoc::GetOptsOO.3
%{prefix}/man/man3/Pod::Perldoc::ToANSI.3
%{prefix}/man/man3/Pod::Perldoc::ToChecker.3
%{prefix}/man/man3/Pod::Perldoc::ToMan.3
%{prefix}/man/man3/Pod::Perldoc::ToNroff.3
%{prefix}/man/man3/Pod::Perldoc::ToPod.3
%{prefix}/man/man3/Pod::Perldoc::ToRtf.3
%{prefix}/man/man3/Pod::Perldoc::ToTerm.3
%{prefix}/man/man3/Pod::Perldoc::ToText.3
%{prefix}/man/man3/Pod::Perldoc::ToTk.3
%{prefix}/man/man3/Pod::Perldoc::ToXml.3
%{prefix}/man/man3/Pod::PlainText.3
%{prefix}/man/man3/Pod::Select.3
%{prefix}/man/man3/Pod::Simple.3
%{prefix}/man/man3/Pod::Simple::Checker.3
%{prefix}/man/man3/Pod::Simple::Debug.3
%{prefix}/man/man3/Pod::Simple::DumpAsText.3
%{prefix}/man/man3/Pod::Simple::DumpAsXML.3
%{prefix}/man/man3/Pod::Simple::HTML.3
%{prefix}/man/man3/Pod::Simple::HTMLBatch.3
%{prefix}/man/man3/Pod::Simple::LinkSection.3
%{prefix}/man/man3/Pod::Simple::Methody.3
%{prefix}/man/man3/Pod::Simple::PullParser.3
%{prefix}/man/man3/Pod::Simple::PullParserEndToken.3
%{prefix}/man/man3/Pod::Simple::PullParserStartToken.3
%{prefix}/man/man3/Pod::Simple::PullParserTextToken.3
%{prefix}/man/man3/Pod::Simple::PullParserToken.3
%{prefix}/man/man3/Pod::Simple::RTF.3
%{prefix}/man/man3/Pod::Simple::Search.3
%{prefix}/man/man3/Pod::Simple::SimpleTree.3
%{prefix}/man/man3/Pod::Simple::Subclassing.3
%{prefix}/man/man3/Pod::Simple::Text.3
%{prefix}/man/man3/Pod::Simple::TextContent.3
%{prefix}/man/man3/Pod::Simple::XHTML.3
%{prefix}/man/man3/Pod::Simple::XMLOutStream.3
%{prefix}/man/man3/Pod::Text.3
%{prefix}/man/man3/Pod::Text::Color.3
%{prefix}/man/man3/Pod::Text::Overstrike.3
%{prefix}/man/man3/Pod::Text::Termcap.3
%{prefix}/man/man3/Pod::Usage.3


%files ext-mm
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/instmodsh
%dir %{prefix}/lib/ExtUtils/Command
%{prefix}/lib/ExtUtils/Command/*
%{prefix}/lib/ExtUtils/Command.pm
%dir %{prefix}/lib/ExtUtils/Liblist
%{prefix}/lib/ExtUtils/Liblist/*
%{prefix}/lib/ExtUtils/Liblist.pm
%{prefix}/lib/ExtUtils/MM.pm
%{prefix}/lib/ExtUtils/MM_*.pm
%{prefix}/lib/ExtUtils/MY.pm
%dir %{prefix}/lib/ExtUtils/MakeMaker
%{prefix}/lib/ExtUtils/MakeMaker/*
%{prefix}/lib/ExtUtils/MakeMaker.pm
%{prefix}/lib/ExtUtils/Mkbootstrap.pm
%{prefix}/lib/ExtUtils/Mksymlists.pm
%{prefix}/lib/ExtUtils/testlib.pm
%dir %{prefix}/man
%dir %{prefix}/man/man3
%{prefix}/man/man3/ExtUtils::MakeMaker.3
%{prefix}/man/man3/ExtUtils::MakeMaker::Config.3
%{prefix}/man/man3/ExtUtils::MakeMaker::FAQ.3
%{prefix}/man/man3/ExtUtils::MakeMaker::Locale.3
%{prefix}/man/man3/ExtUtils::MakeMaker::Tutorial.3
%{prefix}/man/man3/ExtUtils::Liblist.3
%{prefix}/man/man3/ExtUtils::MM.3
%{prefix}/man/man3/ExtUtils::MM_AIX.3
%{prefix}/man/man3/ExtUtils::MM_Any.3
%{prefix}/man/man3/ExtUtils::MM_BeOS.3
%{prefix}/man/man3/ExtUtils::MM_Cygwin.3
%{prefix}/man/man3/ExtUtils::MM_DOS.3
%{prefix}/man/man3/ExtUtils::MM_Darwin.3
%{prefix}/man/man3/ExtUtils::MM_MacOS.3
%{prefix}/man/man3/ExtUtils::MM_NW5.3
%{prefix}/man/man3/ExtUtils::MM_OS2.3
%{prefix}/man/man3/ExtUtils::MM_QNX.3
%{prefix}/man/man3/ExtUtils::MM_UWIN.3
%{prefix}/man/man3/ExtUtils::MM_Unix.3
%{prefix}/man/man3/ExtUtils::MM_VMS.3
%{prefix}/man/man3/ExtUtils::MM_VOS.3
%{prefix}/man/man3/ExtUtils::MM_Win32.3
%{prefix}/man/man3/ExtUtils::MM_Win95.3
%{prefix}/man/man3/ExtUtils::MY.3
%{prefix}/man/man3/ExtUtils::CBuilder.3
%{prefix}/man/man3/ExtUtils::CBuilder::Platform::Windows.3
%{prefix}/man/man3/ExtUtils::Command.3
%{prefix}/man/man3/ExtUtils::Command::MM.3
%{prefix}/man/man3/ExtUtils::Constant.3
%{prefix}/man/man3/ExtUtils::Constant::Base.3
%{prefix}/man/man3/ExtUtils::Constant::Utils.3
%{prefix}/man/man3/ExtUtils::Constant::XS.3
%{prefix}/man/man3/ExtUtils::Embed.3
%{prefix}/man/man3/ExtUtils::Install.3
%{prefix}/man/man3/ExtUtils::Installed.3


%files io-compress
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/zipdetails
%dir %{prefix}/lib/Compress
%{prefix}/lib/Compress/*
%dir %{prefix}/lib/File
%{prefix}/lib/File/GlobMapper.pm
%dir %{prefix}/lib/IO
%dir %{prefix}/lib/IO/Compress
%{prefix}/lib/IO/Compress/*
%dir %{prefix}/lib/IO/Uncompress
%{prefix}/lib/IO/Uncompress/*

%dir %{prefix}/man/man1
%{prefix}/man/man1/zipdetails.1

%dir %{prefix}/man
%dir %{prefix}/man/man3
%{prefix}/man/man3/IO::Compress::Base.3
%{prefix}/man/man3/IO::Compress::Bzip2.3
%{prefix}/man/man3/IO::Compress::Deflate.3
%{prefix}/man/man3/IO::Compress::FAQ.3
%{prefix}/man/man3/IO::Compress::Gzip.3
%{prefix}/man/man3/IO::Compress::RawDeflate.3
%{prefix}/man/man3/IO::Compress::Zip.3
%{prefix}/man/man3/IO::Uncompress::AnyInflate.3
%{prefix}/man/man3/IO::Uncompress::AnyUncompress.3
%{prefix}/man/man3/IO::Uncompress::Base.3
%{prefix}/man/man3/IO::Uncompress::Bunzip2.3
%{prefix}/man/man3/IO::Uncompress::Gunzip.3
%{prefix}/man/man3/IO::Uncompress::Inflate.3
%{prefix}/man/man3/IO::Uncompress::RawInflate.3
%{prefix}/man/man3/IO::Uncompress::Unzip.3

%files json-pp
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/json_pp
%dir %{prefix}/lib/JSON
%{prefix}/lib/JSON/*
%dir %{prefix}/man
%dir %{prefix}/man/man1
%{prefix}/man/man1/json_pp.1
%dir %{prefix}/man/man3
%{prefix}/man/man3/JSON::PP.3
%{prefix}/man/man3/JSON::PP::Boolean.3

%files ext-parsexs
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/xsubpp
%dir %{prefix}/lib/ExtUtils
%dir %{prefix}/lib/ExtUtils/ParseXS
%{prefix}/lib/ExtUtils/ParseXS/*
%{prefix}/lib/ExtUtils/ParseXS.pm
%{prefix}/lib/ExtUtils/ParseXS.pod
%dir %{prefix}/lib/ExtUtils/Typemaps
%{prefix}/lib/ExtUtils/Typemaps/*.pm
%{prefix}/lib/ExtUtils/Typemaps.pm
%{prefix}/lib/ExtUtils/xsubpp
%dir %{prefix}/man
%dir %{prefix}/man/man1
%{prefix}/man/man1/xsubpp.1
%dir %{prefix}/man/man3
%{prefix}/man/man3/ExtUtils::ParseXS.3
%{prefix}/man/man3/ExtUtils::ParseXS::Constants.3
%{prefix}/man/man3/ExtUtils::ParseXS::Eval.3
%{prefix}/man/man3/ExtUtils::ParseXS::Utilities.3
%{prefix}/man/man3/ExtUtils::Typemaps.3
%{prefix}/man/man3/ExtUtils::Typemaps::Cmd.3
%{prefix}/man/man3/ExtUtils::Typemaps::InputMap.3
%{prefix}/man/man3/ExtUtils::Typemaps::OutputMap.3
%{prefix}/man/man3/ExtUtils::Typemaps::Type.3

%files pod-parser
%defattr(-,root,bin)
%dir /opt/jposug/perl5
%dir %{prefix}
%dir %{prefix}/bin
%{prefix}/bin/podselect
%dir %{prefix}/lib
%dir %{prefix}/lib/Pod
%{prefix}/lib/Pod/Find.pm
%{prefix}/lib/Pod/InputObjects.pm
%{prefix}/lib/Pod/ParseUtils.pm
%{prefix}/lib/Pod/Parser.pm
%{prefix}/lib/Pod/PlainText.pm
%{prefix}/lib/Pod/Select.pm
%dir %{prefix}/man
%dir %{prefix}/man/man1
%dir %{prefix}/man/man3
%{prefix}/man/man3/Pod::ParseUtils.3

%changelog
* Fri Feb 14 2020 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
