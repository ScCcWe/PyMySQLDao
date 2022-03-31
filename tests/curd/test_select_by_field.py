# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_by_field.py
# author: ScCcWe
# time: 2022/3/6 9:36 下午
import pytest
import pymysql

from pymysqldao import err_, BaseDao

from tests.curd import base
from tests import none_list, student_list_123


class StudentDao(BaseDao):
    def __init__(self):
        super().__init__(base.connect(cursorclass=pymysql.cursors.DictCursor), "student")


studentDao = StudentDao()


class TestSelectByField(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        self.conn = super().connect(cursorclass=pymysql.cursors.DictCursor)

        with self.conn:
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

            with self.conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO student (student_name, student_age, class_id) 
                VALUES ("张三", "12", 1), ("李四", "13", 1), ("王五", "11", 2);
                """)
            self.conn.commit()

    def test_validation(self):
        for none_value in none_list:
            pytest.raises(ValueError, studentDao.select_by_field, "student_name", none_value)

    def test_query(self):
        assert studentDao.select_by_field("student_name", "张三")[0] == student_list_123[0]
        assert studentDao.select_by_field("student_name", "张三", limit=5)[0] == student_list_123[0]

    def tearDown(self) -> None:
        studentDao.execute_sql("use test1")
        studentDao.execute_sql("drop table student")
