#
# spec file for package libgsm
#
# includes module(s): libgsm
#

%define	src_ver 1.0.13
#%define	src_name libgsm
%define	src_name gsm
#%define	src_url	http://kbs.cs.tu-berlin.de/~jutta/gsm/
#%define src_url http://ftp.de.debian.org/debian/pool/main/libg/libgsm
%define	src_url	http://www.quut.com/gsm/

Name:		SFElibgsm
Summary:	GSM audio encoding/decoding library
Version:	%{src_ver}
IPS_package_name:  library/media/gsm
License:	Free (Copyright (C) Technische Universitaet Berlin)
#Source:		%{src_url}/%{src_name}_%{version}.orig.tar.gz
Source:		%{src_url}/%{src_name}-%{version}.tar.gz
Patch1:		libgsm-01-makefile.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

Meta(info.maintainer_url):      http://sourceforge.jp/forum/forum.php?forum_id=25193
Meta(info.upstream_url):        http://www.quut.com/gsm/
Meta(info.classification):      org.opensolaris.category.2011:Media


%prep
%setup -q -n gsm-1.0-pl13
%patch1 -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

rm -f bin/* lib/* shared/* src/*.o test/*.o

export PICFLAG="-KPIC"
export OPTFLAGS="%optflags"
export LDFLAGS="%_ldflags"

if $( echo "%{_libdir}" | /usr/xpg4/bin/grep -q %{_arch64} ) ; then
	export LDFLAGS="$LDFLAGS -m64"
fi

make 

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{_includedir}/gsm,%{_libdir}}
make install DESTDIR=$RPM_BUILD_ROOT INSTALL_ROOT=%{_prefix}

if $( echo "%{_libdir}" | /usr/xpg4/bin/grep -q %{_arch64} ) ; then
	mkdir -p $RPM_BUILD_ROOT/%{_libdir}
	mv $RPM_BUILD_ROOT/%{_libdir}/../libgsm.* $RPM_BUILD_ROOT/%{_libdir}
fi

if $( echo "%{_libdir}" | /usr/xpg4/bin/grep -q %{sse2_arch} ) ; then
        mkdir -p $RPM_BUILD_ROOT/%{_libdir}
        mv $RPM_BUILD_ROOT/%{_libdir}/../libgsm.* $RPM_BUILD_ROOT/%{_libdir}
fi

# keep compatibility with other distros
cp -r inc/*.h $RPM_BUILD_ROOT%{_includedir}/gsm

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Mar  3 2011 - Satoru MIYAZAKI<s.miyaza@gmail.com>
- Support for Solaris11 Express.
* Sun Nov 28 2010 - Milan Jurik
- add pentium_pro+mmx lib
* Wed Jun 16 2010 - Milan Jurik
- usr/include/gsm for keeping compatibility with other distros
* March 12 2010 - Gilles Dauphin
- update download to official site
* Wed Mar 03 2010 - Milan Jurik
- original homepage disapeared, Debian source used now
* Tue Sep 8 2009 - Milan Jurik
- Initial base spec file
