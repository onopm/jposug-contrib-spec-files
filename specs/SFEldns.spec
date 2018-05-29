#
# spec file for package SFEldns.spec
#
# includes module(s): ldns
#
%include Solaris.inc
%include packagenamemacros.inc

%define src_name	ldns

Name:		SFEldns
IPS_Package_Name:	library/ldns
URL:		http://www.nlnetlabs.nl/projects/ldns/
Summary:	ldns library for DNS programming
Version:	1.7.0
Group:		System/Libraries
License:	BSD
SUNW_Copyright:	ldns.copyright
Source:		http://www.nlnetlabs.nl/downloads/%{src_name}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
%include default-depend.inc
# BuildRequires:	%{pnm_buildrequires_SUNWopenssl_include}
#Requires:	%{pnm_requires_SUNWopenssl_libraries}
BuildRequires:	library/security/openssl
BuildRequires:	runtime/perl-512
Requires:	library/security/openssl

%description
The goal of ldns is to simplify DNS programming, it supports recent RFCs like the DNSSEC documents, and allows developers to easily create software conforming to current RFCs, and experimental software for current Internet Drafts.

%package devel
IPS_Package_Name: library/ldns/developer
Summary:         %{summary} - development files
SUNW_BaseDir:    %{_basedir}
%include default-depend.inc
Requires: %name

%prep
%setup -q -n %{src_name}-%{version}

%build
export PATH=/usr/perl5/5.12/bin:${PATH}
./configure --prefix=%{_prefix}	\
	--sysconfdir=%{_sysconfdir} \
	--disable-static \
	--disable-gost \
        --disable-ecdsa \
        --disable-dane
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_libdir}/libldns.so*

%files devel
%defattr (-, root, bin)
%{_bindir}/ldns-config
%{_includedir}/%{src_name}
%dir %attr (0755, root, sys) %{_datadir}
%{_mandir}

%changelog
* Tue Mar 07 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.0
* Thu Jun 16 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use perl 5.12 to build man pages, because building man pages failed with perl 5.22.
* Wed May 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.17
* Sun Dec 16 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- ues pnmacro
* Wed Jun 06 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.13
- add --disable-ecdsa because ecdsa is enabled by default
* Fri Apr 13 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- set IPS_Package_Name to SFEldns-devel
* Sat Feb 25 2012 - Satoru MIYAZAKI<s.miyaza@gmail.com>
- bump to 1.6.12
* Fri Nov 25 2011 - Milan Jurik
- bump to 1.6.11
* Sun Jul 24 2011 - Guido Berhoerster <gber@openindiana.org>
- added License and SUNW_Copyright tags
* Thu Jun 30 2011 - Milan Juril
- bump to 1.6.10
* Fri Mar 25 2011 - Milan Jurik
- bump to 1.6.9
* Mon Jan 24 2011 - Milan Jurik
- bump to 1.6.8
* Mon Nov 08 2010 - Milan Jurik
- bump to 1.6.7
- disable GOST because of old OpenSSL
* Thu Sep 23 2010 - Milan Jurik
- bump to 1.6.6
* Wed Jun 09 2010 - Milan Jurik
- Initial version
