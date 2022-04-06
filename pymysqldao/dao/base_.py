# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: base_.py
# author: ScCcWe
# time: 2022/3/8 9:48 上午
import logging

from pymysql.connections import Connection
from pymysqldao.constant_ import MODULE_NAME
from pymysqldao.err_ import ParamBoolFalseError, ParamTypeError
from pymysqldao.msg_ import param_cant_none

"""
在使用pymysqldao时，可以自行设置LOGGER的输出方式和格式；

    如下设置例：展示DEBUG及以上信息，并打印在控制台上
    >>> import sys
    >>> import logging
    >>> 
    >>> from pymysqldao import LOGGER
    >>> 
    >>> LOGGER.setLevel(logging.DEBUG)
    >>> LOGGER.addHandler(logging.StreamHandler(sys.stderr))
    
"""
LOGGER = logging.getLogger(MODULE_NAME)


class DatabaseDao:
    def __init__(self, connection: Connection):
        if not connection:
            raise ParamBoolFalseError(param_cant_none("connection"))
        elif type(connection) != Connection:
            raise ParamTypeError("param connection can only accept pymysql.connections.Connection type")
        else:
            # _表示私有属性，别人最好不要在外部修改；
            # 即：最好在创建对象时指定
            self._connection = connection

    def execute_sql(self, sql: str, commit: bool = False):
        """
        如果是["insert", "update", "delete"]，则返回受影响的行数

        否则：都返回：List<Dict>

        :param sql: 需要执行的sql语句
        :param commit: 显式的标出是否需要commit
        :return: rows_num(int) / List<Dict>
        """
        if not sql:
            raise ValueError
        if type(sql) != str:
            raise TypeError

        try:
            with self._connection.cursor() as cursor:
                rows = cursor.execute(sql)

                LOGGER.info(f"Execute SQL: {sql}")
                LOGGER.info(f"Query OK, {rows} rows affected")

                result = cursor.fetchall()

                if self._connection.get_autocommit() or commit:
                    self._connection.commit()

                # 需要commit的操作，会自动commit，并将结果改成受影响的行数
                ops_list = ["insert", "update", "delete"]
                for ops in ops_list:
                    if ops in sql:
                        self._connection.commit()
                        result = rows
                        break

        except Exception as e:
            LOGGER.exception(f"Execute SQL: {sql}")
            LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None
