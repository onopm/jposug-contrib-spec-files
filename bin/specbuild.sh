#!/bin/ksh

getcmd() {
    CMD=''
    for _CMD in $* ; do
        CMD=`[ -x $_CMD ] && echo $_CMD`
        [ -z "$CMD" ] || break;
    done
    echo $CMD
}

PKGTOOL=`getcmd /bin/pkgtool /opt/dtbld/bin/pkgtool`
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
	echo "Solaris 11/OpenIndiana set --ips"
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


${PKGTOOL} build-only \
  --autodeps --nonotify --specdirs=`pwd`:`pwd`/include\
  --patchdirs=`pwd`/patches \
  --sourcedirs=`pwd`/ext-sources:`pwd`/copyright:`pwd`/include \
  ${REPTYPE} \
  --download \
  ${SPEC}

RESULT=$?
if [ ${RESULT} = 0 -a ${REPTYPE} = '--svr4' ];then
    pkgtrans ~/packages/PKGS/ ~/packages/PKGS/${SPEC%.*}.pkg ${SPEC%.*}
fi
exit ${RESULT}
