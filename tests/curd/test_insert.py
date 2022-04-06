# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_insert.py
# author: ScCcWe
# time: 2022/3/4 4:38 下午
from tests.curd import base


class TestInsert(base.PyMySQLDaoTestCase):
    def setUp(self) -> None:
        super().setUp()

    def insert_data(self):
        pass

    def create_table_teacher(self):
        with self.conn.cursor() as cursor:
            teacher_sql = """
            create table teacher(
                teacher_id bigint(20) unsigned primary key auto_increment comment '教师表主键',
                teacher_name varchar(32) not null comment '教师姓名',
                teacher_age char(3) not null comment '教师年龄',
                last_month_average decimal(5, 2) not null comment '上个月平局分',
                joined_time datetime not null comment '入职时间',
                create_time datetime not null default current_timestamp comment '信息创建时间',
                update_time datetime not null default current_timestamp on update CURRENT_TIMESTAMP comment '信息更新时间',
                is_delete tinyint(1) default 0 comment '是否删除【1为是，0为否】'
            )engine=innodb
            auto_increment=1
            default charset=utf8;
            """
            cursor.execute(teacher_sql)
        self.conn.commit()

    def base_func(self, obj_dict_stu):
        assert self.studentDao.insert_one(obj_dict_stu) == 1

    def test_withId_order(self):
        """有id, 正常"""
        obj_dict_stu = {
            "id": 1,
            "student_name": "张麻子",
            "student_age": "20",
            "class_id": 1,
        }
        self.base_func(obj_dict_stu)

    def test_withOutId_order(self):
        """没有id, 正常"""
        obj_dict_stu = {
            "student_name": "张麻子",
            "student_age": "20",
            "class_id": 1,
        }
        self.base_func(obj_dict_stu)

    def test_withId_outOfOrder(self):
        """有id, 乱序dict"""
        obj_dict_stu = {
            "id": 1,
            "class_id": 1,
            "student_age": "20",
            "student_name": "张麻子",
        }
        self.base_func(obj_dict_stu)

    def test_withOutId_outOfOrder(self):
        """没有id, 乱序dict"""
        obj_dict_stu = {
            "class_id": 1,
            "student_age": "20",
            "student_name": "张麻子",
        }
        self.base_func(obj_dict_stu)

    def test_primaryKeyNotId(self):
        import datetime

        teacher_obj = {
            # "teacher_id": 1,
            "teacher_name": "肖刚玉",
            "teacher_age": "46",
            "last_month_average": 125.12,
            # "joined_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "joined_time": datetime.datetime(2020, 3, 9, 15, 8, 2).strftime('%Y-%m-%d %H:%M:%S'),
        }
        assert self.teacherDao.insert_one(teacher_obj, primary_key="teacher_id") == 1

    def tearDown(self) -> None:
        # with self.conn:
        #     with self.conn.cursor() as cursor:
        #         cursor.execute("use test1")
        #         cursor.execute("drop table student")
        #
        #     self.conn.commit()
        self.studentDao.execute_sql("use test1")
        self.studentDao.execute_sql("drop table student")
        self.studentDao.execute_sql("drop table teacher")
