#
# spec file for package: SFEperl-digest-sha
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 1
%include base.inc

%define tarball_version 5.92
%define tarball_name    Digest-SHA
Name:		SFEperl-digest-sha
IPS_package_name: library/perl-5/digest-sha
Version:	5.92
IPS_component_version: 5.92
Summary:	Digest::SHA - Perl extension for SHA-1/224/256/384/512
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~rhandom/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:        http://search.cpan.org/CPAN/authors/id/M/MS/MSHELOR/%{tarball_name}-%{tarball_version}.tar.gz

%include default-depend.inc
%include perl-depend.inc

%description
Digest::SHA is written in C for speed. If your platform lacks a C compiler,
you can install the functionally equivalent (but much slower)
Digest::SHA::PurePerl module.
The programming interface is easy to use: it's the same one found in CPAN's
Digest module. So, if your applications currently use Digest::MD5 and you'd
prefer the stronger security of SHA, it's a simple matter to convert them.

%package 510 
IPS_package_name: library/perl-5/digest-sha-510
Summary: Digest::SHA - Perl extension for SHA-1/224/256/384/512 for perl-510
BuildRequires:	runtime/perl-510
Requires:	runtime/perl-510
Requires:	library/perl-5/digest-sha

%prep
%setup -q -n %{tarball_name}-%{tarball_version}
cat <<EOT >rewrite.sh
#!/bin/bash
find . -name 'Makefile' -exec sed -i -e 's/-xO3/-O3/' -e 's/-xspace//' -e 's/-xildoff//' -e 's/-KPIC/-fPIC/' -e 's/CC = cc/CC = gcc/' {} \;
EOT
chmod 775 rewrite.sh

%build
rm -rf $RPM_BUILD_ROOT

export PERL5LIB=/usr/perl5/vendor_perl/5.10.0
/usr/perl5/5.10.0/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.10.0
./rewrite.sh
make
make test

make pure_install
make clean

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%attr(0755,root,sys) %dir %{_datadir}
%{_mandir}
%{_bindir}

%files 510
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/5.10.0

%changelog
* Jul 21 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial commit
