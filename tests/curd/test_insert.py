# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_insert.py
# author: ScCcWe
# time: 2022/3/4 4:38 下午
from tests.dao.classDao import ClassDao
from tests.dao.studentDao import StudentDao

class_dao = ClassDao()
student_dao = StudentDao()


def test_insert_one1():
    # 新增
    obj_dict = {
        "class_name": "少年班",
    }
    assert class_dao.insert_one(obj_dict) == 1

    # 删除
    class_info_list = class_dao.select_by_field("少年班", "class_name")
    class_dao.delete_by_id(class_info_list[0]["id"])


def test_insert_one2():
    # 新增
    obj_dict_stu = {
        "student_name": "张麻子",
        "student_age": "20",
        "class_id": 1,
    }
    assert student_dao.insert_one(obj_dict_stu) == 1

    # 删除
    student_info_list = student_dao.select_by_field("张麻子", "student_name")
    student_dao.delete_by_id(student_info_list[0]["id"])
