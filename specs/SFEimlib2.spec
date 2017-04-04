#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc
%include packagenamemacros.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use imlib2_64 = imlib2.spec
%endif

%include base.inc
%use imlib2 = imlib2.spec

Name:		SFEimlib2
IPS_Package_Name:	image/library/imlib2
Summary:	General image loading and rendering library
Group:		System/Multimedia Libraries
Version:	1.4.5
License:	BSD
SUNW_Copyright:	imlib2.copyright
Source:		%{sf_download}/enlightenment/imlib2-%{version}.tar.gz
Patch1:		imlib2-01-std99.diff
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	%pnm_buildrequires_x11_clients
Requires:	%pnm_requires_x11_clients
BuildRequires:	library/audio/libid3tag/developer
Requires:	library/audio/libid3tag
BuildRequires:  image/library/giflib/developer
Requires:       image/library/giflib
BuildRequires:  %pnm_buildrequires_compress_bzip2
Requires:       %pnm_requires_compress_bzip2
BuildRequires:  %pnm_buildrequires_image_library_libjpeg
Requires:       %pnm_requires_image_library_libjpeg
BuildRequires:  %pnm_buildrequires_image_library_libtiff
Requires:       %pnm_requires_image_library_libtiff
BuildRequires:  %pnm_buildrequires_library_zlib
Requires:       %pnm_requires_library_zlib
BuildRequires:  %pnm_buildrequires_system_library_freetype_2
Requires:       %pnm_requires_system_library_freetype_2
%include default-depend.inc

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%imlib2_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%imlib2.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%imlib2_64.build -d %name-%version/%_arch64
%endif

%imlib2.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%imlib2_64.install -d %name-%version/%_arch64
rm -rf $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/imlib2-config
%endif
%imlib2.install -d %name-%version/%{base_arch}
%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
for file in imlib2_bumpmap imlib2_colorspace imlib2_conv imlib2_grab imlib2_poly imlib2_show imlib2_test imlib2_view
do
 mv $RPM_BUILD_ROOT%{_bindir}/$file $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
 cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec $file
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%if %can_isaexec
%{_bindir}/%{base_isa}
%hard %{_bindir}/imlib2_bumpmap
%hard %{_bindir}/imlib2_colorspace
%hard %{_bindir}/imlib2_conv
%hard %{_bindir}/imlib2_grab
%hard %{_bindir}/imlib2_poly
%hard %{_bindir}/imlib2_show
%hard %{_bindir}/imlib2_test
%hard %{_bindir}/imlib2_view
%{_bindir}/imlib2-config
%else
%{_bindir}/imlib2_bumpmap
%{_bindir}/imlib2_colorspace
%{_bindir}/imlib2_conv
%{_bindir}/imlib2_grab
%{_bindir}/imlib2_poly
%{_bindir}/imlib2_show
%{_bindir}/imlib2_test
%{_bindir}/imlib2_view
%{_bindir}/imlib2-config
%endif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, other) %{_libdir}/imlib2
%{_libdir}/imlib2/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/imlib2
%{_libdir}/%{_arch64}/imlib2/*
%endif
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/*

%changelog
* Wed Jun 05 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- Added 64bit build
* Sun Feb 05 2012 - Milan Jurik
- bump to 1.4.5
* Thu Aug 26 2010 - brian.cameron@oracle.com
- Bump to 1.4.4.
* Mon Jan 05 2008 - brian.cameron@sun.com
- Bump to 1.4.2.
* Thu Nov 15 2007 - daymobrew@users.sourceforge.net
- Add support for Indiana builds.
* Tue Nov 07 2006 - Eric Boutilier
- Initial spec
