# -*- coding: utf-8 -*-
# file: main.py
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


import argparse

from src.load.load_factory import get_load
from src.extract.extract_factory import get_extract
from src.config import common_config


def parse_args():
    parser = argparse.ArgumentParser(description='WeiBo Scraper. joddiyzhang@gmail.com')

    help_ = 'debug mode for develop. set 1 on, set 0 off.'
    parser.add_argument('-d', '--debug', default='1', help=help_)

    help_ = 'which extract to select.'
    parser.add_argument('-e', '--extract', default='weibo', help=help_)

    help_ = 'which model to select.'
    parser.add_argument('-f', '--model', default='traverse_celebrity', help=help_)

    help_ = 'config sent to model.'
    parser.add_argument('-c', '--config', default='{"keyword":"铃木达央"}', help=help_)

    help_ = 'which load to select.'
    parser.add_argument('-l', '--load', default='mysql', help=help_)

    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    extract = args.extract
    model = args.model
    config = args.config
    load = args.load
    if extract not in common_config.SUPPORT_EXTRACT:
        print('extract %s should be one of' % extract, common_config.SUPPORT_EXTRACT)
    else:
        if args.debug == '1':
            data = get_extract(extract).run(model, config)
            get_load(load).run(extract, model, data)

        elif args.debug == '0':
            pass
