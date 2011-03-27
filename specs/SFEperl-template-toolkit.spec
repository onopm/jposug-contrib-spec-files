#
# spec file for package: perl-Template-Toolkit
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

Name:		SFEperl-template-toolkit
IPS_package_name: library/perl-5/template-toolkit
Version:	2.22
Summary:	Extensive Toolkit for template processing
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~abw/Template-%{version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/A/AB/ABW/Template-Toolkit-%{version}.tar.gz

BuildRequires:	SUNWperl584core
BuildRequires:	SUNWperl584usr
Requires:	SUNWperl584core
Requires:	SUNWperl584usr

Meta(info.maintainer):          pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Andy Wardley <cpan@wardley.org>
Meta(info.upstream_url):        http://search.cpan.org/~abw/Template-%{version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Extensive Toolkit for template processing
%prep
%setup -q -n Template-Toolkit-%{version}

%build
perl Makefile.PL PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT LIB=/usr/perl5/vendor_perl/5.8.4
make

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
%{_prefix}/perl5
%dir %attr(0755, root, sys) %{_datadir}
%{_mandir}
%dir %attr(0755,root, bin) %{_bindir}
%{_bindir}/*

%changelog
