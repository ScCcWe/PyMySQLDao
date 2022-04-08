# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: execute_helper.py
# author: ScCcWe
# time: 2022/3/8 9:48 上午
from pymysql.connections import Connection

from pymysqldao.log_.base_ import LoggerController, LOGGER
from pymysqldao.err_ import ParamBoolFalseError, ParamTypeError
from pymysqldao.msg_ import param_cant_none


class ExecuteHelper:
    def __init__(
            self,
            connection: Connection,
            use_own_log_config=False,
            *args,
            **kwargs,
    ):
        if not connection:
            raise ParamBoolFalseError(param_cant_none("connection"))
        elif type(connection) != Connection:
            raise ParamTypeError("param connection can only accept pymysql.connections.Connection type")
        else:
            # _表示私有属性；
            # 即：供内部使用，如果外部要使用，最好在实例化对象时指定；
            self._connection = connection

            if not use_own_log_config:
                LoggerController().stderr_()

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
