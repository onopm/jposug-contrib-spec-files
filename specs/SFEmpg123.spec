#
# spec file for package SFEmpg123.spec
#
%include Solaris.inc

Name:           SFEmpg123
Summary:        mpg123 - fast console MPEG Audio Player and decoder library
Version:        1.13.2
IPS_package_name:  media/mpg123
URL:            http://www.mpg123.org/
Source:         %{sf_download}/mpg123/mpg123/%{version}/mpg123-%{version}.tar.bz2
License:        LGPL,GPL
Group:          Applications/Multimedia
SUNW_Copyright: %{name}.copyright
SUNW_BaseDir:   %{_basedir}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc
Requires:       library/libtool/libltdl
Requires:       library/sdl
Requires:       system/library/math
Requires:       gnome/gnome-audio

%description
mpg123 is a real time MPEG 1.0/2.0/2.5 audio player/decoder for layers
1, 2, and 3 (MPEG 1.0 layer 3 aka MP3 most commonly tested). mpg123
includes a terminal-based player, the ability to redirect the raw sound
data to stdout, gapless playback of MP3 files, a decoder library for use
with other applications, and much more.

Meta(info.maintainer_url):      http://sourceforge.jp/forum/forum.php?forum_id=25193
Meta(info.upstream_url):        http://www.mpg123.org/
Meta(info.classification):      org.opensolaris.category.2011:Media

%package devel
Summary:        mpg123 - developer files, /usr
Group:          Development/Libraries
SUNW_BaseDir:   %{_basedir}
IPS_package_name:  library/media/mpg123
Requires:       %name
%include default-depend.inc

%prep
%setup -q -n mpg123-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export CFLAGS="-D_FILE_OFFSET_BITS=64 -fast -xtarget=generic -g -xipo"

./configure --prefix=%{_prefix}         \
            --bindir=%{_bindir}         \
            --mandir=%{_mandir}         \
            --libdir=%{_libdir}         \
            --datadir=%{_datadir}       \
            --libexecdir=%{_libexecdir} \
            --sysconfdir=%{_sysconfdir} \
            --enable-shared             \
            --enable-static             \
            --enable-int-quality=yes    \
            --enable-ipv6=yes           \
            --disable-lfs-alias         \
            --with-cpu=i586_dither

make -j$CPUS 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT%{_libdir}/mpg123/output_*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_bindir}
%{_mandir}
%dir %attr (0755, root, sys) %{_datadir}
%{_libdir}/libmpg123.so.*
%{_libdir}/mpg123/output_*.la
%{_libdir}/mpg123/output_*.so

%files devel
%defattr (-, root, bin)
%dir %attr (0755, root, other) %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/libmpg123.pc
%{_includedir}
%{_libdir}/libmpg123.a
%{_libdir}/libmpg123.la
%{_libdir}/libmpg123.so

%changelog
* Wed Mar 02 2011 - Satoru MIYAZAKI<s.miyaza@gmail.com>
- bump to 1.13.2
- use --disable-lfs-alias option
- Support for Solaris11 Express.
* Mon Aug 25 2009 - matt@greenviolet.net
- Initial version
