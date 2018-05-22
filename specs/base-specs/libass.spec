#
# spec file for package SFElibmaa
#
# includes module: libass
#

%define srcname libass

Name:		SFElibass
IPS_Package_Name:	library/video/libass
Summary:	Portable renderer for the ASS/SSA (Substation Alpha) subtitle format
Group:		System/Multimedia Libraries
URL:		http://code.google.com/p/libass/
Version:	0.10.1
License:	ISC
SUNW_Copyright:	libass.copyright
Source:		http://%srcname.googlecode.com/files/%srcname-%version.tar.gz
SUNW_BaseDir:	%_basedir
BuildRoot:	%_tmppath/%name-%version-build
%include default-depend.inc
Requires:	SFElibfribidi

%prep
%setup -q -n %srcname-%version

%build
CPUS=$(psrinfo | gawk '$2=="on-line"{cpus++}END{print (cpus==0)?1:cpus}')

export CC=gcc
export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

./configure --prefix=%_prefix		\
            --libdir=%{_libdir}         \
            --bindir=%{_bindir}         \
            --includedir=%{_includedir} \
            --sysconfdir=%{_sysconfdir} \
            --datadir=%{_datadir}       \
            --mandir=%{_mandir}
gmake -j$CPUS

%install
gmake install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%_libdir/*.*a

%changelog
* Wed May 08 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Sat Feb 09 2013 - Milan Jurik
- bump do 0.10.1
* Thu Jun 21 2012 - Logan Bruns <logan@gedanken.org>
- added missing requires for SFElibfribidi
* Sun Dec 11 2011 - Milan Jurik
- bump to 0.10.0
* Tue Aug 30 2011 - Alex Viskovatoff
- bump to 0.9.13; use gz tarball so spec builds with unpatched pkgtool
* Fri Jul 29 2011 - Alex Viskovatoff
- add SUNW_Copyright
* Sat Jul 16 2011 - Alex Viskovatoff
- Initial spec
