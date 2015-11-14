#!/bin/sh
exec /usr/php/5.3/bin/php -d memory_limit="-1" -C -q -d include_path=/var/php/5.3/pear \
    -d output_buffering=1 /var/php/5.3/pear/pearcmd.php "$@"
