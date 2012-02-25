#
# spec file for package: kcc
#
# includes module(s):
#
%include Solaris.inc

Name:		   kcc
Version:	   2.3
IPS_package_name:  text/kcc
License:           GPLv2
Group:             Applications/Text
Source0:           ftp://ftp.sra.co.jp/pub/os/linux/JE/sources/base/kcc.tar.gz
Buildroot:         %{_tmppath}/%{name}-%{version}-%{release}-root
SUNW_Copyright:    %{name}.copyright

Meta(info.classification):      org.opensolaris.category.2008:Text

%description
KCC (Kanji Code Converter). Convert Japanese character encoding.

%prep
rm -rf %{name}
%setup -q -n %{name}

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
%defattr(-, root, root, -)
%{_bindir}/kcc

%changelog
* Sat Feb 25 2012 Yoichi Imai <sunnyone41@gmail.com>
- Initial release.

