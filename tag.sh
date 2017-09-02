#!/bin/bash
# 打 tag 工具

# 使用前需要提权 chmod +x ./tag.sh

VERSION="V2.4.1"
DATE=$(date +%Y%m%d-%H%M%S)
TAG="$VERSION-$DATE"
git tag -a ${TAG} -m ${TAG}
git push --tag
echo ${TAG}
