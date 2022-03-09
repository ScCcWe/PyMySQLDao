# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: md_examples.py
# author: ScCcWe
# time: 2022/3/9 9:23 上午
import sys
import logging

import pymysql
from pymysqldao import BaseDao, LOGGER

# 设置日志等级为DEBUG，并可以打印出来
# 只需要在顶层设置一次即可，重复设置会重复打印
# （如果不需要日志，不设置即可；默认即为不设置
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(logging.StreamHandler(sys.stderr))

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='beicuide123',
    database='python_example',
    cursorclass=pymysql.cursors.DictCursor
)


class ClassDao(BaseDao):
    def __init__(self):
        super(ClassDao, self).__init__(conn, "class")


if __name__ == '__main__':
    class_dao = ClassDao()

    # select list
    class_dao.select_list()
    class_dao.select_list(limit_size=500)
    class_dao.execute_sql("select * from class limit 500")

    # select by field
    class_dao.select_by_field("火箭班", field_key="class_name")
    class_dao.select_by_field("骏马班", field_key="class_name", limit_size=10)
    class_dao.execute_sql("select * from class where class_name='骏马班' limit 10")

    # select by id
    class_dao.select_by_id(1)
    class_dao.select_by_id("1")
    class_dao.select_by_id(1, primary_key="id")
    class_dao.execute_sql("select * from class where id=1")

    # select by id_list
    class_dao.select_by_id_list([1, 2, 3])  # default primary_key is "id"
    class_dao.select_by_id_list([1, 2, 3], primary_key="id")
    class_dao.execute_sql("select * from class where id in (1, 2, 3)")

    # insert
    class_dao.insert_one({"class_name": "少年班"})

    # update
    result = class_dao.select_by_field("少年班", field_key="class_name")
    result[0]["class_name"] = "少年班修改"
    class_dao.update_by_id(result[0])

    # delete
    class_dao.delete_by_id(result[0]["id"])
