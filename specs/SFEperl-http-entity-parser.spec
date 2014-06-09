#
# spec file for package: SFEperl-http-entity-parser
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.12
%define tarball_name    HTTP-Entity-Parser

Name:		SFEperl-http-entity-parser
IPS_package_name: library/perl-5/http-entity-parser
Version:	0.12
IPS_component_version: 0.12
Summary:	HTTP::Entity::Parser - PSGI compliant HTTP Entity Parser
License:	Perl
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kazeburo/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/HTTP-Entity-Parser-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Masahiro Nagano <kazeburo@gmail.com>
Meta(info.upstream_url):        http://search.cpan.org/~kazeburo/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
HTTP::Entity::Parser - PSGI compliant HTTP Entity Parser

%package 512
IPS_package_name: library/perl-5/http-entity-parser-512
Summary: HTTP::Entity::Parser - PSGI compliant HTTP Entity Parser for perl-512
BuildRequires:	runtime/perl-512
# required for test
BuildRequires:	library/perl-5/www-form-urlencoded-512
BuildRequires:	library/perl-5/http-multipartparser-512
Requires:	runtime/perl-512
Requires:	library/perl-5/encode-512
Requires:	library/perl-5/file-temp-512
Requires:	library/perl-5/module-load-512
Requires:	library/perl-5/json-512
Requires:	library/perl-5/stream-buffered-512
Requires:	library/perl-5/www-form-urlencoded-512
Requires:	library/perl-5/http-multipartparser-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Build.PL \
  --installdirs vendor \
  --destdir $RPM_BUILD_ROOT
/usr/perl5/5.12/bin/perl ./Build
/usr/perl5/5.12/bin/perl ./Build test

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
