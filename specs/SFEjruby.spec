%include Solaris.inc

Name:			SFEjruby
IPS_package_name:       runtime/jruby
Version:		9.1.15.0
Summary:		The Ruby Programming Language on the JVM
License:		Ruby license
URL:			http://jruby.org/
Source:		http://jruby.org.s3.amazonaws.com/downloads/%{version}/jruby-bin-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  developer/java/jdk-8
Requires:	runtime/java/jre-8
Requires:       shell/bash

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
    sed -e "s!^\#\!/usr/bin/env jruby\$!\#\!/opt/jposug/jruby/bin/jruby!" \
        ${i}.bak > ${i}
    rm ${i}.bak
done

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/opt/jposug/jruby/share

cp -r bin lib %{buildroot}/opt/jposug/jruby
#cp -r tool %{buildroot}/opt/jposug/jruby
# cp -r docs samples COPYING LICENSE.RUBY %{buildroot}/opt/jposug/jruby/share
cp -r samples COPYING LICENSE.RUBY %{buildroot}/opt/jposug/jruby/share

mkdir -p %{buildroot}/usr/bin
cd %{buildroot}/usr/bin
ln -s ../../opt/jposug/jruby/bin/jruby .
ln -s ../../opt/jposug/jruby/bin/jgem .
ln -s ../../opt/jposug/jruby/bin/jirb .

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*
%dir %attr (0755, root, bin) /opt/jposug/jruby
%dir %attr (0755, root, bin) /opt/jposug/jruby/bin
%attr (0755, root, bin) /opt/jposug/jruby/bin/*
%attr (0755, root, bin) /opt/jposug/jruby/lib
# %attr (0755, root, bin) /opt/jposug/jruby/tool
%attr (0755, root, bin) /opt/jposug/jruby/share

%changelog
* Tue Jan 30 2018 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.1.15.0
* Wed Jul 05 2017 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.1.12.0
* Tue Feb 21 2017 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.1.7.0
* Sun Dec 27 2015 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- modify shebang and add symbolic links
* Mon Dec 14 2015 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 9.0.4.0
* Mon Jul 14 2014 Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
