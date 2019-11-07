#!/usr/bin/env python
# encoding: utf-8
"""
@author: lemenk
@Blog: blog.lemenk.top
@software: PyCharm
@file: firstfun.py
@time: 2019/11/7 13:43
"""

'''
# hello world!

def hello():
    print("Hello World!")


hello()
'''

'''
# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("python")
w = 4
h = 5
print("width =", w, "height =", h, "area =", area(w, h))
'''


def change(mylist):
    # 修改传入的列表
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用change函数
mylist = [10, 20, 30]
change(mylist)
print("函数外取值: ", mylist)
