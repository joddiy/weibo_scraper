# -*- coding: utf-8 -*-
# author: joddiy@qq.com
# Copyright 2017 joddiy. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='WeiBo Scraper. Joddiy@qq.com')

    help_ = 'debug mode for develop. set 1 on, set 0 off.'
    parser.add_argument('-d', '--debug', default='1', help=help_)

    args_ = parser.parse_args()
    return args_


if __name__ == '__main__':
    args = parse_args()
    if args.debug == '1':
        dispatcher = Dispatcher(id_file_path=None, mode='single', uid=uid, filter_flag=filter_flag)
        dispatcher.execute()
    elif args.debug == '0':
        pass

    else:
        print('debug mode error, set 1 on, set 0 off.')
