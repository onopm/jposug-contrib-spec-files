#
# spec file for package SFElibssh2
#
# includes module(s): libssh2
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use libssh264 = libssh2.spec
%endif

%include base.inc
%use libssh2 = libssh2.spec

Name:		SFElibssh2
IPS_package_name:	library/security/ssh2
SUNW_Copyright:		%{name}.copyright
Summary:	%{libssh2.summary}
Version:	%{libssh2.version}
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%package developer
IPS_package_name:        library/security/ssh2/developer
Summary:         %{summary} - development files
SUNW_BaseDir:    %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version
%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%libssh264.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%libssh2.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%libssh264.build -d %name-%version/%_arch64
%endif

%libssh2.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%libssh264.install -d %name-%version/%_arch64
%endif

%libssh2.install -d %name-%version/%{base_arch}

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
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*


%files developer
%defattr (-, root, bin)
%{_includedir}/*.h
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*.pc
%ifarch amd64 sparcv9
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*.pc
%endif


%changelog
* Fri Dec 04 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Wed Nov  11 2009 - michal.bielicki@halokwadrat.de
- Initial version
