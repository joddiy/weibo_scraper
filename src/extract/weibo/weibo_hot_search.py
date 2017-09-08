# -*- coding: utf-8 -*-
# file: weibo_hot_search.py
# author: joddiyzhang@gmail.com
# time: 2017/9/7 下午5:05
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
import requests
import random
import time
import json
from lxml import etree
from src.utils.utils import addslashes, format_time


class WeiBoHotSearch(object):
    def __init__(self, cookies, headers, config):
        self.cookies = cookies
        self.headers = headers
        self.data = []
        self.config = json.loads(config)

    def run(self):
        for page in range(100):
            self._crawl(self.config['keyword'], page, '15623006741')
            time.sleep(random.uniform(1, 2))
            print(page)
        return self.data

    def _crawl(self, keyword, page, user_id):
        url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%s&filter=hasori&page=%d' % (keyword, page)
        cookie = {
            "Cookie": self.cookies[user_id]
        }
        html = requests.get(url, cookies=cookie, headers=self.headers[user_id]).content
        x_tree = etree.HTML(html)
        divs = x_tree.xpath("/html/body/div[contains(@id,'M_')]")
        for child in divs:
            row = {
                "uid": addslashes(self._get_uid(child)),
                "uname": addslashes(self._get_uname(child)),
                "data": addslashes(self._get_commit_text(child)),
                "commit_time": addslashes(self._get_commit_time(child))
            }
            self.data.append(row)

    @staticmethod
    def _get_uname(x_tree):
        """
        get user name
        :param x_tree:
        :return:
        """
        return x_tree.xpath('div[1]/a[1]/text()')[0]

    @staticmethod
    def _get_uid(x_tree):
        """
        get user id
        :param x_tree:
        :return:
        """
        href = x_tree.xpath('div[1]/a[1]/@href')[0]
        *_, uid = href.split('/')
        return uid

    @staticmethod
    def _get_commit_time(x_tree):
        """
        get comment time
        :param x_tree:
        :return:
        """
        tmp = x_tree.xpath('div[last()]/span[last()]/text()')[0]
        return format_time(tmp)

    @staticmethod
    def _get_commit_text(x_tree):
        """
        get comment time
        :param x_tree:
        :return:
        """
        tmp = x_tree.xpath('string(div/span)')
        if tmp.startswith(':'):
            tmp = tmp[1:]
        if tmp.endswith('全文'):
            tmp = tmp[:-2]
        return tmp
