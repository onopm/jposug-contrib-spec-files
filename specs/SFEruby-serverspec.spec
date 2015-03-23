%include Solaris.inc
%include default-depend.inc

%define gemname serverspec

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}

Summary:          RSpec tests for your provisioned servers
Name:             SFEruby-%{gemname}
IPS_package_name: library/ruby-22/serverspec
Version:          2.12.0
License:          MIT License
# URL:              http://rubygems.org/gems/%{gemname}
URL:              http://serverspec.org/
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

BuildRequires:    runtime/ruby-22 = *
Requires:         runtime/ruby-22 = *
Requires:         library/ruby-22/rspec >= 3.0.0
Requires:         library/ruby-22/rspec-its
Requires:         library/ruby-22/rake
Requires:         library/ruby-22/highline
Requires:         library/ruby-22/specinfra >= 2.23.0
Requires:         library/ruby-22/multi_json

%description
RSpec tests for your provisioned servers

%package 19
IPS_package_name: library/ruby-19/serverspec
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-19 = *
Requires:         runtime/ruby-19 = *
Requires:         library/ruby-19/rspec >= 3.0.0
Requires:         library/ruby-19/rspec-its
Requires:         library/ruby-19/rake
Requires:         library/ruby-19/highline
Requires:         library/ruby-19/specinfra >= 2.23.0
Requires:         library/ruby-19/multi_json

%description 19
RSpec tests for your provisioned servers

%package 20
IPS_package_name: library/ruby-20/serverspec
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-20 = *
Requires:         runtime/ruby-20 = *
Requires:         library/ruby-20/rspec >= 3.0.0
Requires:         library/ruby-20/rspec-its
Requires:         library/ruby-20/rake
Requires:         library/ruby-20/highline
Requires:         library/ruby-20/specinfra >= 2.23.0
Requires:         library/ruby-20/multi_json

%description 20
RSpec tests for your provisioned servers

%package 21
IPS_package_name: library/ruby-21/serverspec
Summary:          RSpec tests for your provisioned servers
BuildRequires:    runtime/ruby-21 = *
Requires:         runtime/ruby-21 = *
Requires:         library/ruby-21/rspec >= 3.0.0
Requires:         library/ruby-21/rspec-its
Requires:         library/ruby-21/rake
Requires:         library/ruby-21/highline
Requires:         library/ruby-21/specinfra >= 2.23.0
Requires:         library/ruby-21/multi_json

%description 21
RSpec tests for your provisioned servers

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

pushd .%{gemdir19}/gems/%{gemname}-%{version}/bin/
ls
mv serverspec-init serverspec-init.bak
sed -e 's/\/usr\/bin\/env ruby/\/usr\/ruby\/1.9\/bin\/ruby/' < serverspec-init.bak > serverspec-init
rm serverspec-init.bak
popd

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

pushd .%{gemdir20}/gems/%{gemname}-%{version}/bin/
mv serverspec-init serverspec-init.bak
sed -e 's/\/usr\/bin\/env ruby/\/usr\/ruby\/2.0\/bin\/ruby/' < serverspec-init.bak > serverspec-init
rm serverspec-init.bak
popd

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

pushd .%{gemdir21}/gems/%{gemname}-%{version}/bin/
mv serverspec-init serverspec-init.bak
sed -e 's/\/usr\/bin\/env ruby/\/usr\/ruby\/2.1\/bin\/ruby/' < serverspec-init.bak > serverspec-init
rm serverspec-init.bak
popd

# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
    --no-ri \
    --no-rdoc \
    -V \
    --force %{SOURCE0}

pushd .%{gemdir22}/gems/%{gemname}-%{version}/bin/
mv serverspec-init serverspec-init.bak
sed -e 's/\/usr\/bin\/env ruby/\/usr\/ruby\/2.1\/bin\/ruby/' < serverspec-init.bak > serverspec-init
rm serverspec-init.bak
popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}

# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

pushd %{buildroot}/%{_bindir}
ln -s "../$( echo "%{geminstdir19}" | cut -d/ -f3-)/bin/serverspec-init" serverspec-init19
popd

mkdir -p %{buildroot}/%{bindir19}
pushd %{buildroot}/%{bindir19}
ln -s "../$( echo "%{geminstdir19}" | cut -d/ -f5-)/bin/serverspec-init" .
popd

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

