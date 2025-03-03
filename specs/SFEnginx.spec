#
# spec file for package SFEnginx
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Owner: lewellyn
#

# NOTE: This package will include all normally-optional modules which do not
#       require dependencies. GeoIP, image-filter, xslt have dependencies and
#       therefore do not get built without explicit request.

# Recognized options:
# --define 'nginxuser USERNAME'		specify the system user (Default: webservd)
# --define 'nginxgroup GROUPNAME'	specify the system group (Default: webservd)
# --define 'cpu CPUTYPE'		specify the target CPU
#					Choose target CPU from:
#					pentium, pentiumpro, pentium3,
#					pentium4, athlon, opteron,
#					sparc32, sparc64
# --with-gcc				build with GCC instead of Sun Studio
# --with-geoip				Enable GeoIP module (not done yet)
# --with-image-filter			Enable image filter module (depends on GD)
# --with-legacy				build "legacy" (old stable) version
# --with-unstable			build development version (overrides legacy)
# --with-xslt				Enable XSLT module (depends on libxml/libxslt)


###
### TODO:
###
### ! Determine if rtsig/select should be included (probably not)
### ! Man Page
### ! Test on SPARC
### ! Verify sanity of default config
### * GeoIP
### 

%include Solaris.inc
%include packagenamemacros.inc

Release:		1

%if %{?_with_legacy:1}%{!?_with_legacy:0}
# Legacy Version
Version:		0.7.67
%define stability -legacy
%else
# Stable Version
Version:		0.8.53
%endif
%if %{?_with_unstable:1}%{!?_with_unstable:0}
# Development Version
Version:		0.8.53
%define stability -unstable
%endif

Name:			SFEnginx
IPS_package_name:       web/server/nginx
Summary:		Free, open-source, high-performance HTTP server and reverse proxy.
Source:			http://nginx.org/download/%{sname}-%{version}.tar.gz
Source1:		http-nginx
Source2:		http-nginx.xml
URL:			http://nginx.org/
Group:			Web Services/Application and Web Servers
License:		BSD
Vendor:			SFE (spec-files-extra)
SUNW_Copyright:		%{sname}.copyright
SUNW_BaseDir:		%{_basedir}
SUNW_Hotline:		http://wiki.nginx.org/NginxFaq
BuildRoot:		%{_tmppath}/%{name}-%{version}-build

# IPS Manifest stuff
Meta(info.upstream):		Igor Sysoev <http://sysoev.ru/en/>
Meta(info.maintainer):		Matt Lewandowsky <matt@greenviolet.net>

%include default-depend.inc

BuildRequires:		%{pnm_buildrequires_SUNWgsed}
BuildRequires:		%{pnm_buildrequires_openssl}
Requires:		%{pnm_requires_SUNWopenssl}
Requires:		%{pnm_requires_SUNWpcre}
Requires:		%{pnm_requires_SUNWzlib}

%if %{?_with_image_filter:1}%{!?_with_image_filter:0}
BuildRequires:		%{pnm_buildrequires_SUNWgd2}
Requires:		%{pnm_requires_SUNWgd2}
%endif

%if %{?_with_xslt:1}%{!?_with_xslt:0}
Requires:		%{pnm_requires_SUNWlxml}
Requires:		%{pnm_requires_SUNWlxsl}
%endif

%package root
Summary:		%{name} - root filesystem files, /
SUNW_BaseDir:		/
Requires: %name

%description
Nginx (pronounced "engine ex") is a free, open-source, high-performance HTTP
server and reverse proxy, as well as an IMAP/POP3 proxy server. Igor Sysoev
started development of Nginx in 2002, with the first public release in 2004.

Nginx is known for its high performance, stability, rich feature set, simple
configuration, and low resource consumption. 

Nginx is one of a handful of servers written to address the C10K problem.
Unlike traditional servers, Nginx doesn't rely on threads to handle requests.
Instead it uses a much more scalable event-driven (asynchronous) architecture.
This architecture uses small, but more importantly, predictable amounts
of memory under load.

Even if you don't expect to handle thousands of simultaneous requests, you can
still benefit from Nginx's high-performance and small memory footprint. Nginx
scales in all directions: from the smallest VPS all the way up to clusters of
servers.

%prep
%setup -q -n %{sname}-%{version}

#########################
# User-overrideable stuff
#########################

# See above for more information.

# Username to run as
%define nginxuser %{?!nginxuser:webservd}%{?nginxuser}

# Group to run as
%define nginxgroup %{?!nginxgroup:webservd}%{?nginxgroup}

# Whether to enable HTTP image filter module
# (Adds a dependency of GD)
%define imagefilter %{?_with_image_filter:--with-http_image_filter_module}%{!?_with_image_filter:}

# Whether to enable HTTP XSLT module
# (Adds dependencies of libxml/libxslt)
%define xslt %{?_with_xslt:--with-http_xslt_module}%{!?_with_xslt:}

