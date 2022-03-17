# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: base.py
# author: ScCcWe
# time: 2022/3/9 3:58 下午
import unittest

import pymysqldao


class PyMySQLDaoTestCase(unittest.TestCase):
    databases = [
        {
            "host": "localhost",
            "user": "root",
            "passwd": "",
            "database": "test1",
            "use_unicode": True,
            "local_infile": True,
        },
        {"host": "localhost", "user": "root", "passwd": "", "database": "test2"},
    ]

