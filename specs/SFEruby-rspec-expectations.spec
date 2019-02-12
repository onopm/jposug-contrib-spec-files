%include Solaris.inc
%include default-depend.inc

%define build23 %( if [ -x /usr/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build23jposug %( if [ -x /opt/jposug/ruby/2.3/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build24jposug %( if [ -x /opt/jposug/ruby/2.4/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build25jposug %( if [ -x /opt/jposug/ruby/2.5/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define build26jposug %( if [ -x /opt/jposug/ruby/2.6/bin/ruby ]; then echo '1'; else echo '0'; fi)
%define generate_executable 0
%define keep_dependency 0

%define gemname rspec-expectations
%define sfe_gemname rspec-expect

# rspec-expectations provides a simple, readable API to express expected outcomes of a code example.

Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
Name:             SFEruby-%{sfe_gemname}
IPS_package_name: library/ruby/%{gemname}
Version:          3.8.2
License:          MIT
URL:              https://github.com/rspec/rspec-expectations
Source0:          http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:        %{_tmppath}/%{name}-%{version}-build

%description
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.

%if %{build23}
%if %{keep_dependency}
%package 23-old
IPS_package_name: library/ruby-23/%{gemname}
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# Requires:         library/ruby/%{gemname}-23

%description 23-old
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%package 23
IPS_package_name: library/ruby/%{gemname}-23
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    runtime/ruby-23 = *
Requires:         runtime/ruby-23 = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         library/ruby/diff-lcs-23
# rspec-support ~> 3.8.0
Requires:         library/ruby/rspec-support-23
# Requires:         library/ruby/%{gemname}

%description 23
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%if %{build23jposug}

%package 23jposug
IPS_package_name: jposug/library/ruby/%{gemname}-23jposug
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    jposug/runtime/ruby-23jposug = *
Requires:         jposug/runtime/ruby-23jposug = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         jposug/library/ruby/diff-lcs-23jposug
# rspec-support ~> 3.8.0
Requires:         jposug/library/ruby/rspec-support-23jposug
# Requires:         library/ruby/%{gemname}

%description 23jposug
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%if %{build24jposug}

%package 24jposug
IPS_package_name: jposug/library/ruby/%{gemname}-24jposug
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    jposug/runtime/ruby-24jposug = *
Requires:         jposug/runtime/ruby-24jposug = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         jposug/library/ruby/diff-lcs-24jposug
# rspec-support ~> 3.8.0
Requires:         jposug/library/ruby/rspec-support-24jposug
# Requires:         library/ruby/%{gemname}

%description 24jposug
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%if %{build25jposug}

%package 25jposug
IPS_package_name: jposug/library/ruby/%{gemname}-25jposug
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    jposug/runtime/ruby-25jposug = *
Requires:         jposug/runtime/ruby-25jposug = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         jposug/library/ruby/diff-lcs-25jposug
# rspec-support ~> 3.8.0
Requires:         jposug/library/ruby/rspec-support-25jposug
# Requires:         library/ruby/%{gemname}

%description 25jposug
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif

%if %{build26jposug}

%package 26jposug
IPS_package_name: jposug/library/ruby/%{gemname}-26jposug
Summary:          rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
BuildRequires:    jposug/runtime/ruby-26jposug = *
Requires:         jposug/runtime/ruby-26jposug = *
# diff-lcs < 2.0, >= 1.2.0
Requires:         jposug/library/ruby/diff-lcs-26jposug
# rspec-support ~> 3.8.0
Requires:         jposug/library/ruby/rspec-support-26jposug
# Requires:         library/ruby/%{gemname}

%description 26jposug
rspec-expectations provides a simple, readable API to express expected outcomes of a code example.
%endif


%prep
%setup -q -c -T

%build
build_for() {
    if [ "x${1}" = 'x2.6jposug' -o "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
    then
        ruby_ver=$(echo $1 | sed -e 's/jposug//')
        bindir="/opt/jposug/ruby/${ruby_ver}/bin"
    else
        ruby_ver=$1
        bindir="/usr/ruby/${ruby_ver}/bin"
    fi
    gemdir="$(${bindir}/ruby -r rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    ${bindir}/gem install --local \
        --no-env-shebang \
        --no-document \
        --install-dir .${gemdir} \
        --bindir .${bindir} \
        -V \
        --force %{SOURCE0}
}

%if %{build23}
# ruby-23
build_for 2.3
%endif
%if %{build23jposug}
# ruby-23jposug
build_for 2.3jposug
%endif
%if %{build24jposug}
# ruby-24jposug
build_for 2.4jposug
%endif
%if %{build25jposug}
# ruby-25jposug
build_for 2.5jposug
%endif
%if %{build26jposug}
# ruby-26jposug
build_for 2.6jposug
%endif

%install
rm -rf %{buildroot}

%if %{generate_executable}
mkdir -p %{buildroot}/%{_bindir}
%endif

install_for() {
    if [ "x${1}" = 'x2.6jposug' -o "x${1}" = 'x2.5jposug' -o "x${1}" = 'x2.4jposug' -o "x${1}" = 'x2.3jposug' ]
    then
        ruby_ver=$(echo $1 | sed -e 's/jposug//')
        dir_prefix="/opt/jposug/ruby/${ruby_ver}"
        dir_prefix_relative="../../opt/jposug/ruby/${ruby_ver}"
        jposug='jposug'
    else
        ruby_ver=$1
        dir_prefix="/usr/ruby/${ruby_ver}"
        dir_prefix_relative="../ruby/${ruby_ver}"
        jposug=''
    fi
    bindir="${dir_prefix}/bin"
    gemdir="$(${bindir}/ruby -r rubygems -e 'puts Gem::dir' 2>/dev/null)"
    geminstdir="${gemdir}/gems/%{gemname}-%{version}"

    mkdir -p %{buildroot}${dir_prefix}
    cp -a .${dir_prefix}/* \
        %{buildroot}/${dir_prefix}/

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
		    sed -e "s!^\#\!/usr/bin/env ruby\$!\#\!${bindir}/ruby!" \
			-e "s!^\#\!/usr/bin/ruby\$!\#\!${bindir}/ruby!" \
			-e "s!^\#\!ruby\$!\#\!${bindir}/ruby!" \
			${i}.bak > ${i}
		    rm ${i}.bak
		fi
	    done
	    popd
	fi
    done

    [ -d %{buildroot}${geminstdir}/test ] && rm -rf %{buildroot}${geminstdir}/test || true

%if %{generate_executable}
    pushd %{buildroot}%{_bindir}
    for i in $(ls ${dir_prefix_relative}/bin/*)
    do
	[ -f ${i} ] && ln -s ${i} $(basename ${i})$(echo ${ruby_ver}|sed -e 's/\.//')${jposug}
    done
    popd
%endif

}

%if %{build23}
install_for 2.3
%endif
%if %{build23jposug}
install_for 2.3jposug
%endif
%if %{build24jposug}
install_for 2.4jposug
%endif
%if %{build25jposug}
install_for 2.5jposug
%endif
%if %{build26jposug}
install_for 2.6jposug
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build23}
%files 23
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /usr
/usr/ruby/2.3
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*23
%endif
%endif

%if %{build23jposug}
%files 23jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.3
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*23jposug
%endif
%endif

%if %{build24jposug}
%files 24jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.4
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*24jposug
%endif
%endif

%if %{build25jposug}
%files 25jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.5
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*25jposug
%endif
%endif

%if %{build26jposug}
%files 26jposug
%defattr(0755,root,bin,-)
%dir %attr (0755, root, sys) /opt
/opt/jposug/ruby/2.6
%if %{generate_executable}
%dir %attr (0755, root, bin) /usr/bin
%attr (0755, root, bin) /usr/bin/*26jposug
%endif
%endif


%changelog
* Wed Feb 13 2019 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.8.2, add package for ruby-26jposug and obsolete ruby-21 and ruby-22
* Fri Dec 29 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.7.0 and build packages for ruby-2{3,4,5}jposug
* Sun Dec 13 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.4.0 and build package for ruby-23
* Fri Jun 12 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.2.1
* Mon Oct 06 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 3.1.2
* Thu Jul 10 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.99.1 and stop to generate package for ruby-18
* Wed Feb 26 2014 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.14.5 and generate package for ruby-21
* Mon Sep 30 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.14.3
* Sun Mar 24 2013 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 2.13.0
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
