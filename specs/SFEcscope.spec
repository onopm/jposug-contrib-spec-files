#
# spec file for package SFEcscope
#
# includes module(s): cscope
#
%include Solaris.inc
%include usr-gnu.inc
%include base.inc
%include packagenamemacros.inc

%define tarball_version  15.8b
Name:                    SFEcscope
IPS_Package_Name:	 developer/cscope
License:                 BSD
Summary:                 interactive source code examiner
Version:                 15.8
Source:                  %{sf_download}/cscope/cscope-%{tarball_version}.tar.gz
URL:                     http://cscope.sourceforge.net/
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:	         cscope.copyright
%include default-depend.inc
# BuildConflicts:        SPROsslnk
BuildRequires:           %{pnm_buildrequires_SUNWbison}
BuildRequires:           %{pnm_buildrequires_SUNWncurses}
Requires:                %{pnm_buildrequires_SUNWncurses}

%prep
%setup -q -n cscope-%{tarball_version}

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="%optflags -I/usr/include/ncurses"
export LDFLAGS="%_ldflags -L/usr/gnu/lib -R/usr/gnu/lib"
./configure --prefix=%{_prefix}	\
	    --mandir=%{_mandir}
	    
make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*

%changelog
* Sat Apr 9 2016 - Osamu Tabata <cantimerny.g@gmail.com>
- build for 11.3
* Fri Aug 21 2015 - Osamu Tabata <cantimerny.g@gmail.com>
- Bump to 15.8b
* Wed Aug 12 2015 - Osamu Tabata
- modify require section
* Fri Jun 14 2013 - Osamu Tabata
- Support for Solaris11 and bump up to 15.8a
* Fri Jun 1 2012 - Osamu Tabata
- Support for openindiana
* Thu Mar 17 2011 - Thomas Wagner
- move to /usr/gnu to avoid conflicts with sunstudio12u1 (/usr/bin/cscope and manpage)
* Wed Nov 18 2009 - halton.huo@sun.com
- Use tarball_version for 15.7a
- Replace SUNWgnu-emacs with SUNWtoo
* Fri Nov 13 2009 - halton.huo@sun.com
- Bump to 15.7a
- ctags in now in SUNWgnu-emacs, so replace Requires: SUNWgnu-emacs
* Fri Feb 20 2009 - halton.huo@sun.com
- Bump to 15.7
- Add ncurses dependency.
* Sat Feb 02 2008 - moinak.ghosh@sun.com
- Slight tweaks and add dependency on ctags and bison.
* Sat Apr 21 2007 - dougs@truemail.co.th
- Added BuildConflicts: SPROsslnk
* Fri Jan 05 2007 - daymobrew@users.sourceforge.net
- Bump to 15.6.
* Fri Jun 23 2006 - laca@sun.com
- rename to SFEcscope
- update file attributes to match JDS
- delete -share subpkg
* Tue Nov 29 2005 - mike kiedrowski (lakeside-AT-cybrzn-DOT-com)
- Initial spec
