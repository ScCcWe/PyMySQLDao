# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: md_examples.py
# author: ScCcWe
# time: 2022/3/9 9:23 上午
import sys
import logging

import pymysql
from pymysqldao import BaseDao, LOGGER

# 设置日志等级为DEBUG，并可以打印出来
# 只需要在顶层设置一次即可，重复设置会重复打印
# （如果不需要日志，不设置即可；默认即为不设置
# LOGGER.setLevel(logging.DEBUG)
# LOGGER.addHandler(logging.StreamHandler(sys.stderr))

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='beicuide123',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)


class ClassDao(BaseDao):
    def __init__(self):
        super(ClassDao, self).__init__(conn, "class")


if __name__ == '__main__':
    dao = ClassDao()

    print(dao.select_by_id_list([1, 2, 3]))
    print(dao.select_by_id_list(1))
