%include Solaris.inc

Name:		SFETheSilverSearcher
IPS_package_name:        text/the_silver_searcher
Version:	2.1.0
Summary:	A code-searching tool similar to ack, but faster.
License:	Apache License
URL:		http://geoff.greer.fm/ag/
Source:		http://geoff.greer.fm/ag/releases/the_silver_searcher-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Silver Searcher is a tool for searching code. It started off as a clone of Ack, but their feature sets have since diverged slightly. In typical usage, Ag is 5-10x faster than Ack. 

%prep
%setup -q -n the_silver_searcher-%{version}

%build
export CC=/usr/bin/gcc
export CFLAGS='-m64'
CPUS=`/usr/sbin/psrinfo | grep on-line | wc -l | tr -d ' '`
if test "x$CPUS" = "x" -o $CPUS = 0; then
     CPUS=1
fi

./configure --prefix=/usr
make -j$CPUS


%install
rm -rf %{buildroot}

make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}



%files
%defattr(-, root, bin)
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, bin) %{_bindir}
%attr (0755, root, bin) %{_bindir}/ag
%attr (0755, root, bin) %{_datadir}/the_silver_searcher
%attr (0755, root, bin) %{_datadir}/man
%dir %attr (0755, root, bin) /usr/share/zsh
%dir %attr (0755, root, bin) /usr/share/zsh/site-functions
%attr (0755, root, bin) /usr/share/zsh/site-functions/_the_silver_searcher


%changelog
* Wed Feb 28 2018 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.1.0
* Wed Jul 05 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.0.0
* Thu Jan 12 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.2 and fix file attr
* Thu Dec 01 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.0.1
* Thu Oct 20 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.33.0
* Tue Mar 29 2016 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.31.0
* Sat Jun 20 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 0.30.0
* Wed Mar 25 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
