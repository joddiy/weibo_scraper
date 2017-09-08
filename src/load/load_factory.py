# -*- coding: utf-8 -*-
# file: load_factory.py
# author: joddiyzhang@gmail.com
# time: 2017/9/8 下午2:37
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


from src.config.common_config import SUPPORT_LOAD
from src.load.mysql_load import MysqlLoad


def get_load(load, extract):
    if load not in SUPPORT_LOAD:
        raise NameError('not supported load')
    if load == "mysql":
        return MysqlLoad(extract)

    assert 0, "Bad shape creation: " + load
