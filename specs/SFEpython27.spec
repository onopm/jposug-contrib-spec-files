#
# spec file for package SFEpython27
#

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define _name Python
%define version 2.7.3
%define unmangled_version 2.7.3
%define release 1
%define pyver 2.7

%define _prefix /usr/python
%define _basedir %{_prefix}
%define _lib64  lib64

Name:                SFEpython27
IPS_Package_Name:    runtime/SFEpython-273
Summary:             The Python interpreter, libraries and utilities
Group:               Development/Python
Version:             %{version}
Release:             %{release}
License:             PSF license
Source:              http://www.python.org/ftp/python/%{unmangled_version}/%{_name}-%{unmangled_version}.tar.bz2
Source1:             SFEpython27-pyconfig.h
Patch1:              SFEpython27-lib64.diff
Url:                 http://www.python.org/download/releases/2.7.3
Group:               Development/Libraries

BuildRoot:           %{_tmppath}/%{name}-%{version}-%{release}-buildroot
SUNW_Basedir:        %{_basedir}
SUNW_Copyright:	     Python27.copyright

# OpenSolaris IPS Manifest Fields
Meta(info.maintainer): A Hettinger <ahettinger@prominic.net>
Meta(info.upstream):  Guido van Rossum and the Python community <python-dev@python.org>
Meta(info.repository_url): http://svn.python.org/projects/python/branches/release32-maint
Meta(info.classification): org.opensolaris.category.2008:Development/Python


%description
Python is an interpreted, interactive, object-oriented programming
language. It is often compared to Tcl, Perl, Scheme or Java.

Python combines remarkable power with very clear syntax. It has
modules, classes, exceptions, very high level dynamic data types, and
dynamic typing. There are interfaces to many system calls andlibraries, as well as to various windowing systems (X11, Motif, Tk,
Mac, MFC). New built-in modules are easily written in C or C++. Python
is also usable as an extension language for applications that need a
programmable interface.

The Python implementation is portable: it runs on many brands of UNIX,
on Windows, DOS, OS/2, Mac, Amiga... If your favorite system isn't
listed here, it may still be supported, if there's a C compiler for
it. Ask around on comp.lang.python -- or just try compiling Python
yourself.

%prep
%setup -c -n %{_name}-%{unmangled_version}

%ifarch amd64 sparcv9
rm -rf %{_name}-%{unmangled_version}-64
cp -rp %{_name}-%{unmangled_version} %{_name}-%{unmangled_version}-64
#rm -rf %{_name}-%{unmangled_version}
%endif

%build

cd %{_name}-%{unmangled_version}
CPUS=$(psrinfo | awk '$2=="on-line"{cpus++}END{if(cpus==0){print 1}else{print cpus }}')
export CFLAGS="-i -xO4 -xspace -xstrconst -mr -mt=yes -I/usr/include"
export LDFLAGS="-R%{_prefix}/lib:/usr/lib/ -L%{_prefix}/lib:/usr/lib"
export LD_OPTIONS="-R%{_prefix}/lib:/usr/lib/ -L%{_prefix}/lib:/usr/lib"
env CFLAGS="$CFLAGS" ./configure --prefix=%{_prefix} \
                                 --bindir=%{_prefix}/bin \
                                 --libdir=%{_prefix}/lib \
 		                 --mandir=%{_prefix}/share/man \
                                 --with-fpectl \
                                 --enable-ipv6 \
                                 --with-threads \
                                 --enable-unicode=ucs4 \
                                 --with-dbmliborder=gdbm \
                                 --enable-loadable-sqlite-extensions \
                                 --with-system-expat \
                                 --with-system-ffi \
                                 --without-gcc \
                                 --enable-shared
make -j$CPUS

%ifarch amd64 sparcv9
cd ../%{_name}-%{unmangled_version}-64
%patch1 -p0
export CFLAGS="-i -xO4 -xspace -xstrconst -mr -mt=yes -m64 -I/usr/include"
export LDFLAGS="-m64 -R%{_prefix}/lib64:/usr/lib/%{_arch64}:%{_prefix}/lib -L%{_prefix}/lib64:/usr/lib/%{_arch64}"
export LD_OPTIONS="-R%{_prefix}/lib64:/usr/lib/%{_arch64}:/usr/sfw/lib/%{_arch64} -L/usr/lib/%{_arch64}:/usr/sfw/lib/%{_arch64}"
env CFLAGS="$CFLAGS" ./configure --prefix=%{_prefix} \
                                  --bindir=%{_prefix}/bin/%{_arch64} \
                                  --libdir=%{_prefix}/%{_lib64} \
                                  --mandir=%{_mandir}/share/man \
                                  --with-fpectl \
                                  --enable-ipv6 \
                                  --with-threads \
                                  --enable-unicode=ucs4 \
                                  --with-dbmliborder=gdbm \
                                  --enable-loadable-sqlite-extensions \
                                  --with-system-expat \
                                  --with-system-ffi \
                                  --without-gcc \
                                  --enable-shared

