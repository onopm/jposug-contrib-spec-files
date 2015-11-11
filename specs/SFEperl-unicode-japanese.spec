#
# spec file for package: SFEperl-unicode-japanese
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

Name:		SFEperl-unicode-japanese
IPS_package_name: library/perl-5/unicode-japanese
Version:	0.49
Summary:	Japanese Character Encoding Handler
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~hio/Unicode-Japanese-%{version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/H/HI/HIO/Unicode-Japanese-%{version}.tar.gz
BuildRequires:  %{pnm_buildrequires_perl_default}
Requires:  	%{pnm_requires_perl_default}

Meta(info.maintainer):          taki@justplayer.com
Meta(info.upstream):            YAMASHINA Hio <hio@hio.jp>
Meta(info.upstream_url):        http://search.cpan.org/~hio/Unicode-Japanese-%{version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Japanese Character Encoding Handler

%package 584
IPS_package_name: library/perl-5/unicode-japanese-584
Summary: Japanese Character Encoding Handler for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/unicode-japanese-512
Summary: Japanese Character Encoding Handler for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512

%prep
%setup -q -n Unicode-Japanese-%{version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
# make test

rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/perl5/5.8.4
mv $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT%{_prefix}/perl5/5.8.4

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL  PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test

%install
# rm -rf $RPM_BUILD_ROOT
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl
mkdir -p $RPM_BUILD_ROOT%{_prefix}/perl5/5.12
mv $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT%{_prefix}/perl5/5.12

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
# %{_prefix}/perl5
%dir %attr(0755, root, sys) %{_datadir}
%{_mandir}
# %dir %attr(0755,root, bin) %{_bindir}
# %{_bindir}/*

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4
%{_prefix}/perl5/5.8.4/bin

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
%{_prefix}/perl5/5.12/bin

%changelog
* Fri Jun 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.49
- generate packages for perl-584 and perl-512