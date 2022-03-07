# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: plus_connections.py
# author: ScCcWe
# time: 2022/3/5 8:17 上午
from pymysqldao import BaseDao
from pymysql.connections import Connection


class PlusConnection(Connection, BaseDao):
    def __init__(self):
        super().__init__()
