#
# spec file for package SFEopenal_new.spec
#
# includes module(s): openal
# to become a official release of SFEopenal until other package that depend
# of me must work or not needed. Gilles Dauphin
#

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

%prep
bzcat %{SOURCE} | gtar xf -
cd openal-soft*
#%patch1 -p1
%patch2 -p1
%patch3 -p0 -b .sfe.orig
cd ..

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CC=gcc
export CFLAGS="%{optflags}"
export LDFLAGS="%{_ldflags}"
export PKG_CONFIG_PATH="%{_pkg_config_path}"

cd %{src_name}-%{version}
cd build
%if %{opt_arch64}
cmake -DHAVE_GCC_VISIBILITY:INTERNAL=0 -DCMAKE_INSTALL_PREFIX=%_prefix -DLIB_SUFFIX=/%{bld_arch} -DHAVE_VISIBILITY_SWITCH:INTERNAL=0 ..
%else
cmake -DHAVE_GCC_VISIBILITY:INTERNAL=0 -DCMAKE_INSTALL_PREFIX=%_prefix -DHAVE_VISIBILITY_SWITCH:INTERNAL=0 ..
%endif
make

%install
cd %{src_name}-%{version}
cd build
mkdir -p $RPM_BUILD_ROOT/%{_prefix}
export DESTDIR=$RPM_BUILD_ROOT
make install
#mv ./sfw_stage/* $RPM_BUILD_ROOT/%{_prefix}
#rm $RPM_BUILD_ROOT/%{_libdir}/lib*.*a

%changelog
* Wed May 16 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Added 64bit build
- If the ffmpeg-1.2.1 was installed and the OPTION "Build and install example programs" is on, cmake will crash.
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
