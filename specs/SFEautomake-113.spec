#
# spec file for package SFEautomake-113
#
# includes module(s): automake
#
%include Solaris.inc

Name:		SFEautomake-113
IPS_Package_Name:	developer/build/automake-113
SUNW_Copyright: %{name}.copyright
Summary:	GNU Automake 1.13
License:	GPLv2
URL:		http://www.gnu.org/software/automake/
Version:	1.13.4
Source:		http://ftp.gnu.org/gnu/automake/automake-%{version}.tar.gz
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc

%prep
%setup -q -n automake-%{version}
sed -i".orig" "s/\(system_includes = ('@datadir@\)\/aclocal/\1\/aclocal-1.13/" aclocal.in

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CFLAGS="%optflags"
export LDFLAGS="%_ldflags"
./configure --prefix=%{_prefix}

make -j$CPUS

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
/bin/rm -f %{buildroot}/%{_bindir}/aclocal
/bin/rm -f %{buildroot}/%{_bindir}/automake
/bin/rm -rf %{buildroot}/%{_infodir}
/bin/rm -rf %{buildroot}/%{_datadir}/doc
/bin/rm -rf %{buildroot}/%{_datadir}/aclocal
for f in automake aclocal; do
    /bin/mv -f $RPM_BUILD_ROOT%{_mandir}/man1/$f.1 $RPM_BUILD_ROOT%{_mandir}/man1/$f-113.1
done

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, bin)
%{_bindir}
%dir %attr (0755, root, sys) %{_datadir}
%{_datadir}/aclocal-1.13
%{_datadir}/automake-1.13
%{_mandir}

%changelog
* Thr May 01 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug
* Tue Oct 11 2011 - Milan Jurik
- Initial spec
* Wed Oct 19 2011 - brian.cameron@oracle.com
- Do not install %{_datadir}/doc since it conflicts with the installed 
  automake if installed via IPS.
