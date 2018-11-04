%include Solaris.inc
%include packagenamemacros.inc

%define build53 %( test -x /usr/php/5.3/bin/php && echo 1 || echo 0)
%define build55 %( test -x /usr/php/5.5/bin/php && echo 1 || echo 0)
%define build56 %( test -x /usr/php/5.6/bin/php && echo 1 || echo 0)
%define build71 %( test -x /usr/php/7.1/bin/php && echo 1 || echo 0)
%define build72 %( test -x /usr/php/7.2/bin/php && echo 1 || echo 0)
%define build71jposug %( test -x /opt/jposug/php/7.1/bin/php && echo 1 || echo 0)
%define build72jposug %( test -x /opt/jposug/php/7.2/bin/php && echo 1 || echo 0)

%define tarball_name     Mail_mimeDecode

Name:                    SFEphp-mail-mimedecode
IPS_package_name:	 	web/php/extension/php-mail-mimedecode
Summary:                 PHP module for MAIL_mimeDecode
Version:                 1.5.6
License:				 BSD Style
Url:                     http://pear.php.net/package/%{tarball_name}
Source:                  http://download.pear.php.net/package/%{tarball_name}-%{version}.tgz
Distribution:            OpenSolaris
Vendor:		        	 OpenSolaris Community
SUNW_Basedir:            /
SUNW_Copyright:          %{name}.copyright
BuildRoot:               %{_tmppath}/%{name}-%{version}-build

%description
Provides a class to deal with the decoding and interpreting of mime messages.
This package used to be part of the Mail_Mime package, but has been split off.

%if %{build53}
%package 53
IPS_package_name:	web/php-53/extension/php-mail-mimedecode
BuildRequires:		web/php-53 = *
Requires:			web/php-53 = *
%define pear_dir_53 %(/usr/php/5.3/bin/pear config-get php_dir)
%endif

%if %{build55}
%package 55
IPS_package_name:	web/php-55/extension/php-mail-mimedecode
BuildRequires:		web/php-55 = *
Requires:			web/php-55 = *
%define pear_dir_55 %(/usr/php/5.5/bin/pear config-get php_dir)
%endif

%if %{build56}
%package 56
IPS_package_name:	web/php/extension/php-mail-mimedecode-56
BuildRequires:		web/php-56 = *
Requires:			web/php-56 = *
%define pear_dir_56 %(/usr/php/5.6/bin/pear config-get php_dir)

%package 56-old
IPS_package_name:	web/php-56/extension/php-mail-mimedecode
BuildRequires:		web/php-56 = *
Requires:			web/php-56 = *
%define _use_internal_dependency_generator 0
IPS_legacy:			false
Meta(pkg.renamed):	true
PkgBuild_Make_Empty_Package: true
Renamed_To:			web/php/extension/php-mail-mimedecode-56 = *
%endif

%if %{build71}
%package 71
IPS_package_name:	web/php/extension/php-mail-mimedecode-71
BuildRequires:		web/php-71 = *
Requires:			web/php-71 = *
%define pear_dir_71 %(/usr/php/7.1/bin/pear config-get php_dir)
%endif

%if %{build72}
%package 72
IPS_package_name:	web/php/extension/php-mail-mimedecode-72
BuildRequires:		web/php-72 = *
Requires:			web/php-72 = *
%define pear_dir_72 %(/usr/php/7.2/bin/pear config-get php_dir)
%endif

%if %{build71jposug}
%package 71jposug
IPS_package_name:	web/php/extension/php-mail-mimedecode-71jposug
BuildRequires:		web/php-71jposug = *
Requires:			web/php-71jposug = *
%define pear_dir_71jposug %(/opt/jposug/php/7.1/bin/pear config-get php_dir)
%endif

%if %{build72jposug}
%package 72jposug
IPS_package_name:	web/php/extension/php-mail-mimedecode-72jposug
BuildRequires:		web/php-72jposug = *
Requires:			web/php-72jposug = *
%define pear_dir_72jposug %(/opt/jposug/php/7.2/bin/pear config-get php_dir)
%endif

%prep

%setup -c -T

%build

gzip -dc %{SOURCE0} > %{tarball_name}-%{version}.tar

%install

rm -rf %{buildroot}

install_for() {
	if [ "x${1}" = 'x7.1jposug' -o "x${1}" = 'x7.2jposug' ]
	then
		php_ver=$(echo $1 | sed -e 's/jposug//')
		pear_cmd="/opt/jposug/php/${php_ver}/bin/pear"
	else
		php_ver=$1
		pear_cmd="/usr/php/${php_ver}/bin/pear"
	fi
	${pear_cmd} -c pearrc install --nodeps --packagingroot %{buildroot} %{tarball_name}-%{version}.tar

	# Clean up unnecessary files
	pear_dir=$(${pear_cmd} config-get php_dir)
	rm %{buildroot}/${pear_dir}/.filemap
	rm %{buildroot}/${pear_dir}/.lock
	rm -rf %{buildroot}/${pear_dir}/.registry/.channel*
	rm -rf %{buildroot}${pear_dir}/.channels
	rm %{buildroot}${pear_dir}/.depdb
	rm %{buildroot}${pear_dir}/.depdblock
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
%if %{build71}
install_for 7.1
%endif
%if %{build72}
install_for 7.2
%endif
%if %{build71jposug}
install_for 7.1jposug
%endif
%if %{build72jposug}
install_for 7.2jposug
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)

%if %{build53}
%files 53
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{pear_dir_53}
%{pear_dir_53}/*
%{pear_dir_53}/.registry/mail_mimedecode.reg
%endif

%if %{build55}
%files 55
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{pear_dir_55}
%{pear_dir_55}/*
%{pear_dir_55}/.registry/mail_mimedecode.reg
%endif

%if %{build56}
%files 56
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{pear_dir_56}
%{pear_dir_56}/*
%{pear_dir_56}/.registry/mail_mimedecode.reg
%endif

%if %{build71}
%files 71
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{pear_dir_71}
%{pear_dir_71}/*
%{pear_dir_71}/.registry/mail_mimedecode.reg
%endif

%if %{build72}
%files 72
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{pear_dir_72}
%{pear_dir_72}/*
%{pear_dir_72}/.registry/mail_mimedecode.reg
%endif

%if %{build71jposug}
%files 71jposug
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{pear_dir_71jposug}
%{pear_dir_71jposug}/*
%{pear_dir_71jposug}/.registry/mail_mimedecode.reg
%endif

%if %{build72jposug}
%files 72jposug
%defattr (-, root, bin)
%dir %attr(0755, root, bin) %{pear_dir_72jposug}
%{pear_dir_72jposug}/*
%{pear_dir_72jposug}/.registry/mail_mimedecode.reg
%endif

%changelog
* Sun Nov 04 2018 <me@tsundoku.ne.jp>
- new multi-PHP spec 1.5.6
