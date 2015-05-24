#
# spec file for package: SFEperl-path-class
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc

%define build584 0
%define build512 1

%define tarball_version 0.35
%define tarball_name    Path-Class

Name:		SFEperl-path-class
IPS_package_name: library/perl-5/path-class
Version:	%{tarball_version}
IPS_component_version: %{tarball_version}
Summary:	Path::Class
License:	perl_5
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Path-Class-%{tarball_version}.tar.gz

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Ken Williams <kwilliams@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~kwilliams/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
Path::Class

%if %{build584}
%package 584
IPS_package_name: library/perl-5/path-class-584
Summary: Path::Class for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/path-class-512
Summary: Path::Class for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512
%endif

%prep
if [ -d $RPM_BUILD_ROOT ]
then
    rm -rf $RPM_BUILD_ROOT
fi

%setup -q -n %{tarball_name}-%{tarball_version}

%build
%if %{build584}
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
make test
make pure_install
%endif

%if %{build512}
export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
make test
make pure_install
%endif

%install
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
#%attr(0755,root,bin) %dir %{_bindir}
#%{_bindir}/*

%if %{build584}
%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4
%endif

%if %{build512}
%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12
%endif

%changelog
* Sun May 25 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.35 and stop to generate package for perl-584
* Sun Jun 10 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
