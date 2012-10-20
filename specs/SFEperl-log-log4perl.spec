#
# spec file for package: SFEperl-log-log4perl
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 1.36
%define tarball_name    Log-Log4perl

Name:		SFEperl-log-log4perl
IPS_package_name: library/perl-5/log-log4perl
Version:	1.36
IPS_component_version: 1.36
Summary:	Log4j implementation in Perl
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~mschilli/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Log-Log4perl-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Michael Schilli <m@perlmeister.com>
Meta(info.upstream_url):        http://search.cpan.org/~mschilli/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Log4j implementation in Perl

%package 584
IPS_package_name: library/perl-5/log-log4perl-584
Summary: Log4j implementation in Perl for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/log-log4perl-512
Summary: Log4j implementation in Perl for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
make test

rm -rf $RPM_BUILD_ROOT
make pure_install
make clean

mkdir -p $RPM_BUILD_ROOT%{_prefix}/perl5/5.8.4
mv $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT%{_prefix}/perl5/5.8.4


export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test

%install
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
%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}
# %attr(755,root,bin) %dir %{_bindir}
#%attr (555, root, bin) %{_bindir}/l4p-tmpl

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4
%{_prefix}/perl5/5.8.4/bin

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
%{_prefix}/perl5/5.12/bin

%changelog
* Sun Jun 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
* Sun May 06 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Requires
* Sat Apr 28 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
