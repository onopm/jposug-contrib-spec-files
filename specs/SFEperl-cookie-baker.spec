#
# spec file for package: SFEperl-cookie-baker
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.03
%define tarball_name    Cookie-Baker

Name:		SFEperl-cookie-baker
IPS_package_name: library/perl-5/cookie-baker
Version:	0.03
IPS_component_version: 0.3
Summary:	Cookie::Baker - Cookie string generator / parser
License:	Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kazeburo/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
# Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KAZEBURO/Cookie-Baker-%{tarball_version}.tar.gz
Source0:	http://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cookie-Baker-0.03.tar.gz

BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Masahiro Nagano <kazeburo@gmail.com>
Meta(info.upstream_url):        http://search.cpan.org/~kazeburo/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Cookie::Baker - Cookie string generator / parser

%package 512
IPS_package_name: library/perl-5/cookie-baker-512
Summary: Cookie::Baker - Cookie string generator / parser for perl-512
BuildRequires:	runtime/perl-512
# for perl ./Build test
#BuildRequires:	library/perl-5/test-time-512
Requires:	runtime/perl-512
Requires:	library/perl-5/exporter-512
Requires:	library/perl-5/uri-512

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Build.PL \
  --installdirs vendor \
  --destdir $RPM_BUILD_ROOT
/usr/perl5/5.12/bin/perl ./Build
# /usr/perl5/5.12/bin/perl ./Build test

%install
rm -rf $RPM_BUILD_ROOT

/usr/perl5/5.12/bin/perl ./Build install --destdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/man
mv $RPM_BUILD_ROOT/usr/perl5/5.12/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

rm -rf $RPM_BUILD_ROOT/usr/perl5/5.12

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(0755,root,bin) %dir %{_bindir}
#%{_bindir}/*

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Mon Jun 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
