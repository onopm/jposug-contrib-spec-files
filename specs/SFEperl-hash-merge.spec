#
# spec file for package: SFEperl-net-snmp
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.200
%define tarball_name    Hash-Merge

Name:			SFEperl-hash-merge
IPS_package_name:	library/perl-5/hash-merge
Version:		0.200
IPS_component_version:	0.200
Summary:		Hash::Merge - Merges arbitrarily deep hashes into a single hash
License:		Perl_5
Distribution:   	OpenSolaris
Vendor:         	OpenSolaris Community
Url:			http://search.cpan.org/~dtown/%{tarball_name}-%{tarball_version}
SUNW_Basedir:		%{_basedir}
# SUNW_Copyright:	%{name}.copyright
Source0:		http://cpan.metacpan.org/authors/id/R/RE/REHSACK/Hash-Merge-%{version}.tar.gz

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Jens Rehsack <rehsack@cpan.org>
Meta(info.upstream_url):        https://metacpan.org/pod/Hash::Merge
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Hash::Merge - Merges arbitrarily deep hashes into a single hash

%package 584
IPS_package_name:	library/perl-5/hash-merge-584
Summary: 		Hash::Merge - Merges arbitrarily deep hashes into a single hash
BuildRequires:		runtime/perl-584
Requires:		runtime/perl-584
Requires:		library/perl-5/clone-584

%package 512
IPS_package_name:	library/perl-5/hash-merge-512
Summary: 		Hash::Merge - Merges arbitrarily deep hashes into a single hash
BuildRequires:		runtime/perl-512
Requires:		runtime/perl-512
Requires:		library/perl-5/clone-512

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Wed Jul 16 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
