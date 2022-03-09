# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_execute.py
# author: ScCcWe
# time: 2022/3/8 9:45 上午
from tests.dao.table_dao import StudentDao

student_dao = StudentDao()


def test_execute_common_sql():
    """版本信息只有一条"""
    result = student_dao.execute_sql("select version();")
    assert type(result) == list
    assert len(result) == 1


def test_execute_ops_sql():
    """默认student表中是三个数据"""
    result = student_dao.execute_sql("select * from student")
    assert type(result) == list
    assert len(result) == 3


def test_execute_steps():
    """先insert，在delete；对比前后查询出的数据数量"""
    origin_len = len(student_dao.select_list())

    insert_row = student_dao.execute_sql("""
    insert into student(`student_name`, `student_age`, `class_id`) 
    values('测试1', '12', 2)""", commit=True)
    assert insert_row == 1

    delete_row = student_dao.execute_sql("""
    delete from student where student_name='测试1' and student_age='12'
    """)
    assert delete_row == 1

    assert origin_len == len(student_dao.select_list())
