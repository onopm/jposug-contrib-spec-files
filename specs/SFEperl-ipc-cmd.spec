#
# spec file for package: SFEperl-ipc-cmd
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# includes module(s):
#
%include Solaris.inc
%include packagenamemacros.inc

%define tarball_version 0.86
%define tarball_name    IPC-Cmd

Name:		SFEperl-ipc-cmd
IPS_package_name: library/perl-5/ipc-cmd
Version:	0.86
IPS_component_version: 0.86
Summary:	IPC::Cmd - finding and running system commands made easy
License:	Artistic
Distribution:   OpenSolaris
Vendor:         OpenSolaris Community
Url:		http://search.cpan.org/~bingos/%{tarball_name}-%{tarball_version}
SUNW_Basedir:	%{_basedir}
SUNW_Copyright: %{name}.copyright
Source0:	http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/IPC-Cmd-%{tarball_version}.tar.gz

# BuildRequires:	runtime/perl-584
BuildRequires:	runtime/perl-512

Meta(info.maintainer):          roboporter by pkglabo.justplayer.com <pkgadmin@justplayer.com>
Meta(info.upstream):            Chris Williams <chris@bingosnet.co.uk>
Meta(info.upstream_url):        http://search.cpan.org/~bingos/%{tarball_name}-%{tarball_version}
Meta(info.classification):	org.opensolaris.category.2008:Development/Perl

%description
IPC::Cmd - finding and running system commands made easy

# %package 584
# IPS_package_name: library/perl-5/ipc-cmd-584
# Summary: IPC::Cmd - finding and running system commands made easy for perl-584
# BuildRequires:	runtime/perl-584
# BuildRequires:	library/perl-5/params-check-584 # not builded yet
# Requires:	runtime/perl-584

%package 512
IPS_package_name: library/perl-5/ipc-cmd-512
Summary: IPC::Cmd - finding and running system commands made easy for perl-512
BuildRequires:	runtime/perl-512
BuildRequires:	library/perl-5/params-check-512
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
# make clean

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
* Thu Nov 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.86