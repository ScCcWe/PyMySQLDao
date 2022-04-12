# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: duo_jicheng.py
# author: ScCcWe
# time: 2022/4/12 11:10 上午
class Animal:
    def __init__(self):
        print("in parent")


class Animal2:
    def __init__(self):
        print("in parent2")


class Dog(Animal2, Animal):
    def __init__(self):
        super().__init__()
        print("in dog")


if __name__ == '__main__':
    ins = Dog()
    print(ins)
