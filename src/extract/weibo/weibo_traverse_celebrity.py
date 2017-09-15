# -*- coding: utf-8 -*-
# file: weibo_traverse_celebrity.py
# author: joddiyzhang@gmail.com
# time: 2017/9/15 下午5:27
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
import pymysql
import random
import time
import json
from src.utils.utils import get_html
from src.config import weibo_config
import redis


class WeiBoTraverseCelebrity(object):
    def __init__(self, cookies, headers, config):
        self.cookies = cookies
        self.headers = headers
        self.config = json.loads(config)
        db_config = weibo_config.DB_CONFIG
        self.db = pymysql.connect(host=db_config['host'], user=db_config['username'],
                                  password=db_config['password'],
                                  db=db_config['db'], charset="utf8")
        self.table = db_config['table']['traverse_celebrity']
        self.redis = redis.StrictRedis(host="localhost", port=6379, db=0)

    def __iter__(self):
        cursor = self.db.cursor()
        idx = self.redis.get('traverse_celebrity_idx')
        if idx is None:
            idx = 0
        else:
            idx = int(idx)
        cursor.execute("SELECT uid FROM find_celebrity WHERE id > %s" % idx)
        row = cursor.fetchone()
        user_id = '15623006741'
        # get a user from db
        while row is not None:
            try:
                print(row[0])
                # get the user's like url
                uurl = "https://weibo.cn/%s" % row[0]
                udiv = self._get_udiv(uurl, self.cookies[user_id], self.headers[user_id])
                url = self._get_like_href(udiv)
                # traverse to get all like persons in 20 pages
                for page in range(1, 21):
                    yield from self._crawl(url, page, user_id)
                    print(page)
            except:
                print("error")
                pass
            time.sleep(random.uniform(1, 2))
            row = cursor.fetchone()
            self.redis.set('traverse_celebrity_idx', idx + 1)
        cursor.close()
        self.db.close()

    def _crawl(self, url, page, user_id):
        url = "https://weibo.cn" + url + '?page=%d' % page
        x_tree = get_html(url, (), self.cookies[user_id], self.headers[user_id])
        divs = x_tree.xpath("/html/body/table")
        # get all info in this page
        for child in divs:
            try:
                uurl = self._get_uurl(child)
                if uurl == 'https://weibo.cn/':
                    continue
                time.sleep(random.uniform(1, 2))
                udiv = self._get_udiv(uurl, self.cookies[user_id], self.headers[user_id])
                row = {
                    "cate": 'traverse',
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

    def _get_udiv(self, uurl, cookie, header):
        """
        get user homepage div
        :param uid:
        :param cookie:
        :param header:
        :return:
        """

        u_tree = get_html(uurl, (), cookie, header)
        return u_tree.xpath("/html/body/div[@class='u'][1]/div")[0]

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
        tmp = x_tree.xpath("a[last()-2]/text()")[0]
        return tmp[3:len(tmp) - 1]

    @staticmethod
    def _get_like_num(x_tree):
        """
        get like number
        :param x_tree:
        :return:
        """
        tmp = x_tree.xpath("a[last()-3]/text()")[0]
        return tmp[3:len(tmp) - 1]

    @staticmethod
    def _get_like_href(x_tree):
        """
        get like href
        :param x_tree:
        :return:
        """
        return x_tree.xpath("a[last()-3]/@href")[0]
