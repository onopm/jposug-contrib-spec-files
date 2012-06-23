#
# spec file for package: SFEperl-params-validate
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 1.06
%define tarball_name    Params-Validate

Name:		SFEperl-params-validate
IPS_package_name: library/perl-5/params-validate
Version:	1.06
IPS_component_version: 1.6
Summary:	Validate sub params against a spec
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~drolsky/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Params-Validate-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Dave Rolsky <autarch@urth.org>
Meta(info.upstream_url):        http://search.cpan.org/~drolsky/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Validate sub params against a spec

# %package 584
# IPS_package_name: library/perl-5/params-validate-584
# Summary: Validate sub params against a spec for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/module-build-584
# BuildRequires:	library/perl-5/module-implementation-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/params-validate-512
Summary: Validate sub params against a spec for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/module-build-512
BuildRequires:	library/perl-5/module-implementation-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
# export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
# /usr/perl5/5.8.4/bin/perl Build.PL \
#   --installdirs vendor \
#   --destdir $RPM_BUILD_ROOT
# /usr/perl5/5.8.4/bin/perl ./Build
# /usr/perl5/5.8.4/bin/perl ./Build test

# rm -rf $RPM_BUILD_ROOT
# /usr/perl5/5.8.4/bin/perl ./Build install --destdir $RPM_BUILD_ROOT
# /usr/perl5/5.8.4/bin/perl ./Build clean

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Build.PL \
  --installdirs vendor \
  --destdir $RPM_BUILD_ROOT
/usr/perl5/5.12/bin/perl ./Build
/usr/perl5/5.12/bin/perl ./Build test

%install
rm -rf $RPM_BUILD_ROOT
/usr/perl5/5.12/bin/perl ./Build install --destdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}
# mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/perl5/5.12/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

rm -rf $RPM_BUILD_ROOT%{_prefix}/perl5/5.12

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
