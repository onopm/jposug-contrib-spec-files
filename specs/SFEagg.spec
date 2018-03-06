# Copyright 2009 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: trisk
#
%include Solaris.inc
%include packagenamemacros.inc

Name:                SFEagg
IPS_package_name:    library/graphics/agg
Summary:             Anti-Grain Geometry (AGG) rendering engine
Version:             2.5
Source:              http://www.antigrain.com/agg-%{version}.tar.gz
# some patches from http://patch-tracker.debian.org/package/agg/
Patch1:              agg-01-disable_gpc.diff
Patch2:              agg-02-rpath.diff
Patch3:              agg-03-fix_recursion_crash.diff
Patch4:              agg-04-libm.diff
Url:                 http://www.antigrain.com/
License:             GPLv2+
SUNW_Copyright:          %{name}.copyright
SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc

BuildRequires: %{pnm_buildrequires_SUNWgnome_common_devel_devel}
BuildRequires: %{pnm_buildrequires_SUNWlibsdl_devel}
#BuildRequires: %{pnm_buildrequires_SUNWxwinc_devel}

%package devel
Summary:                 %{summary} - development files
SUNW_BaseDir:            %{_basedir}

Requires: %{pnm_requires_SUNWlibsdl}
Requires: %{pnm_requires_SUNWfreetype2}
Requires: %{pnm_requires_SUNWxwinc}

%prep
%setup -q -n agg-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CPPFLAGS="-I%{xorg_inc}"
export CFLAGS="%optflags -xlibmil"
# we are doing this for Gnash... feel free to convert this to a base-spec
export CXXFLAGS="%cxx_optflags -xO4 -library=stlport4 -staticlib=stlport4 \
 -norunpath -mt -xlibmil -xlibmopt -features=tmplife -features=tmplrefstatic"
export LDFLAGS="%_ldflags %{xorg_lib_path}"

aclocal
# for stlport
ed -s aclocal.m4 <<'/EOF/' >/dev/null
,s/-lCstd//
w
q
/EOF/
autoheader
autoconf
libtoolize --copy --force
automake -a -c --foreign --ignore-deps
./configure \
            --prefix=%{_prefix}		\
	    --disable-examples		\
	    --disable-gpc		\
	    --x-includes=%{_includedir}	\
	    --x-libraries=%{_libdir}

gmake -j $CPUS

%install
rm -rf $RPM_BUILD_ROOT

gmake install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
#find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

rm -f $RPM_BUILD_ROOT%{_libdir}/libagg*.so.*
rm -f $RPM_BUILD_ROOT%{_libdir}/libagg*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/lib*.a
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/*
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/aclocal
%{_datadir}/aclocal/*

%changelog
* Sun Feb 26 2012 - TAKI,Yasushi <taki@justplayer.com>
- add pnmacro.
- add IPS package name.
* Tue Dec 01 2009 - Albert Lee <trisk@opensolaris.org>
- Initial spec.
