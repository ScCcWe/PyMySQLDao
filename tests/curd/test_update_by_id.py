# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: test_insert.py
# author: ScCcWe
# time: 2022/3/4 4:38 下午
from tests.dao.classDao import ClassDao

class_dao = ClassDao()


def test_update_by_id():
    # 查询出来一个id为1的对象，并修改它的class_name
    obj_id_1 = class_dao.select_by_id(1)
    origin_class_name = obj_id_1["class_name"]
    new_class_name = obj_id_1["class_name"] + "修改"
    obj_id_1["class_name"] = new_class_name

    # 更新
    class_dao.update_by_id(obj_id_1)

    # 对比
    class_obj = class_dao.select_by_id(1)
    assert class_obj["class_name"] == new_class_name

    # 对比完了之后，改回来
    obj_id_1["class_name"] = origin_class_name
    class_dao.update_by_id(obj_id_1)
