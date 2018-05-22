#
# spec file for package SFEnagios
#
# includes module(s): nagios
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
%include Solaris.inc
%include default-depend.inc

Name:		SFEhttp-load
IPS_package_name:        network/http-load
Version:	2006.3.12
Summary:	http_load
License:	unknown
URL:		http://acme.com/software/http_load/
Source:		http://acme.com/software/http_load/http_load-12mar2006.tar.gz
Patch1:		http_load.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
http_load runs multiple http fetches in parallel, to test the throughput of a web server. However unlike most such test clients, it runs in a single process, so it doesn't bog down the client machine. It can be configured to do https fetches as well.

%prep
%setup -q -n http_load-12mar2006
%patch1 -p1

mv Makefile Makefile.orig
sed -e 's/^#SYSV_LIBS/SYSV_LIBS/' Makefile.orig > Makefile

%build
make


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/man/man1

make BINDIR=%{buildroot}/usr/bin \
     MANDIR=%{buildroot}/usr/share/man/man1 \
     install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc README
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, other) /usr/share/doc
/usr/bin/http_load
/usr/share/man/man1/http_load.1

%changelog
* Wed Nov 07 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
- add patch1 from https://github.com/tagomoris/isucon/raw/master/tools/http_load/http_load.patch
