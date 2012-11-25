%include Solaris.inc
%include default-depend.inc

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}

Summary: Migemo is a tool for Japanese incremental search.
Name: SFEmigemo
IPS_package_name:        application/migemo
Version: 0.40
License: Ruby
URL:     http://0xcc.net/migemo/
Source0: http://0xcc.net/migemo/migemo-0.40.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18
Requires:       library/ruby-18/romkan
Requires:       library/ruby-18/bsearch

%description
Migemo is a tool for Japanese incremental search. It makes Japanese character regular expression from alphabet and optimize them.

%prep
%setup -q -n migemo-%{version}

%build
RUBY=/usr/ruby/1.8/bin/ruby ./configure \
    --with-rubydir=%{ruby18_sitelibdir} \
    --prefix=/usr

make migemo.el

cat > migemo-init.el <<EOF
(load "migemo")
EOF

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
/usr/bin/migemo-client
/usr/bin/migemo-server
/usr/bin/migemo-grep
/usr/bin/migemo
%dir /usr/share/migemo
/usr/share/migemo/regex-dict.sample
/usr/share/migemo/migemo-dict
/usr/share/migemo/migemo.ja.rd
/usr/share/migemo/migemo-dict.cache.idx
/usr/share/migemo/migemo-dict.cache
/usr/share/migemo/user-dict.sample
/usr/share/migemo/migemo-dict.idx
%dir /usr/share/emacs
%dir /usr/share/emacs/site-lisp
/usr/share/emacs/site-lisp/migemo.el
/usr/share/emacs/site-lisp/migemo.elc

%changelog
* Sun Nov 25 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
