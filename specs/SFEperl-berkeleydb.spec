#
# spec file for package: SFEperl-berkeleydb
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%include base.inc

%define tarball_version 0.54
%define tarball_name  BerkeleyDB
Name:		SFEperl-berkeleydb
IPS_package_name: library/perl-5/berkeleydb
Version:	1.13
IPS_component_version: 1.13
Summary:	BerkeleyDB - Perl extension for Berkeley DB version 2, 3, 4 or 5
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~rhandom/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:        http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{tarball_name}-%{tarball_version}.tar.gz
# see https://blogs.oracle.com/ali/entry/changing_elf_runpaths
#Source1:	https://blogs.oracle.com/ali/resource/rpath.tgz
%define rpath_tarball_name rpath.tgz
%define rpath_url https://blogs.oracle.com/ali/resource/%{rpath_tarball_name}
Patch0:		%{name}.config.in.patch
%include default-depend.inc
%include perl-depend.inc
BuildRequires:  database/berkeleydb-48
Requires:       database/berkeleydb-48

%if %cc_is_gcc
%if %( expr %{osbuild} '=' 175 )
BuildRequires: developer/gcc-45
Requires:      system/library/gcc-45-runtime
%else
BuildRequires: developer/gcc-46
Requires:      system/library/gcc
Requires:      system/library/gcc-runtime
%endif
%endif

%description
This Perl module provides an interface to most of the functionality available in Berkeley DB versions 2, 3, 5 and 6. In general it is safe to assume that the interface provided here to be identical to the Berkeley DB interface. The main changes have been to make the Berkeley DB API work in a Perl way. Note that if you are using Berkeley DB 2.x, the new features available in Berkeley DB 3.x or later are not available via this module.

%package 510 
IPS_package_name: library/perl-5/berkeleydb-510
Summary: BerkeleyDB - Perl extension for Berkeley DB version 2, 3, 4 or 5 for perl-510
BuildRequires:	runtime/perl-510
Requires:	runtime/perl-510
Requires:	library/perl-5/berkeleydb

%prep
%setup -q -n %{tarball_name}-%{tarball_version}
%patch0 -p0 -b .orig
cat <<EOT >rewrite.sh
#!/bin/bash
find . -name 'Makefile' -exec sed -i -e 's/-xO3/-O3/' -e 's/-xspace//' -e 's/-xildoff//' -e 's/-KPIC/-fPIC/' -e 's/CC = cc/CC = gcc/' {} \;
EOT
chmod 775 rewrite.sh
wget --no-check-certificate %rpath_url
tar xvfz %rpath_tarball_name

%build
rm -rf $RPM_BUILD_ROOT
pushd rpath
make
popd
# see http://search.cpan.org/~mschwern/ExtUtils-MakeMaker-6.62/lib/ExtUtils/MakeMaker.pm
export PERL5LIB=/usr/perl5/vendor_perl/5.10.0
/usr/perl5/5.10.0/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.10.0
./rewrite.sh
make
./rpath/rpath blib/arch/auto/BerkeleyDB/BerkeleyDB.so /usr/gnu/lib
make test

make pure_install
make clean

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}

%files 510
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.10.0

%changelog
* Jul 21 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial commit
