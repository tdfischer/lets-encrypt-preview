#!/bin/bash
tag=$1
archive=letsencrypt-$tag.tar

git archive --prefix=letsencrypt-$tag/ $1 > $archive
xz > $archive.xz < $archive
