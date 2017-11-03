%include Solaris.inc
%include default-depend.inc

%define tarball_name node
%define major_version 6


%define oracle_solaris_11 %(grep 'Oracle Solaris 11' /etc/release > /dev/null ; if [ $? -eq 0 ]; then echo '1'; else echo '0'; fi)

Summary:          Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine.
Name:             SFEnodejs-%{major_version}
IPS_package_name: runtime/node.js-%{major_version}
Version:          6.10.3
License:          MIT License
URL:              http://nodejs.org/
Source0:          https://nodejs.org/dist/v%{verson}/node-v%{version}.tar.xz
Patch0:           nodejs-53-add-defines.patch
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
* Thu May 18 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.10.3
* Thu Feb 02 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.9.5
* Thu Dec 08 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.9.2
* Wed Oct 26 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.9.1
* Wed Oct 19 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.9.0
* Fri Sep 30 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.7.0
* Tue Jul 12 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.3.0
* Fri Jun 24 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.2.2
* Mon May 09 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 6.1.0
* Wed Apr 27 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
