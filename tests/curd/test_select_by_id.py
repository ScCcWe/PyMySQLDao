# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_by_id.py
# author: ScCcWe
# time: 2022/3/4 4:19 下午
import pytest

from pymysqldao import err_
from tests import class_obj_id_1
from tests.dao.table_dao import ClassDao

classDao = ClassDao()


def test_validation():
    for none_value in [0j, None, [], (), {}]:
        pytest.raises(err_.ParamTypeError, classDao.select_by_id, none_value)

    for a in [0, -0, ""]:
        pytest.raises(err_.ParamBoolFalseError, classDao.select_by_id, a)


def test_param_type():
    pytest.raises(err_.ParamTypeError, classDao.select_by_id, 1, 1)


def test_query():
    for item in [1, "1"]:
        assert classDao.select_by_id(item) == class_obj_id_1

    # TODO: 主键值不为'id'
