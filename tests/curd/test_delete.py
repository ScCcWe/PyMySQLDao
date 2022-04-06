# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_delete.py
# author: ScCcWe
# time: 2022/3/6 10:33 下午
from tests.curd import base


class TestDelete(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        super(TestDelete, self).setUp()

    def test_select_by_field_val_value(self):
        # 删除id为1的数据
        # 删除成功返回1
        assert self.studentDao.delete_by_id(1) == 1

        # 总共有三条数据，删除一条之后，还剩两条
        assert 2 == len(self.studentDao.select_list())

    def tearDown(self) -> None:
        self.studentDao.execute_sql("use test1")
        self.studentDao.execute_sql("drop table student")
