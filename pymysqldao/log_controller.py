# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: execute_.py
# author: ScCcWe
# time: 2022/3/27 11:50 上午
import sys
import logging

from .constant_ import MODULE_NAME

LOGGER = logging.getLogger(MODULE_NAME)


class LoggerController(object):
    """
    在使用pymysqldao时，还可以自行设置LOGGER的输出方式和格式；

    详情请看README文件
    """
    def simple_stderr_(self):
        """设置日志等级为DEBUG，只是简单的打印在控制台"""
        LOGGER.setLevel(logging.DEBUG)
        LOGGER.addHandler(logging.StreamHandler(sys.stderr))

    def stderr_(self):
        """设置日志等级为DEBUG，并将指定格式的内容打印在控制台"""
        LOGGER.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setFormatter(logging.Formatter('%(asctime)+s %(name)+s %(levelname)+s %(message)+s'))
        LOGGER.addHandler(stream_handler)
