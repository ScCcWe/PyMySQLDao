# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: reterive_helper.py
# author: ScCcWe
# time: 2022/4/8 2:53 下午
from typing import List, Dict, Union

from pymysql.connections import Connection
from pydantic import BaseModel, validator

import pymysqldao.log_.base_
from pymysqldao import msg_
from pymysqldao.err_ import (
    ParamBoolFalseError,
    PrimaryKeyError,
)
from pymysqldao.helpers.base_helper import BaseHelper


class VSelectById(BaseModel):
    # 主键值
    id_value: str = 1

    # 主键名，默认为"id"
    primary_key: str = 'id'

    @validator("id_value")
    def id_value_cant_none(cls, v):
        if not v:
            raise ValueError(msg_.param_cant_none("id_value"))
        return str(v)


class VSelectByField(BaseModel):
    # 字段名
    field_key: str

    # 字段值
    field_value: str

    # 限制显示的结果数量
    # 默认为20
    limit_size: int = 20

    @validator("field_key")
    def field_key_cant_none(cls, v):
        if not v:
            raise ValueError(msg_.param_cant_none("field_key"))
        return v

    @validator("field_value")
    def field_value_cant_none(cls, v):
        if not v:
            raise ValueError(msg_.param_cant_none("field_value"))
        return v


class VSelectByIdList(BaseModel):
    # 包含需要查询的所有id值的list, eg: [1, 2, 3], ["1", "2", "3"], ["1", 2, "3"];
    id_list: List[Union[str, int]]

    # 限制显示的结果数量
    limit_size: int = 20

    # 主键名默认是"id"；如果主键名不是"id"，应该显式的给出；
    primary_key: str = "id"

    @validator("id_list")
    def id_list_pre_validation(cls, v):
        if not v:
            raise ValueError(msg_.param_cant_none("id_list"))
        # if not isinstance(v, list):
        #     raise TypeError(msg_.param_only_accept_list("id_list"))
        # for item in v:
        #     if type(item) == str or type(item) == int:
        #         ...
        #     else:
        #         raise ParamTypeError(msg_.param_should_listUnionStrInt("id_list"))
        return v


# class VSelectList(BaseModel):
#     # size: 查询的limit值；
#     size: int


class RetreiveHelper(BaseHelper):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            use_own_log_config=False,
            size: int = None,
            *args,
            **kwargs,
    ):
        super().__init__(connection, table_name, use_own_log_config, *args, **kwargs)

        self.size = size
        print("self.size: ", self.size)

    def validation_select_by_id(self, params: VSelectById) -> Dict:
        """

        select * from table_name where `id` = id_value

        :return: Dict
        """
        id_value = params.id_value
        primary_key = params.primary_key
        query_list = self.select_by_field(primary_key, id_value)

        if len(query_list) == 1:
            return query_list[0]
        else:
            msg = f"check out if use the right primary key? current primary key is: {primary_key}"
            pymysqldao.log_.base_.LOGGER.error(msg)
            raise PrimaryKeyError(msg)

    def select_by_id(self, id_value: Union[str, int], primary_key: str = 'id') -> Dict:
        params_input = {
            "id_value": id_value,
            "primary_key": primary_key,
        }
        data = VSelectById(**params_input)
        return self.validation_select_by_id(data)

    def select_by_id_list(self, id_list: List[Union[str, int]], size: int = 20, primary_key: str = "id"):
        """select * from table where primary_key in id_list"""
        params_input = {
            "id_list": id_list,
            "limit_size": size,
            "primary_key": primary_key,
        }
        return self.validation_select_by_id_list(VSelectByIdList(**params_input))

    def validation_select_by_id_list(self, params: VSelectByIdList):
        """
        select * from table where primary_key in id_list
        :return: List[Dict] / None
        """
        id_list, limit_size, primary_key = params.id_list, params.limit_size, params.primary_key

        sql = f"select * from {self._table_name} where {primary_key} in %s"
        try:
            with self._connection.cursor() as cursor:
                execute_result = cursor.execute(sql, ([str(_) for _ in id_list],))

                pymysqldao.log_.base_.LOGGER.info(f"Execute SQL: {sql}")
                pymysqldao.log_.base_.LOGGER.info(f"Query OK, {execute_result} rows affected")

                if limit_size:
                    result = cursor.fetchmany(limit_size)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            pymysqldao.log_.base_.LOGGER.exception(f"Execute SQL: {sql}")
            pymysqldao.log_.base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None

    def validation_select_by_field(self, params: VSelectByField) -> List[Dict[str, object]]:
        """
        :return: List<Dict> / Dict （查询出的结果为单个，会返回Dict
        """
        field_key = params.field_key
        field_value = params.field_value
        limit_size = params.limit_size

        sql = f"select * from {self._table_name} where {field_key} = %s"
        try:
            with self._connection.cursor() as cursor:
                execute_result = cursor.execute(sql, (str(field_value),))

                pymysqldao.log_.base_.LOGGER.info(f"Execute SQL: {sql}")
                pymysqldao.log_.base_.LOGGER.info(f"Query OK, {execute_result} rows affected")

                if limit_size:
                    result = cursor.fetchmany(limit_size)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            pymysqldao.log_.base_.LOGGER.exception(f"Execute SQL: {sql}")
            pymysqldao.log_.base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None

    def select_by_field(self, key: str, value: str, size: int = 20):
        """
        select * from `table` where `key` = value limit `size`
        :param key: 字段名
        :param value: 字段值
        :param size:
        :return:
        """
        input_params = {
            "field_key": key,
            "field_value": value,
            "limit_size": size,
        }
        data = VSelectByField(**input_params)
        return self.validation_select_by_field(data)

    def select_list(self, size: int = None):
        """
        select * from table_name limit size
        :param size:
        :return: List[Dict]
        """
        if not size:
            sql = f"select * from {self._table_name}"
        else:
            sql = f"select * from {self._table_name} limit {size}"

        try:
            with self._connection.cursor() as cursor:
                execute = cursor.execute(sql)
                pymysqldao.log_.base_.LOGGER.info(f"Execute SQL: {sql}")
                pymysqldao.log_.base_.LOGGER.info(f"Query OK, {execute} rows affected")

                result = cursor.fetchall()
        except Exception as e:
            pymysqldao.log_.base_.LOGGER.exception(f"Execute SQL: {sql}")
            pymysqldao.log_.base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result is not None else None
