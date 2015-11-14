#
# Copyright (c) 2008 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#

%include Solaris.inc
%include packagenamemacros.inc

Name:		SFEjasper
IPS_Package_Name:	codec/jasper
Group:		System/Multimedia Libraries
License:	Jasper Software License
Summary:	A free software-based reference implementation of the JPEG-2000 Part-1 CODEC
Version:	1.900.1
SUNW_Copyright:	jasper.copyright
URL:		http://www.ece.uvic.ca/~mdadams/jasper/
Source:		http://www.ece.uvic.ca/~mdadams/jasper/software/jasper-%{version}.zip
Source1:	http://www.ece.uvic.ca/~mdadams/jasper/LICENSE
Patch1:		jasper-01-debian.diff
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%description
JasPer is a collection        
of software (i.e., a library and application programs) for the coding 
and manipulation of images.  This software can handle image data in a 
variety of formats.  One such format supported by JasPer is the JPEG-2000 
format defined in ISO/IEC 15444-1:2000.

%package devel
Summary:	%{summary} - development files
SUNW_BaseDir:	%{_basedir}
%include default-depend.inc
Requires:	%{name}

BuildRequires:	%{pnm_buildrequires_SUNWunzip_devel}
Requires:	%{pnm_requires_SUNWunzip}

%prep
%setup -q -n jasper-%version
%patch1 -p1

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags -I%{gnu_inc} -D__C99FEATURES__"
export LDFLAGS="%_ldflags %{gnu_lib_path}"
gnu_prefix=`dirname %{gnu_bin}`

./configure --prefix=%{_prefix}	\
            --mandir=%{_mandir}	\
            --enable-shared=yes \
            --enable-static=no  \
            --with-pic          \
            --without-docs

make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/jasper
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/doc/jasper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.so*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_mandir}
%{_mandir}/*

%defattr (-, root, other)
%dir %attr (0755, root, other) %{_datadir}/doc
%{_datadir}/doc/*

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*

%changelog
* Tue Nov 28 2012 YAMAMOTO Takashi
- use pnm_macros
* Sat Dec 24 2011 - Milan Jurik
- add several security patches from Debian
* Mon Oct 17 2011 - Milan Jurik
- add IPS package name
* Sun Jul 24 2011 - Guido Berhoerster <gber@openindiana.org>
- added License and SUNW_Copyright tags
* Wed Jan 30 2008 - moinak.ghosh@sun.com
- Initial spec.
