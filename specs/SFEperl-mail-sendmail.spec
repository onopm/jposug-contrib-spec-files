#
# spec file for package: SFEperl-mail-sendmail
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.79

Name:		SFEperl-mail-sendmail
IPS_package_name: library/perl-5/mail-sendmail
Version:	0.79
Summary:	Simple platform independent mailer
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~mivkovic/Mail-Sendmail-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIVKOVIC/Mail-Sendmail-0.79.tar.gz

BuildRequires:  %{pnm_buildrequires_perl_default}
Requires:  	%{pnm_requires_perl_default}

Meta(info.maintainer):          taki@justplayer.com
Meta(info.upstream):            Milivoj Ivkovic <mivkovic@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~mivkovic/Mail-Sendmail-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Simple platform independent mailer

# %package 584
# IPS_package_name: library/perl-5/mail-sendmail-584
# Summary: Simple platform independent mailer for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/json-pp-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/mail-sendmail-512
Summary: Simple platform independent mailer for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/json-pp-512
Requires:	runtime/perl-512

%prep
%setup -q -n Mail-Sendmail-%{tarball_version}

%build
# export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
# /usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
#   DESTDIR=$RPM_BUILD_ROOT \
#   LIB=/usr/perl5/vendor_perl/5.8.4
# make
# make test

# rm -rf $RPM_BUILD_ROOT
# make pure_install DESTDIR=$RPM_BUILD_ROOT

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL  PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
# make test

%install
rm -rf $RPM_BUILD_ROOT
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(755,root,sys) %dir %{_bindir}
#%{_bindir}/*

# %files 584
# %defattr (-, root, bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Tue Jan 22 2013-  TAKI,Yasushi <taki@justplayer.com>
- delete conflict files from base package.
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Fri Jun 15 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-512
