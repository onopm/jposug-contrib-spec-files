%include Solaris.inc
%include default-depend.inc

%define gemname coderay
%define generate_executable 0

%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}

%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}

%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}

Summary: Fast and easy syntax highlighting for selected languages, written in Ruby. 
Name: SFEruby-%{gemname}
IPS_package_name:        library/ruby-21/coderay
Version: 1.0.9
License: MIT License
URL: http://rubygems.org/gems/%{gemname}
Source0: http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires: runtime/ruby-21
Requires:      runtime/ruby-21


%description
Fast and easy syntax highlighting for selected languages, written in Ruby. Comes with RedCloth integration and LOC counter.

%package 19
IPS_package_name: library/ruby-19/coderay
Summary: Fast and easy syntax highlighting for selected languages, written in Ruby. 
BuildRequires: runtime/ruby-19
Requires:      runtime/ruby-19

%description 19
Fast and easy syntax highlighting for selected languages, written in Ruby. Comes with RedCloth integration and LOC counter.

%package 20
IPS_package_name: library/ruby-20/coderay
Summary: Fast and easy syntax highlighting for selected languages, written in Ruby. 
BuildRequires: runtime/ruby-20
Requires:      runtime/ruby-20

%description 20
Fast and easy syntax highlighting for selected languages, written in Ruby. Comes with RedCloth integration and LOC counter.

%prep
%setup -q -c -T

%build

# ruby-19
%{bindir19}/gem install --local \
    --install-dir .%{gemdir19} \
    --bindir .%{bindir19} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-20
%{bindir20}/gem install --local \
    --install-dir .%{gemdir20} \
    --bindir .%{bindir20} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

# ruby-21
%{bindir21}/gem install --local \
    --install-dir .%{gemdir21} \
    --bindir .%{bindir21} \
    --no-rdoc \
    --no-ri \
    -V \
    --force %{SOURCE0}

%install
rm -rf %{buildroot}

%if %generate_executable
mkdir -p %{buildroot}/usr/bin
%endif
# ruby-19
mkdir -p %{buildroot}/%{gemdir19}
cp -a .%{gemdir19}/* \
    %{buildroot}/%{gemdir19}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir19}
cp -a .%{bindir19}/* \
    %{buildroot}%{bindir19}/

pushd %{buildroot}/usr/bin
for i in  ../ruby/1.9/bin/*
do
    ln -s ${i} $(basename ${i})19
done
popd
%endif

# ruby-20
mkdir -p %{buildroot}/%{gemdir20}
cp -a .%{gemdir20}/* \
    %{buildroot}/%{gemdir20}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir20}
cp -a .%{bindir20}/* \
   %{buildroot}%{bindir20}/
pushd %{buildroot}/usr/bin
for i in  ../ruby/2.0/bin/*
do
    ln -s ${i} $(basename ${i})20
done
popd
%endif

# ruby-21
mkdir -p %{buildroot}/%{gemdir21}
cp -a .%{gemdir21}/* \
    %{buildroot}/%{gemdir21}/

%if %generate_executable
mkdir -p %{buildroot}%{bindir21}
cp -a .%{bindir21}/* \
   %{buildroot}%{bindir21}/
pushd %{buildroot}/usr/bin
for i in  ../ruby/2.1/bin/*
do
    ln -s ${i} $(basename ${i})21
done
popd
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %generate_executable
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*21
%endif
/usr/ruby/2.1

%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %generate_executable
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*19
%endif
/usr/ruby/1.9

%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%if %generate_executable
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*20
%endif
/usr/ruby/2.0

%changelog
* Wed Dec 24 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- stop to generate package for ruby-18 and generate package for ruby-20 and ruby-21
* Tue May 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
