# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_insert.py
# author: ScCcWe
# time: 2022/3/4 4:38 下午
from tests.dao.studentDao import StudentDao

student_dao = StudentDao()

# TODO: 主键名不为id


def test_insert_one_normal():
    """没有id, 正常"""
    obj_dict_stu = {
        "class_id": 1,
        "student_age": "20",
        "student_name": "张麻子",
    }
    assert student_dao.insert_one(obj_dict_stu) == 1

    # 删除
    student_info_list = student_dao.select_by_field("张麻子", "student_name")
    student_dao.delete_by_id(student_info_list[0]["id"])


def test_insert_one_outOfOrder():
    """
    没有id, 乱序dict

    obj_dict_stu = {
        "student_name": "张麻子",
        "student_age": "20",
        "class_id": 1,
    }

    """
    obj_dict_stu = {
        "class_id": 1,
        "student_age": "20",
        "student_name": "张麻子",
    }
    assert student_dao.insert_one(obj_dict_stu) == 1

    # 删除
    student_info_list = student_dao.select_by_field("张麻子", field_key="student_name")
    student_dao.delete_by_id(student_info_list[0]["id"])


def test_insert_one_normal_with_id():
    """有id, 正常"""
    obj_dict_stu = {
        "id": 20,
        "class_id": 1,
        "student_age": "20",
        "student_name": "张麻子",
    }
    assert student_dao.insert_one(obj_dict_stu) == 1

    # 删除
    student_info_list = student_dao.select_by_field("张麻子", "student_name")
    student_dao.delete_by_id(student_info_list[0]["id"])


def test_insert_one_outOfOrder_with_id():
    """有id, 乱序"""
    obj_dict_stu = {
        "id": 20,
        "student_age": "20",
        "class_id": 1,
        "student_name": "张麻子",
    }
    assert student_dao.insert_one(obj_dict_stu) == 1

    # 删除
    student_info_list = student_dao.select_by_field("张麻子", "student_name")
    student_dao.delete_by_id(student_info_list[0]["id"])
