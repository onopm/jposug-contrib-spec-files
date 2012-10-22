#
# spec file for package SFEpython27-django
#
# includes module(s): Django
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define python_version  2.7
%define execpython      %{_bindir}/%{_arch64}/python%{python_version}

Name:		SFEpython27-django
IPS_Package_Name:	web/python/django
Version:	1.3.1
Summary:	A high-level Python Web framework that enables Rapid Development
License:	BSD
Group:		Development/Languages/Python
URL:		http://www.djangoproject.com/
Source:		http://media.djangoproject.com/releases/1.3/Django-%{version}.tar.gz
SUNW_Copyright:	SFEpython27-django.copyright
SUNW_BaseDir:	%{_basedir}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build


Requires: SFEpython27
Requires: SFEpython27-setuptools

%prep
%setup -q -n Django-%version

%build
%{execpython} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{execpython} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
cp $RPM_BUILD_ROOT%{_bindir}/django-admin.py $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/django-admin.py
rm $RPM_BUILD_ROOT%{_bindir}/django-admin.py
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/django-admin.py
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages

%changelog
* Sun Apr 4 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Supprt for amd64 arch
* Sun Apr 4 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
