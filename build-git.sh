#!/bin/bash
tag=$(git describe --always)
archive=lets-encrypt-$tag.tar

git archive --prefix=lets-encrypt-$tag/ master > $archive
mkdir lets-encrypt-$tag/ 2>/dev/null
sed -e "s/<GIT-TAG>/$tag/" < lets-encrypt.spec.in > lets-encrypt-$tag/lets-encrypt.spec
tar rf $archive lets-encrypt-$tag/
cat $archive | xz > $archive.xz
rpmbuild -tb $archive
rpmbuild -ts $archive
