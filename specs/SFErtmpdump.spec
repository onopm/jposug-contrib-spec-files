#
# Copyright (c) 2010 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc
#%include usr-gnu.inc
%define cc_is_gcc 1
%include packagenamemacros.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use rtmpdump_64 = rtmpdump.spec
%endif

%include base.inc
%use rtmpdump = rtmpdump.spec

# TODO: write SMF manifest for rtmpsrv

Name:                SFErtmpdump
Summary:             RTMPdump -- a toolkit for RTMP streams
IPS_package_name:    video/rtmpdump
Group:               Applications/Sound and Video
License:             GPLv2+, LGPLv2+
SUNW_copyright:      rtmpdump.copyright
URL:                 http://rtmpdump.mplayerhq.hu/
Version:             2.4
Source:		http://rtmpdump.mplayerhq.hu/download/rtmpdump-%{version}.tar.gz
Patch1:		SFErtmpdump-make.patch
Patch2:		SFErtmpdump-librtmp-make.patch
SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif
%include default-depend.inc
#Requires: SFEboost
BuildRequires: %{pnm_buildrequires_SUNWopenssl}
Requires: %{pnm_requires_SUNWopenssl}
BuildRequires: %{pnm_buildrequires_zlib}
Requires: %{pnm_requires_zlib}

%package devel
IPS_package_name:    video/rtmpdump/developer
Requires: %{pnm_buildrequires_SUNWopenssl}
Summary:         %{summary} - development files
SUNW_BaseDir:    %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%rtmpdump_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%rtmpdump.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%rtmpdump_64.build -d %name-%version/%_arch64
%endif

%rtmpdump.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%rtmpdump_64.install -d %name-%version/%_arch64
%endif

%rtmpdump.install -d %name-%version/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
for file in rtmpdump rtmpgw rtmpsrv rtmpsuck
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
%hard %{_bindir}/rtmpdump
%hard %{_bindir}/rtmpgw
%hard %{_bindir}/rtmpsrv
%hard %{_bindir}/rtmpsuck
%else
%{_bindir}/rtmpdump
%{_bindir}/rtmpgw
%{_bindir}/rtmpsrv
%{_bindir}/rtmpsuck
%endif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*.so*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/rtmpdump.1
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/librtmp.3
%dir %attr (0755, root, bin) %{_mandir}/man8
%{_mandir}/man8/rtmpgw.8
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
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/librtmp/*


%changelog

* Tue May 14 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- Added 64bit build
* Sat Feb 09 2013 - Milan Jurik
- bump to 2.4
* Oct 12 2011 - Alex Viskovatoff
- Fix librtmp.pc; add SUNW_copyright and IPS_package_name
* Dec 28 2010 - jchoi42@pha.jhu.edu
- Initial spec
