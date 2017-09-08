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


class WeiBoHotSearch(object):
    def __init__(self, cookies, headers, config):
        self.cookies = cookies
        self.headers = headers
        self.config = json.loads(config)

    def run(self):
        for page in range(10):
            self._get_html(self.config['keyword'], page, '15623006741')
            time.sleep(random.uniform(1, 2))
        pass

    def _get_html(self, keyword, page, user_id):
            url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%s&page=%d' % (keyword, page)
            cookie = {
                "Cookie": self.cookies[user_id]
            }
            html = requests.get(url, cookies=cookie, headers=self.headers[user_id]).content
            x_tree = etree.HTML(html)
            divs = x_tree.xpath("/html/body/div[contains(@id,'M_')]")
            for child in divs:
                item_name = child.xpath('div[1]/a[1]/text()')[0]
                item_time = child.xpath('div[last()]/span[last()]/text()')[0]
                item_texts = child.xpath('div[1]/span/text()')
                item_text = ','.join(item_texts[:len(item_texts) - 1])
                print(item_name)
                print(item_text)
                print(item_time)
                print()
