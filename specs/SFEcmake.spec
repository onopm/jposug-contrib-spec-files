#
# spec file for package SFEcmake
#
# includes module(s): cmake
#

%include Solaris.inc
%include packagenamemacros.inc

# Avoid conflict with SUNWcmake
%include usr-gnu.inc

Name:             SFEcmake
IPS_Package_Name: sfe/developer/build/cmake 
Summary:          Cross platform make system
Version:          2.8.7
License:          BSD3c
SUNW_Copyright:   cmake.copyright
Source:           http://www.cmake.org/files/v2.8/cmake-%{version}.tar.gz
URL:              http://www.cmake.org
Group:            Development/Distribution Tools
SUNW_BaseDir:     %{_basedir}
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%include default-depend.inc

%prep
%setup -q -n cmake-%{version}

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export CFLAGS="%optflags"
export CXXFLAGS="%cxx_optflags"

./configure --prefix=%{_prefix} \
	    --bindir=%{_bindir}	\
	    --docdir=/share/doc/cmake \
	    --libdir=%{_libdir}	\
	    --mandir=/share/man

#If Ext2 Filesystem headers are present and found, compile errors occur
#disable this: HAVE_EXT2FS_EXT2_FS_H:INTERNAL=1
gsed -i -e 's/^HAVE_EXT2FS_EXT2_FS_H:INTERNAL=.*/HAVE_EXT2FS_EXT2_FS_H:INTERNAL=/' CMakeCache.txt 

gmake -j$CPUS

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, bin)
%{_bindir}
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/aclocal
%{_datadir}/cmake-*
%{_mandir}
%dir %attr (0755, root, other) %{_docdir}
%{_docdir}/cmake

%changelog
* Wed Apr 4 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
