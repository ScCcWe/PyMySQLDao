# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: decorator_.py
# author: ScCcWe
# time: 2022/3/14 2:59 下午
import typing
from typing import Union

from pymysqldao import err_


def all_param_type_check(func):
    def wrapper(self, *args, **kwargs):
        # 执行前添加操作

        origin_kwargs = kwargs
        kwargs = {}
        # 只判断传入的参数，默认值和return值不判断
        for input_param_key in list(func.__annotations__.keys()):
            if input_param_key in origin_kwargs:
                kwargs[input_param_key] = origin_kwargs[input_param_key]

        print("*args: ", args)
        print("**kwargs: ", kwargs)

        print(func.__annotations__)
        # anno_list = list(func.__annotations__.values())[:-1]
        anno_list = list(func.__annotations__.values())
        # print(anno_list)
        # print(isinstance(anno_list[0], int))

        # eg: func(1, 2)
        for arg_index, arg_item in enumerate(args):

            # 预期的参数类型
            expect_param_type = anno_list[arg_index]
            # 如果是union，则需要加上__args__，否则无法比较
            if "union" in str(expect_param_type).lower():
                expect_param_type = expect_param_type.__args__

            if not isinstance(arg_item, expect_param_type):
                raise err_.ParamTypeError(f"the type of {arg_item} should be {anno_list[arg_index]} type")

        # eg: func(x=1, y=2)
        for key, value in kwargs.items():

            expect_param_type = func.__annotations__[key]
            # 如果是union，则需要加上__args__，否则无法比较
            if "union" in str(expect_param_type).lower():
                expect_param_type = expect_param_type.__args__

            if not isinstance(value, expect_param_type):
                raise err_.ParamTypeError(f"param {key} can only accept {func.__annotations__[key]} type")

        # 执行原来的方法
        return func(self, *args, **kwargs)

    return wrapper


class Solution:
    a = 1

    @all_param_type_check
    def nihao(self, x: int, y: Union[int, str], z=1):
        return self.a + x + y + z

    def hello(self):
        return self.nihao(1, 1, z=20)


if __name__ == '__main__':
    # print(nihao.__annotations__)
    # a = list(nihao.__annotations__.values())
    # print(a)
    # print(a[0])
    # print(str(a[0]))
    # print(a[0] == "<class 'int'>")
    # print(Solution().nihao(1, y=1))
    Solution().hello()


    # nihao(x=2, y="nihao")
    # print(nihao(x=2, y="nihaho"))
    # nihao(1, "nihao")

    # print(typing.Union[int, str].__args__)
    # print(isinstance(1, typing.Union[int, str].__args__))
    # print(isinstance("1", typing.Union[int, str].__args__))
    # print(isinstance([], typing.Union[int, str].__args__))

    print(typing.List[Union[str, int]].__args__)
