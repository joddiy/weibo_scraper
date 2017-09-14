# -*- coding: utf-8 -*-
# file: weibo_hot_search.py
# author: joddiyzhang@gmail.com
# time: 2017/9/7 下午5:05
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
from src.utils.utils import format_time


class WeiBoHotSearch(object):
    def __init__(self, cookies, headers, config):
        self.cookies = cookies
        self.headers = headers
        self.config = json.loads(config)

    def __iter__(self):
        for page in range(30):
            yield from self._crawl(self.config['keyword'], page, '15623006741')
            time.sleep(random.uniform(1, 2))
            print(page)

    def _crawl(self, keyword, page, user_id):
        url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%s&filter=hasori&sort=hot&page=%d' % (
            keyword, page)
        cookie = {
            "Cookie": self.cookies[user_id]
        }
        html = requests.get(url, cookies=cookie, headers=self.headers[user_id]).content
        x_tree = etree.HTML(html)
        divs = x_tree.xpath("/html/body/div[contains(@id,'M_')]")
        if len(divs) < 10:
            yield None
        for child in divs:
            row = {
                "topic": self.config['keyword'],
                "cid": self._get_cid(child),
                "uid": self._get_uid(child),
                "uname": self._get_uname(child),
                "data": self._get_commit_text(child),
                "cnum":self._get_comment_num(child),
                "commit_time": self._get_commit_time(child)
            }
            print(row)
            exit()
            yield row

    @staticmethod
    def _get_uname(x_tree):
        """
        get user name
        :param x_tree:
        :return:
        """
        return x_tree.xpath('div[1]/a[1]/text()')[0]

    @staticmethod
    def _get_cid(x_tree):
        """
        get weibo comment id
        :param x_tree:
        :return:
        """
        return x_tree.xpath('@id')[0][2:]

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
    def _get_comment_num(x_tree):
        """
        get comment number
        :param x_tree:
        :return:
        """
        str = x_tree.xpath("div[last()]/a[last()-1]/text()")[0]
        return str[3:len(str) - 1]

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
