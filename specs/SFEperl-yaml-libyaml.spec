#
# spec file for package: SFEperl-yaml-libyaml
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.38
%define tarball_name    YAML-LibYAML
%define perl_version584 5.8.4
%define perl_version512 5.12

Name:		SFEperl-yaml-libyaml
IPS_package_name: library/perl-5/yaml-libyaml
Version:	0.38
IPS_component_version: 0.38
Summary:	YAML-LibYAML
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~ingy/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{tarball_name}-%{tarball_version}.tar.gz

BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires:  %{pnm_buildrequires_perl_default}
BuildRequires:  SFElibyaml
Requires:  	%{pnm_requires_perl_default}
Requires:  	SFElibyaml

%ifarch sparc
%define perl_dir sun4-solaris-64int
%else
%define perl_dir i86pc-solaris-64int 
%endif

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Ingy dot Net <ingy@cpan.org>
Meta(info.upstream_url):        http://search.cpan.org/~ingy/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description

# %package 584
# IPS_package_name: library/perl-5/yaml-libyaml-584
# Summary:  for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/json-pp-584 # not builded yet
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/yaml-libyaml-512
Summary:  for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/json-pp-512
Requires:	runtime/perl-512


%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
# export PERL5LIB=/usr/perl5/vendor_perl/5.8.4
# /usr/perl5/5.8.4/bin/perl Makefile.PL \
#     PREFIX=$RPM_BUILD_ROOT%{_prefix} \
#     INSTALLSITELIB=$RPM_BUILD_ROOT%{_prefix}/perl5/vendor_perl/%{perl_version584} \
#     INSTALLSITEARCH=$RPM_BUILD_ROOT%{_prefix}/perl5/vendor_perl/%{perl_version584}/%{perl_dir} \
#     INSTALLSITEMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
#     INSTALLSITEMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
#     INSTALLMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
#     INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3
# make
# make test

# rm -rf $RPM_BUILD_ROOT
# make pure_install

export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL \
    PREFIX=$RPM_BUILD_ROOT%{_prefix} \
    INSTALLSITELIB=$RPM_BUILD_ROOT%{_prefix}/perl5/vendor_perl/%{perl_version512} \
    INSTALLSITEARCH=$RPM_BUILD_ROOT%{_prefix}/perl5/vendor_perl/%{perl_version512}/%{perl_dir} \
    INSTALLSITEMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    INSTALLSITEMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3 \
    INSTALLMAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
    INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3
make
make test

%install
rm -rf $RPM_BUILD_ROOT
make pure_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}

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
# %{_prefix}/perl5/vendor_perl/%{perl_version584}

%files 512
%defattr (-, root, bin)
%{_prefix}/perl5/vendor_perl/%{perl_version512}


%changelog
* Sun Dec 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- define perl_version584 and perl_version512 and use them
* Thu Jun 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for perl-512
