#
# spec file for package gob
#
# Copyright (c) 2010, Oracle and/or its affiliates. All rights reserved.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner:halton
#

Name:		gob2
License:	GPL
Group:		Development/Libraries
Version:	2.0.18
Release:	1
License:        GPL
Distribution:   Java Desktop System
Vendor:         Sun Microsystems, Inc.
URL:		http://www.5z.com/jirka/gob.html
Summary:	The GObject Builder
Source:         http://download.gnome.org/sources/gob2/2.0/%{name}-%{version}.tar.bz2
# date:2009-11-18 owner:halton type:bug
# "#line 0" is not supportted in C99, gcc allow it but sun cc does not.
Patch1:         %{name}-01-line-control.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

%description
GOB is a simple preprocessor for making GObject objects (glib objects).
It makes objects from a single file which has inline C code so that
you don't have to edit the generated files.  Syntax is somewhat inspired
by java and yacc.  It supports generating C++ code

%package devel
Summary:	Libraries and include files for gob.
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries and header files if you want to make use of the gob library in your
own programs.


%prep
%setup -q
%patch1 -p1

%build
%ifos linux
if [ -x /usr/bin/getconf ]; then
  CPUS=`getconf _NPROCESSORS_ONLN`
fi
%else
  CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
%endif
if test "x$CPUS" = "x" -o $CPUS = 0; then
  CPUS=1
fi

libtoolize --force
aclocal $ACLOCAL_FLAGS
autoheader
automake -a -c -f
autoconf

./configure --prefix=%{_prefix} \
	    --bindir=%{_bindir} \
	    --mandir=%{_mandir} \
	    --libdir=%{_libdir} \
	    --datadir=%{_datadir} \
	    --includedir=%{_includedir} \
	    --sysconfdir=%{_sysconfdir} \
	    %gtk_doc_option

make -j $CPUS

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make -i install DESTDIR=$RPM_BUILD_ROOT
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc README AUTHORS COPYING NEWS TODO ChangeLog
%doc examples

%{_prefix}/bin/*
%{_prefix}/share/aclocal/*

%changelog
* Mon May 30 2011 - Alex Viskovatoff
- Bump to 2.0.18
* Thu Apr 29 2010 - halton.huo@sun.com
- Bump to 2.0.17
* Wed Nov 18 2009 - halton.huo@sun.com
- Add patch line-control
* Fri Aug 08 2009 - halton.huo@sun.com
- Initial spec
