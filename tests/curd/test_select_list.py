# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_list.py
# author: ScCcWe
# time: 2022/3/9 2:01 下午
import pytest

from pymysqldao.err_ import ParamTypeError
from tests import student_obj_list_id_123
from tests.dao.table_dao import StudentDao

studentDao = StudentDao()


def test_select_list_param_validation():
    pytest.raises(ParamTypeError, studentDao.select_list, "3")


def test_select_list_query_length():
    assert len(studentDao.select_list()) == 3
    assert len(studentDao.select_list(0)) == 3
    assert len(studentDao.select_list(1)) == 1
    assert len(studentDao.select_list(2)) == 2
    assert len(studentDao.select_list(3)) == 3


def test_select_list_query_data():
    assert studentDao.select_list() == student_obj_list_id_123
