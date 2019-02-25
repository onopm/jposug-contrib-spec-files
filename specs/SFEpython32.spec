#
# spec file for package SFEpython3
#
#

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define _name Python
%define version 3.2.2
%define unmangled_version 3.2.2
%define release 1
%define pyver 3.2

%define _prefix /usr/python
%define _basedir %{_prefix}
%define _lib64  lib64

Name:                SFEpython32
IPS_Package_Name:    runtime/SFEpython-322
Summary:             The Python interpreter, libraries and utilities
Group:               Development/Python
Version:             %{version}
Release:             %{release}
License:             PSF license
Source:              http://www.python.org/ftp/python/%{unmangled_version}/%{_name}-%{unmangled_version}.tar.bz2
Source1:             SFEpython32-pyconfig.h
Patch1:              SFEpython32-lib64.diff
Url:                 http://www.python.org/download/releases/3.2.2
Group:               Development/Libraries

BuildRoot:           %{_tmppath}/%{name}-%{version}-%{release}-buildroot
SUNW_Basedir:        %{_basedir}
SUNW_Copyright:	     Python3.copyright

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
dynamic typing. There are interfaces to many system calls and
libraries, as well as to various windowing systems (X11, Motif, Tk,
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
%patch1 -p1
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
rm $RPM_BUILD_ROOT%{_prefix}/bin/python3
rm $RPM_BUILD_ROOT%{_prefix}/bin/python3-config
rm $RPM_BUILD_ROOT%{_prefix}/bin/python%{pyver}-config
rm $RPM_BUILD_ROOT%{_prefix}/bin/2to3
rm $RPM_BUILD_ROOT%{_prefix}/bin/idle3
rm $RPM_BUILD_ROOT%{_prefix}/bin/pydoc3
find $RPM_BUILD_ROOT%{_libdir}/python%{pyver} -name '*.pyo' -exec rm -f {} \;
echo "import site; site.addsitedir('%{_prefix}/lib/python%{pyver}/vendor-packages')" > $RPM_BUILD_ROOT%{_prefix}/lib/python%{pyver}/site-packages/vendor-packages.pth

%ifarch amd64 sparcv9
cd ../%{_name}-%{unmangled_version}-64
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/python3
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/python3-config
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/python%{pyver}-config
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/2to3
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/idle3
rm $RPM_BUILD_ROOT%{_prefix}/bin/%{_arch64}/pydoc3
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_prefix}/include/python%{pyver}m/pyconfig.h
find $RPM_BUILD_ROOT%{_prefix}/%{_lib64}/python%{pyver} -name '*.pyo' -exec rm -f {} \;
echo "import site; site.addsitedir('%{_prefix}/%{_lib64}/python%{pyver}/vendor-packages')" > $RPM_BUILD_ROOT%{_prefix}/%{_lib64}/python%{pyver}/site-packages/vendor-packages.pth
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/bin
%{_prefix}/bin/python%{pyver}
%{_prefix}/bin/python%{pyver}m
%{_prefix}/bin/idle%{pyver}
%{_prefix}/bin/pydoc%{pyver}
%{_prefix}/bin/2to3-%{pyver}
%{_prefix}/bin/python%{pyver}m-config
%dir %attr (0755, root, bin) %{_prefix}/lib
%{_prefix}/lib/*
%dir %attr (0755, root, bin) %{_prefix}/include
%{_prefix}/include/python%{pyver}m/*

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_prefix}/bin/%{_arch64}
%{_prefix}/bin/%{_arch64}/python%{pyver}
%{_prefix}/bin/%{_arch64}/python%{pyver}m
%{_prefix}/bin/%{_arch64}/idle%{pyver}
%{_prefix}/bin/%{_arch64}/2to3-%{pyver}
%{_prefix}/bin/%{_arch64}/pydoc%{pyver}
%{_prefix}/bin/%{_arch64}/python%{pyver}m-config
%dir %attr (0755, root, bin) %{_prefix}/%{_lib64}
%{_prefix}/%{_lib64}/*
%dir %attr (0755, root, bin) %{_prefix}/share
%{_prefix}/share/*
%endif

%changelog
* Sun May 12 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris 11.1
* Sun May 12 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Correction of the Import error
* Sun May 11 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Only 64bit Python3.2 package
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- vendor-packages directory support
