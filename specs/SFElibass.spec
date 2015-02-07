#
# spec file for package SFElibass
#
# includes module: libass
#

%include Solaris.inc
%define cc_is_gcc 1
%include packagenamemacros.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libass_64 = libass.spec
%endif

%include base.inc
%use libass = libass.spec

%define srcname libass

Name:		SFElibass
IPS_Package_Name:	library/video/libass
Summary:	%{libass.summary}
Group:		%{libass.group}
URL:		http://code.google.com/p/libass/
Version:	%{libass.version}
License:	%{libass.license}
SUNW_Copyright:	libass.copyright
%include default-depend.inc
BuildRequires:  library/fribidi/developer
Requires:	library/fribidi
Requires:	%{pnm_requires_system_library_freetype_2}
BuildRequires:	%{pnm_buildrequires_system_library_freetype_2}
Requires:	%{pnm_buildrequires_system_library_fontconfig}
BuildRequires:	%{pnm_requires_system_library_fontconfig}
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif

# Copied from Wikipedia
%description
SubStation Alpha (or Sub Station Alpha), abbreviated SSA, is a subtitle file
format created by CS Low (also known as Kotus) that allows for more advanced
subtitles than the conventional SRT and similar formats. This format can be
rendered with VSFilter in conjunction with a DirectShow-aware video player
(on Microsoft Windows), or MPlayer with the SSA/ASS library.

%package devel
IPS_Package_Name:	library/video/libass/developer
Summary:        %summary - development files
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libass_64.prep -d %name-%version/%_arch64
%endif
mkdir %name-%version/%{base_arch}
%libass.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%libass_64.build -d %name-%version/%_arch64
%endif

%libass.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libass_64.install -d %name-%version/%_arch64
%endif

%libass.install -d %name-%version/%{base_arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %_libdir
%_libdir/%srcname.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/%srcname.so*
%endif

%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/%srcname.pc
%ifarch amd64 sparcv9
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/%srcname.pc
%endif

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %_includedir
%_includedir/ass

%changelog
* Wed May 08 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sat Feb 09 2013 - Milan Jurik
- bump do 0.10.1
* Thu Jun 21 2012 - Logan Bruns <logan@gedanken.org>
- added missing requires for SFElibfribidi
* Sun Dec 11 2011 - Milan Jurik
- bump to 0.10.0
* Tue Aug 30 2011 - Alex Viskovatoff
- bump to 0.9.13; use gz tarball so spec builds with unpatched pkgtool
* Fri Jul 29 2011 - Alex Viskovatoff
- add SUNW_Copyright
* Sat Jul 16 2011 - Alex Viskovatoff
- Initial spec
