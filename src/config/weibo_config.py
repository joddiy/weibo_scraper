# -*- coding: utf-8 -*-
# file: weibo_config.py
# author: joddiyzhang@gmail.com
# time: 2017/9/6 下午9:45
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

import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__ + "/../../"))

LOGIN_URL = 'https://passport.weibo.cn/signin/login'

PHANTOM_JS_PATH = '/Users/joddiyzhang/Code/JS/phantomjs-2.1.1-macosx/bin/phantomjs'

COOKIES_SAVE_PATH = PROJECT_DIR + '/src/cache/cookies.pkl'

HEADERS_SAVE_PATH = PROJECT_DIR + '/src/cache/headers.pkl'

ACCOUNTS_PATH = PROJECT_DIR + '/src/cache/accounts.json'

DB_CONFIG = {
    'host': 'localhost',
    'username': 'root',
    'password': '123456',
    'db': 'main',
    'table': {
        'hot_search': 'weibo_hotsearch',
        'find_celebrity': 'find_celebrity',
        'traverse_celebrity': 'find_celebrity',
    }
}

CELEBRITY_CATEGORY = [
    'star',
    'grass',
    'content',
    'media'
]
