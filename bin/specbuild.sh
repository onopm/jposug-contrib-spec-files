#!/bin/ksh

PKGTOOL=/opt/dtbld/bin/pkgtool
SOURCES=~/packages/SOURCES/

SPEC=$1

if [ -z "${SPEC}" ];then
    echo set file.spec
    echo specbuild.sh file.spec
    exit 1
fi

if [ ! -f "${SPEC}" ] ; then
    echo specbuild.sh file.spec
    exit 1
fi
NODE=${1%.spec}

VERSION=`uname -v`

case ${VERSION} in
    snv*)
	echo "OpenSolaris. set --ips"
	REPTYPE='--ips'
	;;
    Generic*)
	echo "Solaris. set --svr4"
	REPTYPE='--svr4'
	;;
    *)
	echo "Default: set --ips"
	REPTYPE='--ips'
esac


${PKGTOOL} build-only --patchdirs=`pwd`/patches --sourcedirs=`pwd` ${REPTYPE} --download ${SPEC}
RESULT=$?
if [ ${RESULT} = 0 -a ${REPTYPE} = '--svr4' ];then
    pkgtrans ~/packages/PKGS/ ~/packages/PKGS/${SPEC%.*}.pkg ${SPEC%.*}
fi
