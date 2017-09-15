# -*- coding: utf-8 -*-
# file: weibo_find_celebrity.py
# author: joddiyzhang@gmail.com
# time: 2017/9/15 上午2:20
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

import requests
import random
import time
import json
from lxml import etree
from src.utils.utils import get_html
from src.config.weibo_config import CELEBRITY_CATEGORY


class WeiBoFindCelebrity(object):
    def __init__(self, cookies, headers, config):
        self.cookies = cookies
        self.headers = headers
        self.config = json.loads(config)

    def __iter__(self):
        for page in range(1, 10):
            for cate in CELEBRITY_CATEGORY:
                try:
                    yield from self._crawl(cate, page, '15623006741')
                    time.sleep(random.uniform(1, 2))
                    print(page, cate)
                except:
                    continue

    def _crawl(self, keyword, page, user_id):
        url = 'https://weibo.cn/pub/top?cat=%s&page=%d'
        params = (keyword, page)
        x_tree = get_html(url, params, self.cookies[user_id], self.headers[user_id])
        divs = x_tree.xpath("/html/body/div[6]/table")
        for child in divs:
            try:
                uurl = self._get_uurl(child)
                if uurl == 'https://weibo.cn/':
                    continue
                u_tree = get_html(uurl, (), self.cookies[user_id], self.headers[user_id])
                udiv = u_tree.xpath("/html/body/div[@class='u'][1]/div")[0]
                row = {
                    "cate": keyword,
                    "uid": self._get_uid(uurl),
                    "uname": self._get_uname(child),
                    "cnum": self._get_post_num(udiv),
                    "fnum": self._get_fan_num(udiv),
                    "lnum": self._get_like_num(udiv),
                }
                print(row)
                yield row
            except:
                continue

    @staticmethod
    def _get_uid(udiv):
        """
        get user id
        :param x_tree:
        :return:
        """
        *_, uid = udiv.split('/')
        return uid

    @staticmethod
    def _get_uname(x_tree):
        """
        get user name
        :param x_tree:
        :return:
        """
        return x_tree.xpath('tr/td[2]/a[1]/text()')[0]

    @staticmethod
    def _get_uurl(x_tree):
        """

        :param x_tree:
        :return:
        """
        tmp = x_tree.xpath('tr/td[2]/a[1]/@href')[0]
        return tmp

    @staticmethod
    def _get_post_num(x_tree):
        """
        get post number
        :param x_tree:
        :return:
        """
        tmp = x_tree.xpath("span/text()")[0]
        return tmp[3:len(tmp) - 1]

    @staticmethod
    def _get_fan_num(x_tree):
        """
        get fans number
        :param x_tree:
        :return:
        """
        tmp = x_tree.xpath("a[last()-3]/text()")[0]
        return tmp[3:len(tmp) - 1]

    @staticmethod
    def _get_like_num(x_tree):
        """
        get like number
        :param x_tree:
        :return:
        """
        tmp = x_tree.xpath("a[last()-2]/text()")[0]
        return tmp[3:len(tmp) - 1]
