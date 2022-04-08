# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: create_helper.py
# author: ScCcWe
# time: 2022/4/8 3:10 下午
from typing import List, Dict, Union

from pymysql.connections import Connection
import pymysqldao.log_.base_
from pymysqldao.err_ import (
    ParamTypeError,
    ParamBoolFalseError,
    PrimaryKeyError,
)
import pymysqldao.log_.base_
from pymysqldao import msg_
from pymysqldao.helpers.base_helper import BaseHelper


class UpdateHelper(BaseHelper):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            use_own_log_config=False,
            *args,
            **kwargs
    ):
        super().__init__(connection, table_name, use_own_log_config, *args, **kwargs)

    def update_by_id(self, obj_dict: Dict, primary_key="id"):
        """

        update table_name set ? = ?, ? = ?... where primary_key = ?

        :param obj_dict:
        :param primary_key:
        :return:
        """

        def generate_sql(obj_dict):
            field_value_list = []
            for field, value in obj_dict.items():
                if field != primary_key:
                    if type(value) == str:
                        value = "'" + value + "'"
                    field_value_list.append(field + '=' + str(value))
            return f"update {self._table_name} set {', '.join(field_value_list)} where {primary_key} = %s"

        if not obj_dict:
            raise ParamBoolFalseError(msg_.param_cant_none("obj_dict"))
        if not isinstance(obj_dict, dict):
            raise ParamTypeError(msg_.param_only_accept_dict("obj_dict"))

        if primary_key == "id" and primary_key not in obj_dict:  # not obj_dict.has_key("id")
            raise PrimaryKeyError("如果主键列名不是`id`，请显式的指出主键列名")

        try:
            with self._connection.cursor() as cursor:
                sql = generate_sql(obj_dict)
                row_num = cursor.execute(sql, (obj_dict.get(primary_key),))

                pymysqldao.log_.base_.LOGGER.info(f"Execute SQL: {sql}")
                pymysqldao.log_.base_.LOGGER.info(f"Query OK, {row_num} rows affected")

            if not self._connection.get_autocommit():
                self._connection.commit()
        except Exception as e:
            pymysqldao.log_.base_.LOGGER.exception(f"Execute SQL: {sql}")
            pymysqldao.log_.base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return row_num if row_num else None
