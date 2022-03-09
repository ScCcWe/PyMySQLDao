# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_by_field.py
# author: ScCcWe
# time: 2022/3/6 9:36 下午
import pytest

from tests import none_list, student_obj_list_id_123
from tests.dao.table_dao import StudentDao

studentDao = StudentDao()


def test_select_by_field_val_value():
    """
    id_list: type: List<int> / List<str>
    """
    for none_value in none_list:
        pytest.raises(ValueError, studentDao.select_by_field, none_value, "student_name")


def test_select_by_field_query():
    """
    id_list: type: List<int> / List<str>
    """
    assert studentDao.select_by_field("张三", "student_name")[0] == student_obj_list_id_123[0]
