# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: msg_.py
# author: ScCcWe
# time: 2022/3/14 2:02 下午
from functools import partial


def generate_err_msg(param=None, **kwargs):
    # print("**kw: ", args)
    # print("**kw: ", kwargs)
    if 'str_tag' in kwargs:

        if kwargs.get('str_tag') == "notNone":
            return f"param `{param}` can't accept none type value"

        elif kwargs.get('str_tag') == "only":
            return f"param `{param}` can only accept {kwargs.get('type')} type"

        elif kwargs.get('str_tag') == "should":
            return f"param `{param}` should be {kwargs.get('type')} type"


param_only_accept_list = partial(generate_err_msg, str_tag="only", type="List")
param_only_accept_str = partial(generate_err_msg, str_tag="only", type="str")
param_only_accept_int = partial(generate_err_msg, str_tag="only", type="int")
param_only_accept_dict = partial(generate_err_msg, str_tag="only", type="Dict")

param_should_listUnionStrInt = partial(generate_err_msg, str_tag="should", type="List[Union[str, int]]")
param_should_unionStrInt = partial(generate_err_msg, str_tag="should", type="Union[str, int]")

param_cant_none = partial(generate_err_msg, str_tag="notNone")
