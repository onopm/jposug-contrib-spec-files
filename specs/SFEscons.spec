%include Solaris.inc

%define tarball_name    scons
%define tarball_version 2.1.0


Name: SFEscons
IPS_package_name:        developer/build/scons
Summary: SCons is an Open Source software tool construction
Version: 2.1.0
License: MIT
Group: System Environment/Base
URL: http://www.puppetlabs.com/puppet/related-projects/%{name}/
Source0: http://prdownloads.sourceforge.net/%{tarball_name}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: runtime/python-26
Requires: runtime/python-26

%description
SCons is an Open Source software tool construction - that is, a next-generation build tool. Think of SCons as an improved, cross-platform substitute for the classic Make utility with integrated functionality similar to autoconf/automake and compiler caches such as ccache. In short, SCons is an easier, more reliable and faster way to build software.

%prep
%setup -q -n %{tarball_name}-%{tarball_version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot} --standard-lib
mkdir -p %{buildroot}%{_mandir}/man1
cp -f scons.1 sconsign.1 scons-time.1 %{buildroot}%{_mandir}/man1
rm -rf %{buildroot}/usr/man
rm -rf %{buildroot}/usr/bin/*-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%doc README.txt RELEASE.txt CHANGES.txt
%dir %attr(0755, root, sys) /usr
%dir %attr(0755, root, sys) %{_datadir}
%dir %attr(0755, root, other) %{_datadir}/doc
%{_bindir}/scons
%{_bindir}/sconsign
%{_bindir}/scons-time
%{_datadir}/man/man1/*
/usr/lib/python2.6/site-packages/

%changelog
* Sun Jun 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
