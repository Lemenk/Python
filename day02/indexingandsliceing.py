#!/usr/bin/env python
# encoding: utf-8
"""
@author: lemenk
@Blog: blog.lemenk.top
@software: PyCharm
@file: indexingandsliceing.py
@time: 2019/11/3 16:42
"""

# 索引和切片

# 序列包括列表、元组、集合、字典、字符串


# 序列中每个元素都有编号，称之为索引
# 索引从0递增，也可以从-1递减

arr = ["西游记", "水浒传", "红楼梦", "三国演义", "西厢记", "寻秦记", "三字经"]
print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[-2])

# 切片：用于访问序列中元素
# 具体语法：arr[start:end:step]
'''
arr：序列名称
start：切片开始位置，默认为0
end：切片结束位置，且不包括该位置，默认为序列长度
step：切片步长，默认为1，可省略
'''
print(arr[1:3])
print(arr[1:6:2])

# 检查序列中是否包含某元素：使用in和not in语句，返回结果为bool类型
print("红楼梦" in arr)
print("兵书" not in arr)
print(type("红楼梦" in arr))
