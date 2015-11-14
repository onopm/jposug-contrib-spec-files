#!/bin/sh
exec /usr/php/5.4/bin/php -C -d include_path=/usr/share/pear/5.4 \
    -d output_buffering=1 //usr/share/pear/5.4/pearcmd.php "$@"
