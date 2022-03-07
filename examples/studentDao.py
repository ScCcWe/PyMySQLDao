# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: studentDao.py
# author: ScCcWe
# time: 2022/3/4 10:54 上午
from src.pymysqldao import BaseDao

from examples.connections_ import db_example_conn


class StudentDao(BaseDao):
    def __init__(self):
        super().__init__(db_example_conn, "student")
        # self.debug = False
