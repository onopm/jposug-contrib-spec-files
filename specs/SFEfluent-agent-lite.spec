%include Solaris.inc
%include packagenamemacros.inc

%define name fluent-agent-lite
%define version 0.6
%define prefix /usr
%define build_perl_path /usr/perl5/5.12/bin/perl

%define _use_internal_dependency_generator 0

# %global debug_package %{nil}

Name:           SFEfluent-agent-lite
IPS_package_name: system/fluentd/fluent-agent-lite
Version:        %{version}
Release:        original
Summary:        Log transfer agent service over fluentd protocol

Group:          Applications/System
License:        Apache Software License v2
URL:            https://github.com/tagomoris/fluent-agent-lite
Source0:        https://github.com/tagomoris/fluent-agent-lite/archive/v%{version}.tar.gz
# Source1:        fluent-agent-lite.conf
# Source2:        fluent-agent.servers.primary
# Source3:        fluent-agent.servers.secondary
BuildRoot:       %{_tmppath}/%{name}-%{version}-build
BuildRequires:  runtime/perl-512

# ExclusiveArch:  x86_64
# AutoReq:        no

%package 512
IPS_package_name: system/fluentd/fluent-agent-lite-512
Summary:          Log transfer agent service over fluentd protocol
BuildRequires:    runtime/perl-512
Requires:         runtime/perl-512
Requires:         system/fluentd/fluent-agent-lite
Requires:         library/perl-5/log-minimal-512
Requires:         library/perl-5/json-xs-512
Requires:         library/perl-5/data-messagepack-512

%description
Log transfer agent service over fluentd protocol.

%prep
%setup -n fluent-agent-lite-%{version}

%build
export PERL5LIB=/usr/perl5/vendor_perl/5.12
/usr/perl5/5.12/bin/perl Makefile.PL PREFIX=%{_prefix} \
  DESTDIR=$RPM_BUILD_ROOT \
  LIB=/usr/perl5/vendor_perl/5.12
make
# make test

%install
rm -rf $RPM_BUILD_ROOT
make pure_install
# mkdir -p $RPM_BUILD_ROOT%{_datadir}
# mv $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_datadir}
# mv $RPM_BUILD_ROOT%{_datadir}/man/man3 $RPM_BUILD_ROOT%{_datadir}/man/man3perl
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp bin/fluent-agent-lite $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
# %config(noreplace) %{_sysconfdir}/fluent-agent-lite.conf
# %config %{_sysconfdir}/fluent-agent.servers.primary
# %config %{_sysconfdir}/fluent-agent.servers.secondary
# %{_sysconfdir}/init.d/fluent-agent-lite
# %attr(0755,root,sys) %dir %{_datadir}
# %{_mandir}
%attr(0755,root,bin) %dir %{_bindir}
%{_bindir}/*


%files 512
%defattr (-, root, bin)
%attr(0755, root, sys) %dir %{_prefix}
%{_prefix}/perl5/vendor_perl/5.12

%changelog
* Mon Feb 04 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add Requires
* Sun Feb 03 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- modify %setup, %install and %files
- fix %attr
- add /usr/bin/fluent-agent-lite to %files
- add Requires