make -j$CPUS
%endif

%install
cd %{_name}-%{unmangled_version}
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_prefix}/bin/python
rm $RPM_BUILD_ROOT%{_prefix}/bin/python2
rm $RPM_BUILD_ROOT%{_prefix}/bin/python2-config
rm $RPM_BUILD_ROOT%{_prefix}/bin/python-config
mv $RPM_BUILD_ROOT%{_prefix}/bin/2to3 $RPM_BUILD_ROOT%{_prefix}/bin/2to3%{pyver}
mv $RPM_BUILD_ROOT%{_prefix}/bin/idle $RPM_BUILD_ROOT%{_prefix}/bin/idle%{pyver}
mv $RPM_BUILD_ROOT%{_prefix}/bin/pydoc $RPM_BUILD_ROOT%{_prefix}/bin/pydoc%{pyver}
mv $RPM_BUILD_ROOT%{_prefix}/bin/smtpd.py  $RPM_BUILD_ROOT%{_prefix}/bin/smtpd%{pyver}.py
find $RPM_BUILD_ROOT%{_libdir}/python%{pyver} -name '*.pyo' -exec rm -f {} \;
echo "import site; site.addsitedir('%{_prefix}/lib/python%{pyver}/vendor-packages')" > $RPM_BUILD_ROOT%{_prefix}/lib/python%{pyver}/site-packages/vendor-packages.pth

%ifarch amd64 sparcv9
cd ../%{_name}-%{unmangled_version}-64
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/python
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/python2
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/python-config
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/python2-config
mv $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/2to3 $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/2to3%{pyver}
mv $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/idle $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/idle%{pyver}
mv $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/pydoc $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/pydoc%{pyver}
mv $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/smtpd.py  $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/smtpd%{pyver}.py
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_prefix}/include/python%{pyver}/pyconfig.h
find $RPM_BUILD_ROOT%{_prefix}/%{_lib64}/python%{pyver} -name '*.pyo' -exec rm -f {} \;
echo "import site; site.addsitedir('%{_prefix}/%{_lib64}/python%{pyver}/vendor-packages')" > $RPM_BUILD_ROOT%{_prefix}/%{_lib64}/python%{pyver}/site-packages/vendor-packages.pth
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/bin
%{_prefix}/bin/python%{pyver}
%{_prefix}/bin/idle%{pyver}
%{_prefix}/bin/pydoc%{pyver}
%{_prefix}/bin/2to3%{pyver}
%{_prefix}/bin/smtpd%{pyver}.py
%{_prefix}/bin/python%{pyver}-config
%dir %attr (0755, root, bin) %{_prefix}/lib
%{_prefix}/lib/*
%dir %attr (0755, root, bin) %{_prefix}/include
%{_prefix}/include/python%{pyver}/*

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/bin/%{_arch64}
%{_prefix}/bin/%{_arch64}/python%{pyver}
%{_prefix}/bin/%{_arch64}/idle%{pyver}
%{_prefix}/bin/%{_arch64}/pydoc%{pyver}
%{_prefix}/bin/%{_arch64}/2to3%{pyver}
%{_prefix}/bin/%{_arch64}/smtpd%{pyver}.py
%{_prefix}/bin/%{_arch64}/python%{pyver}-config
%dir %attr (0755, root, bin) %{_prefix}/%{_lib64}
%{_prefix}/%{_lib64}/*
%dir %attr (0755, root, bin) %{_prefix}/share
%{_prefix}/share/*
%endif

%changelog
* Wed Sep 17 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Add pyconfig.h
* Wed Sep 17 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris11 and version up 2.7.2 to 2.7.3
* Sun May 12 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Correction of the Import error
* Sun May 10 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- vender-packages directory support
* Sun May 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Only 64bit Python2.7 package
* Sun May 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for arch amd64
* Mon Apr 30 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Fixed a file conflict of python2.6
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- vender-packages directory support
* Sun Apr 1 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
