%include Solaris.inc
%include default-depend.inc

%define gemname multipart-post
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

Summary: Use with Net::HTTP to do multipart form posts.
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-22/multipart-post
Version: 2.0.0
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: runtime/ruby-22
Requires:      runtime/ruby-22


%description
Use with Net::HTTP to do multipart form posts. IO values that have #content_type, #original_filename, and #local_path will be posted as a binary file.

%package 19
IPS_package_name: library/ruby-19/multipart-post
Summary: Use with Net::HTTP to do multipart form posts.
BuildRequires: runtime/ruby-19
Requires:      runtime/ruby-19

%description 19
Use with Net::HTTP to do multipart form posts. IO values that have #content_type, #original_filename, and #local_path will be posted as a binary file.

%package 20
IPS_package_name: library/ruby-20/multipart-post
Summary: Use with Net::HTTP to do multipart form posts.
BuildRequires: runtime/ruby-20
Requires:      runtime/ruby-20

%description 20
Use with Net::HTTP to do multipart form posts. IO values that have #content_type, #original_filename, and #local_path will be posted as a binary file.

%package 21
IPS_package_name: library/ruby-21/multipart-post
Summary: Use with Net::HTTP to do multipart form posts.
BuildRequires: runtime/ruby-21
Requires:      runtime/ruby-21

%description 21
Use with Net::HTTP to do multipart form posts. IO values that have #content_type, #original_filename, and #local_path will be posted as a binary file.

%prep
%setup -q -c -T

%build
# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    -V \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    -V \
    --force %{SOURCE0}

# ruby-22
%{bindir22}/gem install --local \
    --install-dir .%{gemdir22} \
    --bindir .%{bindir22} \
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
* Tue Mar 10 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.0 and generate package for ruby-22
* Sun Apr 20 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for ruby-20 and ruby-21 instead of ruby-18
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
