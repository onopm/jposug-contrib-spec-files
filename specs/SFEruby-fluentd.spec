%include Solaris.inc

%define gemname fluentd
%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

%define tarball_name    fluentd
%define tarball_version 0.10.57

Name:             SFEfluentd
IPS_package_name: system/fluentd
Summary:          Fluentd is a log collector daemon written in Ruby.
Version:          %{tarball_version}
License:          Apache License, Version 2.0
URL:              http://fluentd.org/
Source0:          http://rubygems.org/downloads/%{tarball_name}-%{tarball_version}.gem
Source1:          fluentd.xml
Source2:          svc-fluentd
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Fluentd is a log collector daemon written in Ruby. Fluentd receives logs as JSON streams, buffers them, and sends them to other systems like MySQL, MongoDB, or even other instances of Fluentd.

BuildRequires:	runtime/ruby-21
BuildRequires:	library/ruby-21/jeweler
BuildRequires:	library/ruby-21/rr
BuildRequires:	library/ruby-21/timecop
BuildRequires:	library/text/yaml >= 0.1.6
Requires:	runtime/ruby-21
Requires:	library/ruby-21/cool.io >= 1.1.1
Requires:	library/ruby-21/http_parser.rb >= 0.5.1
Requires:	library/ruby-21/json >= 1.4.3
Requires:	library/ruby-21/msgpack >= 0.5.8
Requires:	library/ruby-21/sigdump >= 0.2.2
Requires:	library/ruby-21/yajl-ruby >= 1.0
Requires:	library/ruby-21/tzinfo >= 1.0.0
Requires:	library/ruby-21/tzinfo-data >= 1.0.0

%prep
%setup -q -c -T

mkdir -p .%{gemdir21}
%{bindir21}/gem install --local --install-dir .%{gemdir21} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

pushd usr/bin
for i in fluent*
do
    cat ${i} | sed -e 's$#!/usr/bin/env ruby$#!/usr/ruby/2.1/bin/ruby$' > ${i}.tmp
    mv ${i}.tmp ${i}
done
popd

pushd usr/ruby/2.1/lib/%{_arch64}/ruby/gems/2.1.0/gems/fluentd-%{version}/bin
for i in fluent*
do
    cat ${i} | sed -e 's$#!/usr/bin/env ruby$#!/usr/ruby/2.1/bin/ruby$' > ${i}.tmp
    mv ${i}.tmp ${i}
done
popd


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/bin
cp -a ./usr/bin/* \
        %{buildroot}/usr/bin/

mkdir -p %{buildroot}%{gemdir21}
cp -a .%{gemdir21}/* \
        %{buildroot}%{gemdir21}/

rm -rf %{buildroot}%{geminstdir21}/.yardoc/

# SMF
mkdir -p %{buildroot}/lib/svc/manifest/system
cp %{SOURCE1} %{buildroot}/lib/svc/manifest/system/

mkdir -p %{buildroot}/lib/svc/method
cp %{SOURCE2} %{buildroot}/lib/svc/method/

# log
mkdir -p %{buildroot}/var/log/fluentd

# config
mkdir -p %{buildroot}/etc/fluentd

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%dir %attr(0755, root, sys) /usr
%dir %attr(0755, root, bin) /usr/bin
%attr(0555, root, bin) /usr/bin/fluent-cat
%attr(0555, root, bin) /usr/bin/fluent-debug
%attr(0555, root, bin) /usr/bin/fluent-gem
%attr(0555, root, bin) /usr/bin/fluentd
%{gemdir21}
%dir %attr(0755, root, bin) /lib/
%dir %attr(0755, root, bin) /lib/svc
%dir %attr(0755, root, sys) /lib/svc/manifest
%dir %attr(0755, root, sys) /lib/svc/manifest/system
%attr(0444, root, sys) /lib/svc/manifest/system/fluentd.xml
%dir %attr(0755, root, bin) /lib/svc/method
%attr(0555, root, bin) /lib/svc/method/svc-fluentd
%dir %attr(0755, root, sys) /var
%dir %attr(0755, root, sys) /var/log/
%dir %attr(0755, root, sys) /var/log/fluentd
%dir %attr(0755, root, sys) /etc
%dir %attr(0755, root, sys) /etc/fluentd

%changelog
* Thu Dec 04 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.57
* Mon Nov 03 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.56 and use ruby-21 instead of ruby-19
* Thu Apr 03 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.45
- specify required version of library/text/yaml (CVE-2014-2525)
* Sat Feb 08 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.43
* San Feb 02 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add SMF manifest and method
* Thu Jan 30 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.42
* Sun Nov 17 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.40
* Tue Oct 15 2013 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.39
- modify shebang to use ruby-19
- add /usr/bin/fluent*
* Wed Dec 12 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.30
* Wed Dec 05 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.10.29
* Wed Nov 21 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify Name and IPS_package_name
* Wed Nov 14 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
