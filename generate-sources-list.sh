#!/bin/sh
set -eu

i=1000
for p in $(ls javapackages-bootstrap-*/project/*.properties | xargs -n1 basename | sed s/.properties$//); do
    i=$(expr $i + 1)
    echo "Source$i:     $p.tar.xz"
done
