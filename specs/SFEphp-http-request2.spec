%include Solaris.inc
%include packagenamemacros.inc

%define _prefix /usr
%define tarball_version  2.3.0
%define tarball_name     HTTP_Request2
%define pear 1
%define pecl 0

%define build53 %( if [ -x /usr/php/5.3/bin/php ]; then echo '1'; else echo '0'; fi)
%if %{build53}
%define pear_dir53 %(/usr/php/5.3/bin/pear config-get php_dir)
%endif
%define build55 %( if [ -x /usr/php/5.5/bin/php ]; then echo '1'; else echo '0'; fi)
%if %{build55}
%define pear_dir55 %(/usr/php/5.5/bin/pear config-get php_dir)
%endif
%define build56 %( if [ -x /usr/php/5.6/bin/php ]; then echo '1'; else echo '0'; fi)
%if %{build56}
%define pear_dir56 %(/usr/php/5.6/bin/pear config-get php_dir)
%endif
%define build70 %( if [ -x /usr/php/7.0/bin/php ]; then echo '1'; else echo '0'; fi)
%if %{build70}
%define pear_dir70 %(/usr/php/7.0/bin/pear config-get php_dir)
%endif

%define generate_executable 0

Name:                    SFEphp-http-request2
IPS_package_name:	 web/php/extension/php-http-request2
Summary:                 Provides an easy way to perform HTTP requests.
Version:                 %{tarball_version}
License:		 BSD-3-Clause
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{tarball_version}.tgz
SUNW_Basedir:            /
SUNW_Copyright:          php-%{tarball_name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
Provides an easy way to perform HTTP requests.

%if %{build53}
%package 53
IPS_package_name: web/php-53/extension/php-http-request2
Summary:          Provides an easy way to perform HTTP requests.
BuildRequires:    web/php-53 = *
Requires:         web/php-53 = *

%description 53
Provides an easy way to perform HTTP requests.
%endif

%if %{build55}
%package 55
IPS_package_name: web/php-55/extension/php-http-request2
Summary:          Provides an easy way to perform HTTP requests.
BuildRequires:    web/php-55 = *
Requires:         web/php-55 = *

%description 55
Provides an easy way to perform HTTP requests.
%endif

%if %{build56}
%package 56
IPS_package_name: web/php-56/extension/php-http-request2
Summary:          Provides an easy way to perform HTTP requests.
BuildRequires:    web/php-56 = *
Requires:         web/php-56 = *

%description 56
Provides an easy way to perform HTTP requests.
%endif

%if %{build70}
%package 70
IPS_package_name: web/php-70/extension/php-http-request2
Summary:          Provides an easy way to perform HTTP requests.
BuildRequires:    web/php-70 = *
Requires:         web/php-70 = *

%description 70
Provides an easy way to perform HTTP requests.
%endif


%prep

%setup -c -T

%build
gzip -dc %{SOURCE0} > %{tarball_name}-%{tarball_version}.tar

%install
rm -rf %{buildroot}

install_for() {
    php_ver=$1
    bindir="/usr/php/${php_ver}/bin"
%if %{pear}
    pear_dir=$(${bindir}/pear config-get php_dir)
    ${bindir}/pear -c pearrc install \
        --nodeps \
        --packagingroot %{buildroot} \
        %{tarball_name}-%{tarball_version}.tar
    # Clean up unnecessary files
    rm %{buildroot}/${pear_dir}/.filemap
    rm %{buildroot}/${pear_dir}/.lock
    rm -rf %{buildroot}/${pear_dir}/.registry/.channel*
    rm -rf %{buildroot}${pear_dir}/.channels
    rm %{buildroot}${pear_dir}/.depdb
    rm %{buildroot}${pear_dir}/.depdblock
%endif
}

%if %{build53}
install_for 5.3
%endif

%if %{build55}
install_for 5.5
%endif

%if %{build56}
install_for 5.6
%endif

%if %{build70}
install_for 7.0
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,bin,-)

%if %{build53}
%files 53
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, bin) /var/php
%dir %attr (0755, root, bin) /var/php/5.3
%{pear_dir53}
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*53
%endif
%endif

%if %{build55}
%files 55
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, bin) /var/php
%dir %attr (0755, root, bin) /var/php/5.5
%{pear_dir55}
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*55
%endif
%endif

%if %{build56}
%files 56
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, bin) /var/php
%dir %attr (0755, root, bin) /var/php/5.6
%{pear_dir56}
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*56
%endif
%endif

%if %{build70}
%files 70
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%dir %attr (0755, root, bin) /var/php
%dir %attr (0755, root, bin) /var/php/7.0
%{pear_dir70}
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*70
%endif
%endif

%changelog
* Tue Apr 19 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
