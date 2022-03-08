# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: databaseDao.py
# author: ScCcWe
# time: 2022/3/8 9:48 上午
from pymysql.connections import Connection
from pymysqldao.log.logger import logger
from pymysqldao.constant.COMMON import DEBUG


class DatabaseDao:
    def __init__(self, connection: Connection):
        if not connection:
            raise ValueError
        else:
            self.connection = connection

        self.debug = True

    def execute_sql(self, sql: str, commit=False):
        """
        如果是正常的查询语句，返回的都是：List<Dict>

        如果是["insert", "update", "delete"]，则返回受影响的行数

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
                if DEBUG and self.debug:
                    logger.info(f"Execute SQL: {sql}")
                    logger.info(f"Query OK, {rows} rows affected")

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
            logger.error(f"Execute SQL: {sql}")
            logger.error(f"Query Exception: {e}")
        finally:
            return result if result else None
