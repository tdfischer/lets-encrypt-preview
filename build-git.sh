#!/bin/bash
tag=$1
archive=lets-encrypt-$tag.tar

git archive --prefix=lets-encrypt-$tag/ $1 > $archive
xz > $archive.xz < $archive
