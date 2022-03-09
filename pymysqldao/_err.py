# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: _err.py
# author: ScCcWe
# time: 2022/3/6 10:54 上午
class ParamBooleanFalseError(ValueError):
    """参数值为空错误，这个空包括0, 0.0, -0, 0j, '', None, [], (), {}"""


class ParamTypeError(TypeError):
    """参数值类型错误"""
