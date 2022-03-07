# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: inject_2.py
# author: ScCcWe
# time: 2022/3/5 8:35 上午
from examples.connections_ import db_example_conn


table_name = "python_example.student"


def inject1():
    with db_example_conn.cursor() as cursor:
        id_obj = "'1' or 2=2"
        name_obj = "'张三1' or 1=1"
        sql = f'SELECT count(*) as count FROM {table_name} WHERE id = {id_obj} AND student_name = {name_obj}'
        print("sql: ", sql)
        cursor.execute(sql)
        count = cursor.fetchone()
        print("count: ", count)
    if count is not None and count['count'] > 0:
        print('登陆成功')


def inject2():
    with db_example_conn.cursor() as cursor:
        id_obj = "'1' or 2=2"
        name_obj = "'张三' or 1=1"
        sql = f'SELECT count(*) as count FROM {table_name} WHERE id = %s AND student_name = %s'
        cursor.execute(
            sql,
            (id_obj, name_obj)
        )
        count = cursor.fetchone()
        print("count: ", count)
    if count is not None and count['count'] > 0:
        print('登陆成功')


if __name__ == '__main__':
    # inject1()
    inject2()
