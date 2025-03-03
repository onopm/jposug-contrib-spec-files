#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc
%include osdistro.inc

Name:                SFEnasm
IPS_Package_Name:	developer/nasm 
Summary:             Portable, modular 80x86 assembler
License:             BSD
SUNW_Copyright:      nasm.copyright
Version:             2.10.07
IPS_component_version: 2.10.7
URL:                 http://www.nasm.us/
Source:              http://www.nasm.us/pub/nasm/releasebuilds/%{version}/nasm-%{version}.tar.bz2
License:             2-BSD
Group:               Development/Languages
SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

#SUNWghostscript --- see SFEnasm.spec as example for osbuild dependent switches
#new os2nnn and starting with build 134
%if %{os2nnn}
%if %(expr %{osbuild} '>=' 134)
BuildRequires:		text/texinfo
BuildRequires:		print/filter/ghostscript
%endif
%endif

%if %{os2nnn}
%if %(expr %{osbuild} '>=' 100)
%if %(expr %{osbuild} '<' 134)
BuildRequires:       SUNWtexi
BuildRequires:       SUNWghostscript
%endif
%endif
%endif

%if %{os2nnn}
%if %(expr %{osbuild} '<' 100)
BuildRequires:       SUNWtexi
BuildRequires:       SUNWgscr
%endif
%endif

#SXCE
%if %SXCE
BuildRequires:       SUNWtexi
BuildRequires:       SUNWghostscriptr
BuildRequires:       SUNWghostscriptu
%endif

%prep
%setup -q -n nasm-%version

%build

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

./configure --prefix=%{_prefix}  \
            --mandir=%{_mandir} \
            --infodir=%{_datadir}/info

make everything

%install
rm -rf "$RPM_BUILD_ROOT"

mkdir -p "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"%{_bindir}
mkdir -p "$RPM_BUILD_ROOT"%{_mandir}/man1
mkdir -p "$RPM_BUILD_ROOT"/%{_infodir}
DOC="$RPM_BUILD_ROOT"%{_docdir}/nasm
mkdir -p "$DOC"
mkdir -p "$DOC"/rdoff
make INSTALLROOT="$RPM_BUILD_ROOT" \
        docdir=%{_docdir}/nasm \
        install_everything
cp AUTHORS CHANGES LICENSE README TODO doc/*.doc "$DOC"
cp rdoff/README "$DOC"/rdoff
cp rdoff/doc/* "$DOC"/rdoff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*
%dir %attr(0755, root, bin) %{_datadir}/info
%{_datadir}/info/*
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, other) %{_datadir}/doc/nasm
%{_datadir}/doc/nasm/*

%changelog
* Fri May 03 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sun Mar 3 2013 - Ken Mays <kmays2000@gmail.com>
- Bump to 2.10.07
* Thu Jun 21 2012 - Milan Jurik
- bump to 2.10.01
* Mon Oct 10 2011 - Milan Jurik
- add IPS package name
* Wed Aug 24 2011 - Ken Mays <kmays2000@gmail.com>
- Bump to 2.10rc8
* Sun Jul 24 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Tue Jun 7 2011 - Ken Mays <kmays2000@gmail.com>
- Bumped to 2.10rc6
* Sat Mar 05 2011 - Milan Jurik
- bump to 2.09.06
* Tue Nov 30 2010 - Milan Jurik
- bump to 2.09.04
* Fri Oct 29 2010 - Thomas Wagner
- cleaned up / adjusted BuildRequires to match various osbuilds and IPS/SVR4 
* Mon Aug 30 2010 - Milan Jurik
- bump to 2.09
* May 30 2010 - Thomas Wagner
- added include/osdistro.inc
- changes to (Build)Requires to match SXCE, OS20nn build <134 => 134 (the time the packages got new names)
* Apr 01 2010 - Milan Jurik
- update to 2.08.01
- build dependency fix
* Mar 22 2010 - Gilles Dauphin
- _bindir instead of /usr/bin
* Sat Aug 22 2009 - Milan Jurik
- update to 2.07
* Sat Jun 13 2009 - Milan Jurik
- upgrade to 2.06rc12
* Sat Mar 14 2009 - Milan Jurik
- upgrade to 2.06rc1
* Thu Dec 14 2006 - Eric Boutilier
- Initial spec
