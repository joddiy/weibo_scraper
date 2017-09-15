# -*- coding: utf-8 -*-
# file: utils.py
# author: joddiyzhang@gmail.com
# time: 2017/9/8 下午4:43
# Copyright (C) <2017>  <Joddiy Zhang>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------
import time
import requests
from lxml import etree
import redis

def format_time(s):
    """

    :param s:
    :return:
    """
    tem_pos = s.find('来自')
    tem_txt = s[:tem_pos].strip()
    tem_pos = tem_txt.find('前')
    if tem_pos == -1:
        if tem_txt.find('今天') == -1:
            if tem_txt.find('月') != -1:
                tem_txt = tem_txt.replace('月', '-').replace('日', '').strip()
                return time.strftime("%Y-") + tem_txt + ":00"
            else:
                return tem_txt
        else:
            return time.strftime("%Y-%m-%d ") + tem_txt[3:].strip() + ":00"
    else:
        num = int(tem_txt[:tem_pos - 2].strip())
        t_time = time.gmtime(int(time.time() - 60 * num) + 8 * 3600)
        return time.strftime("%Y-%m-%d %H:%M:00", t_time)


def get_html(url, params, cookie, header):
    """

    :param url:
    :param params:
    :param cookie:
    :param header:
    :return:
    """
    url = url % params
    cookie = {
        "Cookie": cookie
    }
    html = requests.get(url, cookies=cookie, headers=header).content
    return etree.HTML(html)


