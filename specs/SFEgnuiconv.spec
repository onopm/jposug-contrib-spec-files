#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc
%include usr-gnu.inc
%include packagenamemacros.inc
%define tarball_name libiconv
%define major_version 1.14
# patches for future phone in Japan

%define patch_version 1.14-ja-1
%define build_l10n 1
##TODO## Bug SUNWncurses and SUNWtixi do not define group "other" for /usr/gnu/share/doc
##TODO## Bug No SUNWncurses TBD 
##TODO## Bug No SUNWtixi    TBD 
%define workaround_gnu_share_doc_group %( /usr/bin/ls -dl /usr/gnu/share/doc | grep " root.*bin " > /dev/null 2>&1 && echo bin || echo other )
%ifarch amd64 sparcv9
%include arch64.inc
%use iconv_base_64 = gnuiconv.spec
%endif
%include base.inc
%use iconv_base = gnuiconv.spec
Name:		SFEgnuiconv
IPS_Package_Name:	library/text/gnu-iconv
Summary:	GNU iconv - Code set conversion
Group:		System/Libraries
License:	LGPLv2
SUNW_Copyright:	%{name}.copyright
URL:		http://www.gnu.org/s/libiconv/
Version:	%{major_version}

SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%description
Convert encoding of given files from one encoding to another. You need
this package if you want to convert some documet from one encoding to
another or if you have installed some programs which use Generic
Character Set Conversion Interface.

%package developer
IPS_Package_Name:	library/text/gnu-iconv/developer 
Summary:	%{summary} - development files
SUNW_BaseDir:	%{_basedir}
Requires:	%name

%if %build_l10n
%package l10n
IPS_Package_Name:	library/text/gnu-iconv/l10n
Summary:	%{summary} - l10n files
SUNW_BaseDir:	%{_basedir}
Requires:	%{name}
%endif

%prep
rm -rf %name-%version
mkdir %name-%version

%ifarch amd64 sparcv9
mkdir %name-%version/%_arch64
%iconv_base_64.prep -d %name-%version/%_arch64
%endif

mkdir %name-%version/%{base_arch}
%iconv_base.prep -d %name-%version/%{base_arch}

%build
%ifarch amd64 sparcv9
%iconv_base_64.build -d %name-%version/%_arch64
%endif
%iconv_base.build -d %name-%version/%{base_arch}

%install
rm -rf $RPM_BUILD_ROOT
%ifarch amd64 sparcv9
%iconv_base_64.install -d %name-%version/%_arch64
%endif
%iconv_base.install -d %name-%version/%{base_arch}
%if %can_isaexec
mkdir $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
for file in iconv
do
 mv $RPM_BUILD_ROOT%{_bindir}/$file $RPM_BUILD_ROOT%{_bindir}/%{base_isa}
 cd $RPM_BUILD_ROOT%{_bindir} && ln -s ../../lib/isaexec $file
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%if %can_isaexec
%{_bindir}/%{base_isa}
%hard %{_bindir}/iconv
%else
%{_bindir}/iconv
%endif
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/iconv
%endif
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*.so*
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/*.so*
%endif
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/iconv.1
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/iconv*.3

%files developer
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*.h
%dir %attr (0755, root, sys) %{_datadir}
##TODO## fix see bugs on top of the spec
#%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, %{workaround_gnu_share_doc_group}) %{_datadir}/doc
%{_datadir}/doc/*

%if %build_l10n
%files l10n
%defattr (-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
# The following is correct, but setting the group correctly conflicts with gnu-binutils
#%attr (-, root, other) %_datadir/locale
%{_datadir}/locale
%endif

%changelog
* Sat May 31 2014 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- bump to 1.14
* Mon May 05 2014 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- Fixed configure problems when compile with 64 bit.
  I think iconv was compiled with 64 bit, but that was wrong.
* Tue Feb 05 2013 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- change IPS package name
* Tue 29 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- add IPS package name for developer
* Thu 20 2012 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- bump down to 1.13 for Japanese mobile phones
* Thu Oct 06 2011 - Milan Jurik
- bump to 1.14, add IPS package name
* Thu Oct 06 2011 - Milan Jurik
- bump to 1.14, add IPS package name
* Wed Jul 20 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Wed Feb 23 2011 - Milan Jurik
- fix packaging
* May 30 2010 - Thomas Wagner
- build workaround to build this package according to the group set on the
  building machine's directory /usr/gnu/share/doc/, reason behind is
  SUNWncurses creates /usr/gnu/share/doc with root:bin instead root:other
* Wed Feb 24 2010 - Milan Jurik
- update to 1.13.1
- remove runpath patch as not needed
* Fri Oct 09 2009 - Milan Jurik
- update to 1.13
- fix /usr/gnu/share/doc group
* Sun Aug 17 2008 - nonsea@users.sourceforge.net
- Bump to 1.12
- Add patch intmax.diff to fix build issue.
* Sun Jun 29 2008 - river@wikimedia.org
- use rm -fr instead of rm -r, since this directory doesn't seem to exist always
* Sun Nov 18 2007 - daymobrew@users.sourceforge.net
- Add l10n package.
* Sun Apr 21 2007 - Doug Scott
- Added -L/usr/gnu/lib -R/usr/gnu/lib
* Mon Mar 12 2007 - Eric Boutilier
- Initial spec
