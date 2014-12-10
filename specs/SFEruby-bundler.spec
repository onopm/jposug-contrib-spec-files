%include Solaris.inc
%include default-depend.inc

%define gemname bundler
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby-21/bundler
Version:          1.5.3
License:          MIT
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires: runtime/ruby-21
Requires:      runtime/ruby-21

%description
Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably

%package 19
IPS_package_name: library/ruby-19/bundler
Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
BuildRequires:	  runtime/ruby-19
Requires:	  runtime/ruby-19

%package 20
IPS_package_name: library/ruby-20/bundler
Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
BuildRequires:	  runtime/ruby-20
Requires:	  runtime/ruby-20

%package 21
IPS_package_name: library/ruby-21/bundler
Summary:          Bundler manages an application's dependencies through its entire life, across many machines, systematically and repeatably
BuildRequires:	  runtime/ruby-21
Requires:	  runtime/ruby-21

%prep
%setup -q -c -T

%build

/usr/ruby/1.9/bin/gem install --local --install-dir .%{gemdir19} \
    --bindir ./usr/ruby/1.9/bin \
    --no-ri \
    --no-rdoc \
    --force %{SOURCE0}

/usr/ruby/2.0/bin/gem install --local --install-dir .%{gemdir20} \
    --bindir ./usr/ruby/2.0/bin \
    --no-ri \
    --no-rdoc \
    --force %{SOURCE0}

%{bindir21}/gem install --local --install-dir .%{gemdir21} \
    --bindir ./%{bindir21} \
    --no-ri \
    --no-rdoc \
    --force %{SOURCE0}


%install
rm -rf %{buildroot}

# 1.9
mkdir -p %{buildroot}%{gemdir19}
mkdir -p %{buildroot}/usr/ruby/1.9/bin
cp -a .%{gemdir19}/* \
        %{buildroot}%{gemdir19}/

rm -rf %{buildroot}%{geminstdir19}/.yardoc/
rm -rf %{buildroot}%{gemdir19}/doc

# 2.0
mkdir -p %{buildroot}%{gemdir20}
mkdir -p %{buildroot}/usr/ruby/2.0/bin
cp -a .%{gemdir20}/* \
        %{buildroot}%{gemdir20}/

rm -rf %{buildroot}%{geminstdir20}/.yardoc/
rm -rf %{buildroot}%{gemdir20}/doc

# 2.1
mkdir -p %{buildroot}%{gemdir21}
mkdir -p %{buildroot}%{bindir21}
cp -a .%{gemdir21}/* \
        %{buildroot}%{gemdir21}/

rm -rf %{buildroot}%{geminstdir21}/.yardoc/
rm -rf %{buildroot}%{gemdir21}/doc

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%changelog
* Wed Dec 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- not generate package for ruby-18
* Tue Feb 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate package for ruby-21
* Wed Feb 19 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.5.3
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.5
* Sat Mar 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.4
* Mon Feb 04 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify to success building packages
* Thu Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
