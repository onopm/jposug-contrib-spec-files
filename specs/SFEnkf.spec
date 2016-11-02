#
# spec file for package: nkf
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define         perl_vendorarch %(%{__perl} -MConfig -e 'print $Config{vendorarch}')
%define         perl_archlib    %(%{__perl} -MConfig -e 'print $Config{archlib}')
%define         perl_man3dir    %(%{__perl} -MConfig -e 'print $Config{man3dir}')
%define         tarball_name    nkf

Name:		   SFEnkf
Version:	   2.1.3
IPS_package_name:  text/nkf
License:           BSD
Group:             Applications/Text
URL:               http://nkf.sourceforge.jp/
Source0:           http://dl.sourceforge.jp/%{tarball_name}/59912/%{tarball_name}-%{version}.tar.gz
Buildroot:         %{_tmppath}/%{tarball_name}-%{version}-%{release}-root
%if %( expr %{osbuild} '=' 175 )
BuildRequires:     %{pnm_buildrequires_SUNWperl584core_devel}
Requires:          %{pnm_requires_SUNWperl584core}
%else
BuildRequires:     %{pnm_buildrequires_perl510core}
Requires:          %{pnm_requires_perl510core}
%endif
BuildRequires:     %{pnm_buildrequires_system_library_iconv_utf_8}
BuildRequires:          system/library
Requires:          system/library
Requires:          %{pnm_requires_system_library_iconv_utf_8}

SUNW_Copyright:    %{tarball_name}.copyright

Meta(info.maintainer_url):      http://sourceforge.jp/forum/forum.php?forum_id=25193
Meta(info.upstream_url):        http://sourceforge.jp/projects/nkf/
Meta(info.classification):      org.opensolaris.category.2008:Text

%description
Nkf is a Kanji code converter for terminals, hosts, and networks. Nkf
converts input Kanji code to 7-bit JIS, MS-kanji (shifted-JIS) or EUC.

%package -n SFEperl-nkf
IPS_package_name: library/perl-5/nkf
Summary:        Perl extension for Network Kanji Filter
Group:          Applications/Text
%if %( expr %{osbuild} '=' 175 )
BuildRequires:     %{pnm_buildrequires_SUNWperl584core_devel}
Requires:          %{pnm_requires_SUNWperl584core}
%else
BuildRequires:     %{pnm_buildrequires_perl510core}
Requires:          %{pnm_requires_perl510core}
%endif
BuildRequires:     %{pnm_buildrequires_system_library_iconv_utf_8}
BuildRequires:          system/library
Requires:          system/library
#Requires:          %{pnm_requires_system_library}
Requires:          %{pnm_requires_system_library_iconv_utf_8}

%description -n SFEperl-nkf
This is a Perl Extension version of nkf (Network Kanji Filter).
It converts the last argument and return converted result.
Conversion details are specified by flags before the last argument.


%prep
%setup -q -n %{tarball_name}-%{version}

%build
CC=cc
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
%defattr(-, root, sys, -)
%dir %{_prefix}
%dir %{_datadir}
%defattr(-, root, bin, -)
%dir %{_bindir}
%dir %{_mandir}/man1
%dir %{_mandir}/ja_JP.UTF-8
%dir %{_mandir}/ja_JP.UTF-8/man1
%defattr(-, root, bin, -)
%{_bindir}/nkf
%{_mandir}/man1/nkf.1*
%{_mandir}/ja_JP.UTF-8/man1/nkf.1*

%files -n SFEperl-nkf
%defattr (-, root, sys, -)
%dir %{_prefix}
%defattr (-, root, bin, -)
%dir %{perl_vendorarch}
%dir %{perl_man3dir}
%{perl_vendorarch}/NKF.pm
%{perl_vendorarch}/auto/*
%{perl_man3dir}/NKF.3

%changelog
* Wed Nov 12 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.3
* Tue Jan 29 2013 YAMAMOTO Takashi<yamachan@selfnavi.com>
- Support for OpenIndiana
* Sun Jan  6 2013 TAKI, Yasushi <taki@justplayer.com>
- Bump to 2.1.2
- use pnmacro.
- fix minor error
* Thu Mar 15 2012 Satoru MIYAZAKI <s.miyaza@gmail.com>
- add dir entries
* Thu Feb  3 2011 Satoru MIYAZAKI <s.miyaza@gmail.com>
- Support for Solaris11 Express.
