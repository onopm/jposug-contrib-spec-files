#
# spec file for package SFEopenjpeg
#
# includes module(s): openjpeg
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 0
%define _prefix /usr

%define	src_name openjpeg
%define	src_url	http://www.openjpeg.org
%define major_version 1.5

%ifarch amd64 sparcv9
%include arch64.inc
%use openjpeg_64 = openjpeg.spec
%endif
%include base.inc
%use openjpeg = openjpeg.spec

Name:		SFEopenjpeg
IPS_Package_Name:	image/library/openjpeg
Group:		System/Libraries
Summary:	Open Source multimedia framework
License:	BSD
SUNW_Copyright:	openjpeg.copyright
Version:	%{major_version}.1
Source:		http://openjpeg.googlecode.com/files/openjpeg-%{version}.tar.gz
SUNW_BaseDir:   %{_basedir}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

BuildRequires: %{pnm_buildrequires_image_library_libpng}
Requires: %{pnm_requires_image_library_libpng}
BuildRequires: %{pnm_buildrequires_image_library_libtiff}
Requires: %{pnm_requires_image_library_libtiff}
BuildRequires: sfe/developer/build/cmake

%package devel
Summary:         %{summary} - development files
IPS_Package_Name:	image/library/openjpeg/developer
SUNW_BaseDir:    %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir -p %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%openjpeg_64.prep -d %name-%version/%_arch64
%endif
mkdir %name-%version/%{base_arch}
%openjpeg.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%openjpeg_64.build -d %name-%version/%_arch64
%endif
%openjpeg.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%openjpeg_64.install -d %name-%version/%_arch64
%endif
%openjpeg.install -d %name-%version/%{base_arch}
rm -rf $RPM_BUILD_ROOT%{_libdir}/%src_name-%major_version
%ifarch amd64 sparcv9
rm -rf $RPM_BUILD_ROOT%{_libdir}/%_arch64/%src_name-%major_version
%endif
%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
#mv $RPM_BUILD_ROOT%{_bindir}/opj_decompress $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
#mv $RPM_BUILD_ROOT%{_bindir}/opj_compress $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
#mv $RPM_BUILD_ROOT%{_bindir}/opj_dump $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
#cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec opj_decompress
#cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec opj_compress
#cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec opj_dump
mv $RPM_BUILD_ROOT%{_bindir}/j2k_to_image $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/image_to_j2k $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/j2k_dump $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec j2k_to_image
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec image_to_j2k
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec j2k_dump 
%endif

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%if %can_isaexec
%{_bindir}/%{base_isa}
#v2.0
#%hard %{_bindir}/opj_decompress
#%hard %{_bindir}/opj_compress
#%hard %{_bindir}/opj_dump
%hard %{_bindir}/j2k_to_image
%hard %{_bindir}/image_to_j2k
%hard %{_bindir}/j2k_dump
%else
#v2.0
#%{_bindir}/opj_decompress
#%{_bindir}/opj_compress
#%{_bindir}/opj_dump
%{_bindir}/j2k_to_image
%{_bindir}/image_to_j2k
%{_bindir}/j2k_dump

%endif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr(0755,root,other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%{_mandir}
%dir %attr (0755, root, other) %{_docdir}
%{_docdir}/*

%files devel
%defattr (-, root, bin)
%{_includedir}
#%dir %attr (0755, root, sys) %{_datadir}
#%{_datadir}/openjpeg-%{major_version}
#%{_datadir}/pkgconfig/*.pc

%changelog
* Sun May 19 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- rewrite dependency to use sfe's cmake
* Sat May 04 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- bump to 1.5.1
* Sat Feb 18 2012 - Milan Jurik
- bump to 1.5.0
* Tue Oct 11 2011 - Milan Jurik
- bump to 1.4
- add IPS package name
* Sun Jul 24 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Fri May 21 2010 - Milan Jurik
- update to 1.3, split devel package
* Sun Jul 29 2007 - dougs@truemail.co.th
- Initial spec
