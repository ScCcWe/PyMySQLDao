# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: __init__.py
# author: ScCcWe
# time: 2022/3/4 3:43 下午
import datetime
from pymysqldao.constant_ import FALSE_VALUE_LIST

none_list = FALSE_VALUE_LIST

class_1 = {'id': 1, 'class_name': '火箭班', 'is_delete': 0}
class_2 = {'id': 2, 'class_name': '骏马班', 'is_delete': 0}
class_3 = {'id': 3, 'class_name': '明日之星', 'is_delete': 0}

student_list_123: list = [
    {'id': 1, 'student_name': '张三', 'student_age': '12', 'class_id': 1, 'is_delete': 0},
    {'id': 2, 'student_name': '李四', 'student_age': '13', 'class_id': 1, 'is_delete': 0},
    {'id': 3, 'student_name': '王五', 'student_age': '11', 'class_id': 2, 'is_delete': 0}
]

teacher_1 = {
    "teacher_id": 1,
    "teacher_name": "肖刚玉",
    "teacher_age": "46",
    "last_month_average": 125.12,
    # "joined_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "joined_time": datetime.datetime(2020, 3, 9, 15, 8, 2).strftime('%Y-%m-%d %H:%M:%S'),
}

__all__ = [
    "class_1",
    "none_list",
    "student_list_123",
]
