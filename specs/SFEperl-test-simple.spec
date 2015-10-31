#
# spec file for package: perl-Test-Simple
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

Name:		SFEperl-test-simple
IPS_package_name: library/perl-5/test-simple
Version:	1.001014
IPS_component_version: 1.1014
Summary:	Basic utilities for writing tests
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~mschwern/Test-Simple-%{version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/E/EX/EXODIST/Test-Simple-%{version}.tar.gz

BuildRequires:  %{pnm_buildrequires_perl_default}
Requires:  	%{pnm_requires_perl_default}

%description
Basic utilities for writing tests

%package 584
IPS_package_name: library/perl-5/test-simple-584
Summary: Basic utilities for writing tests
Requires: perl-584

%package 512
IPS_package_name: library/perl-5/test-simple-512
Summary: Basic utilities for writing tests
Requires: perl-512


%prep
%setup -q -n Test-Simple-%{version}

%build
/usr/perl5/5.8.4/bin/perl Makefile.PL \
    PREFIX=%{_prefix} \
    DESTDIR=$RPM_BUILD_ROOT \
    LIB=/usr/perl5/vendor_perl/5.8.4
make
make test
rm -rf $RPM_BUILD_ROOT
make pure_install

/usr/perl5/5.12/bin/perl Makefile.PL \
    PREFIX=%{_prefix}\
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
%dir %attr(0755, root, sys) /usr/share
%{_mandir}

%files 584
%defattr (-, root, bin)
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.8.4

%files 512
%defattr (-, root, bin)
%defattr(-,root,bin)
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Sun Nov 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.001014
* Wed Nov 19 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.001009
* Mon 04 Jun 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify %files to avoid file conflict.

* Mon 04 Jun 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.98

* Mon 04 Jun 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
