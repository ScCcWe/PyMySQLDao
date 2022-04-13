# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: log_controller.py
# author: ScCcWe
# time: 2022/4/12 10:21 上午
from pymysql import Connection
from pymysql.connections import Connection

from .err_ import ParamNoneError, ParamTypeError
from .log_controller import LOGGER


class DataBaseConnectionMixin:
    def __init__(
            self,
            connection: Connection,
            *args,
            **kwargs,
    ):
        if not connection:
            raise ParamNoneError("param `connection` can't accept none value")
        elif type(connection) != Connection:
            raise ParamTypeError("param connection can only accept pymysql.connections.Connection type")
        else:
            self.connection = connection

        # 超类继续初始化
        super().__init__(*args, **kwargs)


class TableMixin:
    def __init__(
            self,
            table_name: str,
            *args,
            **kwargs,
    ):
        if not table_name:
            raise ParamNoneError("param `table_name` can't accept none value")
        else:
            self.table_name = table_name

        super().__init__(*args, **kwargs)


class CRUDBaseMixin(DataBaseConnectionMixin, TableMixin):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            *args,
            **kwargs,
    ):
        super().__init__(
            connection,
            table_name,
            *args,
            **kwargs
        )

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
            with self.connection.cursor() as cursor:
                rows = cursor.execute(sql)

                LOGGER.info(f"Execute SQL: {sql}")
                LOGGER.info(f"Query OK, {rows} rows affected")

                result = cursor.fetchall()

                if self.connection.get_autocommit() or commit:
                    self.connection.commit()

                # 需要commit的操作，会自动commit，并将结果改成受影响的行数
                ops_list = ["insert", "update", "delete"]
                for ops in ops_list:
                    if ops in sql:
                        self.connection.commit()
                        result = rows
                        break

        except Exception as e:
            LOGGER.exception(f"Execute SQL: {sql}")
            LOGGER.exception(f"Query Exception: {e}")
        finally:
            return result if result else None


if __name__ == '__main__':
    import pymysql

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='python_example',
        cursorclass=pymysql.cursors.DictCursor
    )
    ins = CRUDBaseMixin(connection=conn, table_name="class", size=500)
    print(ins)
