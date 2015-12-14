#
# spec file for package SFElibntlm
#
# includes module(s): libntlm
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

%define	src_name libntlm
%define	src_url	http://www.nongnu.org/libntlm/releases

Name:		SFElibntlm
IPS_Package_Name:	library/security/libntlm
SUNW_Copyright: %{name}.copyright
Summary:	Microsoft NTLM authentication library
Version:	1.3
Group:		System/Libraries
License:	LGPLv2.1+
URL:		http://www.nongnu.org/libntlm/
Source:		%{src_url}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc-runtime
%endif

%description
A library for authenticating with Microsoft NTLM challenge-response, 
derived from Samba sources.

%package devel
Summary:	%{summary} - development files
SUNW_BaseDir:	%{_prefix}
%include default-depend.inc
Requires: %name

%prep
%setup -q -n %{src_name}-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CC=gcc
export CXX=g++
export CFLAGS="%optflags -I%{gnu_inc} %{gnu_lib_path}"
export CXXFLAGS="%cxx_optflags -I%{gnu_inc} %{gnu_lib_path}"
export LDFLAGS="%_ldflags %gnu_lib_path"

./configure --prefix=%{_prefix}			\
            --bindir=%{_bindir}			\
            --libdir=%{_libdir}			\
            --sysconfdir=%{_sysconfdir}		\
            --includedir=%{_includedir} 	\
            --mandir=%{_mandir}			\
	    --infodir=%{_infodir}		\
	    --disable-static			\
	    --enable-shared

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*

%files devel
%defattr (-, root, bin)
%{_includedir}
%dir %attr (0755, root, bin) %{_libdir}
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*

%changelog
* Sun May 19 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- rewrite dependency to use gcc-46 at oi.
- abolish the use of minpuretext
* Wed Jan  9 2013 - TAKI,Yasushi <taki@justplayer.com>
- add minpuretext
- add some gcc options
* Tue Jan 08 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- fix linker option problem
* Mon Jan 07 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- build with gcc by default
* Sat Dec 08 2012 - YAMAMOTO Takashi
- Initial revision for the jposug
* Mon Dec 12 2011 - Milan Jurik
- bump to 1.3
* Sun Feb 13 2011 - Milan Jurik
- bump to 1.2
* Fri Jul 27 2007 - dougs@truemail.co.th
- Initial spec
