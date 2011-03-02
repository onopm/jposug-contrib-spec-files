#
# spec file for package SFEopenal_new.spec
#
# includes module(s): openal
# to become a official release of SFEopenal until other package that depend
# of me must work or not needed. Gilles Dauphin
#
%include Solaris.inc

%define src_name	openal-soft
%define src_url		http://kcat.strangesoft.net/openal-releases/

Name:                   SFEopenal
Summary:                OpenAL is a cross-platform 3D audio API
Version:                1.13
IPS_package_name:       library/media/openal
Source:                 %{src_url}/%{src_name}-%{version}.tar.bz2
URL:			http://connect.creativelabs.com/openal/
#Patch1:		openal-new-01.diff
Patch2:			openal-cmake-02.diff
SUNW_BaseDir:           %{_basedir}
SUNW_Copyright:         %{name}.copyright
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

BuildRequires: system/library/math/header-math
Requires:      system/library/math/header-math
BuildRequires: system/header/header-audio

#%if %with_libaudioio
#BuildRequires: SFElibaudioio-devel
#Requires: SFElibaudioio
#%endif

BuildRequires: developer/build/cmake

%package devel
Summary:                 %{summary} - development files
IPS_package_name:        library/media/header-openal
SUNW_BaseDir:            %{_prefix}
%include default-depend.inc

Meta(info.maintainer_url):      http://sourceforge.jp/forum/forum.php?forum_id=25193
Meta(info.upstream_url):        http://kcat.strangesoft.net/openal.html
Meta(info.classification):      org.opensolaris.category.2011:Media

%prep
rm -rf openal-soft*
bzcat %{SOURCE} | gtar xf -
cd openal-soft*
#%patch1 -p1
%patch2 -p1
cd ..

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

cd %{src_name}-%{version}
CC=cc
export CC
cd build
cmake -DHAVE_GCC_VISIBILITY:INTERNAL=0 -DCMAKE_INSTALL_PREFIX:PATH=%_prefix -DHAVE_VISIBILITY_SWITCH:INTERNAL=0 ..
make

%install
rm -rf $RPM_BUILD_ROOT
cd %{src_name}-%{version}
cd build
mkdir -p $RPM_BUILD_ROOT/%{_prefix}
export DESTDIR=$RPM_BUILD_ROOT
make install
#mv ./sfw_stage/* $RPM_BUILD_ROOT/%{_prefix}
#rm $RPM_BUILD_ROOT/%{_libdir}/lib*.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_bindir}
%dir %attr(0755,root,bin) %{_libdir}
%dir %attr(0755,root,other) %{_libdir}/pkgconfig
%{_libdir}/lib*.so*
%{_libdir}/pkgconfig/*

%files devel
%defattr (-, root, bin)
%{_includedir}

%changelog
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
