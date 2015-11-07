#
# spec file for package: SFEperl-test-tcp
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define tarball_version 2.02
%define tarball_name    Test-TCP

Name:		SFEperl-test-tcp
IPS_package_name: library/perl-5/test-tcp
Version:	2.02
IPS_component_version: 2.2
Summary:	Test-TCP
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~tokuhirom/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOKUHIROM/Test-TCP-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Tokuhiro Matsuno <tokuhirom+cpan@gmail.com>
Meta(info.upstream_url):        http://search.cpan.org/~tokuhirom/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Test-TCP

# %package 584
# IPS_package_name: library/perl-5/test-tcp-584
# Summary: Test-TCP for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/test-sharedfork-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/test-tcp-512
Summary: Test-TCP for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/test-sharedfork-512
BuildRequires:	library/perl-5/cpan-meta-512
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
# /usr/perl5/5.8.4/bin/perl ./Build install clean

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Build.PL \
  --installdirs vendor \
  --destdir $RPM_BUILD_ROOT
/usr/perl5/5.12/bin/perl ./Build
/usr/perl5/5.12/bin/perl ./Build test

%install
rm -rf $RPM_BUILD_ROOT

/usr/perl5/5.12/bin/perl ./Build install --destdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/man
# rm -rf $RPM_BUILD_ROOT/usr/perl5/5.8.4/man
mv $RPM_BUILD_ROOT/usr/perl5/5.12/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

# rm -rf $RPM_BUILD_ROOT/usr/perl5/5.8.4
rm -rf $RPM_BUILD_ROOT/usr/perl5/5.12


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
* Tue Dec 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Thu Nov 13 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.02
- not generate package for perl-584
* Sun Oct 28 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 1.18
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
