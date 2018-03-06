#
# Copyright (c) 2006 Sun Microsystems, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

Name:		SFEimlib2
IPS_Package_Name:	image/library/imlib2
Summary:	General image loading and rendering library
Group:		System/Multimedia Libraries
Version:	1.4.5
License:	BSD
SUNW_Copyright:	imlib2.copyright
Source:		%{sf_download}/enlightenment/imlib2-%{version}.tar.gz
Patch1:		imlib2-01-std99.diff
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
Requires:	SUNWxwplt
BuildRequires:  library/audio/libid3tag/developer
Requires:       library/audio/libid3tag

%prep
%setup -q -n imlib2-%version
%patch1 -p1

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

#if $( echo "%{bld_arch}" | /usr/gnu/bin/grep -q 'pentium_pro+mmx' ) ; then
#export XARCH="--enable-mmx"
#elif $( echo "%{bld_arch}" | /usr/gnu/bin/grep -q 'amd64' ) ; then
#export XARCH="--enable-amd64"
#else
export XARCH=""
#fi
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
autoreconf
./configure --prefix=%{_prefix}  \
            --mandir=%{_mandir} \
            --bindir=%{_bindir}         \
            --libdir=%{_libdir}         \
            --libexecdir=%{_libexecdir} \
            --sysconfdir=%{_sysconfdir} \
            --enable-static=no \
            $XARCH
/bin/rm -rf libtool
cat <<EOF > libtool
#!/bin/bash
#/usr/bin/libtool --tag=CC \$*
/usr/bin/libtool \$*
EOF

#ln -s /usr/bin/libtool
make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm ${RPM_BUILD_ROOT}%{_libdir}/*.la
rm ${RPM_BUILD_ROOT}%{_libdir}/imlib2/filters/*.la
rm ${RPM_BUILD_ROOT}%{_libdir}/imlib2/loaders/*.la

%changelog
* Wed Jun 05 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
- Added 64bit build
* Sun Feb 05 2012 - Milan Jurik
- bump to 1.4.5
* Thu Aug 26 2010 - brian.cameron@oracle.com
- Bump to 1.4.4.
* Mon Jan 05 2008 - brian.cameron@sun.com
- Bump to 1.4.2.
* Thu Nov 15 2007 - daymobrew@users.sourceforge.net
- Add support for Indiana builds.
* Tue Nov 07 2006 - Eric Boutilier
- Initial spec
