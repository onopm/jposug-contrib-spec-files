#
# spec file for package: kcc
#
# includes module(s):
#
%include Solaris.inc
%define tarball_name kcc

%define _prefix %{_basedir}

Name:		   SFEkcc
Version:	   2.3
IPS_package_name:  text/kcc
License:           GPLv2
Group:             Applications/Text
Source0:           ftp://ftp.sra.co.jp/pub/os/linux/JE/sources/base/kcc.tar.gz
Buildroot:         %{_tmppath}/%{name}-%{version}-%{release}-root
SUNW_Copyright:    %{name}.copyright
SUNW_BaseDir:        %{_basedir}

Meta(info.classification):      org.opensolaris.category.2008:Text

%description
KCC (Kanji Code Converter). Convert Japanese character encoding.

%prep
rm -rf %{tarball_name}
%setup -q -n %{tarball_name}

%build
CC=cc
export CC

make CC="${CC}" BINPATH="%{_bindir}"

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
make BINPATH="$RPM_BUILD_ROOT/%{_bindir}" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, sys)
%dir %attr (0755, root, bin) %{_bindir}
%defattr(-, root, bin)
%{_bindir}/kcc

%changelog
* Tue Mar 20 2012 TAKI Yasushi <taki@justplayer.com>
- rename 'Name' kcc to SFEkcc
- add SFEkcc.copyright
- fix permission for Solaris 11
* Sat Feb 25 2012 Yoichi Imai <sunnyone41@gmail.com>
- Initial release.

