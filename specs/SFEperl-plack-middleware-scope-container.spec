#
# spec file for package: SFEperl-plack-middleware-scope-container
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.02
%define tarball_name    Plack-Middleware-Scope-Container

Name:		SFEperl-plack-mw-scp-cntnr
IPS_package_name: library/perl-5/plack-middleware-scope-container
Version:	0.02
IPS_component_version: 0.2
Summary:	Plack::Middleware::Scope::Container
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kazeburo/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: SFEperl-plack-middleware-scope-container.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KAZEBURO/Plack-Middleware-Scope-Container-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Masahiro Nagano <kazeburo@gmail.com>
Meta(info.upstream_url):        http://search.cpan.org/~kazeburo/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Plack::Middleware::Scope::Container

# %package 584
# IPS_package_name: library/perl-5/plack-middleware-scope-container-584
# Summary: Plack::Middleware::Scope::Container for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/plack-584
# BuildRequires:	library/perl-5/scope-container-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/plack-middleware-scope-container-512
Summary: Plack::Middleware::Scope::Container for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/plack-512
BuildRequires:	library/perl-5/scope-container-512
Requires:	runtime/perl-512


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
#%attr(0755,root,bin) %dir %{_bindir}
#%{_bindir}/*

# %files 584
# %defattr (-, root, bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Sat Jun 23 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
