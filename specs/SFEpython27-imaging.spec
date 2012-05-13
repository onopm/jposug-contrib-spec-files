#
# spec file for package SFEpython27-imaging
#

%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define python_version   2.7
%define execpython      %{_bindir}/%{_arch64}/python%{python_version}

Name:                    SFEpython27-imaging
IPS_package_name:        library/python-2/python-imaging-27
Summary:                 Pythons own image processing library
URL:                     http://www.pythonware.com/products/pil/
Version:                 1.1.7
Source:                  http://effbot.org/downloads/Imaging-%{version}.tar.gz
SUNW_BaseDir:            %{_basedir}
BuildRoot:               %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:          python-imaging.copyright
BuildRequires:           SFEpython27-setuptools
BuildRequires:           SUNWzlib
BuildRequires:           SUNWjpg-devel
BuildRequires:           SUNWpng-devel
#BuildRequires:           SUNWfreetype2
#BuildRequires:           SUNWgnome-base-libs-devel
Requires:                SFEpython27
Requires:                SUNWjpg


%description
The Python Imaging Library (PIL) adds image processing capabilities
to your Python interpreter.

This library provides extensive file format support, an efficient
internal representation, and powerful image processing capabilities.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
%setup -n Imaging-%{version}


%build
perl -pi -e 'print "#!/usr/bin/amd64/python%{python_version}\n" if ( $. == 1 )' Scripts/pilfont.py
%{execpython} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{execpython} setup.py install -O1 --skip-build --root="$RPM_BUILD_ROOT" --prefix="%{_prefix}"

# move to vendor-packages
mkdir -p $RPM_BUILD_ROOT%{_bindir}/%{_arch64}
cp $RPM_BUILD_ROOT%{_bindir}/pildriver.py $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/pildriver%{python_version}.py
cp $RPM_BUILD_ROOT%{_bindir}/pilfont.py $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/pilfont%{python_version}.py
cp $RPM_BUILD_ROOT%{_bindir}/pilfile.py $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/pilfile%{python_version}
cp $RPM_BUILD_ROOT%{_bindir}/pilprint.py $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/pilprint%{python_version}.py
cp $RPM_BUILD_ROOT%{_bindir}/pilconvert.py $RPM_BUILD_ROOT%{_bindir}/%{_arch64}/pilconvert%{python_version}.py
rm $RPM_BUILD_ROOT%{_bindir}/pildriver.py
rm $RPM_BUILD_ROOT%{_bindir}/pilfont.py $RPM_BUIL
rm $RPM_BUILD_ROOT%{_bindir}/pilfile.py
rm $RPM_BUILD_ROOT%{_bindir}/pilprint.py
rm $RPM_BUILD_ROOT%{_bindir}/pilconvert.py

mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages
mv $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages/* \
   $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/
rmdir $RPM_BUILD_ROOT%{_libdir}/%{_arch64}/python%{python_version}/site-packages

echo deleting pyo files
find $RPM_BUILD_ROOT -name '*.pyo' -exec rm {} \;

%{?pkgbuild_postprocess: %pkgbuild_postprocess -v -c "%{version}:%{jds_version}:%{name}:$RPM_ARCH:%(date +%%Y-%%m-%%d):%{support_level}" $RPM_BUILD_ROOT}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{_bindir}/%{_arch64}
%{_bindir}/%{_arch64}/pilconvert2.7.py
%{_bindir}/%{_arch64}/pildriver2.7.py
%{_bindir}/%{_arch64}/pilfont2.7.py
%{_bindir}/%{_arch64}/pilfile2.7
%{_bindir}/%{_arch64}/pilprint2.7.py
%dir %attr (0755, root, bin) %{_libdir}/%{_arch64}
%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/PIL
%{_libdir}/%{_arch64}/python%{python_version}/vendor-packages/PIL.pth

%changelog
* Sun May 14 2012 -  Osamu Tabata<cantimerny.g@gmail.com>
- Support for openindiana
