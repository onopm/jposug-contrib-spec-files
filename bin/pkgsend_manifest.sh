#!/bin/sh

MANIFEST=$1
VERSION=$2

if [ -z "${PKGBUILD_IPS_SERVER}" ];then
    PKGBUILD_IPS_SERVER=http://127.0.0.1/ 
fi

if [ -z "${VERSION}" ];then
    VERSION=1.0.0
fi

if [ -z "${MANIFEST}" ];then
    echo "not set manifestfile" > /dev/stderr
    exit 1
fi


MANIFEST_NODE=${MANIFEST%%.*}
OSVER=`uname -r`
OSREV=`uname -v | sed 's/[a-zA-Z_]//g'`
PKGNAME_FULL=${MANIFEST_NODE}@${VERSION},${OSVER}-0.${OSREV}
eval `pkgsend -s ${PKGBUILD_IPS_SERVER} open ${PKGNAME_FULL}`
pkgsend -s ${PKGBUILD_IPS_SERVER} include ${MANIFEST}
pkgsend -s ${PKGBUILD_IPS_SERVER} close
