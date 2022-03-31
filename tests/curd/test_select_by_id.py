# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_by_id.py
# author: ScCcWe
# time: 2022/3/4 4:19 下午
import pytest
import pymysql

from pymysqldao import err_, BaseDao
from tests import class_1
from tests.curd import base


class ClassDao(BaseDao):
    def __init__(self):
        super().__init__(base.connect(cursorclass=pymysql.cursors.DictCursor), "class")


classDao = ClassDao()


class TestSelectById(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        self.conn = super().connect(cursorclass=pymysql.cursors.DictCursor)

        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                create table class (
                   id bigint(20) unsigned primary key auto_increment,
                   class_name varchar(50) not null unique,
                   is_delete tinyint default 0
                )engine=innodb
                 auto_increment=1
                 default charset=utf8;
                """)
            self.conn.commit()

            with self.conn.cursor() as cursor:
                cursor.execute("""
                insert into class (class_name) 
                values ("火箭班"), ("骏马班"), ("明日之星");
                """)
            self.conn.commit()

    def test_validation(self):
        for none_value in ["", 0j, None, [], (), {}]:
            pytest.raises(ValueError, classDao.select_by_id, none_value)

        # for a in [0, -0]:
        #     pytest.raises(ValueError, classDao.select_by_id, a)

    def test_param_type(self):
        pytest.raises(err_.PrimaryKeyError, classDao.select_by_id, 1, 1)

    def test_query(self):
        for item in [1, "1"]:
            assert classDao.select_by_id(item) == class_1

        # TODO: 主键值不为'id'

    def tearDown(self) -> None:
        classDao.execute_sql("use test1")
        classDao.execute_sql("drop table class")
