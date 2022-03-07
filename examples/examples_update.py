# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: examples_update.py
# author: ScCcWe
# time: 2022/3/5 4:12 下午

from studentDao import StudentDao


student_dao = StudentDao()


def update_by_id():

    obj = student_dao.select_by_id(1)
    print(obj)

    obj['student_name'] = "张三1"
    obj['student_age'] = "121"

    student_dao.update_by_id(obj)

    print(student_dao.select_by_id(1))


if __name__ == '__main__':
    update_by_id()
