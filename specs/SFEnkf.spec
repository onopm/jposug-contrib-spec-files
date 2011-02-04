#
# spec file for package: nkf
#
# includes module(s):
#
%include Solaris.inc

%define         perl_vendorarch %(%{__perl} -MConfig -e 'print $Config{vendorarch}')
%define         perl_archlib    %(%{__perl} -MConfig -e 'print $Config{archlib}')
%define         perl_man3dir    %(%{__perl} -MConfig -e 'print $Config{man3dir}')

Name:		   nkf
Version:	   2.1.1
IPS_package_name:  text/nkf
License:           BSD
URL:               http://nkf.sourceforge.jp/
Source0:           http://dl.sourceforge.jp/%{name}/48945/%{name}-%{version}.tar.gz
Buildroot:         %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:     SUNWperl584core
BuildRequires:     system/library/iconv/utf-8
SUNW_Copyright:    %{name}.copyright

%description
Nkf is a Kanji code converter for terminals, hosts, and networks. Nkf
converts input Kanji code to 7-bit JIS, MS-kanji (shifted-JIS) or EUC.

%package  NKF
IPS_package_name: library/perl-5/nkf
Summary:        Perl extension for Network Kanji Filter
Group:          Applications/Text
BuildRequires:	SUNWperl584core
BuildRequires:	SUNWperl584usr
Requires:	SUNWperl584core
Requires:	SUNWperl584usr


%description  NKF
This is a Perl Extension version of nkf (Network Kanji Filter).
It converts the last argument and return converted result.
Conversion details are specified by flags before the last argument.

Meta(info.maintainer):          s.miyaza@gmail.com
Meta(info.upstream):            Naruse Yui <naruse@users.sourceforge.jp>
Meta(info.upstream_url):        http://sourceforge.jp/projects/nkf/
Meta(info.classification):	org.opensolaris.category.2008:Text

%prep
%setup -q -n %{name}-%{version}

%build
CC=/usr/bin/cc
CFLAGS="-xO3 -xspace -xildoff -KPIC"
export CC CFLAGS

make CC="${CC}" CFLAGS="$CFLAGS" nkf
pushd NKF.mod
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor
make CC="${CC}"
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja_JP.UTF-8/man1

./nkf -e nkf.1j > nkf.1jeuc
iconv -f euc-jp -t utf-8 nkf.1jeuc > nkf.1utf8
ginstall -c -m 755 -p nkf $RPM_BUILD_ROOT%{_bindir}
ginstall -c -m 644 -p nkf.1 $RPM_BUILD_ROOT%{_mandir}/man1
ginstall -c -m 644 -p nkf.1utf8 $RPM_BUILD_ROOT%{_mandir}/ja_JP.UTF-8/man1/nkf.1
pushd NKF.mod
make pure_install PERL_INSTALL_ROOT=${RPM_BUILD_ROOT}
rm -f   $RPM_BUILD_ROOT%{perl_vendorarch}/perllocal.pod         \
        $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod            \
        $RPM_BUILD_ROOT%{perl_vendorarch}/auto/NKF/NKF.bs       \
        $RPM_BUILD_ROOT%{perl_vendorarch}/auto/NKF/.packlist
popd
chmod 0755 $RPM_BUILD_ROOT%{perl_vendorarch}/auto/NKF/NKF.so


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_bindir}/nkf
%{_mandir}/man1/nkf.1*
%{_mandir}/ja_JP.UTF-8/man1/nkf.1*

%files  NKF
%defattr (-, root, root, -)
%{perl_vendorarch}/NKF.pm
%{perl_vendorarch}/auto/*
%{perl_man3dir}/NKF.3

%changelog
* Thu Feb  3 2011 Satoru MIYAZAKI <s.miyaza@gmail.com> 
- Support for Solaris11 Express.
