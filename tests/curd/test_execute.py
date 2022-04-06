# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_execute.py
# author: ScCcWe
# time: 2022/3/8 9:45 上午
from tests.curd import base


class TestExecute(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_select_version(self):
        """版本信息只有一条"""
        result = self.studentDao.execute_sql("select version();")
        assert type(result) == list
        assert len(result) == 1

    def test_execute_ops_sql(self):
        """默认student表中是三个数据"""
        result = self.studentDao.execute_sql("select * from student")
        assert type(result) == list
        assert len(result) == 3

    def test_execute_steps(self):
        """先insert，在delete；对比前后查询出的数据数量"""
        count_num = len(self.studentDao.execute_sql("select * from student"))

        insert_row_num = self.studentDao.execute_sql("""
        insert into student(`student_name`, `student_age`, `class_id`) 
        values('测试1', '12', 2)""", commit=True)
        assert insert_row_num == 1
        assert count_num + 1 == len(self.studentDao.execute_sql("select * from student"))

        delete_row = self.studentDao.execute_sql("""
        delete from student where student_name='测试1' and student_age='12'
        """)
        assert delete_row == 1
        assert count_num == len(self.studentDao.execute_sql("select * from student"))

    def tearDown(self) -> None:
        self.studentDao.execute_sql("use test1")
        self.studentDao.execute_sql("drop table student")
