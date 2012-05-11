#
# spec file for package SFEpython3
#
#

%define _name Python
%define version 3.2.2
%define unmangled_version 3.2.2
%define release 1
%define pyver 3.2

%include Solaris.inc
%include packagenamemacros.inc

Name: SFEpython32
IPS_Package_Name:	runtime/python-32
Summary: The Python interpreter, libraries and utilities
Group: Development/Python
Version: %{version}
Release: %{release}
License: PSF license
Source: http://www.python.org/ftp/python/%{unmangled_version}/%{_name}-%{unmangled_version}.tar.bz2
Patch1: SFEpython32-lib64.diff
Url: http://www.python.org/download/releases/3.2.2
Group: Development/Libraries
%include default-depend.inc

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
SUNW_Basedir:	%{_basedir}
SUNW_Copyright:	Python3.copyright

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
%ifarch amd64 sparcv9
cd %{_name}-%{unmangled_version}-64
%patch1 -p1

export CFLAGS="-i -xO4 -xspace -xstrconst -mr -xregs=no%frameptr -m64"
export LDFLAGS="%_ldflags -m64 -L/usr/gnu/lib/%{_arch64} -R/usr/gnu/lib/%{_arch64}"
export LD_OPTIONS="-m64 -R/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64} -L/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64}"
env CFLAGS="$CFLAGS" ./configure --prefix=%{_prefix} \
                                 --bindir=%{_bindir}/%{_arch64} \
                                 --libdir=%{_libdir}/%{_arch64} \
                                 --mandir=%{_mandir} \
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
%ifarch amd64 sparcv9
cd %{_name}-%{unmangled_version}-64
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{pyver} -name '*.pyo' -exec rm -rf {} \;
echo "import site; site.addsitedir('/usr/lib/%{_arch64}/python%{pyver}/vendor-packages')" > $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{pyver}/site-packages/vendor-packages.pth
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/%{_arch64}/idle3
%{_bindir}/%{_arch64}/idle%{pyver}
%{_bindir}/%{_arch64}/2to3
%{_bindir}/%{_arch64}/2to3-%{pyver}
%{_bindir}/%{_arch64}/python3
%{_bindir}/%{_arch64}/python%{pyver}
%{_bindir}/%{_arch64}/python%{pyver}m
%{_bindir}/%{_arch64}/python3-config
%{_bindir}/%{_arch64}/python%{pyver}-config
%{_bindir}/%{_arch64}/python%{pyver}m-config
%{_bindir}/%{_arch64}/pydoc3
%{_bindir}/%{_arch64}/pydoc%{pyver}
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/%{_arch64}/libpython%{pyver}m.so
%{_libdir}/%{_arch64}/libpython3.so
%{_libdir}/%{_arch64}/libpython%{pyver}m.so.1.0
%{_libdir}/%{_arch64}/python%{pyver}/*
%dir %attr (0755, root, other) %{_libdir}/%{_arch64}/pkgconfig
%{_libdir}/%{_arch64}/pkgconfig/python3.pc
%{_libdir}/%{_arch64}/pkgconfig/python-%{pyver}m.pc
%{_libdir}/%{_arch64}/pkgconfig/python-%{pyver}.pc

%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%{_mandir}/man1/python3.2.1
%dir %attr(0755, root, bin) %{_includedir}
%{_includedir}/python%{pyver}m/*

%changelog
* Sun May 11 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Only 64bit Python3.2 package
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- vendor-packages directory support


