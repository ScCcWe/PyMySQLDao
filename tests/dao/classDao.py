# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: classDao.py
# author: ScCcWe
# time: 2022/3/4 10:54 上午
from pymysqldao import BaseDao

from .connections_ import db_example_conn


class ClassDao(BaseDao):
    def __init__(self):
        super(ClassDao, self).__init__(db_example_conn, "class")
