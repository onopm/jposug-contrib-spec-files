#!/bin/sh
exec /usr/php/5.4/bin/php -d memory_limit="-1" -C -q -d include_path=/usr/share/pear/5.4 \
    -d output_buffering=1 /usr/share/pear/5.4/pearcmd.php "$@"
