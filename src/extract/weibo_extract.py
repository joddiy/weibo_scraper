# -*- coding: utf-8 -*-
# file: weibo_extract.py
# author: joddiyzhang@gmail.com
# time: 2017/9/6 下午9:45
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
from src.extract.weibo.weibo_hot_search import WeiBoHotSearch
from src.driver.weibo_driver import WeiBoDriver
from src.config.weibo_config import SUPPORT_MODEL


class WeiBoExtract(object):
    def __init__(self):
        driver = WeiBoDriver()
        self.cookies = driver.get_cookies()
        self.headers = driver.get_headers()

    def run(self, model, config):
        if model not in SUPPORT_MODEL:
            raise NameError('model %s should be one of' % model, SUPPORT_MODEL)
        if model == "hot_search":
            WeiBoHotSearch(self.cookies, self.headers, config).run()
