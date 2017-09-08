# -*- coding: utf-8 -*-
# file: extract_factory.py
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


from src.config.common_config import SUPPORT_EXTRACT
from src.extract.weibo_extract import WeiBoExtract


def get_extract(name):
    if name not in SUPPORT_EXTRACT:
        raise NameError('not supported model')
    if name == "weibo":
        return WeiBoExtract()

    assert 0, "Bad shape creation: " + name
