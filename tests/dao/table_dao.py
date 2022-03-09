# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: table_dao.py
# author: ScCcWe
# time: 2022/3/4 10:54 上午
import sys
import logging

from pymysqldao import BaseDao, LOGGER

from .connections_ import db_example_conn

# 设置日志等级为DEBUG，并可以打印出来
# （如果你不需要日志，直接注释掉即可
LOGGER.setLevel(logging.DEBUG)
s_h = logging.StreamHandler(sys.stderr)
LOGGER.addHandler(s_h)


class ClassDao(BaseDao):
    def __init__(self):
        super(ClassDao, self).__init__(db_example_conn, "class")


class StudentDao(BaseDao):
    def __init__(self):
        super().__init__(db_example_conn, "student")
