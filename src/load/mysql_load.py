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
    def __init__(self, extract):
        self.db = self._connect_db(extract)
        self.interval = 5000
        pass

    @staticmethod
    def _connect_db(extract):
        if extract == 'weibo':
            db_config = weibo_config.DB_CONFIG
            return pymysql.connect(db_config['host'], db_config['username'], db_config['password'], db_config['db'])

    def run(self, data):
        db = self.db
        cursor = db.cursor()

        # SQL 插入语句
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                 LAST_NAME, AGE, SEX, INCOME)
                 VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        for item in data:
            keys = "','".join(item.keys())
            values = "','".join(item.keys())


        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()

        # 关闭数据库连接
        db.close()
