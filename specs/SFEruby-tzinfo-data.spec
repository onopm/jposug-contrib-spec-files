%include Solaris.inc
%include default-depend.inc

%define gemname tzinfo-data

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%if %{build19}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%endif

%if %{build20}
%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%endif

%if %{build21}
%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}
%endif

%if %{build22}
%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}
%endif

Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          1.2015.4
License:          MIT License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.

%if %{build19}
%package 19-old
IPS_package_name: library/ruby-19/%{gemname}
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-19
Requires:	  runtime/ruby-19
Requires:         library/ruby/tzinfo-data-19

%description 19-old
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.

%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-19
Requires:	  runtime/ruby-19
Requires:         library/ruby-19/tzinfo

%description 19
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
%endif

%if %{build20}
%package 20-old
IPS_package_name: library/ruby-20/%{gemname}
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-20
Requires:	  runtime/ruby-20
Requires:         library/ruby/tzinfo-data-20

%description 20-old
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.

%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-20
Requires:	  runtime/ruby-20
Requires:         library/ruby-20/tzinfo

%description 20
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
%endif

%if %{build21}
%package 21-old
IPS_package_name: library/ruby-21/%{gemname}
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-21
Requires:	  runtime/ruby-21
Requires:         library/ruby/tzinfo-data-21

%description 21-old
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.

%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-21
Requires:	  runtime/ruby-21
Requires:         library/ruby-21/tzinfo

%description 21
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
%endif

%if %{build22}
%package 22-old
IPS_package_name: library/ruby-22/%{gemname}
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-22
Requires:	  runtime/ruby-22
Requires:         library/ruby/tzinfo-data-22

%description 22-old
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.

%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
BuildRequires:	  runtime/ruby-22
Requires:	  runtime/ruby-22
Requires:         library/ruby-22/tzinfo

%description 22
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby modules for use with TZInfo.
%endif


%prep
%setup -q -c -T
%build

# ruby-19
%if %{build19}
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}
%endif

# ruby-20
%if %{build20}
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}
%endif

# ruby-21
%if %{build21}
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}
%endif

# ruby-22
%if %{build22}
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}
%endif

%install
rm -rf %{buildroot}

# ruby-19
%if %{build19}
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
   %{buildroot}%{bindir19}/
%endif
%endif

# ruby-20
%if %{build20}
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
   %{buildroot}%{bindir20}/
%endif
%endif

# ruby-21
%if %{build21}
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
   %{buildroot}%{bindir21}/
%endif
%endif

# ruby-22
%if %{build22}
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir22}
cp -a .%{bindir22}/* \
   %{buildroot}%{bindir22}/
%endif
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)

%if %{build19}
%files 19-old
%defattr(0755,root,bin,-)

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9
%endif

%if %{build20}
%files 20-old
%defattr(0755,root,bin,-)

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0
%endif

%if %{build21}
%files 21-old
%defattr(0755,root,bin,-)

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1
%endif

%if %{build22}
%files 22-old
%defattr(0755,root,bin,-)

%files 22
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2
%endif

%changelog
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2015.4
- make generating package selectable
* Wed Mar 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2015.1 and generate package for ruby-22
* Sat Dec 13 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
