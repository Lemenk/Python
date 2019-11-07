#!/usr/bin/env python
# encoding: utf-8
"""
@author: lemenk
@Blog: blog.lemenk.top
@software: PyCharm
@file: object_oriented.py
@time: 2019/11/7 14:20
"""

'''
class Geese:
    """大雁类"""
    print("我是大雁")


wildGoose = Geese()
print(wildGoose)
'''

'''
class Geese:
    """大雁类"""

    def __init__(self, beak, wing, claw):
        print("我是大雁类，包含以下特征：")
        print(beak)
        print(wing)
        print(claw)


beak_1 = "喙的基部比较高，长度和头部的长度几乎相同"
wing_1 = "翅膀长而尖"
claw_1 = "爪子是蹼状的"
wildGoose = Geese(beak_1, wing_1, claw_1)
'''

'''
class Geese:
    """大雁类"""

    def __init__(self, beak, wing, claw):
        print("我是大雁类，包含以下特征：")
        print(beak)
        print(wing)
        print(claw)

    def fly(self, state):     # 定义实例方法
        print(state)


beak_1 = "喙的基部比较高，长度和头部的长度几乎相同"
wing_1 = "翅膀长而尖"
claw_1 = "爪子是蹼状的"
wildGoose = Geese(beak_1, wing_1, claw_1)
wildGoose.fly("我飞行的时候，一会儿排成人字，一会儿排成一个一字")

'''

'''
# protected
class Swan:
    """天鹅类"""
    _neck_swan = '天鹅的脖子很长'

    def __init__(self):
        print("__init__()", Swan._neck_swan)


swan = Swan()
print("直接访问：", swan._neck_swan)
'''

'''
# private
class Swan:
    """天鹅类"""
    __neck_swan = '天鹅的脖子很长'

    def __init__(self):
        print("__init__()", Swan.__neck_swan)


swan = Swan()
print("加入类名访问：", swan._Swan__neck_swan)
# print("直接访问：", swan.__neck_swan)
'''


class Rect:
    def __init__(self, width, height):
        self.width = width  # 实例属性
        self.height = height  # 实例属性

    @property
    def area(self):
        return self.width * self.height


rect = Rect(800, 600)
print("面积为：", rect.area)
