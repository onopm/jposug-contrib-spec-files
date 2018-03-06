#!/bin/sh

INSTANCE=$1
SRC=$2
ZFS_PREFIX=$3
DATE=`date '+P_%Y%m%d%H%M%S'`

echo Snapshot ${ZFS_PREFIX}/${INSTANCE}@${DATE}
zfs snapshot ${ZFS_PREFIX}/${INSTANCE}@${DATE}
echo Disable pkg/server:${INSTANCE}
svcadm disable -s pkg/server:${INSTANCE}
echo copy contents
rsync -av \
 --exclude 'cfg_cache'\
 --exclude 'index' \
 --delete \
 ${SRC}/*\
 /var/pkg${INSTANCE}/root/
echo Enable pkg/server:${INSTANCE}
svcadm enable -s pkg/server:${INSTANCE}
