# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: connections_.py
# author: ScCcWe
# time: 2022/3/4 11:24 上午
import pymysql

db_example_conn = pymysql.connect(
    host='localhost',
    user="root",
    password='beicuide123',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)
