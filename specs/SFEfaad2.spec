#
# spec file for package SUNWfaad2.spec
#
# includes module(s): faad2
#
%include Solaris.inc
%ifarch amd64 sparcv9
%include arch64.inc
%use faad2_64 = faad2.spec
%endif

%include base.inc
%use faad2 = faad2.spec

Name:                    SFEfaad2
IPS_Package_Name:	audio/faad2 
Summary:                 %{faad2.summary}
Group:                   libraries/multimedia
Version:                 %{faad2.version}
License:                 GPLv2+
SUNW_Copyright:          faad2.copyright
URL:                     http://www.audiocoding.com/
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
Requires: SFEid3lib-gpp
BuildRequires: SFEid3lib-gpp-devel

%package devel
IPS_Package_Name:	audio/faad2/developer
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
mkdir %name-%version
%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%faad2_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%faad2.prep -d %name-%version/%{base_arch}


%build
%ifarch amd64 sparcv9
%faad2_64.build -d %name-%version/%_arch64
%endif

%faad2.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%faad2_64.install -d %name-%version/%_arch64
%endif

%faad2.install -d %name-%version/%{base_arch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/manm
%{_mandir}/manm/faad.man

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Sun May 12 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sat Apr 28 2012 - Thomas Wagner
- switch to renamed SFEid3lib-gpp (already gcc version but now with corrected name)
* Sun Oct 16 2011 - Milan Jurik
- add IPS package name
* Sat Aug 13 2011 - Thomas Wagner
- fix build by:
- use /usr/bin/libtoolize and not new SFE version from /usr/gnu/bin/
* Sat Jul 23 2011 - Guido Berhoerster <gber@openindiana.org>
- added License and SUNW_Copyright tags
* Fri Aug 21 2009 - Milan Jurik
- multiarch support
* Fri May 23 2008 - michal.bielicki <at> voiceworks.pl
- id3 is now part of nevada so dependencies should point to SUNWid3 and SUNWid3-devel, thanks to Giles Dauphin for the fix
* Mon Nov 5 2007 - markwright@internode.on.net
- Bump to 2.6.1.  Bump patch2 and patch4.  Comment patch1, patch3 and patch5.
* Fri Jun 23 2005 - laca@sun.com
- rename to SFEfaad2
- update file attributes
- remove lib*a
* Mon May  8 2006 - drdoug007@yahoo.com.au
- Initial version
