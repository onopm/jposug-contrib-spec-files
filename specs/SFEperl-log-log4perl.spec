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

BuildRequires:	SUNWperl584core
BuildRequires:	SUNWperl584usr
Requires:	SUNWperl584core
Requires:	SUNWperl584usr

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Michael Schilli <m@perlmeister.com>
Meta(info.upstream_url):        http://search.cpan.org/~mschilli/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Log4j implementation in Perl
%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
make

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

%{_prefix}/perl5
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}
%attr(755,root,bin) %dir %{_bindir}
%attr (555, root, bin) %{_bindir}/l4p-tmpl
%changelog
