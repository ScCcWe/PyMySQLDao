# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: __init__.py.py.py
# author: ScCcWe
# time: 2022/3/4 11:33 上午
from pymysql.connections import Connection

from pymysqldao.crud_.create_ import CreateHelper
from pymysqldao.crud_.delete_ import DeleteHelper
from pymysqldao.crud_.retrieve_ import RetrieveHelper
from pymysqldao.crud_.update_ import UpdateHelper
from pymysqldao.log_controller import LoggerController, LOGGER


class CRUDHelper(CreateHelper, RetrieveHelper, UpdateHelper, DeleteHelper):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            use_own_log_config=False,
            size=None,
            *args,
            **kwargs,
    ):
        """
        提供类似于orm的，crud功能增强
        :param connection:
        :param table_name:
        :param use_own_log_config:
        :param size: 全局的limit_size
        :param args:
        :param kwargs:
        """
        if not use_own_log_config:
            LOGGER.info(f"use default log format")
            log_controller_ins = LoggerController()
            log_controller_ins.stderr_()
        else:
            LOGGER.info(f"use own log format")

        super().__init__(connection, table_name, size, *args, **kwargs)
