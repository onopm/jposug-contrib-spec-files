%include Solaris.inc
%include default-depend.inc

%define gemname rmagick

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

Summary: RMagick is an interface between Ruby and ImageMagick.
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-22/rmagick
Version: 2.13.4
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-22
BuildRequires:	image/imagemagick
Requires:       runtime/ruby-22
Requires:	image/imagemagick

%description
RMagick is an interface between Ruby and ImageMagick.

%package 19
IPS_package_name: library/ruby-19/rmagick
Summary: RMagick is an interface between Ruby and ImageMagick.
BuildRequires:	runtime/ruby-19
BuildRequires:	image/imagemagick
Requires:       runtime/ruby-19
Requires:	image/imagemagick

%description 19
RMagick is an interface between Ruby and ImageMagick.

%package 20
IPS_package_name: library/ruby-20/rmagick
Summary: RMagick is an interface between Ruby and ImageMagick.
BuildRequires:	runtime/ruby-20
BuildRequires:	image/imagemagick
Requires:       runtime/ruby-20
Requires:	image/imagemagick

%description 20
RMagick is an interface between Ruby and ImageMagick.

%package 21
IPS_package_name: library/ruby-21/rmagick
Summary: RMagick is an interface between Ruby and ImageMagick.
BuildRequires:	runtime/ruby-21
BuildRequires:	image/imagemagick
Requires:       runtime/ruby-21
Requires:	image/imagemagick

%description 21
RMagick is an interface between Ruby and ImageMagick.

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

# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
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

# ruby-22
mkdir -p %{buildroot}/%{gemdir22}
cp -a .%{gemdir22}/* \
    %{buildroot}/%{gemdir22}/

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0

%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1

%changelog
* Tue Mar 03 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.13.4
* Tue Oct 29 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
