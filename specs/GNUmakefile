
-include common.mak
-include target.mak

BUILDLIST=$(shell if egrep -i "omnios" /etc/release>/dev/null; then echo "build.list."`egrep -o r[0-9][0-9][0-9][0-9][0-9][0-9] /etc/release`; else echo "build.list."`uname -r`; fi)
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
	sudo pkg install -v $(PRE_INSTALL)

clean::
	rm -f $(TARGET) $(TARGETMAK) $(patsubst %.info,%.proto,$(TARGET))

publish:: 
	sudo $(PUBLISH_REPOSITORY) publish /var/pkglocal rpool/pkg

release:: 
	sudo $(PUBLISH_REPOSITORY) release /var/pkgrelease/root rpool/pkg

