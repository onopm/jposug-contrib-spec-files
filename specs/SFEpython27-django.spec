#
# spec file for package SFEpython27-django
#
# includes module(s): Django
#
%include Solaris.inc
%include packagenamemacros.inc

%define python_version  2.7

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
%include default-depend.inc

Requires: SFEpython27
Requires: SFEpython27-setuptools

%prep
%setup -q -n Django-%version

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --prefix=%{_prefix} --no-compile

# move to vendor-packages
mkdir -p %{buildroot}%{_libdir}/python%{python_version}/vendor-packages
mv %{buildroot}%{_libdir}/python%{python_version}/site-packages/* \
   %{buildroot}%{_libdir}/python%{python_version}/vendor-packages/
rmdir %{buildroot}%{_libdir}/python%{python_version}/site-packages

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, bin)
%{_bindir}
%{_libdir}/python%{python_version}/vendor-packages

%changelog
* Sun Apr 4 2012 - Osamu Tabata<cantimerny.g@gmail.com>
- Support for OpenIndiana
