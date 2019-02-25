#
# spec file for package SFEpbzip2
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc

%define srcname pbzip2


Name:                    SFEpbzip2
IPS_Package_Name:	 compress/pbzip2
Summary:                 A parallel implementation of bzip2
Group:                   Utility
Version:                 1.1.6
URL:		         http://compression.ca/pbzip2/
Source:		         http://compression.ca/%{srcname}//%{srcname}-%{version}.tar.gz
License: 		 BSDL
SUNW_Copyright:          %{name}.copyright
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file compressor that uses pthreads and achieves near-linear speedup on SMP machines. The output of this version is fully compatible with bzip2 v1.0.2 or newer (ie: anything compressed with pbzip2 can be decompressed with bzip2). PBZIP2 should work on any system that has a pthreads compatible C++ compiler (such as gcc).

%prep
rm -rf %name-%version
%setup -q -n %srcname-%version

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
#export CFLAGS="%optflags"
#export LDFLAGS="%_ldflags"
#make CC="$CC" CFLAGS="$CFLAGS" -j$CPUS
make -f Makefile.solaris.sunstudio

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mv pbzip2 $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mv pbzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, bin) %{_mandir}
%dir %attr(0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*

%changelog
* Mon Jan  7 JST 2013 TAKI,Yasushi <taki@justplayer.com>
- Initial spec.
