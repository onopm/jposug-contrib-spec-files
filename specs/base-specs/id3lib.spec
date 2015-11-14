#
# spec file for package SFEid3lib-gpp
#
# includes module(s): id3lib
#
#
Name:                    SFEid3lib-gpp
IPS_package_name:	 library/audio/g++/id3lib
Summary:                 id3lib (g++) - a software library for manipulating ID3v1/v1.1 and ID3v2 tags (g++)
Version:                 3.8.3
Source:                  %{sf_download}/id3lib/id3lib-%{version}.tar.gz
Patch1:                  id3lib-01-wall.diff
Patch2:                  id3lib-02-uchar.diff
Patch3:                  id3lib-03-gcc4.diff
Patch4:		id3lib-04-iconv.diff
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%prep
%setup -q -n id3lib-%version
%patch1  -p1
%patch2  -p1
%patch3  -p1
%patch4  -p1

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi

export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"
export CC=gcc
export CFLAGS="%{gcc_optflags}"
export CXX=g++
#oi151a4 g++ 4.6.3 needs -fpermissiv, s11 doesn't (can't tell why)
export CXXFLAGS="%{gcc_cxx_optflags} -fpermissive"
export LDFLAGS="%{_ldflags}"
export LD_OPTIONS="-i -L%{_libdir} -R%{_libdir}"

aclocal -I ./m4 $ACLOCAL_FLAGS
automake -a -c -f
autoconf
libtoolize --copy --force
./configure --prefix=%{_prefix} --mandir=%{_mandir} \
	    --bindir=%{_bindir}         \
            --libdir=%{_libdir}              \
            --libexecdir=%{_libexecdir}      \
            --sysconfdir=%{_sysconfdir}      \
            --enable-fpm=%{fp_arch}          \
            --enable-shared		     \
	    --disable-static

make -j$CPUS 

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{_libdir} -type f -name "*.la" -exec rm -f {} ';'

%changelog
* Fri May 03 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sun Jun 24 2012 - Thomas Wagner
- add -fpermissive to CXXFLAGS, oi151a4 g++ 4.6.3 needs -fpermissiv, s11 doesn't (can't tell why)
* Sat Apr 21 2012 - Thomas Wagner
- %include usr-g++.inc to relocate out from /usr/gnu to --prefix=/usr/g++
- use _std_datadir in ACLOCAL_FLAGS
- add IPS_package_name
- rename package to reflect gcc/g++ compiler and propper location
* Fri Sep 25 2009 - trisk@opensolaris.org
- Add patch3
- Update build system
* Tue Jul 17 2007 - dougs@truemail.co.th
- Converted from SFEid3lib
