# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: base_helper.py
# author: ScCcWe
# time: 2022/4/8 2:55 下午
from pymysql import Connection

from .execute_helper import ExecuteHelper
from pymysqldao.err_ import ParamBoolFalseError
from pymysqldao import msg_


class BaseHelper(ExecuteHelper):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            use_own_log_config=False,
            *args,
            **kwargs,
    ):
        super().__init__(connection, use_own_log_config, *args, **kwargs)

        if not table_name:
            raise ParamBoolFalseError(msg_.param_cant_none("table_name"))
        else:
            self._table_name = table_name
