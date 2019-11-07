#!/usr/bin/env python
# encoding: utf-8
"""
@author: lemenk
@Blog: blog.lemenk.top
@software: PyCharm
@file: extends.py
@time: 2019/11/7 19:39
"""

'''
class Fruit:
    color = "绿色"

    def harves(self, color):
        print("水果是：" + color + "的")
        print("水果已经收获")
        print("水果原来是：" + Fruit.color + "的")


class Apple(Fruit):
    color = "红色"

    def __init__(self):
        print("我是苹果")


class Orange(Fruit):
    color = "橙色"

    def __init__(self):
        print("我是橘子")

    def harves(self, color):
        print("水果是：" + color + "的")
        print("橘子已经收获")
        print("水果原来是：" + Fruit.color + "的")


apple = Apple()
apple.harves(apple.color)
orange = Orange()
orange.harves(orange.color)
'''


class Fruit:

    def __init__(self, color="绿色"):
        Fruit.color = color

    def harvest(self):
        print("水果原来是：" + Fruit.color + "的")


class Apple(Fruit):
    def __init__(self):
        print("我是苹果")
        super().__init__()


apple = Apple()
apple.harvest()
