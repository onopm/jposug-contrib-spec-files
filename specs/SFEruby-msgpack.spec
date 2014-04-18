%include Solaris.inc

%define gemname msgpack

%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define gemdir20 %(/usr/ruby/2.0/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

Name: SFEruby-msgpack
IPS_package_name:        library/ruby-19/msgpack
Summary: MessagePack is an efficient binary serialization format.
Version: 0.5.8
License: ASL 2.0
Group: System Environment/Base
URL:     http://msgpack.org/
Source0: http://rubygems.org/downloads/msgpack-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires: runtime/ruby-19
BuildRequires: runtime/ruby-19

%description
MessagePack is an efficient binary serialization format. It lets you exchange data among multiple languages like JSON but it's faster and smaller. For example, small integers (like flags or error code) are encoded into a single byte, and typical short strings only require an extra byte in addition to the strings themselves.

%package 20
IPS_package_name: library/ruby-20/msgpack
Summary: MessagePack for Ruby 2.0
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20

%prep
%setup -q -c -T
# ruby 1.9
mkdir -p .%{gemdir19}
/usr/ruby/1.9/bin/gem install --local --install-dir .%{gemdir19} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

# ruby 2.0
mkdir -p .%{gemdir20}
/usr/ruby/2.0/bin/gem install --local --install-dir .%{gemdir20} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}


%build

%install
rm -rf %{buildroot}

# 1.9
mkdir -p %{buildroot}%{gemdir19}
cp -a .%{gemdir19}/* \
        %{buildroot}%{gemdir19}/

# mkdir -p %{buildroot}%{_bindir}
# cp -a .%{_bindir}/* \
#         %{buildroot}%{_bindir}/

# 2.0
mkdir -p %{buildroot}%{gemdir20}
cp -a .%{gemdir20}/* \
        %{buildroot}%{gemdir20}/

rm -rf %{buildroot}%{geminstdir19}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr(0755, root, sys) /usr
%{gemdir19}

# 2.0
%files 20
%defattr(0755,root,bin,-)
%dir %attr(0755, root, sys) /usr
%{gemdir20}

%changelog
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18
* Thu Jan 30 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.8
* Wed Oct 16 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.6
* Sat Jan 05 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.5.1
* Mon Nov 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify IPS package_name
* Sun Nov 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use full path to gem
* Sun Jun 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
