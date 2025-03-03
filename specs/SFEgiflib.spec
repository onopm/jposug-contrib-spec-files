#
# spec file for package SFEgiflib
#
# includes module(s): giflib
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use giflib64 = giflib.spec
%endif

%include base.inc
%use giflib = giflib.spec

Name:		SFEgiflib
IPS_Package_Name:	image/library/giflib 
Summary:	%{giflib.summary}
Version:	%{giflib.version}
License:	MIT
SUNW_Copyright:	giflib.copyright
URL:		http://giflib.sourceforge.net/
Group:		System/Libraries
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Requires:       %pnm_requires_runtime_perl_510
Requires:       %pnm_requires_library_python_2_python_pigment_26

%include default-depend.inc

%package devel
IPS_Package_Name:	image/library/giflib/developer 
Summary:         %{summary} - development files
SUNW_BaseDir:    %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version
%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%giflib64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%giflib.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%giflib64.build -d %name-%version/%_arch64
%endif

%giflib.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%giflib64.install -d %name-%version/%_arch64
%endif

%giflib.install -d %name-%version/%{base_arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/gif*
%{_bindir}/*gif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/gif*
%{_bindir}/%{_arch64}/*gif
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif

%files devel
%defattr (-, root, bin)
%{_includedir}

%changelog
* Wed Jun 05 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sun Oct 16 2011 - Milan Jurik
- add IPS package name
* Sun Jul 24 2011 - Guido Berhoerster <gber@openindiana.org>
- added License and SUNW_Copyright tags
* Mon May 17 2010 - Milan Jurik
- bump to 4.1.6
* Thu Sep  6 2007 - dougs@truemail.co.th
- Initial version
