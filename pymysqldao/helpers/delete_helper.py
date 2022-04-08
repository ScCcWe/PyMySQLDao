# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: create_helper.py
# author: ScCcWe
# time: 2022/4/8 3:10 下午
from typing import List, Dict, Union

from pymysql.connections import Connection

import pymysqldao.log_.base_
from pymysqldao import msg_
from pymysqldao.helpers.base_helper import BaseHelper


class DeleteHelper(BaseHelper):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            use_own_log_config=False,
            *args,
            **kwargs
    ):
        super().__init__(connection, table_name, use_own_log_config, *args, **kwargs)

    def delete_by_field(self, field_value, field_key):
        """

        delete from table_name where field_key = field_value

        （此方法会实际删除数据，一般不使用；推荐使用逻辑删除；

        :param field_value: 字段值
        :param field_key: 字段名
        :return:
        """

        def get_primary_key(obj: Dict):
            """从item中获取primary的名，一般是'id'"""
            first_key = list(obj.keys())[0]

            if str(first_key).lower() == "id":
                return str(first_key)
            if "id" in str(first_key).lower():
                return str(first_key)

        del_list = self.select_by_field(field_value, field_key)

        if not del_list:
            return 0
        else:
            for obj_dict in del_list:
                primary_key = get_primary_key(obj_dict)
                self.delete_by_id(obj_dict[primary_key], primary_key)

    def delete_by_id(self, id_value, primary_key="id"):
        """

        delete from table_name where primary_key = id_value

        （此方法会实际删除数据，一般不使用；推荐使用逻辑删除；

        :param id_value: 主键值
        :param primary_key: 主键名
        :return:
        """
        if not id_value:
            raise ValueError(msg_.param_cant_none("id_value"))
        if type(id_value) != str and type(id_value) != int:
            raise TypeError(msg_.param_should_unionStrInt("id_value"))

        try:
            with self._connection.cursor() as cursor:
                sql = f"delete from {self._table_name} where {primary_key} = %s"
                rows = cursor.execute(sql, (id_value,))

                pymysqldao.log_.base_.LOGGER.info(f"Execute SQL: {sql}")
                pymysqldao.log_.base_.LOGGER.info(f"Query OK, {rows} rows affected")

            if not self._connection.get_autocommit():
                self._connection.commit()
        except Exception as e:
            pymysqldao.log_.base_.LOGGER.exception(f"Execute SQL: {sql}")
            pymysqldao.log_.base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return rows if rows else None

    def delete_by_id_list(self, id_list: List):
        if not id_list:
            raise ValueError(msg_.param_cant_none("id_list"))
        if not isinstance(id_list, list):
            raise TypeError(msg_.param_only_accept_list("id_list"))

        [self.delete_by_id(id) for id in id_list]
