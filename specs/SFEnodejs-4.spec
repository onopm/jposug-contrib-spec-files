%include Solaris.inc
%include default-depend.inc

%define tarball_name node
%define major_version 4

%define oracle_solaris_11 %(grep 'Oracle Solaris 11' /etc/release > /dev/null ; if [ $? -eq 0 ]; then echo '1'; else echo '0'; fi)


Summary:          Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
Name:             SFEnodejs-4
IPS_package_name: runtime/node.js-4
Version:          4.4.3
License:          MIT License
URL:              http://nodejs.org/
Source0:          https://nodejs.org/dist/v%{verson}/node-v%{version}.tar.gz
Patch0:           nodejs-42-add-defines.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient.
Node.js' package ecosystem, npm, is the largest ecosystem of open source libraries in the world.

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
ln -s ../nodejs/%{major_version}/bin/node node4
ln -s ../nodejs/%{major_version}/bin/npm npm4

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, bin) /usr/bin
%ips_tag (mediator=nodejs mediator-version=%{major_version}) %attr (0755, root, bin) /usr/bin/node
%ips_tag (mediator=nodejs mediator-version=%{major_version}) %attr (0755, root, bin) /usr/bin/npm
%attr (0755, root, bin) /usr/bin/npm4
%attr (0755, root, bin) /usr/bin/node4
%dir %attr (0755, root, bin) /usr/nodejs
%attr (0755, root, bin) /usr/nodejs/%{major_version}

%changelog
* Fri Apr 22 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.4.3
* Mon Apr 04 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.4.2
* Fri Mar 25 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 4.4.1
* Mon Mar 07 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- rename "runtime/node.js-42" to "runtime/node.js-4"
- bump to 4.3.2
* Fri Dec 18 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
