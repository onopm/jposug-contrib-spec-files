#
# common.mak
#

SPECBUILD=../bin/specbuild.sh 
REPOSITRY=localhost
TARGETMAK=target.mak
SPECDEPEND=../bin/spec_depend.pl
SPECDEPENDINSTALL=../bin/spec_depend_install.pl
CHECK_INSTALL=../bin/check_install.sh
PKGSEND_MANIFEST=../bin/pkgsend_manifest.sh

.SUFFIXES : .spec .proto
.SUFFIXES : .proto .info

.spec.proto :
	$(SPECBUILD) $<
	cp -p ~/packages/PKGMAPS/proto/$@ $@

.proto.info:
	sudo pkg refresh $(REPOSITRY)
	sudo pkg install -v `awk -F: '/^IPS_Package_Name/{print $$2}' $(patsubst %.proto,%,$<).spec` || true
	sudo pkg info `awk -F: '/^IPS_Package_Name/{print $$2}' $(patsubst %.proto,%,$<).spec` > $@
