#
# spec file for package: SFEperl-www-form-urlencoded-xs
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.20
%define tarball_name    WWW-Form-UrlEncoded-XS

Name:		perl-www-form-urlencoded-xs
IPS_package_name: library/perl-5/www-form-urlencoded-xs
Version:	%{tarball_version}
IPS_component_version: %{tarball_version}
Summary:	XS implementation of parser and builder for application/x-www-form-urlencoded
License:	perl_5
Url:		http://search.cpan.org/~kazeburo/%{tarball_name}-%{tarball_version}
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KAZEBURO/WWW-Form-UrlEncoded-XS-%{tarball_version}.tar.gz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

%description
XS implementation of parser and builder for application/x-www-form-urlencoded

# %package 584
# IPS_package_name: library/perl-5/www-form-urlencoded-xs-584
# Summary:  XS implementation of parser and builder for application/x-www-form-urlencoded
# BuildRequires:	runtime/perl-584
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/www-form-urlencoded-xs-512
Summary:  XS implementation of parser and builder for application/x-www-form-urlencoded
BuildRequires:	runtime/perl-512
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
* Fri Jan 30 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
