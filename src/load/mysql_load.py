# -*- coding: utf-8 -*-
# file: mysql_load.py
# author: joddiyzhang@gmail.com
# time: 2017/9/8 下午2:37
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
import pymysql

from src.load.ILoad import ILoad
from src.config import weibo_config
from warnings import filterwarnings


class MysqlLoad(ILoad):
    def __init__(self):
        self.interval = 10
        pass

    def _render_db(self, extract, model):
        if extract == 'weibo':
            db_config = weibo_config.DB_CONFIG
            self.db = pymysql.connect(host=db_config['host'], user=db_config['username'],
                                      password=db_config['password'],
                                      db=db_config['db'], charset="utf8")
            self.db.autocommit(True)
            filterwarnings('ignore', category=pymysql.Warning)
            self.table = db_config['table'][model]

    def run(self, extract, model, data):

        self._render_db(extract, model)
        db = self.db
        cursor = db.cursor()
        cursor.execute("SET NAMES utf8mb4")

        # try:

        cnt = 0
        items = []
        is_first = True
        # SQL 插入语句
        for item in data:
            if item is None:
                break
            if is_first:
                sql = """INSERT INTO {table} ({K}) VALUES ({V}) ON DUPLICATE KEY UPDATE """
                keys = ",".join(item.keys())
                values = "%s," * (len(item) - 1) + "%s"
                for key in item.keys():
                    sql += "%s=VALUES(%s)," % (key, key)
                sql = sql[:len(sql) - 1].format(table=self.table, K=keys, V=values)
                is_first = False
            if cnt >= self.interval:
                cursor.executemany(sql, items)
                cnt = 0
                items.clear()
            else:
                items.append(list(item.values()))
                cnt += 1
        if cnt > 0:
            cursor.executemany(sql, items)
            # except:
            #     db.rollback()

        cursor.close()
        db.close()
