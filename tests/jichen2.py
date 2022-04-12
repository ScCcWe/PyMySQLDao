# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: jichen2.py
# author: ScCcWe
# time: 2022/4/12 11:12 上午
class A:
    def __init__(self, aval, **kwargs):
        print("A: rcd value: ", aval)
        self.aval = aval
        super().__init__(**kwargs)


class B:
    def __init__(self, b1val, b2val, **kwargs):
        print("B: rcd 2 values: ", b2val)
        self.b1val = b1val
        self.b2val = b2val
        super().__init__(**kwargs)


class C(A, B):
    def __init__(self, a, b, c, **kwargs):
        super().__init__(aval=a, b1val=b, b2val=c, **kwargs)


c = C(1, 2, 3)
