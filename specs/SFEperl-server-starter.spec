#
# spec file for package: SFEperl-server-starter
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.11
%define tarball_name    Server-Starter

Name:		SFEperl-server-starter
IPS_package_name: library/perl-5/server-starter
Version:	0.11
IPS_component_version: 0.11
Summary:	Server-Starter
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kazuho/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KAZUHO/Server-Starter-%{tarball_version}.tar.gz

#BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Kazuho Oku <kazuhooku@gmail.com>
Meta(info.upstream_url):        http://search.cpan.org/~kazuho/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Server-Starter

# %package 584
# IPS_package_name: library/perl-5/server-starter-584
# Summary: Server-Starter for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/test-tcp-584
# BuildRequires:	library/perl-5/proc-wait3-584
# BuildRequires:	library/perl-5/scope-guard-584
# library/perl-5/list-moreutils-584 not builded yet
# BuildRequires:	library/perl-5/list-moreutils-584
# Requires:	runtime/perl-584
# Requires:	library/perl-5/server-starter

%package 512
IPS_package_name: library/perl-5/server-starter-512
Summary: Server-Starter for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/test-tcp-512
BuildRequires:	library/perl-5/proc-wait3-512
BuildRequires:	library/perl-5/scope-guard-512
BuildRequires:	library/perl-5/list-moreutils-512
Requires:	runtime/perl-512
Requires:	library/perl-5/server-starter

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

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
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
%attr(0755,root,bin) %dir %{_bindir}
%{_bindir}/*

# %files 584
# %defattr (-, root, bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
