# -*- coding: utf-8 -*-
# file: weibo_driver.py
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

import json
import os
import pickle
import random
import time
from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException

from src.config.weibo_config import COOKIES_SAVE_PATH, LOGIN_URL, ACCOUNTS_PATH, PHANTOM_JS_PATH


class WeiBoDriver(object):
    def __init__(self):
        self.cookies = {}

    def run(self):
        self.load_cookies()

    def load_cookies(self):
        """
        load cookies from local file, if not exist then get it
        :return:
        """
        if os.path.exists(COOKIES_SAVE_PATH):
            with open(COOKIES_SAVE_PATH, 'rb') as f:
                self.cookies = pickle.load(f)

        self._generate_cookies()

        try:
            with open(COOKIES_SAVE_PATH, 'wb') as f:
                pickle.dump(self.cookies, f)
        except Exception as e:
            print(e)

    def _generate_cookies(self):
        """
        generate the account's cookie which hasn't been store in local file
        :return:
        """
        url_login = LOGIN_URL
        phantom_js_driver_file = os.path.abspath(PHANTOM_JS_PATH)
        if os.path.exists(phantom_js_driver_file):
            for account in self.load_accounts():
                account_id = account['id']
                account_password = account['password']
                if account_id in self.cookies:
                    continue
                try:
                    driver = webdriver.PhantomJS(phantom_js_driver_file)
                    # todo add random from specific configs
                    driver.set_window_size(1640, 689)
                    driver.get(url_login)
                    time.sleep(random.uniform(4, 6))
                    driver.find_element_by_xpath('//input[@id="loginName"]').send_keys(account_id)
                    driver.find_element_by_xpath('//input[@id="loginPassword"]').send_keys(account_password)
                    driver.find_element_by_xpath('//a[@id="loginAction"]').click()
                    cookie_list = driver.get_cookies()
                    cookie_string = ''
                    for cookie in cookie_list:
                        if 'name' in cookie and 'value' in cookie:
                            cookie_string += cookie['name'] + '=' + cookie['value'] + ';'
                    if 'SSOLoginState' in cookie_string:
                        self.cookies[account_id] = cookie_string

                except InvalidElementStateException as e:
                    print(e)

        else:
            pass

    @staticmethod
    def load_accounts():
        """
        load accounts from local file
        :return:
        """
        try:
            with open(ACCOUNTS_PATH, 'r') as f:
                data = json.load(f)
                return data['weibo']
        except Exception as e:
            print(e)
