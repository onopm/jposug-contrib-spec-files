%include Solaris.inc
%include default-depend.inc

%define gemname cool.io

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

Summary: A Cool.io provides a high performance event framework for Ruby which uses the libev C library
Name: SFEruby-coolio
IPS_package_name:        library/ruby-19/cool.io
Version: 1.2.2
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-19
Requires:       runtime/ruby-19
# Requires:       library/ruby-19/iobuffer >= 1.0.0

%description
Cool.io provides a high performance event framework for Ruby which uses the libev C library

%package 20
IPS_package_name: library/ruby-20/cool.io
Summary: %{gemname}
BuildRequires:	runtime/ruby-20
Requires:	runtime/ruby-20
#Requires:       library/ruby-20/iobuffer >= 1.0.0

%description 20
Cool.io provides a high performance event framework for Ruby which uses the libev C library

%prep
%setup -q -c -T
mkdir -p .%{gemdir19}
mkdir -p .%{bindir19}
mkdir -p .%{gemdir20}
mkdir -p .%{bindir20}

%build
# export CONFIGURE_ARGS="--with-cflags='%{optflags}'"

# ruby-19
/usr/ruby/1.9/bin/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --force %{SOURCE0}

# ruby-20
/usr/ruby/2.0/bin/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
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

# rm -rf %{buildroot}%{geminstdir}/.yardoc/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%changelog
* Fri Apr 18 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.2.2 and stop to generate package for ruby-18
* Sun Oct 06 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.1.1
* Wed Nov 14 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
