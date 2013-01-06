
-include common.mak
-include target.mak

predepend::
	rm -f $(TARGETMAK)
	if [ -z $${PKGBUILD_IPS_REPO} ];then \
		echo REPOSITRY=localhost >> $(TARGETMAK);\
	else \
		echo REPOSITRY=$${PKGBUILD_IPS_REPO} >> $(TARGETMAK);\
	fi
	printf "TARGET=">> $(TARGETMAK)
	cat build.list | sed 's/^#.*//g;s/\.spec$$/.info/g;' |xargs >> $(TARGETMAK)
	echo 'all : $$(TARGET)' >> $(TARGETMAK)

depend:: predepend
	$(SPECDEPEND) >> $(TARGETMAK)

depend_accurately:: predepend
	$(SPECDEPEND_ACCURATELY) >> $(TARGETMAK)

preinstall::
	sudo pkg install -v $(PRE_INSTALL)

clean::
	rm -f $(TARGET) $(TARGETMAK) $(patsubst %.info,%.proto,$(TARGET))
