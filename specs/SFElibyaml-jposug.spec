#
# spec file for package libyaml
#
# includes module(s): libyaml
#
%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /opt/jposug
%define	tarball_version	0.1.7
%define	tarball_name yaml
%define	src_url	http://pyyaml.org/download/libyaml

Name:		SFElibyaml-jposug
Summary:	LibYAML is a YAML 1.1 parser and emitter written in C.
Version:	%{tarball_version}
IPS_package_name:  jposug/library/text/yaml
License:	MIT license
Source:		%{src_url}/%{tarball_name}-%{tarball_version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          %{name}.copyright

#Meta(info.maintainer_url):      http://pyyaml.org/wiki/LibYAML
Meta(info.upstream_url):        http://pyyaml.org/wiki/LibYAML
#Meta(info.classification):      org.opensolaris.category.2011:Media

%prep
%setup -c -n %{name}-%{version}

%build

CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

cd %{tarball_name}-%{tarball_version}
%ifarch sparc
%define target sparc-sun-solaris
%else
%define target i386-sun-solaris
%endif

export CC=cc
export CFLAGS="-m64 -i -xO4 -xspace -xstrconst -Kpic -xregs=no%frameptr -xCC"

./configure\
 --prefix=%{_prefix}\
 --exec-prefix=%{_prefix}\
 --libdir=%{_libdir} \
 --includedir=%{_includedir} \
 --mandir=%{_mandir}

gmake -j$CPUS

%install
cd %{tarball_name}-%{tarball_version}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr(0755, root, sys) /opt
%dir %attr(0755, root, bin) %{_prefix}
%dir %attr(0755, root, bin) %{_prefix}/lib
%dir %attr(0755, root, other) %{_prefix}/lib/pkgconfig
%dir %attr(0755, root, bin) %{_prefix}/include
%{_prefix}/lib/libyaml*
%{_prefix}/lib/pkgconfig/*
%{_prefix}/include/*

%changelog
* Fri Feb 08 2019 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
