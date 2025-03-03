#
# spec file for package SFEffmpeg
#
# includes module(s): FFmpeg
#
%include Solaris.inc
%define cc_is_gcc 1
%include packagenamemacros.inc

#always set to 1 except debug
%define enable_32 1
%define enable_amd64 0
%ifarch amd64
# If problems was found, set enable_amd64 to 0
%define enable_amd64 1
%include arch64.inc
%define extra_gcc_flags -msse
%define arch_opt --cpu=x86_64 --enable-mmx --enable-sse --enable-ssse3
%use ffmpeg_64 = ffmpeg.spec
%endif

%if %arch_sse2
%define opt_arch64 0
%define arch_opt --cpu=prescott --enable-mmx --enable-sse --enable-ssse3
#make this empty
%define extra_gcc_flags
%include x86_sse2.inc
%use ffmpeg_sse2 = ffmpeg.spec
%endif

%include base.inc

%ifarch sparc sparcv9
#make this empty
%define extra_gcc_flags
%define arch_opt --disable-optimizations
%endif

%ifarch i386
#with -msse (gcc) you can have asm XMM_CLOBBERS accepted
#read line 00079 in http://www.libav.org/doxygen/master/x86__cpu_8h_source.html 
%define extra_gcc_flags -msse
%define arch_opt --enable-runtime-cpudetect --enable-mmx --enable-sse --enable-ssse3 
%endif

%include base.inc
%use ffmpeg = ffmpeg.spec

Name:                    SFEffmpeg
IPS_Package_Name:	video/ffmpeg
Summary:                 %{ffmpeg.summary}
Version:                 %{ffmpeg.version}
License:                 GPLv2+ and LGPLv2.1+
SUNW_Copyright:          ffmpeg.copyright
URL:                     %{ffmpeg.url}
Group:		         System/Multimedia Libraries

SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
Autoreqprov:             on

%include default-depend.inc
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif
BuildRequires: SFEyasm
BuildRequires: %{pnm_buildrequires_SUNWtexi_devel}
BuildRequires: %{pnm_buildrequires_perl_default}
BuildRequires: SUNWxwinc
Requires: %{pnm_buildrequires_SUNWxwrtl}
Requires: %{pnm_buildrequires_SUNWzlib}
BuildRequires: %{pnm_buildrequires_SUNWlibsdl_devel}
Requires:      %{pnm_requires_SUNWlibsdl}
BuildRequires: SFElibgsm-devel
Requires: SFElibgsm
BuildRequires: SFExvid-devel
Requires: SFExvid
BuildRequires: SFElibx264-devel
Requires: SFElibx264
BuildRequires: SFEfaad2-devel
Requires: SFEfaad2
BuildRequires: SFEfaac-devel
Requires: SFEfaac
BuildRequires: SFElame-devel
Requires: SFElame
BuildRequires: %{pnm_buildrequires_SUNWogg_vorbis_devel}
Requires: %{pnm_buildrequires_SUNWogg_vorbis}
BuildRequires: %{pnm_buildrequires_SUNWlibtheora_devel}
Requires: %{pnm_buildrequires_SUNWlibtheora}
BuildRequires: %{pnm_buildrequires_SUNWspeex_devel}
Requires: %{pnm_buildrequires_SUNWspeex}
BuildRequires: SFEopencore-amr-devel
Requires: SFEopencore-amr
BuildRequires: %{pnm_buildrequires_SUNWgsed_devel}
BuildRequires: SFEopenjpeg-devel
Requires: SFEopenjpeg
BuildRequires: SFElibschroedinger-devel
Requires: SFElibschroedinger
BuildRequires: SFErtmpdump-devel
Requires: SFErtmpdump
BuildRequires: SFElibass-devel
Requires: SFElibass
BuildRequires: SFEopenal-devel
Requires: SFEopenal
BuildRequires: SFElibvpx-devel
Requires: SFElibvpx
BuildRequires: %{pnm_buildrequires_ggrp}

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version

%if %enable_amd64
%ifarch amd64
mkdir %name-%version/%_arch64
%ffmpeg_64.prep -d %name-%version/%_arch64
%endif
%endif

