#
# spec file for package: SFEperl-extutils-parsexs
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 3.22
%define tarball_name    ExtUtils-ParseXS

Name:		SFEperl-extutils-parsexs
IPS_package_name: library/perl-5/extutils-parsexs
Version:	3.22
IPS_component_version: 3.22
Summary:	Converts Perl XS code into C code
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/ExtUtils-ParseXS-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Ken Williams <kwilliams@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Converts Perl XS code into C code

# %package 584
# IPS_package_name: library/perl-5/extutils-parsexs-584
# Summary: Converts Perl XS code into C code for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/json-pp-584
# # BuildRequires:	library/perl-5/extutils-cbuilder-584
# Requires:	runtime/perl-584
# Requires:	%{IPS_package_name}

%package 512
IPS_package_name: library/perl-5/extutils-parsexs-512
Summary: Converts Perl XS code into C code for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/json-pp-512
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
mkdir -p $RPM_BUILD_ROOT/usr/perl5/5.12
mv $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT/usr/perl5/5.12

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
# %attr(0755,root,bin) %dir /usr/perl5/5.8.4/bin
# /usr/perl5/5.8.4/bin/*

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
%attr(0755,root,bin) %dir /usr/perl5/5.12/bin
/usr/perl5/5.12/bin/*

%changelog
* Tue Nov 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.22
* Tue Feb 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequire to %package 584
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
