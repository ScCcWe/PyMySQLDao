# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: baseDao.py
# author: ScCcWe
# time: 2022/3/4 12:35 下午
from typing import List, Dict, Union

from pymysql.connections import Connection
from pydantic import BaseModel, validator

from pymysqldao import msg_
from pymysqldao.err_ import (
    ParamTypeError,
    ParamBoolFalseError,
    PrimaryKeyError,
)
from pymysqldao.dao import base_


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


class VSelectList(BaseModel):
    #         :param limit_size: 查询的limit值；可以为空，默认值是20；
    limit_size: int = 20


class BaseDao(base_.DatabaseDao):
    def __init__(self, connection: Connection, table_name: str):
        super(BaseDao, self).__init__(connection)

        if not table_name:
            raise ParamBoolFalseError(msg_.param_cant_none("table_name"))
        else:
            # __表示受保护的属性，不希望别人在外部修改
            self.__table_name = table_name

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
            base_.LOGGER.error(msg)
            raise PrimaryKeyError(msg)

    def select_by_id(self, id_value: Union[str, int], primary_key: str = 'id') -> Dict:
        params_input = {
            "id_value": id_value,
            "primary_key": primary_key,
        }
        data = VSelectById(**params_input)
        return self.validation_select_by_id(data)

    # @all_param_type_check
    def select_by_id_list(self, id_list: List[Union[str, int]], limit_size: int = 20, primary_key: str = "id"):
        """select * from table where primary_key in id_list"""
        params_input = {
            "id_list": id_list,
            "limit_size": limit_size,
            "primary_key": primary_key,
        }
        return self.validation_select_by_id_list(VSelectByIdList(**params_input))

    def validation_select_by_id_list(self, params: VSelectByIdList):
        """
        select * from table where primary_key in id_list
        :return: List[Dict] / None
        """
        id_list, limit_size, primary_key = params.id_list, params.limit_size, params.primary_key

        sql = f"select * from {self.__table_name} where {primary_key} in %s"
        try:
            with self._connection.cursor() as cursor:
                execute_result = cursor.execute(sql, ([str(_) for _ in id_list],))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {execute_result} rows affected")

                if limit_size:
                    result = cursor.fetchmany(limit_size)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None

    def validation_select_by_field(self, params: VSelectByField) -> List[Dict[str, object]]:
        """

        select * from table_name where `field_key` = field_value

        :return: List<Dict> / Dict （查询出的结果为单个，会返回Dict
        """
        field_key = params.field_key
        field_value = params.field_value
        limit_size = params.limit_size

        # assert not field_value

        # if not field_value:
        #     raise ParamBoolFalseError(msg_.param_cant_none("field_value"))

        sql = f"select * from {self.__table_name} where {field_key} = %s"
        try:
            with self._connection.cursor() as cursor:
                execute_result = cursor.execute(sql, (str(field_value),))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {execute_result} rows affected")

                if limit_size:
                    result = cursor.fetchmany(limit_size)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None

    def select_by_field(self, key: str, value: str, limit: int = 20):
        """

        :param key: 字段名
        :param value: 字段值
        :param limit:
        :return:
        """
        input_params = {
            "field_key": key,
            "field_value": value,
            "limit_size": limit,
        }
        data = VSelectByField(**input_params)
        return self.validation_select_by_field(data)

    def select_list(self, limit: int = 20):
        params_input = {
            "limit_size": limit
        }
        return self.validation_select_list(VSelectList(**params_input))

    def validation_select_list(self, params: VSelectList):
        """

        select * from table_name limit limit_size

        :return: List[Dict]
        """
        limit_size = params.limit_size

        sql = f"select * from {self.__table_name}"
        try:
            with self._connection.cursor() as cursor:
                execute = cursor.execute(sql)

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {execute} rows affected")

                if limit_size:
                    result = cursor.fetchmany(limit_size)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result is not None else None

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
            sql = f"INSERT INTO {self.__table_name} ({', '.join(field_list)}) " \
                  f"VALUES ({', '.join(placeholder_list)})"
            return sql, value_list

        if not isinstance(obj_dict, dict):
            raise TypeError(msg_.param_only_accept_dict("obj_dict"))

        try:
            with self._connection.cursor() as cursor:
                sql, value_list = generate_sql(obj_dict)
                row_num = cursor.execute(sql, tuple(value_list))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {row_num} rows affected")

            if not self._connection.get_autocommit():
                self._connection.commit()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return row_num if row_num else None

    def insert_many(self, obj_dict_list: List[Dict[str, object]]):
        if not obj_dict_list:
            raise ParamBoolFalseError(msg_.param_cant_none("obj_dict_list"))
        if not isinstance(obj_dict_list, list):
            raise ParamTypeError(msg_.param_only_accept_list("obj_dict_list"))

        for obj in obj_dict_list:
            self.insert_one(obj)

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
            return f"update {self.__table_name} set {', '.join(field_value_list)} where {primary_key} = %s"

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

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {row_num} rows affected")

            if not self._connection.get_autocommit():
                self._connection.commit()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return row_num if row_num else None

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
                sql = f"delete from {self.__table_name} where {primary_key} = %s"
                rows = cursor.execute(sql, (id_value,))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {rows} rows affected")

            if not self._connection.get_autocommit():
                self._connection.commit()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return rows if rows else None

    def delete_by_id_list(self, id_list: List):
        if not id_list:
            raise ValueError(msg_.param_cant_none("id_list"))
        if not isinstance(id_list, list):
            raise TypeError(msg_.param_only_accept_list("id_list"))

        [self.delete_by_id(id) for id in id_list]
