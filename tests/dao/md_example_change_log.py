# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: md_examples.py
# author: ScCcWe
# time: 2022/3/9 9:23 上午
import sys
import logging

import pymysql
from pymysqldao import CRUDHelper, LOGGER

LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler(sys.stderr))

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)


class ClassDao(CRUDHelper):
    def __init__(self):
        super().__init__(connection=conn, table_name="class", size=500, use_own_log_config=True)


if __name__ == '__main__':
    # print(ClassDao.__mro__)
    dao = ClassDao()

    # select * from class limit 20
    dao.select_list()

    # select * from class limit 2
    dao.select_list(2)

    # select * from class where class_name='火箭班' limit 20
    dao.select_by_field("class_name", "火箭班")

    # select * from class where class_name='骏马班' limit 10
    dao.select_by_field("class_name", "骏马班", size=10)

    # select * from class where id=1
    dao.select_by_id(1)

    # select * from class where id in (1, 2, 3)
    dao.select_by_id_list([1, 2, 3])

    # insert into class("class_name") values("少年班")
    dao.insert_one({"class_name": "少年班"})

    # update by id
    result = dao.select_by_field("class_name", "少年班")
    result[0]["class_name"] = "少年班修改"
    dao.update_by_id(result[0])

    # delete by id
    dao.delete_by_id(result[0]["id"])
