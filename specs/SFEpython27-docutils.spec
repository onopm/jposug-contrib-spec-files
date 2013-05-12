#
# spec file for package SFEpython27-docutils
#
%include Solaris.inc
%include packagenamemacros.inc
%include default-depend.inc

%define src_url         http://sunet.dl.sourceforge.net/docutils
%define src_name        docutils
%define pyprefix        /usr/python
%define pyver           2.7
%define docver          0.10
%define execpython      %{pyprefix}/bin/python%{pyver}
%define execpython64    %{pyprefix}/bin/%{_arch64}/python%{pyver}
%define _lib32          lib
%define _lib64          lib64

Name:                   SFEpython27-docutils
IPS_package_name:       library/python-2/SFEpython27-docutils
Summary:                Python Documentation Utilities
URL:                    http://pypi.python.org/pypi/docutils
Version:                0.10
Source:                 %{src_url}/%{src_name}-%{version}.tar.gz
SUNW_BaseDir:           %{_basedir}
BuildRoot:              %{_tmppath}/%{name}-%{version}-build
License:                BSD-2 GPL-3 public-domain
SUNW_Copyright:         SFEpython27-docutils.copyright

BuildRequires:          SFEpython27-setuptools
Requires:               SFEpython27-pygments
Requires:               SFEpython27

%prep
%setup -c -n %{src_name}-%{version}

%ifarch amd64 sparcv9
rm -rf %{src_name}-%{version}-64
cp -rp %{src_name}-%{version} %{src_name}-%{version}-64
%endif

%build
cd %{src_name}-%{version}
%{execpython} setup.py build

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py build
%endif

%install
cd %{src_name}-%{version}
%{execpython} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}

# Rename temporary file name
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xetex.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xetex_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2latex.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2latex_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt_prepstyles.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt_prepstyles_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2man.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2man_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2html.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2html_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2s5.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2s5_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2pseudoxml.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2pseudoxml_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xml.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xml_.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rstpep2html.py $RPM_BUILD_ROOT%{pyprefix}/bin/rstpep2html_.py

%ifarch amd64 sparcv9
cd ../%{src_name}-%{version}-64
%{execpython64} setup.py install --root=$RPM_BUILD_ROOT --prefix=%{pyprefix}
mkdir -p $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}

mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xetex.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2xetex.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2latex.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2latex.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt_prepstyles.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2odt_prepstyles.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2man.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2man.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2html.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2html.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2odt.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2s5.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2s5.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2pseudoxml.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2pseudoxml.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xml.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rst2xml.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rstpep2html.py $RPM_BUILD_ROOT%{pyprefix}/bin/%{_arch64}/rstpep2html.py

# Reneme 32bit scripts
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2latex_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2latex.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt_prepstyles_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt_prepstyles.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2man_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2man.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2html_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2html.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2odt.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2s5_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2s5.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2pseudoxml_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2pseudoxml.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xml_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rst2xml.py
mv $RPM_BUILD_ROOT%{pyprefix}/bin/rstpep2html_.py $RPM_BUILD_ROOT%{pyprefix}/bin/rstpep2html.py


%endif

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{pyprefix}/%{_lib32}
%{pyprefix}/%{_lib32}/python%{pyver}/*
%{pyprefix}/bin/*.py

%ifarch amd64 sparcv9
%defattr (-, root, bin)
%dir %attr (0755, root, bin) %{pyprefix}/%{_lib64}
%{pyprefix}/%{_lib64}/python%{pyver}/*
%{pyprefix}/bin/%{_arch64}/*.py
%endif


%changelog
* Sun May 12 2013 - Osamu Tabata<cantimerny.g@gmail.com>
- Initial commit
