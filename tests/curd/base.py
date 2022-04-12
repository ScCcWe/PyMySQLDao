# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: base.py
# author: ScCcWe
# time: 2022/3/9 3:58 下午
import unittest

import pymysql
from pymysql.connections import Connection

from pymysqldao import CRUDHelper

databases = [
    {
        "host": "localhost",
        "user": "root",
        "passwd": "",
        "database": "test1"
    }
]


def connect(**params):
    p = databases[0].copy()
    p.update(params)

    conn = pymysql.connect(**p)

    return conn


class StudentDao(CRUDHelper):
    def __init__(self):
        super().__init__(connect(cursorclass=pymysql.cursors.DictCursor), "student")


class ClassDao(CRUDHelper):
    def __init__(self):
        super().__init__(connect(cursorclass=pymysql.cursors.DictCursor), "class")


class TeacherDao(CRUDHelper):
    def __init__(self):
        super().__init__(connect(cursorclass=pymysql.cursors.DictCursor), "teacher")


class PyMySQLDaoTestCase(unittest.TestCase):
    databases = databases
    studentDao = StudentDao()
    teacherDao = TeacherDao()
    classDao = ClassDao()

    conn: Connection

    def setUp(self) -> None:
        self.conn = connect(cursorclass=pymysql.cursors.DictCursor)
        with self.conn:
            self.create_table_student()
            self.insert_data()

            self.create_table_teacher()

    def create_table_teacher(self):
        pass

    def create_table_student(self):
        with self.conn.cursor() as cursor:
            student_sql = """
                create table if not exists student(
                    id bigint(20) unsigned primary key auto_increment,
                    student_name varchar(10) not null,
                    student_age varchar (5) not null,
                    class_id bigint(20) not null ,
                    is_delete tinyint default 0,
                    index idx_clsid (class_id),
                    index idx_name (student_name),
                    index idx_age (student_age)
                )engine=innodb
                 auto_increment=1
                 default charset=utf8;
                """
            cursor.execute(student_sql)
        self.conn.commit()

    def insert_data(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO student (student_name, student_age, class_id) 
                VALUES ("张三", "12", 1), ("李四", "13", 1), ("王五", "11", 2);
                """)
        self.conn.commit()

    # def connect(self, **params):
    #     p = self.databases[0].copy()
    #     p.update(params)
    #
    #     self.conn = pymysql.connect(**p)
    #
    #     return self.conn

    # def tearDown(self) -> None:
    #     with self.conn:
    #         with self.conn.cursor() as cursor:
    #             cursor.execute("drop table student")
    #         self.conn.commit()
