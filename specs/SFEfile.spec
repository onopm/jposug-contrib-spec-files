#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%include Solaris.inc
%include packagenamemacros.inc

%define _prefix %{_basedir}/gnu
%define tarball_name file

Name:                SFEfile
IPS_package_name:    file/astron-file
Summary:             determine file type
Version:             5.05
IPS_component_version: 5.5
Source:              ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz
SUNW_Copyright:      %{name}.copyright
SUNW_BaseDir:        %{_basedir}
BuildRoot:           %{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%prep
%setup -c -n %{tarball_name}-%version
%ifarch amd64 sparcv9
rm -rf %{tarball_name}-%{version}-64
cp -rp %{tarball_name}-%{version} %{tarball_name}-%{version}-64
%endif

%build

cd %{tarball_name}-%{version}

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"

./configure \
 --prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir} \
 --bindir=%{_bindir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir} \
 --enable-static=no

make -j$CPUS

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{version}-64
export CFLAGS="%optflags64"
./configure \
 --prefix=%{_prefix}\
 --sysconfdir=%{_sysconfdir} \
 --libdir=%{_libdir}/%{_arch64} \
 --bindir=%{_bindir}/%{_arch64} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir} \
 --enable-static=no

make -j$CPUS

%endif

%install
cd %{tarball_name}-%{version}
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{version}-64
make install DESTDIR=$RPM_BUILD_ROOT
cd ..
%endif

find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
rmdir ${RPM_BUILD_ROOT}%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*
%dir %attr (0755, root, bin) %{_includedir}
%{_includedir}/*
%dir %attr (0755, root, bin) %{_libdir}
%{_libdir}/*
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/misc/*
%dir %attr (0755, root, bin) %{_mandir}
%dir %attr (0755, root, bin) %{_mandir}/man1
%{_mandir}/man1/*.1
%dir %attr (0755, root, bin) %{_mandir}/man3
%{_mandir}/man3/*.3
%dir %attr (0755, root, bin) %{_mandir}/man4
%{_mandir}/man4/*.4

%changelog
* Wed Feb  2 2011 - taki@justplayer.com
- Bump to 5.05
- Support for Solaris11 Express.
* Thu Jun 10 2010 - pradhap (at) gmail.com
- Bump to 5.04
* Tue Oct 22 2008  - Pradhap Devarajan <pradhap (at) gmail.com>
- Bump to 4.26
* Sat Jul 15 2007 - dougs@truemail.co.th
- Bump to 4.21
* Thu May 03 2007 - nonsea@users.sourceforge.net
- Bump to 4.20.
- Add patch file-01-REG_STARTEND.diff, get original copy from
  ftp://ftp.astron.com/pub/file/patch-4.20-REG_STARTEND
* Mon Jan 15 2007 - laca@sun.com
- bump to 4.19
* Tue Nov 07 2006 - Eric Boutilier
- Initial spec
