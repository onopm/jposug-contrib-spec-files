%include Solaris.inc
%include default-depend.inc

%define tarball_name node
%define major_version 7


%define oracle_solaris_11 %(grep 'Oracle Solaris 11' /etc/release > /dev/null ; if [ $? -eq 0 ]; then echo '1'; else echo '0'; fi)

Summary:          Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
Name:             SFEnodejs-%{major_version}
IPS_package_name: runtime/node.js-%{major_version}
Version:          7.10.0
License:          MIT License
URL:              http://nodejs.org/
Source0:          https://nodejs.org/dist/v%{verson}/node-v%{version}.tar.xz
Patch0:           nodejs-7-add-defines.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-build
SUNW_Copyright:   %{name}.copyright

%description
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient.
Node.js' package ecosystem, npm, is the largest ecosystem of open source libraries in the world.

BuildRequires: developer/gcc
Requires:      system/library/gcc/gcc-runtime

%prep
%setup -q -n node-v%{version}

%if %oracle_solaris_11
%patch0 -p0
%endif

%build
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

export CC=/usr/bin/gcc
export CXX=/usr/bin/g++

./configure \
    --dest-os=solaris \
    --dest-cpu=x64 \
    --prefix=/usr/nodejs/%{major_version}

make -j${CPUS}
# make test

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

install -d %{buildroot}/usr/bin
pushd %{buildroot}/usr/bin
ln -s ../nodejs/%{major_version}/bin/node node
ln -s ../nodejs/%{major_version}/bin/npm npm
ln -s ../nodejs/%{major_version}/bin/node node%{major_version}
ln -s ../nodejs/%{major_version}/bin/npm npm%{major_version}

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%ips_tag (mediator=nodejs mediator-version=%{major_version}) %attr (0755, root, bin) /usr/bin/node
%ips_tag (mediator=nodejs mediator-version=%{major_version}) %attr (0755, root, bin) /usr/bin/npm
%attr (0755, root, bin) /usr/bin/npm%{major_version}
%attr (0755, root, bin) /usr/bin/node%{major_version}
%dir %attr (0755, root, bin) /usr/nodejs
%attr (0755, root, bin) /usr/nodejs/%{major_version}

%changelog
* Fri May 19 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.10.0
* Wed Apr 12 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.9.0
* Wed Mar 29 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.8.0
* Thu Mar 23 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.7.4 and update patch0
* Thu Mar 09 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.7.2
* Mon Mar 06 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.7.1
* Wed Feb 22 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.6.0
* Wed Feb 01 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.5.0
* Sun Jan 08 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.4.0
* Tue Jan 03 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.3.0
* Wed Dec 07 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.2.1
* Fri Nov 25 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 7.2.0
* Wed Oct 26 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
