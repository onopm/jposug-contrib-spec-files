#
# spec file for package: SFEperl-archive-zip
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 1.46
%define tarball_name    Archive-Zip

Name:		SFEperl-archive-zip
IPS_package_name: library/perl-5/archive-zip
Version:	%{tarball_version}
IPS_component_version: %{tarball_version}
Summary:	Provides an interface to ZIP archive files
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~adamk/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
#Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Archive-Zip-%{tarball_version}.tar.gz
Source0:	http://cpan.metacpan.org/authors/id/P/PH/PHRED/Archive-Zip-%{tarball_version}.tar.gz

#BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.upstream):            Adam Kennedy <adamk@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~adamk/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Provides an interface to ZIP archive files

# %package 584
# IPS_package_name: library/perl-5/archive-zip-584
# Summary: Provides an interface to ZIP archive files for perl-584
# BuildRequires:  runtime/perl-584
# BuildRequires:  library/perl-5/compress-raw-zlib-584
# Requires:       runtime/perl-584
# Requires:       library/perl-5/compress-raw-zlib-584

%package 512
IPS_package_name: library/perl-5/archive-zip-512
Summary: Provides an interface to ZIP archive files for perl-512
BuildRequires:  runtime/perl-512
BuildRequires:  library/perl-5/compress-raw-zlib-512
Requires:       runtime/perl-512
Requires:       library/perl-5/compress-raw-zlib-512

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
# /usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
# make
# make test
# rm -rf $RPM_BUILD_ROOT
# make pure_install

/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.12
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
# %attr(0755,root,bin) %dir %{_bindir}
%{_bindir}/crc32

# %files 584
# %defattr(-,root,bin)
# %{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.12



%changelog
* Tue Jun 05 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.46 and stop to generate package for perl-584
* Tue Jun 05 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
