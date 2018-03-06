#
# common.mak
#

SPECBUILD=../bin/specbuild.sh 
TARGETMAK=target.mak
SPECDEPEND=../bin/spec_depend.pl
SPECDEPEND_ACCURATELY=../bin/spec_depend_spectool.pl
SPECDEPENDINSTALL=../bin/spec_depend_install.pl
CHECK_INSTALL=../bin/check_install.sh
PKGSEND_MANIFEST=../bin/pkgsend_manifest.sh
INSTALL_SPEC=../bin/install_spec.sh
PUBLISH_REPOSITORY=../bin/publish_repository.sh

.SUFFIXES : .spec .proto
.SUFFIXES : .proto .info

.spec.proto :
	$(SPECBUILD) $<
	cat ~/packages/PKGMAPS/proto/$@ > $@

.proto.info:
	sudo pkg refresh $(REPOSITRY)
	$(INSTALL_SPEC) $<
