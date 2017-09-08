# -*- coding: utf-8 -*-
# file: mysql_load.py
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
import pymysql

from src.load.ILoad import ILoad
from src.config import weibo_config


class MysqlLoad(ILoad):
    def __init__(self):
        self.interval = 5000
        pass

    def _render_db(self, extract, model):
        if extract == 'weibo':
            db_config = weibo_config.DB_CONFIG
            self.db = pymysql.connect(host=db_config['host'], user=db_config['username'],
                                      password=db_config['password'],
                                      db=db_config['db'], charset="utf8")
            self.table = db_config['table'][model]

    def run(self, extract, model, data):
        self._render_db(extract, model)
        db = self.db
        cursor = db.cursor()
        cursor.execute("SET NAMES utf8");

        insert_sql = ""
        # SQL 插入语句
        for item in data:
            sql = """INSERT INTO {table} ({K}) VALUES ('{V}')"""
            keys = ",".join(item.keys())
            values = "','".join(item.values())
            sql = sql.format(table=self.table, K=keys, V=values)
            insert_sql += sql + ";\n"
        print(insert_sql)
        try:
            # 执行sql语句
            cursor.execute(insert_sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()

        # 关闭数据库连接
        db.close()
