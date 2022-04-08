# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_list.py
# author: ScCcWe
# time: 2022/3/9 2:01 下午
from tests.curd import base
from tests import student_list_123


class TestSelectList(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        super(TestSelectList, self).setUp()

    def test_query_length(self):
        assert len(self.studentDao.select_list()) == 3 == len(self.studentDao.select_list(3))
        assert len(self.studentDao.select_list(1)) == 1
        assert len(self.studentDao.select_list(2)) == 2

    def test_query(self):
        assert self.studentDao.select_list() == student_list_123

    def tearDown(self) -> None:
        self.studentDao.execute_sql("use test1")
        self.studentDao.execute_sql("drop table student")
