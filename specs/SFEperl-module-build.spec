#
# spec file for package: SFEperl-module-build
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 0.40
%define tarball_name    Module-Build

Name:		SFEperl-module-build
IPS_package_name: library/perl-5/module-build
Version:	0.40
IPS_component_version: 0.40
Summary:	Build, test, and install Perl modules
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/Module-Build-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512
# BuildRequires:	library/perl-5/perl-ostype

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Ken Williams <kwilliams@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Build, test, and install Perl modules

%package 584
IPS_package_name: library/perl-5/module-build-584
Summary: Build, test, and install Perl modules for perl-584
BuildRequires:	runtime/perl-584
BuildRequires:	library/perl-5/extutils-install-584
# BuildRequires:	library/perl-5/extutils-cbuilder-584
# BuildRequires:	library/perl-5/exttuils-parsexs-584
# BuildRequires:	library/perl-5/extutils-manifest-584
# BuildRequires:	library/perl-5/file-temp-584
# BuildRequires:	library/perl-5/archive-tar-584
# BuildRequires:	library/perl-5/pod-readme-584
BuildRequires:	library/perl-5/perl-ostype-584
BuildRequires:	library/perl-5/module-metadata-584
Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/module-build-512
Summary: Build, test, and install Perl modules for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/extutils-install-512
BuildRequires:	library/perl-5/perl-ostype-512
BuildRequires:	library/perl-5/module-metadata-512
Requires:	runtime/perl-512

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4

/usr/perl5/5.8.4/bin/perl Build.PL \
  --installdirs vendor \
  --destdir $RPM_BUILD_ROOT
/usr/perl5/5.8.4/bin/perl ./Build
# /usr/perl5/5.8.4/bin/perl ./Build test

rm -rf $RPM_BUILD_ROOT
/usr/perl5/5.8.4/bin/perl ./Build install --destdir $RPM_BUILD_ROOT
/usr/perl5/5.8.4/bin/perl ./Build install clean

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Build.PL \
  --installdirs vendor \
  --destdir $RPM_BUILD_ROOT
/usr/perl5/5.12/bin/perl ./Build
# /usr/perl5/5.12/bin/perl ./Build test

%install
/usr/perl5/5.12/bin/perl ./Build install --destdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/man
rm -rf $RPM_BUILD_ROOT/usr/perl5/5.8.4/man
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
#%attr(755,root,sys) %dir %{_bindir}
#%{_bindir}/*

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4
%attr(755,root,bin) %dir /usr/perl5/5.8.4/bin
/usr/perl5/5.8.4/bin/*

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
# %attr(755,root,bin) %dir /usr/perl5/5.12/bin
# /usr/perl5/5.12/bin/*

%changelog
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Tue Jun 19 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-584
* Wed Jun 13 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- exclude executable files whitch conflict with perl-512
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify %attr
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use Build.PL instead of Makefile.PL
- stop to generate package for perl-584
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
