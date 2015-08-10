%include Solaris.inc
%include default-depend.inc

%define build19 0
%define build20 0
%define build21 1
%define build22 1
%define generate_executable 0

%define gemname nokogiri
%define sfe_gemname nokogiri

%if %{build19}
%define bindir19 /usr/ruby/1.9/bin
%define gemdir19 %(%{bindir19}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir19 %{gemdir19}/gems/%{gemname}-%{version}
%endif

%if %{build20}
%define bindir20 /usr/ruby/2.0/bin
%define gemdir20 %(%{bindir20}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir20 %{gemdir20}/gems/%{gemname}-%{version}
%endif

%if %{build21}
%define bindir21 /usr/ruby/2.1/bin
%define gemdir21 %(%{bindir21}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir21 %{gemdir21}/gems/%{gemname}-%{version}
%endif

%if %{build22}
%define bindir22 /usr/ruby/2.2/bin
%define gemdir22 %(%{bindir22}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir22 %{gemdir22}/gems/%{gemname}-%{version}
%endif

Summary:          Nokogiri is an HTML, XML, SAX, and Reader parser
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          1.6.6.2
License:          MIT
URL:              http://nokogiri.org
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build



%description
Nokogiri is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.

XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.

%if %{build19}
%package 19
IPS_package_name: library/ruby/%{gemname}-19
Summary:          Nokogiri is an HTML, XML, SAX, and Reader parser
BuildRequires:    runtime/ruby-19 = *
BuildRequires:    library/ruby/mini_portile-19
BuildRequires:    library/libxml2
Requires:         runtime/ruby-19 = *
# mini_portile ~> 0.6.0
Requires:         library/ruby/mini_portile-19
Requires:         library/libxml2

%description 19
Nokogiri is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.

XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.
%endif

%if %{build20}
%package 20
IPS_package_name: library/ruby/%{gemname}-20
Summary:          Nokogiri is an HTML, XML, SAX, and Reader parser
BuildRequires:    runtime/ruby-20 = *
BuildRequires:    library/ruby/mini_portile-20
BuildRequires:    library/libxml2
Requires:         runtime/ruby-20 = *
# mini_portile ~> 0.6.0
Requires:         library/ruby/mini_portile-20
Requires:         library/libxml2

%description 20
Nokogiri is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.

XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.
%endif

%if %{build21}
%package 21
IPS_package_name: library/ruby/%{gemname}-21
Summary:          Nokogiri is an HTML, XML, SAX, and Reader parser
BuildRequires:    runtime/ruby-21 = *
BuildRequires:    library/ruby/mini_portile-21
BuildRequires:    library/libxml2
Requires:         runtime/ruby-21 = *
# mini_portile ~> 0.6.0
Requires:         library/ruby/mini_portile-21
Requires:         library/libxml2

%description 21
Nokogiri is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.

XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.
%endif

%if %{build22}
%package 22
IPS_package_name: library/ruby/%{gemname}-22
Summary:          Nokogiri is an HTML, XML, SAX, and Reader parser
BuildRequires:    runtime/ruby-22 = *
BuildRequires:    library/ruby/mini_portile-22
BuildRequires:    library/libxml2
Requires:         runtime/ruby-22 = *
# mini_portile ~> 0.6.0
Requires:         library/ruby/mini_portile-22
Requires:         library/libxml2

%description 22
Nokogiri is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.

XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.
%endif

%prep
%setup -q -c -T

%build
export NOKOGIRI_USE_SYSTEM_LIBRARIES=yes

build_for() {
    ruby_ver=$1
    bindir="/usr/ruby/${ruby_ver}/bin"
    gemdir="$(${bindir}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    ${bindir}/gem install --local \
        --no-env-shebang \
        --install-dir .${gemdir} \
        --bindir .${bindir} \
        --no-ri \
        --no-rdoc \
        -V \
        --force %{SOURCE0}
}

%if %{build19}
# ruby-19
build_for 1.9
%endif

%if %{build20}
# ruby-20
build_for 2.0
%endif

%if %{build21}
# ruby-21
build_for 2.1
%endif

%if %{build22}
# ruby-22
build_for 2.2
%endif

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

install_for() {
    ruby_ver=$1
    bindir="/usr/ruby/${ruby_ver}/bin"
    gemdir="$(${bindir}/ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    mkdir -p %{buildroot}/usr/ruby/${ruby_ver}
    cp -a ./usr/ruby/${ruby_ver}/* \
        %{buildroot}/usr/ruby/${ruby_ver}/

    for dir in %{buildroot}${geminstdir}/bin %{buildroot}%{_bindir}
    do
	if [ -d ${dir} ]
	then
	    pushd ${dir}
	    for i in ./*
	    do
		if [ -f ${i} ]
		then
		    mv ${i} ${i}.bak
		    sed -e "s!^\#\!/usr/bin/env ruby\$!\#\!/usr/ruby/${ruby_ver}/bin/ruby!" \
			-e "s!^\#\!/usr/bin/ruby\$!\#\!/usr/ruby/${ruby_ver}/bin/ruby!" \
			-e "s!^\#\!ruby\$!\#\!/usr/ruby/${ruby_ver}/bin/ruby!" \
			${i}.bak > ${i}
		    rm ${i}.bak
		fi
	    done
	    popd
	fi
    done
   
%if %{generate_executable}
    pushd %{buildroot}%{_bindir}
    for i in $(ls ../ruby/${ruby_ver}/bin/*)
    do
	[ -f ${i} ] && ln -s ${i} $(basename ${i})$(echo ${ruby_ver}|sed -e 's/\.//')
    done
    popd
%endif

}

%if %{build19}
# ruby-19
install_for 1.9
%endif

%if %{build20}
install_for 2.0
%endif

%if %{build21}
# ruby-21
install_for 2.1
%endif

%if %{build22}
install_for 2.2
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build19}
%files 19
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/1.9
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*19
%endif
%endif

%if %{build20}
%files 20
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.0
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*20
%endif
%endif

%if %{build21}
%files 21
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.1
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*21
%endif
%endif

%if %{build22}
%files 22
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.2
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*22
%endif
%endif

%changelog
* Tue Aug 11 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- update specfile based on bin/make_rubygem_spec.rb
* Sat Mar 07 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.6.2 and build package for ruby-22
* Tue Jul 01 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.6.1
* Tue Mar 26 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
