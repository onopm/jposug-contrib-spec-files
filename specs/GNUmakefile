
-include common.mak
-include target.mak

all: ${TARGET}

depend:
	rm -f $(TARGETMAK)
	if [ -z $${PKGBUILD_IPS_REPO} ];then \
		echo REPOSITRY=localhost >> $(TARGETMAK);\
	else \
		echo REPOSITRY=$${PKGBUILD_IPS_REPO} >> $(TARGETMAK);\
	fi
	echo TARGET=$(patsubst %.spec,%.info,$(wildcard *.spec)) >> $(TARGETMAK)
	echo 'all : $$(TARGET)' >> $(TARGETMAK)
	$(SPECDEPEND) >> $(TARGETMAK)

preinstall:
	$(SPECDEPENDINSTALL) $(wildcard *.spec) | xargs pfexec pkg install -v

check_install:
	$(CHECK_INSTALL) $(wildcard *.spec)

clean:
	rm -f $(TARGET) $(patsubst %.info,%.proto,$(TARGET))
