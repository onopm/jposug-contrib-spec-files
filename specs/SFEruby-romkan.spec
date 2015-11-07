%include Solaris.inc
%include default-depend.inc


%{!?ruby_libdir: %define ruby_libdir %(ruby -rrbconfig -e 'puts Config::CONFIG["rubylibdir"]')}
%{!?ruby_archdir: %define ruby_archdir %(ruby -rrbconfig -e 'puts Config::CONFIG["archdir"]')}

Summary: Ruby/Romkan is a Romaji <-> Kana conversion library for Ruby.
Name: SFEruby-romkan
IPS_package_name:        library/ruby-18/romkan
Version: 0.4
License: Ruby
URL:     http://0xcc.net/ruby-romkan/
Source0: http://0xcc.net/ruby-romkan/ruby-romkan-0.4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:	runtime/ruby-18
Requires:       runtime/ruby-18

%description
Ruby/Romkan is a Romaji <-> Kana conversion library for Ruby. It can convert a Japanese Romaji string to a Japanese Kana string or vice versa. 

%prep
%setup -q -n ruby-romkan-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{ruby_libdir}
install -m 644 romkan.rb %{buildroot}%{ruby_libdir}

%clean
rm -rf %{buildroot}


%files
%defattr(0755,root,bin,-)
%doc ChangeLog romkan.en.rd  romkan.ja.rd
%dir %attr (0755, root, sys) %{_datadir}
%dir %attr (0755, root, other) %{_datadir}/doc
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.8/lib/ruby/1.8/romkan.rb

%changelog
* Sun Nov 25 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
