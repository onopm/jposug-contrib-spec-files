#!/bin/sh

if [ -z $1 ];then
    echo "install_spec.sh protofile"
    exit 1
fi

SPECNAME=${1%.proto}.spec
INFONAME=${1%.proto}.info
S2I=./spec2ipsname.list

PKGNAME=`cat ${S2I} | awk -F: '{if($1 == "'${SPECNAME}'"){print $2}}'`
echo "[${PKGNAME}]"
if [ ! -z $PKGNAME ];then
    echo sudo pkg install -v ${PKGNAME}
    sudo pkg install -v ${PKGNAME}
    RES=$?
    if [ $${RES} = 0 -o $${RES} = 4 ] ; then
	echo Get info files ${INFONAME}
	sudo pkg info ${PKGNAME} > ${INFONAME}
    fi
else
    echo "PKGNAME is not found in $SPECNAME"
    exit 1
fi
