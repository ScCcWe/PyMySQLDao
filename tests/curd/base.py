# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: base.py
# author: ScCcWe
# time: 2022/3/9 3:58 下午
import unittest

import pymysql
from pymysql.connections import Connection

import pymysqldao


databases = [
    {
        "host": "localhost",
        "user": "root",
        "passwd": "beicuide123",
        "database": "test1"
    },
    # {
    #     "host": "localhost",
    #     "user": "root",
    #     "passwd": "beicuide123",
    #     "database": "test2"
    # }
]


def connect(**params):
    p = databases[0].copy()
    p.update(params)

    conn = pymysql.connect(**p)

    return conn


class PyMySQLDaoTestCase(unittest.TestCase):
    databases = databases

    conn: Connection = None

    # def setUp(self) -> None:
    #     with self.conn:
    #         with self.conn.cursor() as cursor:
    #             cursor.execute("create database if not exists test1;")
    #         self.conn.commit()

    def connect(self, **params):
        p = self.databases[0].copy()
        p.update(params)

        conn = pymysql.connect(**p)

        return conn

    # def tearDown(self) -> None:
    #     if self.conn.open:
    #         self.conn.close()
