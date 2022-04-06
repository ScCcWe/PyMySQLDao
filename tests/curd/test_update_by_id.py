# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_insert.py
# author: ScCcWe
# time: 2022/3/4 4:38 下午
from tests.curd import base


class TestUpdate(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        super(TestUpdate, self).setUp()

    def test_update_by_id(self):
        # 查询出来一个id为1的对象
        select_by_id_student_obj = self.studentDao.select_by_id(1)

        new_student_name = select_by_id_student_obj["student_name"] + "修改"
        select_by_id_student_obj["student_name"] = new_student_name

        # 更新它的student_name
        self.studentDao.update_by_id(select_by_id_student_obj)

        # 验证更新
        assert self.studentDao.select_by_id(1)["student_name"] == new_student_name

    def tearDown(self) -> None:
        self.studentDao.execute_sql("use test1")
        self.studentDao.execute_sql("drop table student")
