
-include common.mak
-include target.mak

depend:
	echo TARGET=$(patsubst %.spec,%.info,$(wildcard *.spec)) > $(TARGETMAK)
	echo 'all : $$(TARGET)' >> $(TARGETMAK)
	$(SPECDEPEND) $(wildcard *.spec) >> $(TARGETMAK)

preinstall:
	$(SPECDEPENDINSTALL) $(wildcard *.spec) | xargs pfexec pkg install -v

check_install:
	$(CHECK_INSTALL) $(wildcard *.spec)

clean:
	rm -f $(TARGET) $(patsubst %.info,%.manifest,$(TARGET))
