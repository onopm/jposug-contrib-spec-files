
-include common.mak
-include target.mak

all: ${TARGET}

depend::
	rm -f $(TARGETMAK)
	if [ -z $${PKGBUILD_IPS_REPO} ];then \
		echo REPOSITRY=localhost >> $(TARGETMAK);\
	else \
		echo REPOSITRY=$${PKGBUILD_IPS_REPO} >> $(TARGETMAK);\
	fi
	echo "TARGET=\\">> $(TARGETMAK)
	cat build.list | sed 's/^#.*//g;s/\.spec$$/.info/g;' |xargs >> $(TARGETMAK)
	$(SPECDEPEND) >> $(TARGETMAK)
	echo 'all : $$(TARGET)' >> $(TARGETMAK)

preinstall::
	sudo pkg install -v $(PRE_INSTALL)

clean::
	rm -f $(TARGET) $(TARGETMAK) $(patsubst %.info,%.proto,$(TARGET))
