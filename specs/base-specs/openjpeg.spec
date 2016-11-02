#
# spec file for package SFEopenjpeg
#
# includes module(s): openjpeg
#
%define	src_name openjpeg
%define	src_url	http://www.openjpeg.org

Name:		SFEopenjpeg
IPS_Package_Name:	image/library/openjpeg
Group:		System/Libraries
Summary:	Open Source multimedia framework
License:	BSD
SUNW_Copyright:	openjpeg.copyright
Version:	%{major_version}.1
Source:		http://openjpeg.googlecode.com/files/openjpeg-%{version}.tar.gz
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

BuildRequires: SFEcmake

%package devel
Summary:         %{summary} - development files
IPS_Package_Name:	image/library/openjpeg/developer
SUNW_BaseDir:    %{_basedir}
%include default-depend.inc
Requires: %name

%prep
%setup -q -n %src_name-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DOPENJPEG_INSTALL_LIB_DIR:PATH=%{_libdir} -DOPENJPEG_INSTALL_BIN_DIR=%{_bindir} .
make VERBOSE=1 -j$CPUS

%install
make install DESTDIR=%{buildroot}

rm -f %{buildroot}/%{_includedir}/openjpeg.h
ln -s openjpeg-%{major_version}/openjpeg.h %{buildroot}/%{_includedir}/openjpeg.h

%changelog
* Sat May 04 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sat Feb 18 2012 - Milan Jurik
- bump to 1.5.0
* Tue Oct 11 2011 - Milan Jurik
- bump to 1.4
- add IPS package name
* Sun Jul 24 2011 - Alex Viskovatoff
- Add SUNW_Copyright
* Fri May 21 2010 - Milan Jurik
- update to 1.3, split devel package
* Sun Jul 29 2007 - dougs@truemail.co.th
- Initial spec