%if %enable_32
%if %arch_sse2
mkdir %name-%version/%sse2_arch
%ffmpeg_sse2.prep -d %name-%version/%sse2_arch
%endif

mkdir %name-%version/%base_arch
%ffmpeg.prep -d %name-%version/%base_arch
%endif

%build

%if %enable_amd64
%ifarch amd64
%ffmpeg_64.build -d %name-%version/%_arch64
%endif
%endif

%if %enable_32
%if %arch_sse2
%ffmpeg_sse2.build -d %name-%version/%sse2_arch
%endif

%ffmpeg.build -d %name-%version/%base_arch
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %enable_amd64
%ifarch amd64
%ffmpeg_64.install -d %name-%version/%_arch64
%endif
%endif

%if %enable_32
%if %arch_sse2
%ffmpeg_sse2.install -d %name-%version/%sse2_arch
%endif

%ffmpeg.install -d %name-%version/%base_arch
%endif

%if %can_isaexec
%if %enable_32
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/ffserver $RPM_BUILD_ROOT%{_bindir}/%{base_isa}/
mv $RPM_BUILD_ROOT%{_bindir}/ffplay $RPM_BUILD_ROOT%{_bindir}/%{base_isa}/
mv $RPM_BUILD_ROOT%{_bindir}/ffmpeg $RPM_BUILD_ROOT%{_bindir}/%{base_isa}/
mv $RPM_BUILD_ROOT%{_bindir}/ffprobe $RPM_BUILD_ROOT%{_bindir}/%{base_isa}/
%endif
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec ffserver
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec ffplay
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec ffmpeg
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec ffprobe
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%define _pkg_docdir %_docdir/ffmpeg
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%if %can_isaexec
%if %enable_32
%{_bindir}/%{base_isa}/*
%endif
%if %enable_amd64
%ifarch amd64
%{_bindir}/%{_arch64}/*
%endif
%endif
%if %enable_32
%if %arch_sse2
%{_bindir}/%{sse2_arch}/*
%endif
%endif
%hard %{_bindir}/ffserver
%hard %{_bindir}/ffplay
%hard %{_bindir}/ffmpeg
%hard %{_bindir}/ffprobe
#%hard %{_bindir}/avconv
%else
%if %enable_32
%{_bindir}/*
%endif
%endif
%dir %attr (0755, root, bin) %{_libdir}
%if %enable_32
%{_libdir}/lib*.so*
%endif
%if %enable_amd64
%ifarch amd64
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%endif
%if %enable_32
%if %arch_sse2
%dir %attr (0755, root, bin) %{_libdir}/%{sse2_arch}
%{_libdir}/%{sse2_arch}/lib*.so*
%endif
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/ffmpeg
%{_mandir}

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%if %enable_32
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%endif
%if %enable_amd64
%ifarch amd64
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*.pc
%endif
%endif
%if %enable_32
%if %arch_sse2
%dir %attr (0755, root, other) %{_libdir}/%{sse2_arch}/pkgconfig
%{_libdir}/%{sse2_arch}/pkgconfig/*.pc
%endif
%endif
%if %enable_32
%{_libdir}/ffmpeg
%endif
%if %enable_amd64
%ifarch amd64
%{_libdir}/%{_arch64}/ffmpeg
%endif
%endif
%if %enable_32
%if %arch_sse2
%{_libdir}/%{sse2_arch}/ffmpeg
%endif
%endif
%{_includedir}

%changelog
* Sun May 19 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- Added 64bit build except sparcv9
* Sun Sep 30 2012 - Milan Jurik
- bump to 1.0
* Sun Jun 24 2012 - Thomas Wagner
- change (Build)Requires to %{pnm_buildrequires_SUNWlibsdl_devel}
* Sun May 27 2012 - Milan Jurik
- bump to 0.11
* Sun Apr 29 2012 - Pavel Heimlich
- really add vpx dependency
* Tue Jan 24 2012 - James Choi
- update files for 0.10
* Mon Dec 12 2011 - Milan Jurik
- bump to 0.9
* Sun Nov 13 2011 - Michael Kosarev
- add libvpx dependency
* Sun Oct 23 2011 - Milan Jurik
- add IPS package name
- add rtmp dep
* Wed Aug 17 2011 - Thomas Wagner
- %arch_sse2 change minimum-CPU i686 to prescott, add --enable-sse --enable-ssse2
- for arch i86 by default --enable-runtime-cpudetect, add extra_gcc_flags -msse
  to have asm being lucky with XMM_CLOBBERS, remove --disable-asm (asm active again)
- remove build-time pkgtool commandline option --with-runtime_cpudetect (now 
  always enabled for i86)
- Implementation note: Programs using pentium_pro+mmx must request these libs 
  with isaexec (see what ffmpeg binary does via /usr/lib/isaexec) or in other
  progams tell the linker to select the library for you, via 
  export LD_OPTIONS='-f libavcodec.so.53:libavdevice.so.53:libavfilter.so.2:
  libavformat.so.53:libavutil.so.51:libswscale.so.2:libpostproc.so.51'
  and -R this early in LD_FLAGS="-R%{_libdir}/\$ISALIST %_ldflags"
  At least put ISALIST before any other -R/usr/lib !
  For debug use       LD_DEBUG=libs program_to_test
* Sat Aug 13 2011 - Thomas Wagner
- bump to 0.8.2
- change in include/x86_sse2.inc to not set -xarch=sse2 in arch_ldadd 
  for case cc_is_gcc == 1 - this avoids gcc errors in configure
  "gcc: error: language arch=sse2 not recognized"
- add switch with_runtime_cpudetect, by default set to off 
  (Distro builders may switch this to on with pkgtool --with-runtime_cpudetect )
##TODO## might need some testing if acceleration works on CPUs
- comment %doc, manpages - files not present in 0.8.2
- re-add patches removed with r3618, reworked,
  patch9: configure gnuism, re-add manpages by pod2man if texi2html not available,
  (reworked ffmpeg-02-configure.diff and ffmpeg-03-gnuisms.diff)
  patch10: *new* get texi2html work again - fix probably incomplete or needs updated
  texi2html, re-add %doc and manpages
- allow parallel build gmake -j$CPUS
- add patch11: ffmpeg-11-add-sys_videodev2_h.diff (reworked ffmpeg-03-v4l2.diff)
##TODO## v4l2 patch11 incomplete, maybe needs more from ffmpeg-03-v4l2.diff, ffmpeg-07-new-v4l2.diff
- for pod2man add in %install export PATH=/usr/perl5/bin:$PATH
- fix perms for %{_datadir}/doc
- replace %doc with manual install
- make all /bin/sh script in source tree use /usr/bin/bash
##TODO## patch11 incomplete, maybe needs more from ffmpeg-03-v4l2.diff, ffmpeg-07-new-v4l2.diff
##TODO## verify build-time dependencies (texi2html, pod2man, others)
##TODO## check if v4l patches still apply on Solaris
* Sat Jul 16 2011 - Alex Viskovatoff
- Add SFEyasm as a dependency; package documentation files
- Add --disable-asm as option for i386 so that newer versions build
* Wed May 11 2011 - Alex Viskovatoff
- Add SFEgccruntime as a dependency
* Mon Jan 24 2011 - Alex Viskovatoff
- Add missing build dependency
* Wed Jun 16 2010 - Milan Jurik
- update to 0.6
- remove older amr codecs, add libschroedinger and openjpeg
- remove mlib because it is broken now
- remove Solaris V4L2 support, more work needed
* Tue Apr 06 2010 - Milan Jurik
- missing perl build dependency (pod2man)
* Sun Mar 07 2010 - Milan Jurik
- replace amrXX for opencore implementation
* Tue Sep 08 2009 - Milan Jurik
- amrXX optional
- improved multiarch support (64-bit not done because of missing SUNW libraries)
* Mon Mar 16 2009 - Milan Jurik
- version 0.5
* Fri Jun 13 2008 - trisk@acm.jhu.edu
- New spec for base-spec