pushd %{buildroot}/%{_bindir}
ln -s "../$( echo "%{geminstdir20}" | cut -d/ -f3-)/bin/serverspec-init" serverspec-init20
popd

mkdir -p %{buildroot}/%{bindir20}
pushd %{buildroot}/%{bindir20}
ln -s "../$( echo "%{geminstdir20}" | cut -d/ -f5-)/bin/serverspec-init" .
popd

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

pushd %{buildroot}/%{_bindir}
ln -s "../$( echo "%{geminstdir20}" | cut -d/ -f3-)/bin/serverspec-init" serverspec-init21
popd

mkdir -p %{buildroot}/%{bindir21}
pushd %{buildroot}/%{bindir21}
ln -s "../$( echo "%{geminstdir21}" | cut -d/ -f5-)/bin/serverspec-init" .
popd

# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

pushd %{buildroot}/%{_bindir}
ln -s "../$( echo "%{geminstdir20}" | cut -d/ -f3-)/bin/serverspec-init" serverspec-init22
popd

mkdir -p %{buildroot}/%{bindir22}
pushd %{buildroot}/%{bindir22}
ln -s "../$( echo "%{geminstdir22}" | cut -d/ -f5-)/bin/serverspec-init" .
popd

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/bin/serverspec-init22
/usr/ruby/2.2

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/bin/serverspec-init19
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/bin/serverspec-init20
/usr/ruby/2.0

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/bin/serverspec-init21
/usr/ruby/2.1

%changelog
* Tue Mar 24 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.12.0
* Sun Mar 22 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.11.0
* Sat Feb 28 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.10.0
* Sat Feb 28 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.9.1
* Wed Feb 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.2
* Sun Feb 01 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.8.1
* Fri Jan 23 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.7.2
- generate package for ruby-22
* Sun Dec 14 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- fix symbolic links
* Mon Dec 08 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.7.0
* Fri Dec 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.6.0
* Thu Dec 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.5.0
* Wed Nov 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.4.0
* Sun Sep 05 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.0
* Mon Sep 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.15.0
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.10.0
* Tue Jul 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.1
* Thu Jun 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.9.0
* Tue Jun 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.1
* Fri May 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.7.0
* Wed May 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4.2
* Tue Apr 15 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.3.0
* Mon Apr 07 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18
- bump to 1.1.0
* Fri Mar 28 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.0
* Tue Feb 25 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- build package for ruby-21
* Mon Feb 17 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.15.3
* Wed Jan 29 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.15.0
* Sun Jan 12 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.14.3
* Sun Dec 29 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.14.2
* Thu Dec 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.6
- bump to 0.13.7
* Tue Dec 17 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.4
- bump to 0.13.5
* Mon Dec 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.3
* Thu Dec 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.2
* Wed Dec 04 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.13.1
* Mon Dec 02 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.12.0
* Wed Nov 27 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.11.5 and modify shebang
* Mon Nov 18 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.11.4
* Thu Oct 31 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.13
* Fri Oct 18 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.8
* Thu Oct 17 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.6
* Wed Oct 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.5
* Tue Oct 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.4
* Tue Oct 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.8
* Thu Oct 03 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.7
* Wed Sep 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.9.6
* Thu Aug 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.6
* Tue Jul 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.7.0
* Mon Jul 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.28
* Fri Jul 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.22
* Wed Jun 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.10
* Tue Jun 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.7
* Wed Jun 19 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.4
- bump to 0.6.5
* Fri Jun 14 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.6.2
* Mon Jun 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.5
- bump to 0.5.6
* Thu Jun 06 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.0
* Tue May 28 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.12
* Sat May 25 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.10
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.9
- generate package for ruby-20
* Mon May 20 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.7
* Fri May 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.4.0
* Tue May 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.3.1
* Fri May 10 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.26
* Wed May 08 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.24
* Tue May 07 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.23
* Mon May 06 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.22
* Wed May 01 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.17
* Wed Apr 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.16
* Wed Apr 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.13
* Mon Apr 15 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.9
* Fri Apr 12 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.7 and add Requires
* Thu Apr  9 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.2.3
* Thu Apr  4 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.1.6
* Sat Mar 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.0.17
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
