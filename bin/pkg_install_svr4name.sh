#!/bin/ksh

PKG_CLIENT_TIMEOUT=120;export PKG_CLIENT_TIMEOUT
VERSION=`uname -v | sed 's/[^0-9]//g'`
TEMP=`mktemp /tmp/pkg_install_svr4name.XXXXXX`

function get_ips_name {
    svr4pkgname=$1
    pkg search -r $svr4pkgname 2> /dev/null | awk '/^legacy_pkg.*'${VERSION}'$/{print $4}' | sort | tail -1
}

touch ${TEMP}
for pkgname in $*;do
    echo searching $pkgname' ... \c'
    if pkginfo $pkgname >/dev/null 2>1 ; then
	echo already installed
    else
	IPSNAME=`get_ips_name $pkgname`
	echo ${IPSNAME}
	echo ${IPSNAME}>> ${TEMP}
   fi
done
sort ${TEMP} | uniq | xargs echo pkg install -v 
rm -f ${TEMP}
