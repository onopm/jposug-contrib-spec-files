#
# spec file for package SFEopenal_new.spec
#
# includes module(s): openal
# to become a official release of SFEopenal until other package that depend
# of me must work or not needed. Gilles Dauphin
#
%include Solaris.inc
%define cc_is_gcc 1
%include packagenamemacros.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use openal_64 = openal.spec
%endif

%include base.inc
%use openal = openal.spec

%define src_name	openal-soft
%define src_url		http://kcat.strangesoft.net/openal-releases/
%define with_libaudioio %(pkginfo -q SFElibaudioio && echo 1 || echo 0)

Name:                   SFEopenal
Summary:                OpenAL is a cross-platform 3D audio API
Version:                1.14
IPS_package_name:       library/media/openal
Source:                 %{src_url}/%{src_name}-%{version}.tar.bz2
URL:			http://connect.creativelabs.com/openal/
#Patch1:		openal-new-01.diff
Patch2:			openal-cmake-02.diff
Patch3:			SFEopenal-CMakeLists.patch
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:         %{name}.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

BuildRequires: system/library/math/header-math
Requires:      system/library/math/header-math
BuildRequires: system/header/header-audio

%if %with_libaudioio
BuildRequires: SFElibaudioio-devel
Requires: SFElibaudioio
%endif

BuildRequires: sfe/developer/build/cmake
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif
BuildRequires: SUNWlibms
Requires: SUNWlibms
BuildRequires: %{pnm_buildrequires_SUNWaudh}

%package devel
Summary:                 %{summary} - development files
IPS_package_name:        library/media/header-openal
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc
Requires: %{name}

Meta(info.maintainer_url):      http://sourceforge.jp/forum/forum.php?forum_id=25193
Meta(info.upstream_url):        http://kcat.strangesoft.net/openal.html
Meta(info.classification):      org.opensolaris.category.2011:Media

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%openal_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%openal.prep -d %name-%version/%{base_arch}

%build

%ifarch amd64 sparcv9
%openal_64.build -d %name-%version/%_arch64
%endif

%openal.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%openal_64.install -d %name-%version/%_arch64
%endif

%openal.install -d %name-%version/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/openal-info $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/makehrtf $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec openal-info
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec makehrtf
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%if %can_isaexec
%{_bindir}/%{base_isa}
%hard %{_bindir}/openal-info
%hard %{_bindir}/makehrtf
%else
%{_bindir}/openal-info
%{_bindir}/makehrtf
%endif
%dir %attr(0755,root,bin) %{_libdir}
%dir %attr(0755,root,other) %{_libdir}/pkgconfig
%{_libdir}/lib*.so*
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%files devel
%defattr (-, root, bin)
%{_includedir}

%changelog
* Sun May 19 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- rewrite dependency to use sfe's cmake
* Wed May 16 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Added 64bit build
* Sun Aug 19 2012 - Thomas Wagner
- change to BuildRequires to %{pnm_buildrequires_SUNWaudh}, %include packagenamacros.inc
- add standard CFLAGS, LDFLAGS
* Sun Aug 19 2012 - Milan Jurik
- bump to 1.14
* Wed Mar 02 2011 - Satoru MIYAZAKI<s.miyaza@gmail.com>
- bump to 1.13
- Support for Solaris11 Express.
* Mon Jan 17 2011 - Thomas Wagner
- add env var DESTDIR, remove mv ./sfw_stage/*
* Fri Oct 29 2010 - Thomas Wagner
- bump to 1.12.854
- new Download Source
- remove patch1 openal-new-01.diff
* Fri May 14 2010 - Milan Jurik
- use OSS/Boomer as main audio interface
* Sun Apr 11 2010 - Milan Jurik
- update to 1.11.753
- once again reverting install because it is not working for all make commands and across openal versions
* Mar 03 2010 - Gilles Dauphin
- DESTDIR work for me in b133 and install perfectly well
- work with last CBE and last pkgbuild 1.3.101 in 2009.06 and b133.
* Sun Aug 09 2009 - Thomas Wagner
- (Build)Requires: SUNWlibms
- install with DESTDIR is broken, revert back to version wich works with standard make (CBE)
* Jul 20 2009 - dauphin@enst.fr
- install with DESTDIR as usual
* Sun Feb 15 2009 - Thomas Wagner
- bump to 1.7.411
- rework patch openal-new-01.diff and "cd" into sourcedir to patch version independently
* Sun Mar 15 2009 - Milan Jurik
- original source URL
* Sun Feb  8 2009 - Thomas Wagner
- quick fix for complaining make install about already defined "relative" installtarget (./sfw_stage)
* Mon Dec 22 2008 - Thomas Wagner
- make conditional BuildRequirement SUNWcmake / SFEcmake
* Sat Nov 15 2008 - dauphin@enst.fr
- change to new release of openal 1.5.304.
* Tue Jun  5 2007 - dougs@truemail.co.th
- Added patch for Sun Studio 12 builds - openal-03-packed.diff
* Tue May  1 2007 - dougs@truemail.co.th
- Initial version
