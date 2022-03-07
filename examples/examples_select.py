# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: examples_select.py
# author: ScCcWe
# time: 2022/3/5 10:41 上午
import time

from classDao import ClassDao
from studentDao import StudentDao

class_dao = ClassDao()
student_dao = StudentDao()


def select_list():
    dao_select_list = class_dao.select_list()
    time.sleep(1)
    for item in dao_select_list:
        print(item)


def select_by_id():
    print(class_dao.select_by_id(1, primary_key="id"))
    print(class_dao.select_by_id(2))
    print(class_dao.select_by_id("3"))


def select_by_field():
    print(class_dao.select_by_field("火箭班", field_key="class_name"))


def select_by_id_list():
    print(class_dao.select_by_id_list([1, 2, 3]))
    print(student_dao.select_by_id_list([1, 2, 3]))


if __name__ == '__main__':
    # select_list()
    select_by_id()
    # select_by_field()
    # select_by_id_list()
