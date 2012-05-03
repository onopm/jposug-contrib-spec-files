#
# spec file for package SFEpython27
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
%setup -c -n %{_name}-%{unmangled_version}

%ifarch amd64 sparcv9
rm -rf %{_name}-%{unmangled_version}-64
cp -rp %{_name}-%{unmangled_version} %{_name}-%{unmangled_version}-64
%endif

%build
cd %{_name}-%{unmangled_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

CPUS=$(psrinfo | awk '$2=="on-line"{cpus++}END{if(cpus==0){print 1}else{print cpus }}')

env CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} \
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


%ifarch amd64 sparcv9
cd ../%{_name}-%{unmangled_version}-64
export CFLAGS="-i -xO4 -xspace -xstrconst -mr -xregs=no%frameptr -m64"
export LDFLAGS="%_ldflags -m64 -L/usr/gnu/lib/%{_arch64} -R/usr/gnu/lib/%{_arch64}"
export LD_OPTIONS="-m64 -R/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64} -L/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64}"
env CFLAGS="$CFLAGS" ./configure --prefix=%{_prefix} \
                                 --bindir=%{_prefix}/bin/%{_arch64} \
                                 --libdir=%{_prefix}/lib/%{_arch64} \
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
cd %{_name}-%{unmangled_version}
make install DESTDIR=$RPM_BUILD_ROOT
echo "import site; site.addsitedir('/usr/lib/python2.7/vendor-packages')" > $RPM_BUILD_ROOT%{_libdir}/python2.7/site-packages/vendor-packages.pth
mv $RPM_BUILD_ROOT%{_bindir}/python $RPM_BUILD_ROOT%{_bindir}/python2.7
mv $RPM_BUILD_ROOT%{_bindir}/idle $RPM_BUILD_ROOT%{_bindir}/idle2.7
mv $RPM_BUILD_ROOT%{_bindir}/pydoc $RPM_BUILD_ROOT%{_bindir}/pydoc2.7
mv $RPM_BUILD_ROOT%{_bindir}/2to3 $RPM_BUILD_ROOT%{_bindir}/2to32.7
mv $RPM_BUILD_ROOT%{_bindir}/smtpd.py $RPM_BUILD_ROOT%{_bindir}/smtpd2.7.py
rm $RPM_BUILD_ROOT%{_bindir}/python-config
cd ..


%ifarch amd64 sparcv9
cd %{_name}-%{unmangled_version}-64
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/idle $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/idle2.7
mv $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/pydoc $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/pydoc2.7
mv $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/2to3 $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/2to32.7
mv $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/smtpd.py $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/smtpd2.7.py
rm $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/python-config
rm $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/python
rm $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/pkgconfig/python.pc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/python2.7
%{_bindir}/idle2.7
%{_bindir}/pydoc2.7
%{_bindir}/2to32.7
%{_bindir}/smtpd2.7.py
%{_bindir}/python2.7-config
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/libpython2.7.so
%{_libdir}/libpython2.7.so.1.0
%{_libdir}/python2.7/*

# %{_bindir}/amd64
%dir %attr (0755, root, bin) %{_bindir}/amd64
%{_bindir}/amd64/python2.7
%{_bindir}/amd64/idle2.7
%{_bindir}/amd64/pydoc2.7
%{_bindir}/amd64/2to32.7
%{_bindir}/amd64/smtpd2.7.py
%{_bindir}/amd64/python2.7-config
# %{_libdir}/amd64
%dir %attr (0755, root, bin) %{_libdir}/amd64
%{_libdir}/amd64/libpython2.7.so
%{_libdir}/amd64/libpython2.7.so.1.0
%{_libdir}/amd64/python2.7/*
# %{_libdir}/amd64/pkgconfig
%dir %attr (0755, root, other) %{_libdir}/amd64/pkgconfig 
%{_libdir}/amd64/pkgconfig/python-2.7.pc

%dir %attr (0755, root, other) %{_libdir}/pkgconfig 
%{_libdir}/pkgconfig/python.pc
%{_libdir}/pkgconfig/python-2.7.pc
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%{_mandir}/man1/python2.7.1
%dir %attr(0755, root, bin) %{_includedir}
%{_includedir}/python2.7/*

%changelog
* Sun May 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for arch amd64
* Mon Apr 30 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Fixed a file conflict of python2.6
* Sun Apr 3 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- vender-packages directory support
* Sun Apr 1 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
