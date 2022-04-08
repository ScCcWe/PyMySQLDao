# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: create_helper.py
# author: ScCcWe
# time: 2022/4/8 3:10 下午
from typing import List, Dict, Union

from pymysql.connections import Connection

import pymysqldao.log_.base_
from pymysqldao import msg_
from pymysqldao.err_ import (
    ParamTypeError,
    ParamBoolFalseError,
    PrimaryKeyError,
)
from pymysqldao.helpers.base_helper import BaseHelper


class CreateHelper(BaseHelper):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            use_own_log_config=False,
            *args,
            **kwargs,
    ):
        super().__init__(connection, table_name, use_own_log_config, *args, **kwargs)

    def insert_one(self, obj_dict: Dict, primary_key: str = "id"):
        """

        insert into table_name () values ()

        :param obj_dict: 需要插入的数据（以dict格式
        :param primary_key: 主键名，默认为"id"
        :return: affect_rows_num（1）
        """

        def generate_sql(obj: Dict):
            field_list = []
            value_list = []
            placeholder_list = []
            for key, value in obj.items():
                if key != primary_key:
                    field_list.append(key)
                    value_list.append(str(value))
                else:
                    # id值必须要第一位（如果有的情况下
                    field_list.insert(0, key)
                    value_list.insert(0, str(value))
                placeholder_list.append("%s")
            sql = f"INSERT INTO {self._table_name} ({', '.join(field_list)}) " \
                  f"VALUES ({', '.join(placeholder_list)})"
            return sql, value_list

        if not isinstance(obj_dict, dict):
            raise TypeError(msg_.param_only_accept_dict("obj_dict"))

        try:
            with self._connection.cursor() as cursor:
                sql, value_list = generate_sql(obj_dict)
                row_num = cursor.execute(sql, tuple(value_list))

                pymysqldao.log_.base_.LOGGER.info(f"Execute SQL: {sql}")
                pymysqldao.log_.base_.LOGGER.info(f"Query OK, {row_num} rows affected")

            if not self._connection.get_autocommit():
                self._connection.commit()
        except Exception as e:
            pymysqldao.log_.base_.LOGGER.exception(f"Execute SQL: {sql}")
            pymysqldao.log_.base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return row_num if row_num else None

    def insert_many(self, obj_dict_list: List[Dict[str, object]]):
        if not obj_dict_list:
            raise ParamBoolFalseError(msg_.param_cant_none("obj_dict_list"))
        if not isinstance(obj_dict_list, list):
            raise ParamTypeError(msg_.param_only_accept_list("obj_dict_list"))

        for obj in obj_dict_list:
            self.insert_one(obj)
