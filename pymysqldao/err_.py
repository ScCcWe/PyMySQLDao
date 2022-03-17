# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: err_.py
# author: ScCcWe
# time: 2022/3/6 10:54 上午
class ParamBoolFalseError(ValueError):
    """
    bool(value) -> False

    参数值为空错误；

    这个空包括：0, 0.0, -0, 0j, '', None, [], (), {} 等一切为bool为False的值
    """


class ParamTypeError(TypeError):
    """参数类型错误"""


class PrimaryKeyError(KeyError):
    """主键使用错误"""
