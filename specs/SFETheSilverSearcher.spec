%include Solaris.inc

Name:		SFETheSilverSearcher
IPS_package_name:        text/the_silver_searcher
Version:	0.29.1
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

%changelog
* Sat Dev 15 2012 Fumihisa TONAKA <fumi.ftnk@gmail.com>