# Whether to enable HTTP image filter module
# (Adds an unspecified dependency; not yet done.)
%define geoip %{?_with_geoip:--with-http_geoip_module}%{!?_with_geoip:}

# Is there a better way to refer to /lib?
%define methodpath /lib/svc/method
%define manifestpath %{_localstatedir}/svc/manifest/network

#############################
# End User-overrideable stuff
#############################

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
    CPUS=1
fi
export ACLOCAL_FLAGS="-I %{_datadir}/aclocal"

%if %{?_with_gcc}
# GCC
%define %cc_is_gcc 1
export CC=gcc
export CXX=g++
export LDFLAGS="%{_ldflags}"

%else
# Sun Studio
export LDFLAGS="%{_ldflags}"

%endif # _with_gcc

export LD=/usr/ccs/bin/ld

# Define the things we use more than once.
%define statedir %{_localstatedir}/%{sname}
%define logdir %{statedir}/logs
%define confpath %{_sysconfdir}/%{sname}/%{sname}.conf
%define pidpath %{statedir}/nginx.pid
%define sbinpath %{_sbindir}/%{sname}

./configure								\
		--conf-path=%{confpath}					\
		--error-log-path=%{logdir}/error.log			\
		--group=%{nginxgroup}					\
		--http-client-body-temp-path=%{statedir}/client_body_temp \
		--http-fastcgi-temp-path=%{statedir}/fastcgi_temp	\
		--http-log-path=%{logdir}/access.log			\
		--http-proxy-temp-path=%{statedir}/proxy_temp		\
		--http-scgi-temp-path=%{statedir}/scgi_temp		\
		--http-uwsgi-temp-path=%{statedir}/uwsgi_temp		\
		--lock-path=%{statedir}/nginx.lock			\
		--pid-path=%{pidpath}					\
		--prefix=%{statedir}					\
		--sbin-path=%{sbinpath}					\
		--user=%{nginxuser}					\
		--with-http_addition_module				\
		--with-http_dav_module					\
		--with-http_flv_module					\
		--with-http_gzip_static_module				\
		--with-http_random_index_module				\
		--with-http_realip_module				\
		--with-http_secure_link_module				\
		--with-http_ssl_module					\
		--with-http_stub_status_module				\
		--with-http_sub_module					\
		--with-ipv6						\
		--with-rtsig_module					\
		--with-select_module					\
		%{geoip}						\
		%{imagefilter}						\
		%{xslt}

make -j$CPUS || make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{methodpath}
install -d $RPM_BUILD_ROOT%{manifestpath}
install %{SOURCE1} $RPM_BUILD_ROOT%{methodpath} # SMF method
install %{SOURCE2} $RPM_BUILD_ROOT%{manifestpath} # SMF manifest

gsed -i 's~-CONF_PATH-~%{confpath}~' $RPM_BUILD_ROOT%{methodpath}/http-nginx
gsed -i 's~-PID_PATH-~%{pidpath}~' $RPM_BUILD_ROOT%{methodpath}/http-nginx
gsed -i 's~-SBIN_PATH-~%{sbinpath}~' $RPM_BUILD_ROOT%{methodpath}/http-nginx

gsed -i 's~-METHOD_PATH-~%{methodpath}/http-nginx~' $RPM_BUILD_ROOT%{manifestpath}/http-nginx.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%{_sbindir}

%files root
%defattr (-, root, sys)
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, bin) %{_sysconfdir}/%{sname}
%attr (0644, root, bin) %{_sysconfdir}/%{sname}/*
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, %{nginxuser}, %{nginxgroup}) %{_localstatedir}/%{sname}
%dir %attr (0755, root, bin) %{_localstatedir}/%{sname}/html
%attr (0644, root, bin) %{_localstatedir}/%{sname}/html/*
%dir %attr (0755, %{nginxuser}, %{nginxgroup}) %{_localstatedir}/%{sname}/logs
%dir %attr (0755, root, bin) /lib
%dir %attr (0755, root, bin) /lib/svc
%dir %attr (0755, root, bin) /lib/svc/method
%attr (0755, root, bin) /lib/svc/method/*
%class(manifest) %attr(0755, root, sys)/var/svc/manifest/*


%changelog
* Sat Feb 25 2012 - TAKI,Yasushi <taki@justplayer.com>
- add IPS_package_name.
- change requires for pnmacro.
* Thr Mar 17 2011 - Thomas Wagner
- fix packaging ownergroup of directories to smf manifest 
- fix directory and files permissions in %files root for /lib/..., method, manifest
* Wed Nov 17 2010 - Matt Lewandowsky <matt@greenviolet.net>
- Added SMF manifest/method.
* Tue Nov 16 2010 - Matt Lewandowsky <matt@greenviolet.net>
- Initial version
