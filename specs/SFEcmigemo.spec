#
# spec file for package SFEproftpd-13
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#
%include Solaris.inc
%include packagenamemacros.inc

%define _prefix	/usr
%define _basedir	/

Name:                    SFEcmigemo
IPS_package_name:        text/cmigemo
Summary:                 C interface of Ruby/Migemo Japanese incremental search tool
Version:                 1.3
IPS_component_version:   1.3.20140319
License:		 MIT License
Url:                     https://github.com/koron/cmigemo
Source:                  cmigemo-20140319.tar.gz
Source1:                 cmigemo-config.mk

SUNW_Basedir:            %{_basedir}
#SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: developer/gcc-45
BuildRequires: text/nkf

%description
C interface of Ruby/Migemo Japanese incremental search tool

%prep
%setup -n cmigemo-20140319

cp %{SOURCE1} config.mk

%build

make sun-all

%install
rm -rf $RPM_BUILD_ROOT

make sun-install prefix=$RPM_BUILD_ROOT/usr
mv $RPM_BUILD_ROOT/usr/doc/migemo/README_j.txt $RPM_BUILD_ROOT/usr/share/migemo
rm -r $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%attr (0555, root, bin) /usr/bin/cmigemo
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, bin) /usr/share/migemo
/usr/share/migemo/*
%dir %attr (0755, root, bin) /usr/lib
/usr/lib/*
%dir %attr (0755, root, bin) /usr/include
/usr/include/*

%changelog
* Tue Sep 23 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
