# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: base_.py
# author: ScCcWe
# time: 2022/3/27 11:50 上午
import sys
import logging

from pymysqldao import LOGGER


class LoggerController(object):

    def __init__(self):
        ...

    def stderr_(self):
        LOGGER.setLevel(logging.DEBUG)
        LOGGER.addHandler(logging.StreamHandler(sys.stderr))
