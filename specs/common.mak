#
# common.mak
#

SPECBUILD=../bin/specbuild.sh 
REPOSITRY=${PKGBUILD_IPS_REPO}
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
	PKGNAME=`awk -F: 'tolower($$1)~/^ips_package_name/{print $$2}' $(patsubst %.proto,%,$<).spec` ;\
		    if [ -n "$${PKGNAME}" ] ; then \
		       sudo pkg install -v $${PKGNAME} &&\
		       sudo pkg info $${PKGNAME} > $@ ;\
		    else \
		       echo ips_package_name is not found in $<;\
		       exit 1;\
		    fi
