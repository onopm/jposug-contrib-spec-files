#
# spec file for package: SFEperl-plack
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 1.0029
%define tarball_name    Plack

Name:		SFEperl-plack
IPS_package_name: library/perl-5/plack
Version:	1.0029
IPS_component_version: 1.29
Summary:	Plack
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~miyagawa/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Plack-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Tatsuhiko Miyagawa <miyagawa@bulknews.net>
Meta(info.upstream_url):        http://search.cpan.org/~miyagawa/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Plack

# %package 584
# IPS_package_name: library/perl-5/plack-584
# Summary: Plack for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/file-sharedir-584
# BuildRequires:	library/perl-5/http-message-584
# BuildRequires:	library/perl-5/http-message-584
# BuildRequires:	library/perl-5/lwp-584
# BuildRequires:	library/perl-5/test-requires-584
# BuildRequires:	library/perl-5/test-tcp-584
# BuildRequires:	library/perl-5/uri-584
# BuildRequires:	library/perl-5/parent-584
# library/perl-5/json-pp-584 not builded yet
# BuildRequires:	library/perl-5/json-pp-584
# BuildRequires:	library/perl-5/hash-multivalue-584
# BuildRequires:	library/perl-5/devel-stacktrace-ashtml-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/plack-512
Summary: Plack for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/file-sharedir-512
BuildRequires:	library/perl-5/http-message-512
BuildRequires:	library/perl-5/lwp-512
BuildRequires:	library/perl-5/test-requires-512
BuildRequires:	library/perl-5/test-tcp-512
BuildRequires:	library/perl-5/uri-512
BuildRequires:	library/perl-5/parent-512
BuildRequires:	library/perl-5/hash-multivalue-512
BuildRequires:	library/perl-5/devel-stacktrace-512
BuildRequires:	library/perl-5/devel-stacktrace-ashtml-512
BuildRequires:  library/perl-5/stream-buffered-512
BuildRequires:  library/perl-5/file-sharedir-install-512
BuildRequires:  library/perl-5/http-tiny-512
BuildRequires:  library/perl-5/http-body-512
BuildRequires:  library/perl-5/http-cookies-512
Requires:	runtime/perl-512
Requires:	library/perl-5/test-tiny-512
Requires:	library/perl-5/http-body-512
Requires:	library/perl-5/file-sharedir-512
Requires:       library/perl-5/stream-buffered-512
Requires:       library/perl-5/hash-multivalue-512
Requires:       library/perl-5/LWP-512
Requires:	library/perl-5/devel-stacktrace-512
Requires:	library/perl-5/devel-stacktrace-ashtml-512
Requires:	library/perl-5/apache-logformat-compiler-512
Requires:       library/perl-5/http-tiny-512

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
mkdir -p $RPM_BUILD_ROOT/usr/perl5/5.12
mv $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/perl5/5.12

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
# %attr(0755,root,bin) %dir %{_bindir}
# %{_bindir}/*

# %files 584
# %defattr (-, root, bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
%{_prefix}/perl5/5.12/bin


%changelog
* Tue Dec 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Sun Oct 06 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0029
* Thu May 02 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0024
* Mon Apr 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Sun Oct 28 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0009
- add BuildRequires: library/perl-5/stream-buffered

* Thu Oct 04 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0004

* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
