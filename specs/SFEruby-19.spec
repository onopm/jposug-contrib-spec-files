#
# spec file for package SFEruby-19
#
#
%define _name ruby
%define version 1.9.3
%define patchlevel 429

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc
%define cc_is_gcc 1
%define _gpp g++
%include base.inc

Name: SFEruby-19
IPS_Package_Name:	runtime/ruby-19
Summary: An interpreter of object-oriented scripting language
Version: %{version}
Release: %{patchlevel}
IPS_component_version: %{version}.%{patchlevel}
License: GPL
Source: http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-%{version}-p%{patchlevel}.tar.gz
Url: http://www.ruby-lang.org/
Requires: %{pnm_requires_gnu_dbm}
BuildRequires: %{pnm_buildrequires_gnu_dbm}
Requires: %{pnm_requires_library_libffi}
BuildRequires: %{pnm_buildrequires_library_libffi}
Requires: %{pnm_requires_library_ncurses}
BuildRequires: %{pnm_buildrequires_library_ncurses}
Requires: %{pnm_requires_library_readline}
BuildRequires: %{pnm_buildrequires_library_readline}
Requires: %{pnm_requires_library_security_openssl}
BuildRequires: %{pnm_buildrequires_library_security_openssl}
Requires: library/text/yaml 
BuildRequires: library/text/yaml
Requires:       %{pnm_requires_library_zlib}
BuildRequires:  %{pnm_buildrequires_library_zlib}

%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
BuildRequires: system/library/math
Requires:      system/library/math
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
BuildRequires: system/library/math/header-math
Requires:      system/library/math/header-math
Requires:      system/library/gcc-runtime
%endif

# OpenSolaris IPS Manifest Fields
#Meta(pkg.depend.runpath):usr/gnu/lib/

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
# %setup -c -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}-p%{patchlevel}
%build
export CXXFLAGS="%cxx_optflags"
export LDFLAGS="%_ldflags %gnu_lib_path"
export CFLAGS="%optflags"
%if %( expr %{osbuild} '=' 175 )
export CC=gcc
export CXX=g++
%else
export CC=/usr/gcc/4.6/bin/gcc
export CXX=/usr/gcc/4.6/bin/g++
%endif
$CC -v
$CXX -v
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
./configure \
%if %( expr %{osbuild} '=' 175 )
%else
ac_cv_func_dl_iterate_phdr=no \
%endif
    --prefix=/usr/ruby/1.9 \
    --bindir=/usr/ruby/1.9/bin \
    --libdir=/usr/ruby/1.9/lib \
    --sbindir=/usr/ruby/1.9/sbin \
    --enable-dtrace \
    --enable-shared \
    --enable-install-doc \
    --disable-option-checking \
    --with-openssl \
    --with-tk-dir=/usr \
    --with-curses-dir=/usr
make -j$CPUS

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cd $RPM_BUILD_ROOT/usr/bin
ln -s ../ruby/1.9/bin/erb erb19
ln -s ../ruby/1.9/bin/gem gem19
ln -s ../ruby/1.9/bin/irb irb19
ln -s ../ruby/1.9/bin/rake rake19
ln -s ../ruby/1.9/bin/rdoc rdoc19
ln -s ../ruby/1.9/bin/ri ri19
ln -s ../ruby/1.9/bin/ruby ruby19

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /usr
/usr/bin/*19
/usr/ruby/1.9

%changelog
* Wed May 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to patchlevel 429 and modify BuildRequires/Requires for Solaris 11
* Mon Apr 22 2013 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- bump to patch level 392
* Mon Feb 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to patch level 385
* Tue Feb 05 2013 - YAMAMOTO Takashi<yamachan@selfnavi.com>
- change BuildRequires that refer to gcc at OI
* Tue Jan 29 2013 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Support for OpenIndiana
* Fri Dec 20 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add symbolic link from /usr/ruby/1.9/bin/ruby to /usr/bin/ruby19 and so on.
* Mon Nov 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires and Requires
* Sun Nov 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify configure option and use gcc
* Mon Oct 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to patchlevel 286
* Sat Jun 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
