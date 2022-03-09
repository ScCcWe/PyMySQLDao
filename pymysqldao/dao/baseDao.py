# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: baseDao.py
# author: ScCcWe
# time: 2022/3/4 12:35 下午
from typing import List, Dict

from pymysql.connections import Connection

from pymysqldao._err import ParamTypeError, ParamBooleanFalseError
from pymysqldao.dao import base_


class BaseDao(base_.DatabaseDao):
    def __init__(self, connection: Connection, table_name: str):
        super(BaseDao, self).__init__(connection)

        if not table_name:
            raise ValueError
        else:
            self.table_name = table_name

        # 全局limit值
        self.limit = 500

        # 默认如果不配置此属性的话，都是有DEBUG的;
        # 可以单独配置关闭；防止多个DaoClass，有的想debug，有的不想;
        self.debug = True

    def select_by_id(self, id_value, primary_key="id"):
        return self.select_by_field(id_value, field_key=primary_key, limit_size=1)

    def select_by_id_list(self, id_list, primary_key="id", limit_tag=False):
        """

        query data by id_list

        :param id_list: 包含需要查询的所有id值的list
                        eg: [1, 2, 3], ["1", "2", "3"]
                        # type: List<int/str>
        :param primary_key: 主键名默认是"id"；如果主键名不是"id"，应该显式的给出；
        :param limit_tag: control show all or show limit; if use, the default limit num is self.limit;
        :return: List[Dict] / None
        """
        if not id_list:
            raise ParamBooleanFalseError("param `id_list` can't be null-type value")
        if not isinstance(id_list, list):
            raise ParamTypeError("param `id_list` can only accept List type")
        if type(primary_key) != str:
            raise ParamTypeError("param `primary_key` can only accept str type")
        for item in id_list:
            if not item:
                raise ParamTypeError("param `id_list` can't be null-type value")
            if type(item) == str or type(item) == int:
                ...
            else:
                raise ParamTypeError("the type of param `id_list` can be `List<int>`, `List<str>` or `List<str/int>`")

        sql = f"select * from {self.table_name} where {primary_key} in %s"
        try:
            with self.connection.cursor() as cursor:
                execute_result = cursor.execute(sql, ([str(_) for _ in id_list],))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {execute_result} rows affected")

                if limit_tag:
                    result = cursor.fetchmany(self.limit)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None

    def select_by_field(self, field_value, field_key: str, limit_size=20):
        """

        根据指定的字段名和字段值查询数据

        :param field_value: 字段值
        :param field_key: 字段名
        :param limit_size: 如果方法上设置了limit_size，则优先使用limit_size，而不是self.size
        :return: List<Dict> / Dict （除了id查询会返回Dict之外，即便是查询出的结果为单个，也会返回List<Dict>
        """
        if not field_value:
            raise ParamBooleanFalseError("param `field_value` can't accept null-type value")
        if type(field_value) != int and type(field_value) != str:
            raise ParamTypeError("param `field_value` can only accept int or str type")
        if type(field_key) != str:
            raise ParamTypeError("param `field_key` can only accept str type")

        sql = f"select * from {self.table_name} where {field_key} = %s"
        try:
            with self.connection.cursor() as cursor:
                execute_result = cursor.execute(sql, (str(field_value),))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {execute_result} rows affected")

                if limit_size:  # by_id / by_unique_field
                    if limit_size == 1 and "id" in field_key:
                        result = cursor.fetchone()
                    else:
                        result = cursor.fetchmany(limit_size)
                elif self.limit:  # by_field
                    result = cursor.fetchmany(self.limit)
                else:
                    result = cursor.fetchall()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None

    def select_list(self, limit_size=20):
        """

        根据limit值，查询出一个list

        :param limit_size: 查询的limit值；可以为空，默认值是20；
        :return: List[Dict]
        """
        if not limit_size:
            raise ValueError("param `limit_size` can't be none-type value")
        if type(limit_size) != int:
            raise TypeError("param `limit_size` can only accept int type")

        sql = f"select * from {self.table_name}"
        try:
            with self.connection.cursor() as cursor:
                execute = cursor.execute(sql)

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {execute} rows affected")

                result = cursor.fetchmany(limit_size if self.limit > limit_size else self.limit)
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result is not None else None

    def insert_one(self, obj_dict: Dict, primary_key="id"):
        """
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
            sql = f"INSERT INTO {self.table_name} ({', '.join(field_list)}) " \
                  f"VALUES ({', '.join(placeholder_list)})"
            return sql, value_list

        if not isinstance(obj_dict, dict):
            raise TypeError("param `obj_dict` can only accept dict type")

        try:
            with self.connection.cursor() as cursor:
                sql, value_list = generate_sql(obj_dict)
                row_num = cursor.execute(sql, tuple(value_list))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {row_num} rows affected")

            if not self.connection.get_autocommit():
                self.connection.commit()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return row_num if row_num else None

    def insert_many(self, obj_dict_list: List[Dict[str, object]]):
        if not obj_dict_list:
            raise ParamBooleanFalseError("param `obj_dict_list` can't be none-type value")
        if not isinstance(obj_dict_list, list):
            raise ParamTypeError("param `obj_dict_list` can only accept list type")

        for obj in obj_dict_list:
            self.insert_one(obj)

    def update_by_id(self, obj_dict: Dict, primary_key="id"):
        def generate_sql(obj_dict):
            field_value_list = []
            for field, value in obj_dict.items():
                if field != primary_key:
                    if type(value) == str:
                        value = "'" + value + "'"
                    field_value_list.append(field + '=' + str(value))
            return f"update {self.table_name} set {', '.join(field_value_list)} where {primary_key} = %s"

        if not obj_dict:
            raise ValueError("param `obj_dict` can't accept null-type value")
        if not isinstance(obj_dict, dict):
            raise TypeError("参数类型错误")
        if primary_key not in obj_dict:  # not obj_dict.has_key("id")
            raise KeyError("如果主键列名不是'id'，请显式的指出id列名")
        
        try:
            with self.connection.cursor() as cursor:
                sql = generate_sql(obj_dict)
                row_num = cursor.execute(sql, (obj_dict.get(primary_key),))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {row_num} rows affected")

            if not self.connection.get_autocommit():
                self.connection.commit()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return row_num if row_num else None

    def delete_by_id(self, id, primary_key="id"):
        if not id:
            raise ValueError("param `id` can't accept null-type value")
        if type(id) != str and type(id) != int:
            raise TypeError("param `id` can accept str or int type")

        try:
            with self.connection.cursor() as cursor:
                sql = f"delete from {self.table_name} where {primary_key} = %s"
                rows = cursor.execute(sql, (id,))

                base_.LOGGER.info(f"Execute SQL: {sql}")
                base_.LOGGER.info(f"Query OK, {rows} rows affected")

            if not self.connection.get_autocommit():
                self.connection.commit()
        except Exception as e:
            base_.LOGGER.exception(f"Execute SQL: {sql}")
            base_.LOGGER.exception(f"Query Exception: {e}")
        finally:
            return rows if rows else None

    def delete_by_id_list(self, id_list: List):
        if not id_list:
            raise ValueError("param `id_list` can't accept null-type value")
        if not isinstance(id_list, list):
            raise TypeError("param `id_list` can only be list type")

        for id in id_list:
            self.delete_by_id(id)
