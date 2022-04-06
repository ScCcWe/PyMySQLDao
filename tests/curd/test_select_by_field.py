# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_by_field.py
# author: ScCcWe
# time: 2022/3/6 9:36 下午
import pytest

from tests.curd import base
from tests import student_list_123


class TestSelectByField(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        super(TestSelectByField, self).setUp()

    def test_validation(self):
        for none_value in [None, "", [], (), {}]:
            pytest.raises(ValueError, self.studentDao.select_by_field, "student_name", none_value)

    def test_query(self):
        assert self.studentDao.select_by_field("student_name", "张三")[0] == student_list_123[0]
        assert self.studentDao.select_by_field("student_name", "张三", limit=5)[0] == student_list_123[0]

    def tearDown(self) -> None:
        # super(TestSelectByField, self).tearDown()
        self.studentDao.execute_sql("use test1")
        self.studentDao.execute_sql("drop table student")
