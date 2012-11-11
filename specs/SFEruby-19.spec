#
# spec file for package SFEpython3
#
#

%define _name ruby
%define version 1.9.3
%define unmangled_version 1.9.3
%define patchlevel 286

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

Name: SFEruby-19
IPS_Package_Name:	runtime/ruby-19
Summary: An interpreter of object-oriented scripting language
Version: %{version}
Release: %{patchlevel}
License: GPL
Source: http://ftp.ruby-lang.org/pub/ruby/1.9/ruby-%{version}-p%{patchlevel}.tar.gz
Url: http://www.ruby-lang.org/



%description

%prep
# %setup -c -n ruby-%{version}-p%{patchlevel}
%setup -n ruby-%{version}-p%{patchlevel}
%build
./configure --prefix=/usr/ruby/1.9 \
    --bindir=/usr/ruby/1.9/bin \
    --libdir=/usr/ruby/1.9/lib \
    --sbindir=/usr/ruby/1.9/sbin \
    --enable-dtrace \
    --enable-shared \
    --enable-install-doc \
    --disable-option-checking \
    --with-openssl \
    --with-tk-dir=/usr \
    --with-curses-dir=/usr \
    CC=/usr/bin/gcc \
    CXX=/usr/bin/g++

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Sun Nov 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify configure option and use gcc
* Mon Oct 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to patchlevel 286
* Sat Jun 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
