%include Solaris.inc
%include default-depend.inc

%define gemname specinfra

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary:          Common layer for serverspec and configspec
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby-21/specinfra
Version:          2.10.0
License:          MIT License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:    runtime/ruby-21
Requires:         runtime/ruby-21 = *
Requires:         library/ruby-21/net-ssh
Requires:         library/ruby-21/net-scp

%description
Common layer for serverspec and configspec

%package 19
IPS_package_name: library/ruby-19/specinfra
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-19
Requires:         runtime/ruby-19 = *
Requires:         library/ruby-19/net-ssh
Requires:         library/ruby-19/net-scp

%description 19
Common layer for serverspec and configspec

%package 20
IPS_package_name: library/ruby-20/specinfra
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-20
Requires:         runtime/ruby-20 = *
Requires:         library/ruby-20/net-ssh
Requires:         library/ruby-20/net-scp

%description 20
Common layer for serverspec and configspec

%prep
%setup -q -c -T

%build
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

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
* Fri Dec 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.0
* Wed Dec 03 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.9.2
* Wed Nov 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.0
* Thu Nov 02 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.2
* Thu Sep 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.2.2
- bump to 2.2.1
* Sun Sep 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.0
* Mon Sep 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.26.0
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.20.0
* Mon Jul 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.19.0
* Tue Jul 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.18.3
* Fri Jun 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.18.2
* The Jun 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.18.0
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.16.0
* Fri May 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.15.0
* Wed May 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.0
* Sun Apr 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.1
* Tue Apr 15 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.0
* Mon Apr 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.4
- stop to generate package for ruby-18
* Fri Mar 28 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
* Thu Mar 27 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.8.0
* Wed Mar 19 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.2
* Sat Feb 22 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.0 and build package for ruby-21
* Sat Feb 22 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.1
* Mon Feb 17 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.8
* Sun Jan 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.1
* Sun Jan 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.1
* Thu Jan 09 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.0
* Sun Dec 29 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.1.1
* Sat Dec 21 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.17
* Thu Dec 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.16
* Tue Dec 17 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.14
- bump to 0.0.15
* Mon Dec 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.12
- bump to 0.0.13
* Thu Dec 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.8
* Wed Dec 04 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.7
- bump to 0.0.6
* Mon Dec 02 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
