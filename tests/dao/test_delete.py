# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_delete.py
# author: ScCcWe
# time: 2022/3/6 10:33 下午
from examples.studentDao import StudentDao

student_dao = StudentDao()


def test_select_by_field_val_value():
    # 新增
    obj_dict_stu = {
        "student_name": "新增学生A",
        "student_age": "20",
        "class_id": 1,
    }
    student_dao.insert_one(obj_dict_stu)
    student_info = student_dao.select_by_field("新增学生A", "student_name")

    # 删除
    assert student_dao.delete_by_id(student_info[0]["id"]) == 1
