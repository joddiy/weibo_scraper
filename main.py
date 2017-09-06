# -*- coding: utf-8 -*-
# file: main.py
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


import argparse

from src.extract.extract_factory import get_extract
from src.config import weibo_config


def parse_args():
    parser = argparse.ArgumentParser(description='WeiBo Scraper. joddiyzhang@gmail.com')

    help_ = 'debug mode for develop. set 1 on, set 0 off.'
    parser.add_argument('-d', '--debug', default='1', help=help_)

    help_ = 'which model to select.'
    parser.add_argument('-m', '--model', default='weibo', help=help_)

    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    model = args.model
    if model not in weibo_config.SUPPORT_MODEL:
        print('model %s should be one of' % model, weibo_config.SUPPORT_MODEL)
    else:
        if args.debug == '1':
            extract = get_extract(model)
            extract.run()

        elif args.debug == '0':
            pass

        else:
            print('debug mode error, set 1 on, set 0 off.')
