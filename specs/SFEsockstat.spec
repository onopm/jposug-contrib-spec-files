#
# spec file for package SFEsockstat
#

%include Solaris.inc
%include base.inc
%include default-depend.inc

%define revision 0e029f59de721d8ea3ec5e831b7defce8198de04
%define commit_date 2015.5.29

Name:			SFEsockstat
IPS_Package_Name:	diagnostic/sockstat
Summary:		List open sockets on Illumos with process information
URL:			https://github.com/bahamas10/illumos-sockstat
Version:		0.%{commit_date}
Source:			https://github.com/bahamas10/illumos-sockstat/archive/%{revision}.zip
License:		CDDL
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: developer/gcc
Requires: system/library/gcc/gcc-runtime

%prep
%setup -q -c -n  socat-%version

%build
cd illumos-sockstat-%{revision}
cp README.md ../

export CC=/usr/bin/gcc
export CFLAGS='-m64'

gmake

%install
rm -rf $RPM_BUILD_ROOT
cd illumos-sockstat-%{revision}
mkdir -p $RPM_BUILD_ROOT/usr/bin
install sockstat $RPM_BUILD_ROOT/usr/bin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
%doc README.md
%dir %attr (0755, root, bin) %{_bindir}
%{_bindir}/*


%changelog
* Tue Dec 06 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
