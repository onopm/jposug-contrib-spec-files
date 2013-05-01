#
# spec file for package SFElibmms
#
# includes module(s): libmms
#
# Copyright 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: halton
#

%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 0
%define _gpp g++
%include base.inc
%define _prefix /usr
%use libmms = libmms.spec

Name:		SFElibmms
IPS_Package_Name:	library/video/libmms
Summary:	mms stream protocol library
Group:		System/Multimedia Libraries
License:	LGPLv2
SUNW_Copyright:	libmms.copyright
URL:		http://libmms.sourceforge.net/
Version:	%{libmms.version}
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
Requires:	%{pnm_requires_SUNWgnome_base_libs}
Requires:	%{pnm_requires_SUNWlibm}
BuildRequires:	%{pnm_buildrequires_SUNWgnome_base_libs_devel}
Conflicts:	%{pnm_buildrequires_SUNWmms}
BuildRequires:	%{pnm_buildrequires_SUNWgnome_common_devel_devel}
Requires:       %{pnm_requires_glib2}
BuildRequires:  %{pnm_buildrequires_glib2}
Requires:       %{pnm_requires_system_library}
BuildRequires:  %{pnm_buildrequires_system_library}

%package devel
Summary:	%{summary} - development files
SUNW_BaseDir:	%{_basedir}
%include default-depend.inc
Requires:	%{name}

%prep
rm -rf %name-%version
mkdir -p %name-%version
%libmms.prep -d %name-%version

%build
#export CFLAGS="%optflags"
#export RPM_OPT_FLAGS="$CFLAGS"
%libmms.build -d %name-%version

%install
rm -rf $RPM_BUILD_ROOT
%libmms.install -d %name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%changelog
* Thr May 01 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- 64 bit ready
* Wed Jul 20 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Tue Sep 02 2008 - halton.huo@sun.com
- Initial version
