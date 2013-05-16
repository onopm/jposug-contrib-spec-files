
-include common.mak
-include target.mak

BUILDLIST=build.list.`uname -v`

predepend::
	rm -f $(TARGETMAK)
	if [ -z $${PKGBUILD_IPS_REPO} ];then \
		echo REPOSITRY=localhost >> $(TARGETMAK);\
	else \
		echo REPOSITRY=$${PKGBUILD_IPS_REPO} >> $(TARGETMAK);\
	fi
	printf "TARGET=">> $(TARGETMAK)
	cat $(BUILDLIST) | sed 's/^#.*//g;s/\.spec$$/.info/g;' |xargs >> $(TARGETMAK)
	echo 'all : $$(TARGET)' >> $(TARGETMAK)

depend:: predepend
	$(SPECDEPEND) $(BUILDLIST) >> $(TARGETMAK)

depend_accurately:: predepend
	$(SPECDEPEND_ACCURATELY) $(BUILDLIST) >> $(TARGETMAK)

preinstall::
	${SUPERCMD} pkg install -v $(PRE_INSTALL)

clean::
	rm -f $(TARGET) $(TARGETMAK) $(patsubst %.info,%.proto,$(TARGET))

publish:: 
	${SUPERCMD} $(PUBLISH_REPOSITORY) publish /var/pkglocal rpool/pkg

release:: 
	${SUPERCMD} $(PUBLISH_REPOSITORY) release /var/pkgrelease/root rpool/pkg

