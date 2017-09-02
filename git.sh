#!/bin/bash
# 一键发布工具

# 使用前需要提权 chmod +x ./git.sh
Resource_Branch="master"
Destination_Branch="RELEASE"

# git checkout ${Resource_Branch}
git add -A
git commit -m 'commit'
git pull
git push
# git checkout ${Destination_Branch}
# git merge ${Resource_Branch} -m 'merge'
# git pull
# git push
# source $(cd $(dirname ${BASH_SOURCE:-$0});pwd)"/"tag.sh
# git checkout ${Resource_Branch}
