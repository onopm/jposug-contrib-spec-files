#
# spec file for package SFElibmpc
#
# includes module(s): GNU mpc
#
%include Solaris.inc
%include usr-gnu.inc
%include packagenamemacros.inc

%ifarch amd64 sparcv9
%include arch64.inc
%use libmpc_64 = libmpc.spec
%endif

%include base.inc
%use libmpc = libmpc.spec

##TODO## think on usr-gnu.inc define infodir inside /usr/gnu/share to avoid conflicts
%define _infodir	%{_datadir}/info

##TODO## move to packagenamemacros.inc to specify which osbuild supplies
#suffiently *fresh* library versions of gmp and mpfr
#%define SFEgmp	%(/usr/bin/pkginfo -q SFEgmp && echo 1 || echo 0)
%define SFEgmp	1
#%define SFEmpfr	%(/usr/bin/pkginfo -q SFEmpfr && echo 1 || echo 0)
%define SFEmpfr	1

Name:		SFElibmpc
IPS_Package_Name:	library/mpc
Summary:	%{libmpc.summary}
Group:		Development/Libraries
URL:		%{libmpc.url}
License:	LGPLv3+
SUNW_Copyright:	libmpc.copyright
Version:	%{libmpc.version}
SUNW_BaseDir:	%{_basedir}/%{_subdir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%if %SFEgmp
BuildRequires: library/gmp-5/developer
Requires: library/gmp-5
#IPS doesn't honour SUNW_BaseDir
##TODO## ##FIXME##
#%define SFEgmpbasedir %(pkgparam SFEgmp BASEDIR)
%define SFEgmpbasedir %{_prefix} 
%else
BuildRequires: SUNWgnu-mp
Requires: SUNWgnu-mp
%endif

%if %SFEmpfr
BuildRequires: SFEmpfr-devel
Requires: SFEmpfr
#IPS doesn't honour SUNW_BaseDir 
##TODO## ##FIXME##
#%define SFEmpfrbasedir %(pkgparam SFEmpfr BASEDIR)
%define SFEmpfrbasedir %{_prefix} 
%else
BuildRequires: SUNWgnu-mp
Requires: SUNWgnu-mp
%endif

Requires: %{pnm_requires_SUNWpostrun}

%package devel
IPS_Package_Name:	library/mpc/developer
Name:		%{name}-devel
Summary:	%{summary} - developer files
SUNW_BaseDir:	%{_basedir}/%{_subdir}
%include default-depend.inc
Requires: %name

%prep
rm -rf %name-%version
%ifarch amd64 sparcv9
mkdir -p %name-%version/%_arch64
%libmpc_64.prep -d %name-%version/%_arch64
%endif

mkdir -p %name-%version/%base_arch
%libmpc.prep -d %name-%version/%base_arch


%build
%ifarch amd64 sparcv9
%libmpc_64.build -d %name-%version/%_arch64
%endif

%libmpc.build -d %name-%version/%{base_arch}

%install
rm -rf %{buildroot}
%ifarch amd64 sparcv9
%libmpc_64.install -d %name-%version/%_arch64
%endif

%libmpc.install -d %name-%version/%{base_arch}

%clean
rm -rf %{buildroot}


%post
( echo 'PATH=/usr/bin:/usr/sfw/bin; export PATH' ;
  echo 'infos="';
  echo 'mpc.info' ;
  echo '"';
  echo 'retval=0';
  echo 'for info in $infos; do';
  echo '  install-info --info-dir=%{_infodir} %{_infodir}/$info || retval=1';
  echo 'done';
  echo 'exit $retval' ) | $PKG_INSTALL_ROOT/usr/lib/postrun -b -c SFE

%preun
( echo 'PATH=/usr/bin:/usr/sfw/bin; export PATH' ;
  echo 'infos="';
  echo 'mpc.info' ;
  echo '"';
  echo 'for info in $infos; do';
  echo '  install-info --info-dir=%{_infodir} --delete %{_infodir}/$info';
  echo 'done';
  echo 'exit 0' ) | $PKG_INSTALL_ROOT/usr/lib/postrun -b -c SFE

%files
%defattr (-, root, bin)
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%{_infodir}
%ifarch amd64 sparcv9
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/lib*.so*
%endif

%files devel
%defattr (-, root, bin)
%{_includedir}

%changelog
* Sun Feb 16 2014 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- Added IPS_Package_Name
* Sun May 19 2013 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- change dependency
* Tue Feb 05 2013 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- delete sfe prefix from IPS package name
* Thu 20 2012 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- use pnm macros
* Mon Dec 17 2012 - Logan Bruns <logan@gedanken.org>
- bump to 1.0.1
* Sun Jul 22 2012 - Milan Jurik
- bump to 1.0
* Mon Oct 10 2011 - Milan Jurik
- add IPS package name
* Thu Jul 21 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Sat Mar 12 2011 - Thomas Wagner
- make SFEgmp and SFEmpfr a hard requirement to overide autodetect 
  (always use SFEgmp/SFEmpfr/SFElibmpc for SFEgcc with --autodeps)
  for primary use as gcc4 supporting lib
* Tue Mar 01 2011 - Milan Jurik
- start proper multiarch
* Sat Oct 23 2010 - Thomas Wagner
- initial spec (derived from SFEmpfr.spec)
- avoid naming clush by naming the package: "libmpc" (SFEMpc to be removed)
