#
# spec file for package SFEruby-hoe
#
%include Solaris.inc
%include default-depend.inc

%define with_ruby18 0
%define gemname hoe
%if %with_ruby18
%define gemdir18 %(/usr/ruby/1.8/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir18 %{gemdir18}/gems/%{gemname}-%{version}
%define bindir18 /usr/ruby/1.8/bin
%endif
%define gemdir19 %(/usr/ruby/1.9/bin/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%define bindir19 /usr/ruby/1.9/bin

Summary: Hoe is a rake/rubygems helper for project Rakefiles
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby/hoe
SUNW_Copyright:   %name.copyright
Version: 3.12.0
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if %with_ruby18
%package 18
BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage, maintain, and release your project and includes a dynamic plug-in system allowing for easy extensibility. Hoe ships with plug-ins for all your usual project tasks including rdoc generation, testing, packaging, deployment, and announcement.. See class rdoc for help. Hint: `ri Hoe` or any of the plugins listed below. For extra goodness, see: http://seattlerb.rubyforge.org/hoe/Hoe.pdf
%endif

%package 19
IPS_package_name: library/ruby-19/hoe
Summary: Hoe is a rake/rubygems helper for project Rakefiles
BuildRequires:	runtime/ruby-19
Requires:	runtime/ruby-19

%description 19
Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage, maintain, and release your project and includes a dynamic plug-in system allowing for easy extensibility. Hoe ships with plug-ins for all your usual project tasks including rdoc generation, testing, packaging, deployment, and announcement.. See class rdoc for help. Hint: `ri Hoe` or any of the plugins listed below. For extra goodness, see: http://seattlerb.rubyforge.org/hoe/Hoe.pdf

%prep
%setup -q -c -T
%if %with_ruby18
mkdir -p .%{gemdir18}
mkdir -p .%{bindir18}
%endif
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}

%build
# export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

# ruby-18
%if %with_ruby18
/usr/ruby/1.8/bin/gem install --local \
    --install-dir .%{gemdir18} \
    --bindir .%{bindir18} \
    -V \
    --force %{SOURCE0}
%endif

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

# ruby-18
%if %with_ruby18
mkdir -p %{buildroot}/%{gemdir18}
cp -a .%{gemdir18}/* \
    %{buildroot}/%{gemdir18}/

mkdir -p %{buildroot}%{bindir18}
cp -a .%{bindir18}/* \
    %{buildroot}%{bindir18}/
%endif
# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}%{bindir19}/

rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%if %with_ruby18
%files 18
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /var
%attr (0755, root, bin) /var/ruby/1.8/gem_home
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8
%endif

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%changelog
* Thr June 05 2014 - YAMAMOTO Takashi <yamachan@selfnavi.com>
- Bump to 3.12.0
- Add tag SUNW_Copyright
- Add switch with_ruby18, set default version 1.9.
* Wed Jan 23 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
