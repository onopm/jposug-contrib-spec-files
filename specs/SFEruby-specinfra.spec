%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1

%define gemname specinfra

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

Summary:          Common layer for serverspec and configspec
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby/specinfra
Version:          2.36.4
License:          MIT License
URL:              http://rubygems.org/gems/%{gemname}
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:    runtime/ruby-22
Requires:         runtime/ruby-22 = *

%description
Common layer for serverspec and configspec

%if %{build19}
%package 19-old
IPS_package_name: library/ruby-19/specinfra
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-19
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/specinfra-19 >= %{version}

%description 19-old
Common layer for serverspec and configspec

%package 19
IPS_package_name: library/ruby/specinfra-19
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-19
Requires:         runtime/ruby-19 = *
Requires:         library/ruby/net-ssh-19
Requires:         library/ruby/net-scp-19

%description 19
Common layer for serverspec and configspec
%endif

%if %{build20}
%package 20-old
IPS_package_name: library/ruby-20/specinfra
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-20
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/specinfra-20 >= %{version}

%description 20-old
Common layer for serverspec and configspec

%package 20
IPS_package_name: library/ruby/specinfra-20
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-20
Requires:         runtime/ruby-20 = *
Requires:         library/ruby/net-ssh-20
Requires:         library/ruby/net-scp-20

%description 20
Common layer for serverspec and configspec
%endif

%if %{build21}
%package 21-old
IPS_package_name: library/ruby-21/specinfra
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-21
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/specinfra-21 >= %{version}

%description 21-old
Common layer for serverspec and configspec

%package 21
IPS_package_name: library/ruby/specinfra-21
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-21
Requires:         runtime/ruby-21 = *
Requires:         library/ruby/net-ssh-21
Requires:         library/ruby/net-scp-21

%description 21
Common layer for serverspec and configspec
%endif

%if %{build22}
%package 22-old
IPS_package_name: library/ruby-22/specinfra
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-22
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/specinfra-22 >= %{version}

%description 22-old
Common layer for serverspec and configspec

%package 22
IPS_package_name: library/ruby/specinfra-22
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-22
Requires:         runtime/ruby-22 = *
Requires:         library/ruby/net-ssh-22
Requires:         library/ruby/net-scp-22

%description 22
Common layer for serverspec and configspec
%endif


%prep
%setup -q -c -T

%build
%if %{build19}
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build20}
# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build21}
# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%if %{build22}
# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}
%endif

%install
rm -rf %{buildroot}

%if %{build19}
# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/
%endif

%if %{build20}
# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/
%endif

%if %{build21}
# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/
%endif

%if %{build22}
# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/
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
* Wed Jun 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.36.4
* Tue Jun 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.36.3
* Mon Jun 22 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.36.1
* Fri Jun 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Requires according to changes of IPS packagename
* Thu Jun 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.35.1
* Tue Jun 09 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.34.8
* Mon Jun 08 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.34.7
- rename IPS_package_names and keep old name packages to resolve dependency
* Sun May 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.34.2
* Tue May 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.31.1
* Tue Mar 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.24.2
- bump to 2.25.0
* Sun Mar 22 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.21.0
* Fri Mar 06 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.18.2
* Tue Mar 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.18.0
* Sat Feb 28 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.15.2
* Wed Feb 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.12.6
* Sun Feb 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.12.3
* Fri Jan 23 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.11.8
- generate package for ruby-22
* Wed Dec 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.2
* Mon Dec 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.1
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
