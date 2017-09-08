# -*- coding: utf-8 -*-
# file: utils.py
# author: joddiyzhang@gmail.com
# time: 2017/9/8 下午4:43
# Copyright (C) <2017>  <Joddiy Zhang>
#
# This file is part of GNU Bash, the Bourne Again SHell.
#
# Bash is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Bash is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Bash.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------
import time


def addslashes(s):
    d = {'"': '\\"', "'": "\\'", "\0": "\\\0", "\\": "\\\\"}
    return ''.join(d.get(c, c) for c in s)


def format_time(s):
    tem_pos = s.find('来自')
    tem_txt = s[:tem_pos].strip()
    tem_pos = tem_txt.find('前')
    if tem_pos == -1:
        if tem_txt.find('今天') == -1:
            if tem_txt.find('年') == -1:
                tem_txt = tem_txt.replace('月', '-').replace('日', '').strip()
                return time.strftime("%Y-") + tem_txt + ":00"
            else:
                tem_txt = tem_txt.replace('年', '-').replace('月', '-').replace('日', '').strip()
                return tem_txt + ":00"
        else:
            return time.strftime("%Y-%m-%d ") + tem_txt[3:].strip() + ":00"
    else:
        num = int(tem_txt[:tem_pos - 2].strip())
        t_time = time.gmtime(int(time.time() - 60 * num) + 8 * 3600)
        return time.strftime("%Y-%m-%d %H:%M:00", t_time)


if __name__ == '__main__':
    # text = '2016年09月06日 06:39 来自iPhone 7 Plus'
    # text = '55分钟前 来自微博 weibo.com'

    print(format_time(text))
