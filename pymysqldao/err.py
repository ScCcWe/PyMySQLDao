# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: err.py
# author: ScCcWe
# time: 2022/3/6 10:54 上午
class ParamNoneError(ValueError):
    """参数值为None"""


class ParamTypeError(TypeError):
    """参数值类型错误"""
