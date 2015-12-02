#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%ifarch amd64 sparcv9
%include arch64.inc
%use libast_64 = libast.spec
%endif
%include base.inc
%use libast = libast.spec
%define option_with_fox 0

Name:                SFElibast
IPS_Package_Name:	 library/desktop/libast 
Summary:             Library of Assorted Spiffy Things
Version:             0.7
Source:              http://eterm.org/download/libast-%{version}.tar.gz
License:             MIT
Group:		Desktop (GNOME)/Libraries
SUNW_Copyright:      libast.copyright
URL:                 http://www.eterm.org/download/

SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif
#BuildRequires: SFEgcc
BuildRequires: image/library/imlib2 
Requires: image/library/imlib2
Requires: %pnm_requires_SUNWfreetype2
%if %option_with_fox
Requires: FSWxorg-clientlibs
Requires: FSWxwrtl
BuildRequires: FSWxorg-headers
%else
Requires: %pnm_requires_x11_clients
%endif
#Requires: SFEgccruntime

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libast_64.prep -d %name-%version/%_arch64
%endif
mkdir %name-%version/%{base_arch}
%libast.prep -d %name-%version/%{base_arch}

%build

%ifarch amd64 sparcv9
%libast_64.build -d %name-%version/%_arch64
%endif

%libast.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%libast_64.install -d %name-%version/%_arch64
/bin/rm -rf $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/libast-config
%endif
%libast.install -d %name-%version/%{base_arch}

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_libdir}/lib*.so*
%{_bindir}/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*

%changelog
* Mon Jun 10 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- Added 64bit build
* Wed Jul 20 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Sun Jul 10 2011 - Alex Viskovatoff
- Build with SFEgcc
* Fri Mar 21 2008 - nonsea@users.sourceforge.net
- Fix Source error.
* Thu Nov 15 2007 - daymobrew@users.sourceforge.net
- Add support for Indiana builds.
* Mon Mar 19 2007 - dougs@truemail.co.th
- Fixed -fno-omit-frame-pointer flag
* Tue Nov 07 2006 - Eric Boutilier
- Initial spec
