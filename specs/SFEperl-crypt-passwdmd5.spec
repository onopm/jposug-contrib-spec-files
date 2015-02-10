#
# spec file for package: SFEperl-crypt-passwdmd5
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 1.40
%define tarball_name    Crypt-PasswdMD5

Name:			SFEperl-crypt-passwdmd5
IPS_package_name:	library/perl-5/crypt-passwdmd5
Version:		1.40
IPS_component_version:	1.40
Summary:		Interoperable MD5-based crypt() function
License:		perl_5
Url:		http://search.cpan.org/~luismunoz/%{tarball_name}-%{tarball_version}
Source0:	http://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Crypt-PasswdMD5-%{tarball_version}.tgz

BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

%description
Interoperable MD5-based crypt() function

%package 584
IPS_package_name: library/perl-5/crypt-passwdmd5-584
Summary: Interoperable MD5-based crypt() function for perl-584
BuildRequires:	runtime/perl-584
Requires:	runtime/perl-584
Requires:	library/perl-5/digest-md5-584

%package 512
IPS_package_name: library/perl-5/crypt-passwdmd5-512
Summary: Interoperable MD5-based crypt() function for perl-512
BuildRequires:	runtime/perl-512
Requires:	runtime/perl-512
Requires:	library/perl-5/digest-md5-512

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
/usr/perl5/5.8.4/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.8.4
make
make test

rm -rf $RPM_BUILD_ROOT
make pure_install
make clean

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
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
%defattr(-,root,bin)
#%{_prefix}/perl5
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
#%attr(0755,root,bin) %dir %{_bindir}
#%{_bindir}/*

%files 584
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Wed Feb 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
