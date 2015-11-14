#
# spec file for package SFElibfribidi.spec
#
# includes module(s): libfribidi
#
# Copyright (c) 2007 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

%include Solaris.inc
%include packagenamemacros.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use fribidi_64 = fribidi.spec
%endif

%include base.inc
%use fribidi = fribidi.spec

Name:                   SFElibfribidi
IPS_Package_Name:	library/fribidi 
Summary:                %{fribidi.summary}
URL:			%{fribidi.url}
Version:                %{fribidi.version}
License:		%{fribidi.license}
Group:			%{fribidi.group}
SUNW_Copyright:		fribidi.copyright
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%description
A library to handle bidirectional scripts (eg. hebrew, arabic), so that
the display is done in the proper way; while the text data itself is
always written in logical order.

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_prefix}
IPS_Package_Name:	library/fribidi/developer 
Requires:		%{name}

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%fribidi_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%fribidi.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%fribidi_64.build -d %name-%version/%_arch64
%endif

%fribidi.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%fribidi_64.install -d %name-%version/%_arch64
%endif

%fribidi.install -d %name-%version/%{base_arch}

%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
mv $RPM_BUILD_ROOT%{_bindir}/fribidi $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../lib/isaexec fribidi
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%if %can_isaexec
%{_bindir}/%{base_isa}
%hard %{_bindir}/fribidi
%else
%{_bindir}/fribidi
%endif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/fribidi
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%ifarch amd64 sparcv9
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/*
%endif

%changelog
* Thr May 16 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Mon Oct 10 2011 - Milan Jurik
- add IPS package name
* Wed Jul 20 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Sun Apr 11 2010 - Milan Jurik
- cleanup for the latest pkgtool
* Sun Aug 17 2008 - nonsea@users.sourceofrge.net
- Add man page to %files
* Mon Oct 22 2007 - nonsea@users.sourceforge.net
- Spilit into fribidi.spec
* Tue Jun  5 2007 - dougs@truemail.co.th
- Initial version
