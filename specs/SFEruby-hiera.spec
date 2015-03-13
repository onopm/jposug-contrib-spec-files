%include Solaris.inc
%include default-depend.inc

%define gemname hiera

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir21}/gems/%{gemname}-%{version}

%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir22}/gems/%{gemname}-%{version}

Summary: A pluggable data store for hierarcical data
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-22/hiera
Version: 1.3.4
License: Apache License 2.0
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-22
Requires:       runtime/ruby-22
Requires:	library/ruby-22/json_pure

%description
A pluggable data store for hierarcical data

%package 19
IPS_package_name: library/ruby-19/hiera
Summary: %{gemname}
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19
Requires:	library/ruby-19/json_pure

%description 19
A pluggable data store for hierarcical data

%package 20
IPS_package_name: library/ruby-20/hiera
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
Requires:	library/ruby-20/json_pure

%description 20
A pluggable data store for hierarcical data

%package 21
IPS_package_name: library/ruby-21/hiera
Summary: %{gemname}
BuildRequires:	runtime/ruby-21
Requires:	runtime/ruby-21
Requires:	library/ruby-21/json_pure

%description 21
A pluggable data store for hierarcical data

%prep
%setup -q -c -T

%build
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    -V \
    --force %{SOURCE0}

# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}%{bindir19}/

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
    %{buildroot}%{bindir20}/

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
    %{buildroot}%{bindir21}/

# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

mkdir -p %{buildroot}%{bindir22}
cp -a .%{bindir22}/* \
    %{buildroot}%{bindir22}/

rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1

%changelog
* Fri Mar 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-22
* Wed Jun 11 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.4
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18
* Thu May 29 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.3
* Thu Feb 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.2 and generate package for ruby-21
* Wed Jan 29 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.1
* Wed Jan 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Thu Sep 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1
* Thu Jan 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix path in %define gemdir18 and gemdir19
* Thu Dec 20 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use full path in %define gemdir18 and gemdir19
- add BuildRequires
* Sun Oct 21 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
