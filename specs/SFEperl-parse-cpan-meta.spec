%include Solaris.inc
%include default-depend.inc

%define build584 0
%define build510 %( if [ -x /usr/perl5/5.10/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build512 %( if [ -x /usr/perl5/5.12/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build516 %( if [ -x /usr/perl5/5.16/bin/perl ]; then echo '1'; else echo '0'; fi)
%define build522 %( if [ -x /usr/perl5/5.22/bin/perl ]; then echo '1'; else echo '0'; fi)


%define cpan_name Parse-CPAN-Meta
%define sfe_cpan_name parse-cpan-meta

Summary:               Parse META.yml and META.json CPAN metadata files
Name:                  SFEperl-%{sfe_cpan_name}
IPS_package_name:      library/perl-5/%{sfe_cpan_name}
Version:               1.4417
IPS_component_version: 1.4417
License:               perl_5
URL:                   https://metacpan.org/pod/Parse::CPAN::Meta
Source0:               http://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Parse-CPAN-Meta-%{version}.tar.gz
BuildRoot:             %{_tmppath}/%{name}-%{version}-build

%description
Parse META.yml and META.json CPAN metadata files

%if %{build584}
%package 584
IPS_package_name: library/perl-5/%{sfe_cpan_name}-584
Summary:          Parse META.yml and META.json CPAN metadata files
BuildRequires:    runtime/perl-584 = *
Requires:         runtime/perl-584 = *
Requires:         library/perl-5/cpan-meta-584 >= 2.150010

%description 584
Parse META.yml and META.json CPAN metadata files
%endif

%if %{build512}
%package 512
IPS_package_name: library/perl-5/%{sfe_cpan_name}-512
Summary:          Parse META.yml and META.json CPAN metadata files
BuildRequires:    runtime/perl-512 = *
Requires:         runtime/perl-512 = *
Requires:         library/perl-5/cpan-meta-512 >= 2.150010

%description 512
Parse META.yml and META.json CPAN metadata files
%endif

%if %{build516}
%package 516
IPS_package_name: library/perl-5/%{sfe_cpan_name}-516
Summary:          Parse META.yml and META.json CPAN metadata files
BuildRequires:    runtime/perl-516 = *
Requires:         runtime/perl-516 = *
Requires:         library/perl-5/cpan-meta-516 >= 2.150010

%description 516
Parse META.yml and META.json CPAN metadata files
%endif

%if %{build522}
%package 522
IPS_package_name: library/perl-5/%{sfe_cpan_name}-522
Summary:          Parse META.yml and META.json CPAN metadata files
BuildRequires:    runtime/perl-522 = *
Requires:         runtime/perl-522 = *
Requires:         library/perl-5/cpan-meta-522 >= 2.150010

%description 522
Parse META.yml and META.json CPAN metadata files
%endif


%prep
%setup -q -n %{cpan_name}-%{version}

%install

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,bin,-)

%if %{build584}
%files 584
%defattr(0755,root,bin,-)
%endif

%if %{build512}
%files 512
%defattr(0755,root,bin,-)
%endif

%if %{build516}
%files 516
%defattr(0755,root,bin,-)
%endif

%if %{build522}
%files 522
%defattr(0755,root,bin,-)
%endif

%changelog
* Thu Jun 01 2017 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- Obsolete. parse-cpan-meta is included cpan-meta >= 2.150010
* Wed Nov 04 2015 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- bump to 1.4417 and build packages for perl-516 and perl-520
* Sat Dec 22 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- add BuildRequires
* Tue Jun 12 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- generate packages for perl-584 and perl-512
* Tue May 01 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
