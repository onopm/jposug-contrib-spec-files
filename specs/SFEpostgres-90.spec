#
# spec file for package PostgreSQL 9.0
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
#
%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr/postgres
%define _var_prefix /var/postgres
%define tarball_name     postgresql
%define tarball_version  9.0.16
%define major_version	 9.0
%define prefix_name      SFEpostgres-90

%define _basedir         %{_prefix}/%{major_version}

Name:                    %{prefix_name}-client
IPS_package_name:        database/postgres-90
Summary:	         PostgreSQL client tools
Version:                 %{tarball_version}
License:		 PostgreSQL
Group:		System/Databases
Url:                     http://www.postgresql.org/
Source:                  http://ftp.postgresql.org/pub/source/v%{tarball_version}/%{tarball_name}-%{tarball_version}.tar.bz2
Source1:		 postgres-90-postgres_90
Source2:		 postgres-90-postgresql_90.xml
Source3:		 postgres-90-auth_attr
Source4:		 postgres-90-prof_attr
Source5:		 postgres-90-exec_attr
Source6:		 postgres-90-user_attr
Distribution:            OpenSolaris
Vendor:		         OpenSolaris Community
SUNW_Basedir:            /usr
SUNW_Copyright:          %{prefix_name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

BuildRequires: %{pnm_buildrequires_SUNWlxsl}
BuildRequires: %{pnm_buildrequires_SUNWlxml}
BuildRequires: %{pnm_buildrequires_SUNWgss}
BuildRequires: %{pnm_buildrequires_SUNWopenssl}
BuildRequires: %{pnm_buildrequires_SUNWzlib}
BuildRequires: %{pnm_buildrequires_SUNWcsl}
BuildRequires: %{pnm_buildrequires_SUNWlibms}
BuildRequires: %{pnm_buildrequires_SUNWgss}
BuildRequires: %{pnm_buildrequires_SUNWTcl}
BuildRequires: SFEeditline

Requires: %{pnm_requires_SUNWlxsl}
Requires: %{pnm_requires_SUNWlxml}
Requires: %{pnm_requires_SUNWzlib}
Requires: %{pnm_requires_SUNWcsl}
Requires: %{pnm_requires_SUNWopenssl}
Requires: %{pnm_requires_SUNWlibms}
Requires: %{pnm_requires_SUNWgss}
Requires: SFEeditline

Requires: %{prefix_name}-libs

# OpenSolaris IPS Package Manifest Fields
Meta(info.upstream):	 	PostgreSQL Global Development Group
Meta(info.maintainer):	 	pkglabo.justplayer.com <pkgadmin@justplayer.com>
# Meta(info.repository_url):	[open source code repository]
Meta(info.classification):	System Database

%description
PostgreSQL is a powerful, open source object-relational database system. It has more than 15 years of active development and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness. It runs on all major operating systems, including Linux, UNIX (AIX, BSD, HP-UX, SGI IRIX, Mac OS X, Solaris, Tru64), and Windows. It is fully ACID compliant, has full support for foreign keys, joins, views, triggers, and stored procedures (in multiple languages). It includes most SQL:2008 data types, including INTEGER, NUMERIC, BOOLEAN, CHAR, VARCHAR, DATE, INTERVAL, and TIMESTAMP. It also supports storage of binary large objects, including pictures, sounds, or video. It has native programming interfaces for C/C++, Java, .Net, Perl, Python, Ruby, Tcl, ODBC, among others, and exceptional documentation.

%package -n %{prefix_name}-libs

IPS_package_name: database/postgres-90/library
Summary: PostgreSQL client libraries
Requires: %{pnm_requires_SUNWlibms}
Requires: %{pnm_requires_SUNWcsl}

%package -n %{prefix_name}-pl
IPS_package_name: database/postgres-90/language-bindings
Summary: PostgreSQL additional Perl, Python & TCL server procedural languages

#Requires: runtime/perl-584
#Requires: runtime/python-24
Requires: %{pnm_requires_SUNWlibms}
Requires: %{pnm_requires_SUNWcsl}
Requires: %{pnm_requires_SUNWTcl}
Requires: %{name}
Requires: %{prefix_name}-libs

%package -n %{prefix_name}-devel
IPS_package_name: database/postgres-90/developer
Summary: PostgreSQL development tools and header files

Requires: %{pnm_requires_SUNWlxsl}
Requires: %{pnm_requires_SUNWlxml}
Requires: %{pnm_requires_SUNWgss}
Requires: %{pnm_requires_SUNWopenssl}
Requires: %{pnm_requires_SUNWcsl}
Requires: %{pnm_requires_SUNWzlib}
Requires: %{pnm_requires_SUNWlibms}
Requires: %{name}
Requires: %{prefix_name}-libs

%package -n %{prefix_name}-docs
IPS_package_name: database/postgres-90/documentation
Summary: PostgreSQL documentation and man pages

%package -n %{prefix_name}-server
IPS_package_name: service/database/postgres-90
Summary: PostgreSQL database server

SUNW_Basedir:            /

Requires: %{pnm_requires_SUNWlxsl}
Requires: %{pnm_requires_SUNWlxml}
Requires: %{pnm_requires_SUNWgss}
Requires: %{pnm_requires_SUNWopenssl}
Requires: %{pnm_requires_SUNWcsl}
Requires: %{pnm_requires_SUNWzlib}
Requires: %{pnm_requires_SUNWlibms}
Requires: %{name}
Requires: %{prefix_name}-libs
Requires: SFEpostgres-common

%package -n %{prefix_name}-contrib
IPS_package_name: database/postgres-90/contrib
Summary: PostgreSQL community contributed tools not part of core product

Requires: %{pnm_requires_SUNWlxsl}
Requires: %{pnm_requires_SUNWlxml}
Requires: %{pnm_requires_SUNWgss}
Requires: %{pnm_requires_SUNWopenssl}
Requires: %{pnm_requires_SUNWcsl}
Requires: %{pnm_requires_SUNWzlib}
Requires: %{pnm_requires_SUNWlibms}
Requires: %{name}
Requires: %{prefix_name}-libs

%prep
%setup -c -n %{tarball_name}-%{tarball_version}
#%patch1 -p0

%ifarch amd64 sparcv9
rm -rf %{tarball_name}-%{tarball_version}-64
cp -rp %{tarball_name}-%{tarball_version} %{tarball_name}-%{tarball_version}-64
%endif

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

export CCAS=/usr/bin/cc
export CCASFLAGS=
export CC=cc
# export CFLAGS="%optflags"
export CFLAGS="-i -xO4 -xspace -xstrconst -Kpic -xregs=no%frameptr -xCC"
export LDFLAGS="%_ldflags -L/usr/gnu/lib -R/usr/gnu/lib -lncurses"
export LD_OPTIONS="-R/usr/sfw/lib:/usr/gnu/lib -L/usr/sfw/lib:/usr/gnu/lib"

./configure --prefix=%{_prefix}/%{major_version} \
            --exec-prefix=%{_prefix}/%{major_version} \
            --bindir=%{_prefix}/%{major_version}/bin \
            --libexecdir=%{_prefix}/%{major_version}/bin \
            --sbindir=%{_prefix}/%{major_version}/bin \
            --datadir=%{_prefix}/%{major_version}/share \
            --sysconfdir=%{_prefix}/%{major_version}/etc \
            --mandir=%{_prefix}/%{major_version}/man \
            --libdir=%{_prefix}/%{major_version}/lib \
            --includedir=%{_prefix}/%{major_version}/include \
            --sharedstatedir=%{_var_prefix}/%{major_version} \
            --localstatedir=%{_var_prefix}/%{major_version} \
            --localedir=%{_prefix}/%{major_version}/share/locale/ \
            --enable-nls \
            --docdir=%{_prefix}/%{major_version}/doc \
            --with-system-tzdata=/usr/share/lib/zoneinfo \
            --with-tcl \
            --with-perl \
            --with-python \
            --with-pam \
            --with-openssl \
            --with-libedit-preferred \
            --with-libxml \
            --with-libxslt \
            --with-gssapi \
            --enable-thread-safety \
            --enable-dtrace \
            --with-includes=/usr/include:/usr/sfw/include:/usr/sfw/include:/usr/gnu/include \
            --with-tclconfig=/usr/lib \
            --with-libs=/usr/lib:/usr/sfw/lib:/usr/gnu/lib

gmake -j$CPUS world

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{tarball_version}-64

#export CFLAGS="%optflags64"
export CFLAGS="-m64 -i -xO4 -xspace -xstrconst -Kpic -xregs=no%frameptr -xCC"
export LDFLAGS="%_ldflags -L/usr/gnu/lib/%{_arch64} -R/usr/gnu/lib/%{_arch64} -lncurses"
export LD_OPTIONS="-R/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64} -L/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64}"

./configure --prefix=%{_prefix}/%{major_version} \
            --exec-prefix=%{_prefix}/%{major_version} \
            --bindir=%{_prefix}/%{major_version}/bin/%{_arch64} \
            --libexecdir=%{_prefix}/%{major_version}/bin/%{_arch64} \
            --sbindir=%{_prefix}/%{major_version}/bin/%{_arch64} \
            --datadir=%{_prefix}/%{major_version}/share \
            --sysconfdir=%{_prefix}/%{major_version}/etc \
            --mandir=%{_prefix}/%{major_version}/man \
            --libdir=%{_prefix}/%{major_version}/lib/%{_arch64} \
            --includedir=%{_prefix}/%{major_version}/include \
            --sharedstatedir=%{_var_prefix}/%{major_version} \
            --localstatedir=%{_var_prefix}/%{major_version} \
            --localedir=%{_prefix}/%{major_version}/share/locale/ \
            --enable-nls \
            --docdir=%{_prefix}/%{major_version}/doc \
            --with-system-tzdata=/usr/share/lib/zoneinfo \
            --with-tcl \
            --with-python \
            --with-pam \
            --with-openssl \
            --with-libedit-preferred \
            --with-libxml \
            --with-libxslt \
            --with-gssapi \
            --enable-thread-safety \
            --enable-dtrace \
            --with-includes=/usr/include:/usr/sfw/include:/usr/sfw/include:/usr/gnu/include \
            --with-tclconfig=/usr/lib \
            --with-libs=/usr/lib/%{_arch64}:/usr/sfw/lib/%{_arch64}:/usr/gnu/lib/%{_arch64}

gmake -j$CPUS world

%endif
%install
cd %{tarball_name}-%{tarball_version}
gmake install-world DESTDIR=$RPM_BUILD_ROOT
if test -d sun-manpages; then
	cd sun-manpages
	make install DESTDIR=$RPM_BUILD_ROOT
	cd ..
fi

%ifarch amd64 sparcv9
cd ../%{tarball_name}-%{tarball_version}-64
gmake install-world DESTDIR=$RPM_BUILD_ROOT

#export OLD_PATH=`pwd`
#cd $RPM_BUILD_ROOT%{_prefix}/%{major_version}/bin
#ln -fs %{_arch64} 64
#cd ../lib
#ln -fs %{_arch64} 64
#cd ${OLD_PATH}
#cd ..
%endif

mkdir -p $RPM_BUILD_ROOT/etc/security
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/backups
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/data
mkdir -p $RPM_BUILD_ROOT%{_var_prefix}/%{major_version}/data_64

mkdir -p $RPM_BUILD_ROOT/lib/svc/method/
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/svc/method/postgres_90
chmod +x $RPM_BUILD_ROOT/lib/svc/method/postgres_90
mkdir -p $RPM_BUILD_ROOT/var/svc/manifest/application/database/
cp %{SOURCE2} $RPM_BUILD_ROOT/var/svc/manifest/application/database/postgresql_90.xml

# attribute
mkdir -p $RPM_BUILD_ROOT/etc/security/auth_attr.d/
cp %{SOURCE3} $RPM_BUILD_ROOT/etc/security/auth_attr.d/service\%2Fdatabase\%2Fpostgres-90
mkdir -p $RPM_BUILD_ROOT/etc/security/exec_attr.d/
cp %{SOURCE4} $RPM_BUILD_ROOT/etc/security/exec_attr.d/service\%2Fdatabase\%2Fpostgres-90
mkdir -p $RPM_BUILD_ROOT/etc/security/prof_attr.d/
cp %{SOURCE5} $RPM_BUILD_ROOT/etc/security/prof_attr.d/service\%2Fdatabase\%2Fpostgres-90
mkdir -p $RPM_BUILD_ROOT/etc/user_attr.d/
cp %{SOURCE5} $RPM_BUILD_ROOT/etc/user_attr.d/service\%2Fdatabase\%2Fpostgres-90


mkdir -p $RPM_BUILD_ROOT/usr/share

# delete amd64
rm -f $RPM_BUILD_ROOT%{_prefix}/%{major_version}/lib/amd64/libecpg.a
rm -f $RPM_BUILD_ROOT%{_prefix}/%{major_version}/lib/amd64/libpq.a
rm -f $RPM_BUILD_ROOT%{_prefix}/%{major_version}/lib/amd64/libpgtypes.a
rm -f $RPM_BUILD_ROOT%{_prefix}/%{major_version}/lib/amd64/amd64
rm -f $RPM_BUILD_ROOT%{_prefix}/%{major_version}/lib/amd64/libpgport.a
rm -f $RPM_BUILD_ROOT%{_prefix}/%{major_version}/lib/amd64/libecpg_compat.a

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

# make symbolic link

cd $RPM_BUILD_ROOT/%{_prefix}/%{major_version}/bin/
[ -r 64 ] || ln -fs amd64 64

mkdir -p $RPM_BUILD_ROOT/usr/bin/amd64
cd $RPM_BUILD_ROOT/usr/bin/
ln -fs ../postgres/%{major_version}/bin/clusterdb .
ln -fs ../postgres/%{major_version}/bin/createdb .
ln -fs ../postgres/%{major_version}/bin/createlang .
ln -fs ../postgres/%{major_version}/bin/createuser .
ln -fs ../postgres/%{major_version}/bin/dropdb .
ln -fs ../postgres/%{major_version}/bin/droplang .
ln -fs ../postgres/%{major_version}/bin/dropuser .
ln -fs ../postgres/%{major_version}/bin/ecpg .
ln -fs ../postgres/%{major_version}/bin/initdb .
ln -fs ../postgres/%{major_version}/bin/oid2name .
ln -fs ../postgres/%{major_version}/bin/pg_archivecleanup .
ln -fs ../postgres/%{major_version}/bin/pg_config .
ln -fs ../postgres/%{major_version}/bin/pg_controldata .
ln -fs ../postgres/%{major_version}/bin/pg_ctl .
ln -fs ../postgres/%{major_version}/bin/pg_dump .
ln -fs ../postgres/%{major_version}/bin/pg_dumpall .
ln -fs ../postgres/%{major_version}/bin/pg_resetxlog .
ln -fs ../postgres/%{major_version}/bin/pg_restore .
ln -fs ../postgres/%{major_version}/bin/pg_standby .
ln -fs ../postgres/%{major_version}/bin/pg_upgrade .
ln -fs ../postgres/%{major_version}/bin/pgbench .
ln -fs ../postgres/%{major_version}/bin/pltcl_delmod .
ln -fs ../postgres/%{major_version}/bin/pltcl_listmod .
ln -fs ../postgres/%{major_version}/bin/pltcl_loadmod .
ln -fs ../postgres/%{major_version}/bin/postgres .
ln -fs ../postgres/%{major_version}/bin/postmaster .
ln -fs ../postgres/%{major_version}/bin/psql .
ln -fs ../postgres/%{major_version}/bin/reindexdb .
ln -fs ../postgres/%{major_version}/bin/vacuumdb .
ln -fs ../postgres/%{major_version}/bin/vacuumlo .

cd $RPM_BUILD_ROOT/usr/bin/amd64
ln -fs ../postgres/%{major_version}/bin/amd64/clusterdb .
ln -fs ../postgres/%{major_version}/bin/amd64/createdb .
ln -fs ../postgres/%{major_version}/bin/amd64/createlang .
ln -fs ../postgres/%{major_version}/bin/amd64/createuser .
ln -fs ../postgres/%{major_version}/bin/amd64/dropdb .
ln -fs ../postgres/%{major_version}/bin/amd64/droplang .
ln -fs ../postgres/%{major_version}/bin/amd64/dropuser .
ln -fs ../postgres/%{major_version}/bin/amd64/ecpg .
ln -fs ../postgres/%{major_version}/bin/amd64/initdb .
ln -fs ../postgres/%{major_version}/bin/amd64/oid2name .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_archivecleanup .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_config .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_controldata .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_ctl .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_dump .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_dumpall .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_resetxlog .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_restore .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_standby .
ln -fs ../postgres/%{major_version}/bin/amd64/pg_upgrade .
ln -fs ../postgres/%{major_version}/bin/amd64/pgbench .
ln -fs ../postgres/%{major_version}/bin/amd64/pltcl_delmod .
ln -fs ../postgres/%{major_version}/bin/amd64/pltcl_listmod .
ln -fs ../postgres/%{major_version}/bin/amd64/pltcl_loadmod .
ln -fs ../postgres/%{major_version}/bin/amd64/postgres .
ln -fs ../postgres/%{major_version}/bin/amd64/postmaster .
ln -fs ../postgres/%{major_version}/bin/amd64/psql .
ln -fs ../postgres/%{major_version}/bin/amd64/reindexdb .
ln -fs ../postgres/%{major_version}/bin/amd64/vacuumdb .
ln -fs ../postgres/%{major_version}/bin/amd64/vacuumlo .


%clean
rm -rf $RPM_BUILD_ROOT

#%actions server
#group groupname="postgres"
#user ftpuser=false gcos-field="PostgreSQL Reserved UID" username="postgres" password=NP group="postgres"

%files
%defattr (-, root, bin)

%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin/amd64
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*/LC_MESSAGES
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/psql
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/clusterdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/createdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/createlang
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/createuser
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/dropdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/droplang
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/dropuser
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pg_dump
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pg_dumpall
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pg_restore
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/vacuumdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/reindexdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/psql
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/clusterdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/createdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/createlang
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/createuser
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/dropdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/droplang
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/dropuser
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_dump
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_dumpall
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_restore
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/vacuumdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/reindexdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/psql
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/clusterdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/createdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/createlang
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/createuser
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/dropdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/droplang
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/dropuser
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pg_dump
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pg_dumpall
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pg_restore
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/reindexdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/vacuumdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/psql
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/clusterdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/createdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/createlang
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/createuser
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/dropdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/droplang
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/dropuser
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_dump
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_dumpall
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_restore
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/reindexdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/vacuumdb
%attr (0644, root, other) %{_prefix}/%{major_version}/share/psqlrc.sample
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ta/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/pg_dump-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/pgscripts-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/psql-%{major_version}.mo



%files -n %{prefix_name}-libs
%defattr (-, root, bin)

%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64
%attr (0755, root, bin) %{_prefix}/%{major_version}/bin/64
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*/LC_MESSAGES
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/man
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/man/man5
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/libecpg.so.6.2
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/libecpg_compat.so.3.2
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/libpgtypes.so.3.1
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libecpg.so.6.2
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libecpg_compat.so.3.2
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libpgtypes.so.3.1
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libpgport.a
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libpq.a
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libecpg.a
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libpgtypes.a
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libecpg_compat.a
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/psql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ta/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_CN/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/ecpg-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/ecpglib6-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/libpq5-%{major_version}.mo
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libecpg.so.6
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libpq.so.5.3
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libpq.so
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libpgtypes.so
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libecpg_compat.so
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libpgtypes.so.3
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libpq.so.5
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libecpg.so
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libecpg.so.6
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libecpg_compat.so
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libecpg_compat.so.3
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libpgtypes.so
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libpgtypes.so.3
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libpq.so
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libpq.so.5
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/libpq.so.5.3
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libecpg_compat.so.3
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/libecpg.so

%files -n %{prefix_name}-pl
%defattr (-, root, bin)

%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin/amd64
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*/LC_MESSAGES
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pltcl_listmod
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pltcl_loadmod
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pltcl_delmod
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pltcl_delmod
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pltcl_listmod
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pltcl_loadmod
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pltcl_listmod
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pltcl_loadmod
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pltcl_delmod
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pltcl_delmod
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pltcl_listmod
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pltcl_loadmod

%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/zh_TW/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/plpython.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/pltcl.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/plperl.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/plpython.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/pltcl.so
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/unknown.pltcl


%files -n %{prefix_name}-devel
%defattr (-, root, bin)

%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin/amd64
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/informix
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/informix/esql
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/internal
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/internal/libpq
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/libpq
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/access
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/bootstrap
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/catalog
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/commands
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/executor
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/foreign
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/lib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/libpq
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/mb
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/nodes
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/optimizer
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/parser
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/port
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/port/win32
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/arpa
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/netinet
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/sys
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc/sys
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/portability
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/postmaster
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/regex
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/rewrite
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/snowball
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/storage
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/tcop
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/tsearch
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/dicts
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/include/server/utils
%dir %attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/replication
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/config
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/makefiles
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/test
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/test/regress
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/pgxs
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/pgxs/config
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/makefiles
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/test
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/test/regress
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*/LC_MESSAGES
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/tablespace.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/trigger.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/typecmds.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/user.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/vacuum.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/variable.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/view.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/dynloader.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/execdebug.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/execdefs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/execdesc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/executor.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/functions.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/hashjoin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/instrument.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeAgg.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeAppend.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeBitmapAnd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeBitmapHeapscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeBitmapIndexscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeBitmapOr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeCtescan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeFunctionscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeGroup.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeHash.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeHashjoin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeIndexscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeLimit.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeMaterial.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeMergejoin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeNestloop.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeRecursiveunion.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeResult.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeSeqscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeSetOp.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeSort.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeSubplan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeSubqueryscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeTidscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeUnique.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeValuesscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeWindowAgg.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeWorktablescan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/spi.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/spi_priv.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/tstoreReceiver.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/tuptable.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeLockRows.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/executor/nodeModifyTable.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/fmgr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/foreign/foreign.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/funcapi.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/getaddrinfo.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/getopt_long.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/lib/dllist.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/lib/stringinfo.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/auth.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/be-fsstubs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/crypt.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/hba.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/ip.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/libpq-be.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/libpq-fs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/libpq.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/md5.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/pqcomm.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/pqformat.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/libpq/pqsignal.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/mb/pg_wchar.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/miscadmin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/bitmapset.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/execnodes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/makefuncs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/memnodes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/nodeFuncs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/nodes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/params.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/parsenodes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/pg_list.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/plannodes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/primnodes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/print.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/readfuncs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/relation.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/tidbitmap.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/nodes/value.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/clauses.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/cost.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_copy.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_gene.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_misc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_mutation.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_pool.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_random.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_recombination.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/geqo_selection.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/joininfo.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/pathnode.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/paths.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/placeholder.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/plancat.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/planmain.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/planner.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/predtest.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/prep.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/restrictinfo.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/subselect.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/tlist.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/optimizer/var.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/analyze.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/gram.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/gramparse.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/keywords.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/kwlist.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_agg.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_clause.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_coerce.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_cte.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_expr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_func.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_node.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_oper.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_relation.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_target.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_type.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_utilcmd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parser.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parsetree.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/scansup.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/pg_config_manual.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/pg_config_os.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/pg_trace.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/pgstat.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/pgtime.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/aix.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/bsdi.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/cygwin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/darwin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/dgux.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/freebsd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/hpux.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/irix.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/linux.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/netbsd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/nextstep.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/openbsd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/osf.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/sco.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/solaris.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/sunos4.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/svr4.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/ultrix4.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/univel.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/unixware.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/arpa/inet.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/dlfcn.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/grp.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/netdb.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/netinet/in.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/pwd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/sys/socket.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32/sys/wait.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc/dirent.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc/sys/file.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc/sys/param.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc/sys/time.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc/unistd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/port/win32_msvc/utime.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/portability/instr_time.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postgres.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postgres_ext.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postgres_fe.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postmaster/autovacuum.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postmaster/bgwriter.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postmaster/fork_process.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postmaster/pgarch.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postmaster/postmaster.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postmaster/syslogger.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/postmaster/walwriter.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/regex/regcustom.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/regex/regerrs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/regex/regex.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/regex/regguts.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/rewrite/prs2lock.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/rewrite/rewriteDefine.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/rewrite/rewriteHandler.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/rewrite/rewriteManip.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/rewrite/rewriteRemove.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/rewrite/rewriteSupport.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/rusagestub.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/header.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/api.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/header.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_danish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_dutch.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_english.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_finnish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_french.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_german.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_hungarian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_italian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_norwegian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_porter.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_portuguese.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_spanish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_1_swedish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_ISO_8859_2_romanian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_KOI8_R_russian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_danish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_dutch.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_english.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_finnish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_french.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_german.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_hungarian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_italian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_norwegian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_porter.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_portuguese.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_romanian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_russian.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_spanish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_swedish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/snowball/libstemmer/stem_UTF_8_turkish.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/backendid.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/block.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/buf.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/buf_internals.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/buffile.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/bufmgr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/bufpage.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/fd.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/freespace.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/fsm_internals.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/indexfsm.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/ipc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/item.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/itemid.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/itemptr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/large_object.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/lmgr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/lock.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/lwlock.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/off.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/pg_sema.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/pg_shmem.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/pmsignal.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/pos.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/proc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/procarray.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/relfilenode.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/s_lock.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/shmem.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/sinval.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/sinvaladt.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/smgr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/spin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tcop/dest.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tcop/fastpath.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tcop/pquery.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tcop/tcopdebug.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tcop/tcopprot.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tcop/utility.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/dicts/regis.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/dicts/spell.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/ts_cache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/ts_locale.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/ts_public.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/ts_type.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/tsearch/ts_utils.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/acl.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/array.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/ascii.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/builtins.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/cash.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/catcache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/combocid.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/date.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/datetime.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/datum.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/dynahash.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/dynamic_loader.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/elog.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/errcodes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/fmgroids.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/fmgrtab.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/formatting.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/geo_decls.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/guc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/guc_tables.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/help_config.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/hsearch.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/inet.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/int8.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/inval.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/logtape.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/lsyscache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/memutils.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/nabstime.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/numeric.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/palloc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/pg_crc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/pg_locale.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/pg_lzcompress.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/pg_rusage.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/plancache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/portal.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/probes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/ps_status.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/rel.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/relcache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/resowner.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/selfuncs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/snapmgr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/snapshot.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/syscache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/timestamp.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/tqual.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/tuplesort.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/tuplestore.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/typcache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/tzparser.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/uuid.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/varbit.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/xml.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/windowapi.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/sql3types.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/sqlca.h
%attr (0755, root, bin) %{_prefix}/%{major_version}/lib/pgxs/config/install-sh
%attr (0644, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/Makefile.port
%attr (0644, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/Makefile.shlib
%attr (0644, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/makefiles/pgxs.mk
%attr (0644, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/nls-global.mk
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/ecpg
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pg_config
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/ecpg
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pg_config
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/ecpg
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_config
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/ecpg
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_config
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pg_config.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/pg_config.h
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/config/install-sh
%attr (0444, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/Makefile.global
%attr (0444, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/Makefile.port
%attr (0444, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/Makefile.shlib
%attr (0444, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/makefiles/pgxs.mk
%attr (0444, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/nls-global.mk
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/pgxs/src/test/regress/pg_regress
%attr (0644, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/Makefile.global
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/pgxs/src/test/regress/pg_regress
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/nb/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ta/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/pg_config-%{major_version}.mo
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/ecpg_config.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/ecpg_informix.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/ecpgerrno.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/ecpglib.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/ecpgtype.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/informix/esql/datetime.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/informix/esql/decimal.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/informix/esql/sqltypes.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/internal/c.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/internal/libpq-int.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/internal/libpq/pqcomm.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/internal/port.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/internal/postgres_fe.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/internal/pqexpbuffer.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/libpq-events.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/libpq-fe.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/libpq/libpq-fs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pg_config_manual.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pg_config_os.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pgtypes_date.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pgtypes_error.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pgtypes_interval.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pgtypes_numeric.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/pgtypes_timestamp.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/postgres_ext.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/attnum.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/clog.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/genam.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/gin.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/gist.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/gist_private.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/gistscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/hash.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/heapam.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/hio.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/htup.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/itup.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/multixact.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/nbtree.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/printtup.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/reloptions.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/relscan.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/rewriteheap.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/rmgr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/sdir.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/skey.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/slru.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/subtrans.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/sysattr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/transam.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/tupconvert.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/tupdesc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/tupmacs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/tuptoaster.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/twophase.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/twophase_rmgr.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/valid.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/xlog_internal.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/xlogdefs.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/xlogutils.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/xact.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/visibilitymap.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/access/xlog.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/bootstrap/bootstrap.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/c.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/catalog.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/catversion.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/dependency.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/genbki.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/heap.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/index.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/indexing.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/namespace.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_aggregate.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_am.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_amop.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_amproc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_attrdef.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_attribute.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_auth_members.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_authid.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_cast.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_class.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_constraint.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_control.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_conversion.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_conversion_fn.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_database.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_depend.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_description.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_enum.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_foreign_data_wrapper.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_foreign_server.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_index.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_inherits.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_inherits_fn.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_language.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_largeobject.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_namespace.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_opclass.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_operator.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_opfamily.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_pltemplate.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_proc.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_proc_fn.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_rewrite.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_shdepend.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_shdescription.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_statistic.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_tablespace.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_trigger.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_ts_config.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_ts_config_map.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_ts_dict.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_ts_parser.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_ts_template.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_type.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_type_fn.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_user_mapping.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/storage.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/toasting.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_db_role_setting.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_default_acl.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/pg_largeobject_metadata.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/catalog/schemapg.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/alter.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/async.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/cluster.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/comment.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/conversioncmds.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/copy.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/dbcommands.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/defrem.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/discard.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/explain.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/lockcmds.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/portalcmds.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/prepare.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/proclang.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/schemacmds.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/sequence.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/commands/tablecmds.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/parse_param.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/parser/scanner.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/replication/walprotocol.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/replication/walreceiver.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/replication/walsender.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/procsignal.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/storage/standby.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/attoptcache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/bytea.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/rbtree.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/relmapper.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/server/utils/spccache.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/sqlda-compat.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/sqlda-native.h
%attr (0644, root, bin) %{_prefix}/%{major_version}/include/sqlda.h

%files -n %{prefix_name}-docs
%defattr (-, root, bin)

%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/doc
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/doc/html
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/man
%{_prefix}/%{major_version}/doc/html/*
%{_prefix}/%{major_version}/man/*
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/doc/contrib
%{_prefix}/%{major_version}/doc/contrib/autoinc.example
%{_prefix}/%{major_version}/doc/contrib/insert_username.example
%{_prefix}/%{major_version}/doc/contrib/moddatetime.example
%{_prefix}/%{major_version}/doc/contrib/refint.example
%{_prefix}/%{major_version}/doc/contrib/timetravel.example


%files -n %{prefix_name}-server
%defattr (-, root, bin)

%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, bin) %{_prefix}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin/amd64
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale/*/LC_MESSAGES
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/share/timezonesets
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/share/tsearch_data
%dir %attr (0755, postgres, postgres) %{_var_prefix}
%dir %attr (0755, postgres, postgres) %{_var_prefix}/%{major_version}
%dir %attr (0700, postgres, postgres) %{_var_prefix}/%{major_version}/backups
%dir %attr (0700, postgres, postgres) %{_var_prefix}/%{major_version}/data
%dir %attr (0700, postgres, postgres) %{_var_prefix}/%{major_version}/data_64
%dir %attr (0755, root, sys) /etc
%dir %attr (0755, root, sys) /etc/security
%dir %attr (0755, root, sys) /etc/security/auth_attr.d
%dir %attr (0755, root, sys) /etc/security/exec_attr.d
%dir %attr (0755, root, sys) /etc/security/prof_attr.d
%dir %attr (0755, root, sys) /etc/user_attr.d
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, sys) /var/svc
%dir %attr (0755, root, sys) /var/svc/manifest
%dir %attr (0755, root, sys) /var/svc/manifest/application
%dir %attr (0755, root, sys) /var/svc/manifest/application/database
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/hungarian.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/hunspell_sample.affix
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/ispell_sample.affix
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/ispell_sample.dict
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/italian.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/norwegian.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/portuguese.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/russian.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/spanish.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/swedish.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/synonym_sample.syn
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/thesaurus_sample.ths
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/turkish.stop
%attr (0555, root, bin) /lib/svc/method/postgres_90
%attr (0644, root, sys) /etc/security/auth_attr.d/service\%2Fdatabase\%2Fpostgres-90
%attr (0644, root, sys) /etc/security/exec_attr.d/service\%2Fdatabase\%2Fpostgres-90
%attr (0644, root, sys) /etc/security/prof_attr.d/service\%2Fdatabase\%2Fpostgres-90
%attr (0644, root, sys) /etc/user_attr.d/service\%2Fdatabase\%2Fpostgres-90
%attr (0444, root, sys) /var/svc/manifest/application/database/postgresql_90.xml

%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/initdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pg_controldata
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pg_ctl
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/pg_resetxlog
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/postgres
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/postmaster
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/initdb
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pg_controldata
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pg_ctl
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/pg_resetxlog
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/postgres
%attr (0555, root, bin) %{_prefix}/%{major_version}/bin/amd64/postmaster
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/initdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_controldata
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_ctl
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_resetxlog
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/postgres
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/postmaster
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/initdb
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_controldata
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_ctl
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_resetxlog
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/postgres
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/postmaster
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/ascii_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/cyrillic_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/dict_snowball.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/euc_cn_and_mic.so
#%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/euc_jis_2004_and_shift_jis_2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/euc_jp_and_sjis.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/euc_kr_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/euc_tw_and_big5.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/latin2_and_win1250.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/latin_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/plpgsql.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_ascii.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_big5.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_cyrillic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_euc_cn.so
#%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_euc_jis_2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_euc_jp.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_euc_kr.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_euc_tw.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_gb18030.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_gbk.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_iso8859.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_iso8859_1.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_johab.so
#%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_shift_jis_2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_sjis.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_uhc.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_win.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/ascii_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/cyrillic_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/dict_snowball.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/euc_cn_and_mic.so
#%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/euc_jis_2004_and_shift_jis_2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/euc_jp_and_sjis.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/euc_kr_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/euc_tw_and_big5.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/latin2_and_win1250.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/latin_and_mic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/plpgsql.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_ascii.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_big5.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_cyrillic.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_euc_cn.so
#%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_euc_jis_2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_euc_jp.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_euc_kr.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_euc_tw.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_gb18030.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_gbk.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_iso8859.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_iso8859_1.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_johab.so
#%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_shift_jis_2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_sjis.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_uhc.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_win.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/euc2004_sjis2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/libpqwalreceiver.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_euc2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/utf8_and_sjis2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/plpython2.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_euc2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/utf8_and_sjis2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/euc2004_sjis2004.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/plpython2.so
%attr (0555, root, bin) %{_prefix}/%{major_version}/lib/amd64/libpqwalreceiver.so
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/cs/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/de/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/es/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/fr/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/it/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ja/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ko/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pl/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/pt_BR/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/plperl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/plpython-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ro/LC_MESSAGES/pltcl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ru/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/sv/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ta/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ta/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ta/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/ta/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/initdb-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/pg_controldata-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/pg_ctl-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/pg_resetxlog-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/plpgsql-%{major_version}.mo
%attr (0644, root, other) %{_prefix}/%{major_version}/share/locale/tr/LC_MESSAGES/postgres-%{major_version}.mo
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/conversion_create.sql
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/information_schema.sql
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/pg_hba.conf.sample
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/pg_ident.conf.sample
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/pg_service.conf.sample
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/postgres.bki
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/postgres.description
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/postgres.shdescription
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/postgresql.conf.sample
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/recovery.conf.sample
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/snowball_create.sql
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/sql_features.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/system_views.sql
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Africa.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/America.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Antarctica.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Asia.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Atlantic.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Australia
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Australia.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Default
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Etc.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Europe.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/India
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Indian.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/timezonesets/Pacific.txt
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/danish.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/dutch.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/english.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/finnish.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/french.stop
%attr (0444, root, bin) %{_prefix}/%{major_version}/share/tsearch_data/german.stop

%files -n %{prefix_name}-contrib
%defattr (-, root, bin)

%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/bin
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/lib/amd64
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/locale
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share
%dir %attr (0755, root, other) %{_prefix}/%{major_version}/share/contrib
%dir %attr (0755, root, bin) %{_prefix}/%{major_version}/share/tsearch_data
%{_prefix}/%{major_version}/lib/adminpack.so
%{_prefix}/%{major_version}/lib/auto_explain.so
%{_prefix}/%{major_version}/lib/btree_gin.so
%{_prefix}/%{major_version}/lib/btree_gist.so
%{_prefix}/%{major_version}/lib/chkpass.so
%{_prefix}/%{major_version}/lib/citext.so
%{_prefix}/%{major_version}/lib/cube.so
%{_prefix}/%{major_version}/lib/dblink.so
%{_prefix}/%{major_version}/lib/dict_int.so
%{_prefix}/%{major_version}/lib/dict_xsyn.so
%{_prefix}/%{major_version}/lib/earthdistance.so
%{_prefix}/%{major_version}/lib/fuzzystrmatch.so
%{_prefix}/%{major_version}/lib/hstore.so
%{_prefix}/%{major_version}/lib/_int.so
%{_prefix}/%{major_version}/lib/isn.so
%{_prefix}/%{major_version}/lib/lo.so
%{_prefix}/%{major_version}/lib/ltree.so
%{_prefix}/%{major_version}/lib/pageinspect.so
%{_prefix}/%{major_version}/lib/passwordcheck.so
%{_prefix}/%{major_version}/lib/pg_buffercache.so
%{_prefix}/%{major_version}/lib/pg_freespacemap.so
%{_prefix}/%{major_version}/lib/pg_stat_statements.so
%{_prefix}/%{major_version}/lib/pg_trgm.so
%{_prefix}/%{major_version}/lib/pg_upgrade_support.so
%{_prefix}/%{major_version}/lib/pgcrypto.so
%{_prefix}/%{major_version}/lib/pgrowlocks.so
%{_prefix}/%{major_version}/lib/pgstattuple.so
%{_prefix}/%{major_version}/lib/seg.so
%{_prefix}/%{major_version}/lib/autoinc.so
%{_prefix}/%{major_version}/lib/insert_username.so
%{_prefix}/%{major_version}/lib/moddatetime.so
%{_prefix}/%{major_version}/lib/refint.so
%{_prefix}/%{major_version}/lib/timetravel.so
%{_prefix}/%{major_version}/lib/tablefunc.so
%{_prefix}/%{major_version}/lib/test_parser.so
%{_prefix}/%{major_version}/lib/tsearch2.so
%{_prefix}/%{major_version}/lib/unaccent.so
%{_prefix}/%{major_version}/lib/sslinfo.so
%{_prefix}/%{major_version}/lib/pgxml.so
%{_prefix}/%{major_version}/lib/amd64/autoinc.so
%{_prefix}/%{major_version}/lib/amd64/adminpack.so
%{_prefix}/%{major_version}/lib/amd64/auto_explain.so
%{_prefix}/%{major_version}/lib/amd64/btree_gin.so
%{_prefix}/%{major_version}/lib/amd64/btree_gist.so
%{_prefix}/%{major_version}/lib/amd64/chkpass.so
%{_prefix}/%{major_version}/lib/amd64/citext.so
%{_prefix}/%{major_version}/lib/amd64/cube.so
%{_prefix}/%{major_version}/lib/amd64/dblink.so
%{_prefix}/%{major_version}/lib/amd64/dict_int.so
%{_prefix}/%{major_version}/lib/amd64/dict_xsyn.so
%{_prefix}/%{major_version}/lib/amd64/earthdistance.so
%{_prefix}/%{major_version}/lib/amd64/fuzzystrmatch.so
%{_prefix}/%{major_version}/lib/amd64/hstore.so
%{_prefix}/%{major_version}/lib/amd64/_int.so
%{_prefix}/%{major_version}/lib/amd64/insert_username.so
%{_prefix}/%{major_version}/lib/amd64/isn.so
%{_prefix}/%{major_version}/lib/amd64/lo.so
%{_prefix}/%{major_version}/lib/amd64/ltree.so
%{_prefix}/%{major_version}/lib/amd64/moddatetime.so
%{_prefix}/%{major_version}/lib/amd64/pageinspect.so
%{_prefix}/%{major_version}/lib/amd64/passwordcheck.so
%{_prefix}/%{major_version}/lib/amd64/pg_buffercache.so
%{_prefix}/%{major_version}/lib/amd64/pg_freespacemap.so
%{_prefix}/%{major_version}/lib/amd64/pg_stat_statements.so
%{_prefix}/%{major_version}/lib/amd64/pg_trgm.so
%{_prefix}/%{major_version}/lib/amd64/pg_upgrade_support.so
%{_prefix}/%{major_version}/lib/amd64/pgcrypto.so
%{_prefix}/%{major_version}/lib/amd64/pgrowlocks.so
%{_prefix}/%{major_version}/lib/amd64/pgstattuple.so
%{_prefix}/%{major_version}/lib/amd64/pgxml.so
%{_prefix}/%{major_version}/lib/amd64/refint.so
%{_prefix}/%{major_version}/lib/amd64/seg.so
%{_prefix}/%{major_version}/lib/amd64/sslinfo.so
%{_prefix}/%{major_version}/lib/amd64/tablefunc.so
%{_prefix}/%{major_version}/lib/amd64/test_parser.so
%{_prefix}/%{major_version}/lib/amd64/timetravel.so
%{_prefix}/%{major_version}/lib/amd64/tsearch2.so
%{_prefix}/%{major_version}/lib/amd64/unaccent.so
%{_prefix}/%{major_version}/share/contrib/uninstall_adminpack.sql
%{_prefix}/%{major_version}/share/contrib/adminpack.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_btree_gin.sql
%{_prefix}/%{major_version}/share/contrib/btree_gin.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_btree_gist.sql
%{_prefix}/%{major_version}/share/contrib/btree_gist.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_chkpass.sql
%{_prefix}/%{major_version}/share/contrib/chkpass.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_citext.sql
%{_prefix}/%{major_version}/share/contrib/citext.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_cube.sql
%{_prefix}/%{major_version}/share/contrib/cube.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_dblink.sql
%{_prefix}/%{major_version}/share/contrib/dblink.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_dict_int.sql
%{_prefix}/%{major_version}/share/contrib/dict_int.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_dict_xsyn.sql
%{_prefix}/%{major_version}/share/contrib/dict_xsyn.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_earthdistance.sql
%{_prefix}/%{major_version}/share/contrib/earthdistance.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_fuzzystrmatch.sql
%{_prefix}/%{major_version}/share/contrib/fuzzystrmatch.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_hstore.sql
%{_prefix}/%{major_version}/share/contrib/hstore.sql
%{_prefix}/%{major_version}/share/contrib/int_aggregate.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_int_aggregate.sql
%{_prefix}/%{major_version}/share/contrib/uninstall__int.sql
%{_prefix}/%{major_version}/share/contrib/_int.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_isn.sql
%{_prefix}/%{major_version}/share/contrib/isn.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_lo.sql
%{_prefix}/%{major_version}/share/contrib/lo.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_ltree.sql
%{_prefix}/%{major_version}/share/contrib/ltree.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pageinspect.sql
%{_prefix}/%{major_version}/share/contrib/pageinspect.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pg_buffercache.sql
%{_prefix}/%{major_version}/share/contrib/pg_buffercache.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pg_freespacemap.sql
%{_prefix}/%{major_version}/share/contrib/pg_freespacemap.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pg_stat_statements.sql
%{_prefix}/%{major_version}/share/contrib/pg_stat_statements.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pg_trgm.sql
%{_prefix}/%{major_version}/share/contrib/pg_trgm.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pgcrypto.sql
%{_prefix}/%{major_version}/share/contrib/pgcrypto.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pgrowlocks.sql
%{_prefix}/%{major_version}/share/contrib/pgrowlocks.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pgstattuple.sql
%{_prefix}/%{major_version}/share/contrib/pgstattuple.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_seg.sql
%{_prefix}/%{major_version}/share/contrib/seg.sql
%{_prefix}/%{major_version}/share/contrib/autoinc.sql
%{_prefix}/%{major_version}/share/contrib/insert_username.sql
%{_prefix}/%{major_version}/share/contrib/moddatetime.sql
%{_prefix}/%{major_version}/share/contrib/refint.sql
%{_prefix}/%{major_version}/share/contrib/timetravel.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_tablefunc.sql
%{_prefix}/%{major_version}/share/contrib/tablefunc.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_test_parser.sql
%{_prefix}/%{major_version}/share/contrib/test_parser.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_tsearch2.sql
%{_prefix}/%{major_version}/share/contrib/tsearch2.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_unaccent.sql
%{_prefix}/%{major_version}/share/contrib/unaccent.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_sslinfo.sql
%{_prefix}/%{major_version}/share/contrib/sslinfo.sql
%{_prefix}/%{major_version}/share/contrib/uninstall_pgxml.sql
%{_prefix}/%{major_version}/share/contrib/pgxml.sql
%{_prefix}/%{major_version}/share/tsearch_data/xsyn_sample.rules
%{_prefix}/%{major_version}/share/tsearch_data/unaccent.rules
%{_prefix}/%{major_version}/bin/oid2name
%{_prefix}/%{major_version}/bin/pg_archivecleanup
%{_prefix}/%{major_version}/bin/pg_standby
%{_prefix}/%{major_version}/bin/pg_upgrade
%{_prefix}/%{major_version}/bin/pgbench
%{_prefix}/%{major_version}/bin/vacuumlo
%{_prefix}/%{major_version}/bin/amd64/oid2name
%{_prefix}/%{major_version}/bin/amd64/pg_archivecleanup
%{_prefix}/%{major_version}/bin/amd64/pg_standby
%{_prefix}/%{major_version}/bin/amd64/pg_upgrade
%{_prefix}/%{major_version}/bin/amd64/pgbench
%{_prefix}/%{major_version}/bin/amd64/vacuumlo

%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/oid2name
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_archivecleanup
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_standby
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pg_upgrade
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/pgbench
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/vacuumlo
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/oid2name
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_archivecleanup
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_standby
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pg_upgrade
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/pgbench
%attr (0555, root, bin) %ips_tag (mediator=postgres mediator-version=%{major_version}) /usr/bin/amd64/vacuumlo

%changelog
* Fri Feb 21 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 9.0.16
* Tue Feb 18 JST 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 9.0.15
* Sun Oct 20 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 9.0.14
* Fri Apr 05 JST 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Bump to 9.0.13
* Thu Feb 07 JST 2013 TAKI, Yasushi <taki@justplayer.com>
- Bump to 9.0.12
* Thu Jan 23 JST 2013 TAKI, Yasushi <taki@justplayer.com>
- merge SFE and jposug.
* Thu Jan 17 PST 2013 TAKI, Yasushi <taki@justplayer.com>
- support mediator.
* Thu Dec 13 JST 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.0.11
* Thu Sep 27 JST 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.0.10
* Thu Aug 30 - Milan Jurik
- redo packaging
* Fri Aug 24 2012 Ken Mays <kmays2000@gmail.com>
- Bump to 9.0.9
* Mon Sep 10 JST 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.0.9
* Thu Jun 14 JST 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.0.8
- modify Source URL
* Sun Jun  5 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- fix dependency using for pnm.
* Mon Apr 18 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- Bump to 9.0.4
* Fri Feb  4 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- Support 9.0.3
* Tue Feb  1 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- Fix some problems.
* Tue Jan 25 JST 2011 TAKI, Yasushi <taki@justplayer.com>
- Initial Revision
