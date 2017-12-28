#!/bin/sh

if [ -z $1 ];then
    echo "install_spec.sh .proto"
    exit 1
fi

if [ -z $PKGBUILD_IPS_REPO ];then
    PKGBUILD_IPS_REPO=localhost
fi

if [ ${1%.proto} != $1 ];then
    NODENAME=${1%.proto}
elif [ ${1%.spec} != $1 ];then
    NODENAME=${1%.spec}
else
    NODENAME=$1
fi

SPECNAME=${NODENAME}.spec
INFONAME=${NODENAME}.info
S2I=./spec2ipsname.list

PKGNAME=`cat ${S2I} | awk -F: '
{
    if($1 == "'${SPECNAME}'") {
        num=split($2,arr," ")
      	for(i = 1; i <= num; i++) {
            printf "pkg://'${PKGBUILD_IPS_REPO}'/%s ",arr[i]
	}
    }
}
'`

echo "Install packages : ${PKGNAME}"
if [ ! -z $PKGNAME ];then
    sudo pkg install -v ${PKGNAME}
    RES=$?
    if [ ${RES} = 0 -o ${RES} = 4 ] ; then
	echo Get info files ${INFONAME}
	sudo pkg info ${PKGNAME} > ${INFONAME}
    fi
    exit $RES
else
    echo "PKGNAME is not found in $SPECNAME"
    exit 1
fi
