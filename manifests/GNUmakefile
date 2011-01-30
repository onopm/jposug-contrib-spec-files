#
# only dependency environment.
#

-include ../bin/common.mak
-include $(TARGETMAK)

all: $(TARGET)

.SUFFIXES: .lst .manifest
.SUFFIXES : .manifest .info

.lst.manifest:
	cat $< | ../bin/mk-Requires.pl -i -n `echo $<| sed 's/\.lst$$//` > $@

.manifest.info:
	$(PKGSEND_MANIFEST) $<
	pfexec pkg refresh $(REPOSITRY) 
	pfexec pkg install -v pkg://$(REPOSITRY)/$(patsubst %.manifest,%,$<)
	pfexec pkg info $(patsubst %.manifest,%,$<) > $@

depend:
	echo TARGET=$(patsubst %.lst,%.info,$(wildcard *.lst)) > $(TARGETMAK)
	echo 'all : $$(TARGET)' >> $(TARGETMAK)

