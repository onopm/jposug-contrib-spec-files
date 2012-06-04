#
# spec file for package: SFEperl-digest-sha
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 5.71
%define tarball_name    Digest-SHA

Name:		SFEperl-digest-sha
IPS_package_name: library/perl-5/digest-sha
Version:	5.71
IPS_component_version: 5.71
Summary:	Perl extension for SHA-1/224/256/384/512
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~mshelor/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSHELOR/Digest-SHA-%{tarball_version}.tar.gz

BuildRequires:  runtime/perl-584
BuildRequires:  runtime/perl-512

Meta(info.upstream):            Mark Shelor <mshelor@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~mshelor/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Perl extension for SHA-1/224/256/384/512
%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%package 584
IPS_package_name: library/perl-5/digest-sha-584
Summary: Module signature file manipulation for perl-584
Requires: perl-584
Requires: library/perl-5/digest-sha

%package 512
IPS_package_name: library/perl-5/digest-sha-512
Summary: Module signature file manipulation for perl-512
Requires: perl-512
Requires: library/perl-5/digest-sha

%build
/usr/perl5/5.8.4/bin/perl Makefile.PL \
    PREFIX=%{_prefix} \
    DESTDIR=$RPM_BUILD_ROOT \
    LIB=/usr/perl5/vendor_perl/5.8.4
make
make test
rm -rf $RPM_BUILD_ROOT
make pure_install

/usr/perl5/5.12/bin/perl Makefile.PL \
    PREFIX=%{_prefix}\
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
%defattr (-, root, bin)
%defattr(-,root,bin)
/usr/bin/shasum
%attr(755,root,sys) %dir %{_datadir}
%{_mandir}

%files 584
%defattr (-, root, bin)
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Mon 04 Jun 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit