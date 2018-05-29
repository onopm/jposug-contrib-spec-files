#
# spec file for package SFEmimms
#
# includes module(s): mimms
#
%include Solaris.inc
%include packagenamemacros.inc
%define cc_is_gcc 0
%define _gpp g++
%include base.inc
%define _prefix /usr
%define tarball_name mimms

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: MMS stream downloader
Name: SFEmimms
IPS_Package_Name: audio/mimms
Version: 3.2.1
License: GPLv3+
SUNW_Copyright: %{name}.copyright
Group: Applications/Multimedia
URL: http://savannah.nongnu.org/projects/mimms/
Source: http://download.savannah.gnu.org/releases/mimms/mimms-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: library/video/libmms
Requires: library/video/libmms
BuildRequires: %{pnm_buildrequires_runtime_python_26}
Requires: %{pnm_requires_runtime_python_26}
%include default-depend.inc

%description
mimms is a program designed to allow you to download streams using the MMS
protocol and save them to your computer, as opposed to watching them live.

%prep
%setup -q -n %{tarball_name}-%{version}

%build
# No configure or SMP, this is just some python code
make

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (0755, root, bin)
%doc AUTHORS COPYING NEWS README
%{_bindir}/mimms
%{python_sitelib}/mimms-*.egg-info
%{python_sitelib}/libmimms/
%{_mandir}/man1/mimms.1*

%changelog
* Thr May 02 2013 YAMAMOTO Takashi <yamachan@selfnavi.com>
- Initial revision for the jposug

* Sun Mar 18 2008 Matthias Saou <http://freshrpms.net/> 3.2.1-1
- Initial RPM release.
