#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name:		SFEgnuiconv
IPS_Package_Name:	library/text/gnu-iconv
Summary:	GNU iconv - Code set conversion
Group:		System/Libraries
License:	LGPLv2
SUNW_Copyright:	%{name}.copyright
URL:		http://www.gnu.org/s/libiconv/
Version:	%{major_version}
Source:		http://ftp.gnu.org/pub/gnu/libiconv/%{tarball_name}-%{version}.tar.gz
#up to 1.13
#Patch0:         http://www2d.biglobe.ne.jp/~msyk/software/libiconv/%{tarball_name}-%{patch_version}.patch.gz
#1.14
Patch0:         http://apolloron.org/software/libiconv-1.14-ja/%{tarball_name}-%{patch_version}.patch
Patch2:		libiconv-02-646.diff

%prep
%setup -q -n %{tarball_name}-%{version}
%patch0 -p1
%patch2 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags -D__C99FEATURES__"
export LDFLAGS="%_ldflags"
echo %_ldflags
./configure			\
--prefix=%{_prefix}		\
--mandir=%{_mandir}		\
--bindir=%{_bindir}		\
--libdir=%{_libdir}		\
--libexecdir=%{_libexecdir}	\
--sysconfdir=%{_sysconfdir}	\
--enable-static=no
make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f ${RPM_BUILD_ROOT}%{_libdir}/lib*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/charset.alias
%if %build_l10n
%else
# REMOVE l10n FILES
rm -fr $RPM_BUILD_ROOT%{_datadir}/locale
#rm -r $RPM_BUILD_ROOT%{_datadir}/gnome/help/gnome-commander/[a-z]*
#rm -r $RPM_BUILD_ROOT%{_datadir}/omf/gnome-commander/*-[a-z]*.omf
%endif

%changelog
* Sat May 31 2014 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- bump to 1.14
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
