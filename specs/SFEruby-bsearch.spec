%include Solaris.inc
%include default-depend.inc

%{!?ruby_libdir: %define ruby_libdir %(ruby -rrbconfig -e 'puts Config::CONFIG["rubylibdir"]')}
%{!?ruby_archdir: %define ruby_archdir %(ruby -rrbconfig -e 'puts Config::CONFIG["archdir"]')}


Summary: The binary search algorithm is extracted from Jon Bentley's # Programming Pearls 2nd ed. p.93
Name: SFEruby-bsearch
IPS_package_name:        library/ruby-18/bsearch
Version: 1.5
License: Ruby
URL:     http://0xcc.net/ruby-bsearch/
Source0: http://0xcc.net/ruby-bsearch/ruby-bsearch-1.5.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18

%description
The binary search algorithm is extracted from Jon Bentley's # Programming Pearls 2nd ed. p.93


%prep
%setup -q -n ruby-bsearch-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{ruby_libdir}
install -m 644 bsearch.rb %{buildroot}%{ruby_libdir}

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)
%doc ChangeLog bsearch.en.rd  bsearch.ja.rd
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8/lib/ruby/1.8/bsearch.rb

%changelog
* Sun Nov 25 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
