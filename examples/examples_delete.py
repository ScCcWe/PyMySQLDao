# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: examples_delete.py
# author: ScCcWe
# time: 2022/3/5 8:19 下午
from studentDao import StudentDao


student_dao = StudentDao()


def delete_example():

    # obj = student_dao.select_by_id(1)
    # print(obj)

    # del obj["id"]
    # del obj["is_delete"]
    # student_dao.insert_one(obj)

    student_dao_select_list = student_dao.select_list()
    for item in student_dao_select_list:
        print(item)

    # student_dao.delete_by_id(15)

    # student_dao_select_list = student_dao.select_list()
    # for item in student_dao_select_list:
    #     print(item)


if __name__ == '__main__':
    delete_example()
