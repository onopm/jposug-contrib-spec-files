#
# spec file for package SFEid3lib-gpp
#
# includes module(s): id3lib
#
#
%include Solaris.inc
%include packagenamemacros.inc
#%include usr-g++.inc
%define cc_is_gcc 1

%ifarch amd64 sparcv9
%include arch64.inc
%use id3lib_64 = id3lib.spec
%endif

%include base.inc
%use id3lib = id3lib.spec
%include base.inc

Name:                    SFEid3lib-gpp
IPS_package_name:	 library/audio/g++/id3lib
SUNW_Copyright: %name.copyright
License: LGPLv2
Summary:                 id3lib (g++) - a software library for manipulating ID3v1/v1.1 and ID3v2 tags (g++)
Version:                 3.8.3
Source:                  %{sf_download}/id3lib/id3lib-%{version}.tar.gz
Patch1:                  id3lib-01-wall.diff
Patch2:                  id3lib-02-uchar.diff
Patch3:                  id3lib-03-gcc4.diff
Patch4:		id3lib-04-iconv.diff
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
Requires: %{pnm_requires_SUNWzlib}
Requires: SUNWlibC
Requires: %{pnm_buildrequires_SUNWlibms}
BuildRequires: sfe/developer/build/cmake
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif

%package devel
IPS_package_name:        library/audio/g++/id3lib/developer
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%id3lib_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%id3lib.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%id3lib_64.build -d %name-%version/%_arch64
%endif

%id3lib.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT

%ifarch amd64 sparcv9
%id3lib_64.install -d %name-%version/%_arch64
%endif

%id3lib.install -d %name-%version/%{base_arch}
%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
for file in id3convert id3cp id3info id3tag
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
%hard %{_bindir}/id3convert
%hard %{_bindir}/id3cp
%hard %{_bindir}/id3info
%hard %{_bindir}/id3tag
%else
%{_bindir}/id3convert
%{_bindir}/id3cp
%{_bindir}/id3info
%{_bindir}/id3tag
%endif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/*
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Sun May 19 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- change dependency
* Fri May 03 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Fri May 03 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sun Jun 24 2012 - Thomas Wagner
- add -fpermissive to CXXFLAGS, oi151a4 g++ 4.6.3 needs -fpermissiv, s11 doesn't (can't tell why)
* Sat Apr 21 2012 - Thomas Wagner
- %include usr-g++.inc to relocate out from /usr/gnu to --prefix=/usr/g++
- use _std_datadir in ACLOCAL_FLAGS
- add IPS_package_name
- rename package to reflect gcc/g++ compiler and propper location
* Fri Sep 25 2009 - trisk@opensolaris.org
- Add patch3
- Update build system
* Tue Jul 17 2007 - dougs@truemail.co.th
- Converted from SFEid3lib
