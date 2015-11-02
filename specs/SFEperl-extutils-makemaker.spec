#
# spec file for package: SFEperl-extutils-makemaker
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 6.64
%define tarball_name    ExtUtils-MakeMaker

Name:		SFEperl-extutils-makemaker
IPS_package_name: library/perl-5/extutils-makemaker
Version:	6.64
IPS_component_version: 6.64
Summary:	Writes Makefiles for extensions
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~mschwern/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/ExtUtils-MakeMaker-%{tarball_version}.tar.gz
# Source0:	http://cpan.metacpan.org/authors/id/B/BI/BINGOS/ExtUtils-MakeMaker-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Michael G Schwern <mschwern@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~mschwern/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Writes Makefiles for extensions

%package 584
IPS_package_name: library/perl-5/extutils-makemaker-584
Summary: Writes Makefiles for extensions for perl-584
BuildRequires:	runtime/perl-584
BuildRequires:	library/perl-5/extutils-install-584
BuildRequires:	library/perl-5/parse-cpan-meta-584
BuildRequires:  library/perl-5/version-584
Requires:	runtime/perl-584
Requires:	library/perl-5/extutils-makemaker
Requires:	library/perl-5/extutils-install-584
Requires:	library/perl-5/parse-cpan-meta-584
#Requires:	library/perl-5/extutils-manifest-584
Requires:       library/perl-5/version-584

%package 512
IPS_package_name: library/perl-5/extutils-makemaker-512
Summary: Writes Makefiles for extensions for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/extutils-install-512
BuildRequires:	library/perl-5/parse-cpan-meta-512
#BuildRequires:	library/perl-5/extutils-manifest-512
BuildRequires:  library/perl-5/version-512
Requires:	runtime/perl-512
Requires:	library/perl-5/extutils-makemaker
Requires:	library/perl-5/extutils-install-512
Requires:	library/perl-5/parse-cpan-meta-512
#Requires:	library/perl-5/extutils-manifest-512
Requires:       library/perl-5/version-512

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
#make test

rm -rf $RPM_BUILD_ROOT
make pure_install

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
#make test


%install
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

# to avoid confilict with SFEperl-extutils-manifest
# usr/perl5/vendor_perl/5.84/ExtUtils/MANIFEST.SKIP
# usr/perl5/vendor_perl/5.12/ExtUtils/MANIFEST.SKIP
# usr/perl5/vendor_perl/5.12/ExtUtils/Manifest.pm

if [ -f $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/ExtUtils/Manifest.pm ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/ExtUtils/Manifest.pm
fi
if [ -f $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/ExtUtils/MANIFEST.SKIP ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/ExtUtils/MANIFEST.SKIP
fi
if [ -f $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/ExtUtils/Manifest.pm ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/ExtUtils/Manifest.pm
fi
if [ -f $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/ExtUtils/MANIFEST.SKIP ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/ExtUtils/MANIFEST.SKIP
fi
if [ -f $RPM_BUILD_ROOT/usr/share/man/man3perl/ExtUtils::Manifest.3 ]
then
    rm -rf $RPM_BUILD_ROOT/usr/share/man/man3perl/ExtUtils::Manifest.3
fi

# to avoid confilict with SFEperl-file-copy-recursive
if [ -d $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/File/Copy ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/File/Copy
fi
if [ -d $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/File/Copy ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/File/Copy
fi
if [ -f $RPM_BUILD_ROOT%{_datadir}/man/man3perl/File::Copy::Recursive.3 ]
then
    rm -f $RPM_BUILD_ROOT%{_datadir}/man/man3perl/File::Copy::Recursive.3
fi

# to avoid confilict with SFEperl-cpan-meta
if [ -d $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/CPAN ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/CPAN
fi
if [ -d $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/CPAN ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/CPAN
fi
if [ -f $RPM_BUILD_ROOT%{_datadir}/man/man3perl/CPAN::Meta.3 ]
then
    rm -rf $RPM_BUILD_ROOT%{_datadir}/man/man3perl/CPAN::Meta*
fi

# to avoid confilict with SFEperl-json-pp
if [ -f $RPM_BUILD_ROOT/usr/share/man/man3perl/JSON::PP.3 ]
then
    rm -rf $RPM_BUILD_ROOT/usr/share/man/man3perl/JSON::PP.3
fi
if [ -f $RPM_BUILD_ROOT/usr/share/man/man3perl/Parse::CPAN::Meta.3 ]
then
    rm -rf $RPM_BUILD_ROOT/usr/share/man/man3perl/Parse::CPAN::Meta.3
fi
if [ -f $RPM_BUILD_ROOT/usr/share/man/man3perl/JSON::PP::Boolean.3 ]
then
    rm -rf $RPM_BUILD_ROOT/usr/share/man/man3perl/JSON::PP::Boolean.3
fi

# to avoid confilict with SFEperl-file-temp
if [ -f $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/File/Temp.pm ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.8.4/File/Temp.pm
fi
if [ -f $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/File/Temp.pm ]
then
    rm -rf $RPM_BUILD_ROOT/usr/perl5/vendor_perl/5.12/File/Temp.pm
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(755,root,sys) %dir %{_bindir}
%{_bindir}/*

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Mon Nov 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.64
* Thu Nov 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete man to avoid conflict
- add Requires and BuildRequires
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete some files to avoid confilict with SFEperl-cpan-meta
* Tue Jan 22 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- delete Manifest.pm to avoid conflit with SFEperl-extutils-manifest
- delete some files which conflict with SFEperl-file-copy-recursive
* Mon Jan 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix %attr
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add library/perl-5/parse-cpan-meta to BuildRequire
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires and BuildRequires
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires to avoid confilict with file-copy-recursive
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires library/perl-5/extutils-install
- export PERL5LIB to adjust @inc
* Sat Jun 09 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
