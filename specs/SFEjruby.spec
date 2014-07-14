%include Solaris.inc

Name:			SFEjruby
IPS_package_name:       runtime/jruby
Version:		1.7.13
Summary:		The Ruby Programming Language on the JVM
License:		Ruby license
URL:			http://jruby.org/
Source:		http://jruby.org.s3.amazonaws.com/downloads/%{version}/jruby-bin-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:	runtime/jre


%description
The Ruby Programming Language on the JVM

%prep
%setup -q -n jruby-%{version}

%build

ls bin/
rm bin/*{.bat,.exe,.dll,.bash}


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/jruby/share

cp -r bin lib %{buildroot}/usr/jruby
#cp -r tool %{buildroot}/usr/jruby
cp -r docs samples COPYING LICENSE.RUBY %{buildroot}/usr/jruby/share

# mkdir -p %{buildroot}/usr/bin
# cd %{buildroot}/usr/bin
# ln -s ../jruby/bin/jruby .
# ln -s ../jruby/bin/jgem .
# xln -s ../jruby/bin/jirb .

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) /usr
# %dir %attr (0755, root, bin) /usr/bin
%dir %attr (0755, root, bin) /usr/jruby
%dir %attr (0755, root, bin) /usr/jruby/bin
# %attr (0755, root, bin) /usr/bin/*
%attr (0755, root, bin) /usr/jruby/bin/*
%attr (0755, root, bin) /usr/jruby/lib
# %attr (0755, root, bin) /usr/jruby/tool
%attr (0755, root, bin) /usr/jruby/share

%changelog
* Mon Jul 14 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
