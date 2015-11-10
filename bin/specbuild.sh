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
    11.*|s12_*)
	echo "Solaris 11 mode. use IPS."
	REPTYPE='--ips'
	;;
    snv*)
	echo "OpenIndiana mode. use IPS."
	REPTYPE='--ips'
	;;
    oi*)
	echo "OpenIndiana mode. use IPS."
	REPTYPE='--ips'
	;;
    omnios*)
        echo "OpenIndiana(OmniOS) mode. use IPS."
        REPTYPE='--ips'
        ;;
    Generic*)
	echo "Solaris 10 mode. use SVr4."
	REPTYPE='--svr4'
	;;
    *)
	echo "Warning: OS mode is known. VERSION=$VERSION"
	exit 1
	;;
esac


LC_ALL=C ${PKGTOOL} build-only \
  --autodeps --nonotify --specdirs=`pwd`:`pwd`/include:`pwd`/base-specs \
  --patchdirs=`pwd`/patches \
  --sourcedirs=`pwd`/ext-sources:`pwd`/copyright:`pwd`/include \
  ${REPTYPE} \
  --download \
  ${SPEC}

RESULT=$?
if [ ${RESULT} = 0 -a ${REPTYPE} = '--svr4' ];then
    LC_ALL=C pkgtrans ~/packages/PKGS/ ~/packages/PKGS/${SPEC%.*}.pkg ${SPEC%.*}
fi
exit ${RESULT}
