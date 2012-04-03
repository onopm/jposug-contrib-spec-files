#
# spec file for package SFEpython27
#
#

%define _name Python
%define version 2.7.2
%define unmangled_version 2.7.2
%define release 1

%include Solaris.inc
%include packagenamemacros.inc

Name: SFEpython27
IPS_Package_Name:	runtime/python-27
Summary: The Python interpreter, libraries and utilities
Group: Development/Python
Version: %{version}
Release: %{release}
License: PSF license
Source: http://www.python.org/ftp/python/%{unmangled_version}/%{_name}-%{unmangled_version}.tar.bz2
Url: http://www.python.org/download/releases/2.7.2
Group: Development/Libraries
%include default-depend.inc

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
SUNW_Basedir:	%{_basedir}
SUNW_Copyright:	Python27.copyright

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
%setup -n %{_name}-%{unmangled_version}

%build
CPUS=$(psrinfo | awk '$2=="on-line"{cpus++}END{if(cpus==0){print 1}else{print cpus }}')

env CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} \
					--mandir=%{_mandir}
make -j$CPUS

%install
make install DESTDIR=$RPM_BUILD_ROOT
echo "import site; site.addsitedir('/usr/lib/python2.7/vendor-packages')" > $RPM_BUILD_ROOT%{_libdir}/python2.7/site-packages/vendor-packages.pth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/idle
%{_bindir}/2to3
%{_bindir}/python
%{_bindir}/python2.7
%{_bindir}/python2.7-config
%{_bindir}/python-config
%{_bindir}/pydoc
%{_bindir}/smtpd.py
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/python2.7/*
%dir %attr (0755, root, other) %{_libdir}/pkgconfig 
%{_libdir}/pkgconfig/python.pc
%{_libdir}/pkgconfig/python-2.7.pc
%{_libdir}/libpython2.7.a
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/*
%{_mandir}/*/*
%dir %attr(0755, root, bin) %{_includedir}
%{_includedir}/python2.7/*

%changelog
* Sun Apr 1 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- vender-packages directory support
