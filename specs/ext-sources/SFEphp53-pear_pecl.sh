#!/bin/sh
exec /usr/php/5.3/bin/php -C -n -q -d include_path=/var/php/5.3/pear \
    -d output_buffering=1 /var/php/5.3/pear/peclcmd.php "$@"
