#
# spec file for package SFEpython27-imaging
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_name        Imaging
%define pyprefix        /usr/python
%define pyver           2.7
%define imgver          1.1.7
%define execpython      %{pyprefix}/bin/python%{pyver}
%define execpython64    %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32          lib
%define _lib64          lib64


Name:                   SFEpython27-imaging
IPS_package_name:       library/python-2/SFEpython27-imaging-%{imgver}
Summary:                Pythons own image processing library
URL:                    http://www.pythonware.com/products/pil/
Version:                %{imgver}
Source:                 http://effbot.org/downloads/Imaging-%{version}.tar.gz
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:         python-imaging.copyright
BuildRequires:          SFEpython27-setuptools
BuildRequires:          SUNWzlib
BuildRequires:          SUNWjpg-devel
BuildRequires:          SUNWpng-devel
BuildRequires:          SUNWfreetype2
BuildRequires:          SUNWgnome-base-libs-devel
Requires:               runtime/SFEpython-273
Requires:               SUNWjpg
Requires:               SUNWpng


%description
The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.


%prep
%setup -c -n %{src_name}-%{version}

%ifarch amd64 sparcv9
rm -rf %{src_name}-%{version}-64
cp -rp %{src_name}-%{version} %{src_name}-%{version}-64
%endif


%build
cd %{src_name}-%{version}
perl -pi -e 'print "#!/usr/python/bin/python%{pyver}\n" if ( $. == 1 )' Scripts/pilfont.py
%{execpython} setup.py build

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
perl -pi -e 'print "#!/usr/python/bin/amd64/python%{pyver}\n" if ( $. == 1 )' Scripts/pilfont.py
%{execpython64} setup.py build
%endif


%install
cd %{src_name}-%{version}
%{execpython} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pildriver.py $RPM_BUILD_ROOT%{pyprefix}/bin/pildriver%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilconvert.py $RPM_BUILD_ROOT%{pyprefix}/bin/pilconvert%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilfile.py $RPM_BUILD_ROOT%{pyprefix}/bin/pilfile%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilprint.py $RPM_BUILD_ROOT%{pyprefix}/bin/pilprint%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilfont.py $RPM_BUILD_ROOT%{pyprefix}/bin/pildfont%{pyver}.py


%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py install --root="$RPM_BUILD_ROOT" --prefix=%{pyprefix}
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pildriver.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/pildriver%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilconvert.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/pilconvert%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilfile.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/pilfile%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilprint.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/pilprint%{pyver}.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/pilfont.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/pildfont%{pyver}.py
%endif

# move to vendor-packages
# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/vendor-packages
mv $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/site-packages/* \
   $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{pyprefix}/%{_lib32}/python%{pyver}/site-packages

%ifarch amd64 sparcv9
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/vendor-packages
mv $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/site-packages/* \
   $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{pyprefix}/%{_lib64}/python%{pyver}/site-packages
%endif

echo deleting pyo files
find $RPM_BUILD_ROOT -name '*.pyo' -exec rm {} \;

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
#%dir %attr (0755, root, sys) /usr
%{pyprefix}/bin/pilfile%{pyver}.py
%{pyprefix}/bin/pildfont%{pyver}.py
%{pyprefix}/bin/pilconvert%{pyver}.py
%{pyprefix}/bin/pildriver%{pyver}.py
%{pyprefix}/bin/pilprint%{pyver}.py
%{pyprefix}/%{_lib32}/python%{pyver}/*

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%{pyprefix}/bin/%{_arch64}/pilfile%{pyver}.py
%{pyprefix}/bin/%{_arch64}/pildfont%{pyver}.py
%{pyprefix}/bin/%{_arch64}/pilconvert%{pyver}.py
%{pyprefix}/bin/%{_arch64}/pildriver%{pyver}.py
%{pyprefix}/bin/%{_arch64}/pilprint%{pyver}.py
%{pyprefix}/%{_lib64}/python%{pyver}/*
%endif


%changelog
* Tue Sep 23 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for Solaris11
* Sun May 14 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for openindiana
