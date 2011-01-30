#
# common.mak
#

SPECBUILD=../bin/specbuild.sh 
REPOSITRY=mypkgs
TARGETMAK=target.mak
SPECDEPEND=../bin/spec_depend.pl
SPECDEPENDINSTALL=../bin/spec_depend_install.pl
CHECK_INSTALL=../bin/check_install.sh
PKGSEND_MANIFEST=../bin/pkgsend_manifest.sh

.SUFFIXES : .spec .manifest
.SUFFIXES : .manifest .info

.spec.manifest :
	$(SPECBUILD) $<
	cp -p ~/packages/PKGMAPS/manifests/$@ $@

.manifest.info:
	pfexec pkg refresh $(REPOSITRY)
	pfexec pkg install -v pkg://$(REPOSITRY)/$(patsubst %.manifest,%,$<)
	pfexec pkg info $(patsubst %.manifest,%,$<) > $@
