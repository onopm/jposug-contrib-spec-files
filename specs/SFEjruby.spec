%include Solaris.inc

Name:			SFEjruby
IPS_package_name:       runtime/jruby
Version:		9.0.4.0
Summary:		The Ruby Programming Language on the JVM
License:		Ruby license
URL:			http://jruby.org/
Source:		http://jruby.org.s3.amazonaws.com/downloads/%{version}/jruby-bin-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  developer/java/jdk
Requires:	runtime/jre

%description
The Ruby Programming Language on the JVM

%prep
%setup -q -n jruby-%{version}

%build

# ls bin/
rm bin/*{.bat,.exe,.dll,.bash}

pushd bin
for i in ./*
do
    mv ${i} ${i}.bak
    sed -e "s!^\#\!/usr/bin/env jruby\$!\#\!/usr/jruby/bin/jruby!" \
        ${i}.bak > ${i}
    rm ${i}.bak
done

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/jruby/share

cp -r bin lib %{buildroot}/usr/jruby
#cp -r tool %{buildroot}/usr/jruby
# cp -r docs samples COPYING LICENSE.RUBY %{buildroot}/usr/jruby/share
cp -r samples COPYING LICENSE.RUBY %{buildroot}/usr/jruby/share

mkdir -p %{buildroot}/usr/bin
cd %{buildroot}/usr/bin
ln -s ../jruby/bin/jruby .
ln -s ../jruby/bin/jgem .
ln -s ../jruby/bin/jirb .

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*
%dir %attr (0755, root, bin) /usr/jruby
%dir %attr (0755, root, bin) /usr/jruby/bin
%attr (0755, root, bin) /usr/jruby/bin/*
%attr (0755, root, bin) /usr/jruby/lib
# %attr (0755, root, bin) /usr/jruby/tool
%attr (0755, root, bin) /usr/jruby/share

%changelog
* Sun Dec 27 2015 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify shebang and add symbolic links
* Mon Dec 14 2015 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.0.4.0
* Mon Jul 14 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
