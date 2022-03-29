# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_by_field.py
# author: ScCcWe
# time: 2022/3/6 9:36 下午
import pytest

from pydantic import ValidationError

from pymysqldao import err_

from tests import none_list, student_obj_list_id_123
from tests.dao.table_dao import StudentDao

studentDao = StudentDao()


def test_select_by_field_val_value():
    """
    id_list: type: List<int> / List<str>
    """
    for none_value in none_list:
        pytest.raises(ValueError, studentDao.select_by_field, "student_name", none_value)


def test_select_by_field_query():
    """
    id_list: type: List<int> / List<str>
    """
    assert studentDao.select_by_field("student_name", "张三")[0] == student_obj_list_id_123[0]


def test_select_by_field_query_many():
    """
    id_list: type: List<int> / List<str>
    """
    assert studentDao.select_by_field("student_name", "张三", limit=5)[0] == student_obj_list_id_123[0]
