%include Solaris.inc

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%{!?ruby_sitelibdir: %define ruby19_sitelibdir %(ruby19 -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')}

%define gemname msgpack
%define gemdir18 %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir19}/gems/%{gemname}-%{version}
%define gemdir19 %(ruby19 -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

Name: SFEruby-msgpack
IPS_package_name:        library/ruby/msgpack
Summary: MessagePack is an efficient binary serialization format.
Version: 0.4.7
License: ASL 2.0
Group: System Environment/Base
URL:     http://msgpack.org/
Source0: http://rubygems.org/downloads/msgpack-0.4.7.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires: runtime/ruby-18
BuildRequires: runtime/ruby-18

%description
MessagePack is an efficient binary serialization format. It lets you exchange data among multiple languages like JSON but it's faster and smaller. For example, small integers (like flags or error code) are encoded into a single byte, and typical short strings only require an extra byte in addition to the strings themselves.

%package 18
IPS_package_name: library/ruby/msgpack-18
Summary: MessagePack for Ruby 1.8
BuildRequires:	runtime/ruby-18
Requires:	runtime/ruby-18

%package 19
IPS_package_name: library/ruby/msgpack-19
Summary: MessagePack for Ruby 1.9
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%prep
%setup -q -c -T
# ruby 1.8
mkdir -p .%{gemdir18}
/usr/ruby/1.8/bin/gem install --local --install-dir .%{gemdir18} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

mkdir -p .%{gemdir19}
/usr/ruby/1.9/bin/gem install --local --install-dir .%{gemdir19} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}


%build

%install
rm -rf %{buildroot}

# 1.8
mkdir -p %{buildroot}%{gemdir18}
cp -a .%{gemdir18}/* \
        %{buildroot}%{gemdir18}/

# mkdir -p %{buildroot}%{_bindir}
# cp -a .%{_bindir}/* \   
#         %{buildroot}%{_bindir}/

rm -rf %{buildroot}%{geminstdir18}/.yardoc/
rm -rf %{buildroot}%{gemdir18}/doc

# 1.9
mkdir -p %{buildroot}%{gemdir19}
cp -a .%{gemdir19}/* \
        %{buildroot}%{gemdir19}/

# mkdir -p %{buildroot}%{_bindir}
# cp -a .%{_bindir}/* \   
#         %{buildroot}%{_bindir}/

rm -rf %{buildroot}%{geminstdir19}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
# %dir %{geminstdir18}
%dir %attr (0755, root, sys) /var
# 1.8
%files 18
%defattr(0755,root,bin,-)
# %{gemdir18}/doc/%{gemname}-%{version}
%dir %attr (0755, root, sys) /var
%{gemdir18}/gems/%{gemname}-%{version}/
%{gemdir18}/cache/%{gemname}-%{version}.gem
%{gemdir18}/specifications/%{gemname}-%{version}.gemspec

# 1.9
%files 19
%defattr(0755,root,bin,-)
%dir %attr(0755, root, sys) /usr
%{gemdir19}

%changelog
* Sun Nov 11 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- use full path to gem
* Sun Jun 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
