# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: crud_helper.py
# author: ScCcWe
# time: 2022/3/4 12:35 下午
from typing import List, Dict, Union

from pymysql.connections import Connection

from pymysqldao.helpers.reterive_helper import RetreiveHelper
from pymysqldao.helpers.create_helper import CreateHelper
from pymysqldao.helpers.delete_helper import DeleteHelper
from pymysqldao.helpers.update_helper import UpdateHelper


class CRUDHelper(CreateHelper, RetreiveHelper, UpdateHelper, DeleteHelper):
    def __init__(
            self,
            connection: Connection,
            table_name: str,
            use_own_log_config=False,
            size=None,
            *args,
            **kwargs,
    ):
        print("size: ", size)
        super().__init__(connection, table_name, use_own_log_config, size, *args, **kwargs)
