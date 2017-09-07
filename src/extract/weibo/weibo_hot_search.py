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
from lxml import etree


class WeiBoHotSearch:
    def __init__(self, cookies, headers):
        self.cookies = cookies
        self.headers = headers
        self.keyword = '111'
        self.current_page = 1

    def run(self):
        self._get_html('15623006741')
        pass

    def _get_html(self, user_id):
        url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword=%s&page=%d' % (self.keyword, self.current_page)
        cookie = {
            "Cookie": self.cookies[user_id]
        }
        self.html = requests.get(url, cookies=cookie, headers=self.headers[user_id]).content
        xtree = etree.HTML(self.html)

    def _get_user_name(self):
        print('-- getting user name')
        try:

            self.user_name = selector.xpath('//table//div[@class="ut"]/span[1]/text()')[0]
            print('current user name is: {}'.format(self.user_name))
        except Exception as e:
            print(e)
            print('html not properly loaded, maybe cookies out of date or account being banned. '
                  'change an account please')
            exit()
