%include Solaris.inc
%include packagenamemacros.inc
%include base.inc
%define cc_is_gcc 0

%define _bindir /usr/ruby/1.8/bin
%define _sbindir /usr/ruby/1.8/sbin
%define _mandir /usr/ruby/1.8/share/man

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%define confdir conf/solaris

Name:           puppet3
IPS_package_name:        system/management/puppet3
Version:        3.0.0
#Release:        0.1rc1%{?dist}
Release:        1%{?dist}
Summary:        A network tool for managing many disparate systems
Group:		Applications/System
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        http://puppetlabs.com/downloads/puppet/puppet-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  runtime/ruby-18
BuildRequires:  runtime/ruby-18/facter
Requires:  runtime/ruby-18
Requires:  runtime/ruby-18/facter

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%package server
IPS_package_name:        system/management/puppet3/master
Group:		Applications/System
Summary:        Server for the puppet system management tool
Requires:       system/management/puppet3 = %{version}

%description server
Provides the central puppet server daemon which provides manifests to clients.
The server can also function as a certificate authority and file server.

%prep
%setup -q -n puppet-%{version}

%build

%install
rm -rf %{buildroot}
ruby install.rb --destdir=%{buildroot} --quick --no-rdoc

install -d -m0755 %{buildroot}%{_sysconfdir}/puppet/manifests
install -d -m0755 %{buildroot}%{_datadir}/puppet/modules
install -d -m0755 %{buildroot}%{_localstatedir}/lib

install -Dp -m0644 ext/ips/puppet-agent %{buildroot}/lib/svc/method/puppet-agent
install -Dp -m0644 ext/ips/puppet-master %{buildroot}/lib/svc/method/puppet-master
install -Dp -m0644 ext/ips/puppetagent.xml %{buildroot}%{_localstatedir}/svc/manifest/system/management/puppetagent.xml
install -Dp -m0644 ext/ips/puppetmaster.xml %{buildroot}%{_localstatedir}/svc/manifest/system/management/puppetmaster.xml
install -Dp -m0644 ext/ips/puppet.conf %{buildroot}%{_sysconfdir}/puppet/puppet.conf

# Install the ext/ directory to %%{_datadir}/%puppet
install -d %{buildroot}%{_datadir}/puppet
cp -a ext/ %{buildroot}%{_datadir}/puppet

# emacs and vim bits are installed elsewhere
rm -rf %{buildroot}%{_datadir}/puppet/ext/{emacs,vim}

# Install emacs mode files
emacsdir=%{buildroot}%{_datadir}/emacs/site-lisp
install -Dp -m0644 ext/emacs/puppet-mode.el $emacsdir/puppet-mode.el
install -Dp -m0644 ext/emacs/puppet-mode-init.el \
    $emacsdir/site-start.d/puppet-mode-init.el

# Install vim syntax files
vimdir=%{buildroot}%{_datadir}/vim/vimfiles
install -Dp -m0644 ext/vim/ftdetect/puppet.vim $vimdir/ftdetect/puppet.vim
install -Dp -m0644 ext/vim/syntax/puppet.vim $vimdir/syntax/puppet.vim

#
mkdir -p %{buildroot}/usr/bin
cd %{buildroot}/usr/bin
ln -s ../../%{_bindir}/extlookup2hiera .
ln -s ../../%{_bindir}/puppet .


%files
%defattr(-, root, bin, 0755)
%doc LICENSE README.md README_DEVELOPER.md README_HIERA.md CONTRIBUTING.md
/usr/bin/puppet
/usr/bin/extlookup2hiera
%{_bindir}/extlookup2hiera
%{_bindir}/puppet
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/system
%attr (0755, root, bin) %{ruby_sitelibdir}/
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, sys) %{_sysconfdir}/puppet
%dir %attr (0755, root, sys) /usr/share
%dir %attr (0755, root, other) /usr/share/doc
%ghost %config(noreplace,missingok) %{_sysconfdir}/puppet/puppet.conf
%config(noreplace,missingok) %{_sysconfdir}/puppet/auth.conf
# We don't want to require emacs or vim, so we need to own these dirs
%attr (0755, root, bin) %{_datadir}/emacs
%attr (0755, root, bin) %{_datadir}/vim
%{_datadir}/puppet
%dir %attr(0755, root, other) %{_localstatedir}/lib
%{_mandir}/man5/puppet.conf.5.gz
%{_mandir}/man8/puppet-agent.8.gz
%{_mandir}/man8/puppet-apply.8.gz
%{_mandir}/man8/puppet-ca.8.gz
%{_mandir}/man8/puppet-catalog.8.gz
%{_mandir}/man8/puppet-cert.8.gz
%{_mandir}/man8/puppet-certificate.8.gz
%{_mandir}/man8/puppet-certificate_request.8.gz
%{_mandir}/man8/puppet-certificate_revocation_list.8.gz
%{_mandir}/man8/puppet-config.8.gz
%{_mandir}/man8/puppet-describe.8.gz
%{_mandir}/man8/puppet-device.8.gz
%{_mandir}/man8/puppet-doc.8.gz
%{_mandir}/man8/puppet-facts.8.gz
%{_mandir}/man8/puppet-file.8.gz
%{_mandir}/man8/puppet-filebucket.8.gz
%{_mandir}/man8/puppet-help.8.gz
%{_mandir}/man8/puppet-inspect.8.gz
%{_mandir}/man8/puppet-instrumentation_data.8.gz
%{_mandir}/man8/puppet-instrumentation_listener.8.gz
%{_mandir}/man8/puppet-instrumentation_probe.8.gz
%{_mandir}/man8/puppet-key.8.gz
%{_mandir}/man8/puppet-kick.8.gz
%{_mandir}/man8/puppet-man.8.gz
%{_mandir}/man8/puppet-master.8.gz
%{_mandir}/man8/puppet-module.8.gz
%{_mandir}/man8/puppet-node.8.gz
%{_mandir}/man8/puppet-parser.8.gz
%{_mandir}/man8/puppet-plugin.8.gz
%{_mandir}/man8/puppet-queue.8.gz
%{_mandir}/man8/puppet-report.8.gz
%{_mandir}/man8/puppet-resource.8.gz
%{_mandir}/man8/puppet-resource_type.8.gz
%{_mandir}/man8/puppet-secret_agent.8.gz
%{_mandir}/man8/puppet-status.8.gz
%{_mandir}/man8/puppet.8.gz
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/system/management/puppetagent.xml
%attr (0555, root, bin) /lib/svc/method/puppet-agent



%files server
%defattr(-, root, bin, 0755)
%dir %attr (0755, root, sys) /usr
%dir %attr (0755, root, sys) %{_localstatedir}
%dir %attr (0755, root, sys) %{_localstatedir}/svc
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest
%dir %attr (0755, root, sys) %{_localstatedir}/svc/manifest/system
# %config(noreplace) %{_sysconfdir}/puppet/fileserver.conf
%dir %attr (0755, root, sys) %{_sysconfdir}
%dir %attr (0755, root, sys) %{_sysconfdir}/puppet
%dir %attr (0755, root, sys) %{_sysconfdir}/puppet/manifests
%dir %attr(0755, root, other) %{_localstatedir}/lib
%class(manifest) %attr(0444, root, sys) %{_localstatedir}/svc/manifest/system/management/puppetmaster.xml
%attr (0555, root, bin) /lib/svc/method/puppet-master

%clean
rm -rf %{buildroot}

%changelog
* Wed Oct 24 2012 - Fumihisa TONAKA <fumi.ftnk@gmail.com>
- initial commit
