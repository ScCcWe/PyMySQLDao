# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_select_by_id.py
# author: ScCcWe
# time: 2022/3/4 4:19 下午
import pytest

from tests import none_list, class_obj_id_1
from tests.dao.classDao import ClassDao

classDao = ClassDao()


def test_select_by_id_validation():
    for none_value in none_list:
        pytest.raises(ValueError, classDao.select_by_id, none_value)

    pytest.raises(TypeError, classDao.select_by_id, "1", 1)


def test_select_by_id_query():
    assert classDao.select_by_id(1) is not None
    assert classDao.select_by_id(1) == class_obj_id_1
    assert classDao.select_by_id(1, primary_key="id") is not None
    assert classDao.select_by_id(1, primary_key="id") == class_obj_id_1

    assert classDao.select_by_id("1") is not None
    assert classDao.select_by_id("1") == class_obj_id_1
    assert classDao.select_by_id("1", primary_key="id") is not None
    assert classDao.select_by_id("1", primary_key="id") == class_obj_id_1
