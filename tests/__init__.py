# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: __init__.py
# author: ScCcWe
# time: 2022/3/4 3:43 下午
none_list = ["", None, {}, [], ()]
class_obj_id_1 = {'id': 1, 'class_name': '火箭班', 'is_delete': 0}
class_obj_id_2 = {'id': 2, 'class_name': '骏马班', 'is_delete': 0}
class_obj_id_3 = {'id': 3, 'class_name': '明日之星', 'is_delete': 0}
student_obj_list_id_123 = [
    {'id': 1, 'student_name': '张三1', 'student_age': '121', 'class_id': 1, 'is_delete': 0},
    {'id': 2, 'student_name': '李四', 'student_age': '13', 'class_id': 1, 'is_delete': 0},
    {'id': 3, 'student_name': '王五', 'student_age': '11', 'class_id': 2, 'is_delete': 0}
]

__all__ = [
    "class_obj_id_1",
    "none_list",
    "student_obj_list_id_123",
]
