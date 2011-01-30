#!/bin/sh

function check_install {
    TEMP=`mktemp /tmp/check_install.XXXXXX`
    FMRI=${1%.spec}
    
    if pkg info $FMRI >$TEMP 2>1 ; then
	echo Already installed $FMRI
	mv $TEMP $FMRI.info 
	touch -c -t `cat $FMRI.info |perl -ne 'if(/FMRI:.*:20(\d\d)(\d\d)(\d\d)T(\d\d)(\d\d)(\d\d)/){print "$1$2$3$4$5.$6"}'` $FMRI.info
    else
	rm -f $TEMP
    fi
}

for SPEC in $*; do
    check_install $SPEC
done

