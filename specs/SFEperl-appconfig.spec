#
# spec file for package: SFEperl-appconfig
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

Name:		SFEperl-appconfig
IPS_package_name: library/perl-5/appconfig
Version:	1.66
Summary:	Application config (from ARGV, file, ...)
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~abw/AppConfig-%{version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/A/AB/ABW/AppConfig-%{version}.tar.gz
BuildRequires:  %{pnm_buildrequires_perl_default}
Requires:  	%{pnm_requires_perl_default}


Meta(info.maintainer):          taki@justplayer.com
Meta(info.upstream):            Andy Wardley <cpan@wardley.org>
Meta(info.upstream_url):        http://search.cpan.org/~abw/AppConfig-%{version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Application config (from ARGV, file, ...)

# %package 584
# IPS_package_name: library/perl-5/appconfig-584
# Summary: Application config (from ARGV, file, ...) for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/json-pp-584 # not builded yet
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/appconfig-512
Summary: Application config (from ARGV, file, ...) for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/json-pp-512
Requires:	runtime/perl-512

%prep
%setup -q -n AppConfig-%{version}

%build
# export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
# /usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
#   DESTDIR=$RPM_BUILD_ROOT \
#   LIB=/usr/perl5/vendor_perl/5.8.4
# make
# make test

# rm -rf $RPM_BUILD_ROOT
# make pure_install

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test

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
%dir %{_prefix}/perl5
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
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Wed Jun 16 2013 - TAKI, Yasushi <taki@justplayer.com>
- fix install problems because of conflict package files.
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-512
- add make test
* Wed Jun 13 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
