#!/usr/bin/env python
# encoding: utf-8
"""
@author: lemenk
@Blog: blog.lemenk.top
@software: PyCharm
@file: regex.py
@time: 2019/11/3 18:00
"""

import re

'''
# match()方法：re.match(pattern, string, [flags])
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match1 = re.match(pattern, string, re.I)
print(match1)
string = 'new MR_SHOP mr_shop'
match2 = re.match(pattern, string, re.I)
print(match2)
print('匹配值的起始位置：', match1.start())
print('匹配值的结束位置：', match1.end())
print('匹配位置的元组：', match1.span())
print('被匹配的字符串：', match1.string)
print('匹配数据：', match1.group())

'''
'''
# 验证输入的手机号码
pattern = r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
print('请输入11位电话号码：')
mobile = input()
# mobile = '13634555555'
match3 = re.match(pattern, mobile)
if match3 is None:
    print(mobile, '可能不是有效的中国移动手机号码')
else:
    print(mobile, '是有效的中国移动手机号码')
'''

'''
# search()方法：re.search(pattern, string, [flags])
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
search = re.search(pattern, string, re.I)
print(search)
'''
'''
# findall()方法：re.findall(pattern, string, [flags])，返回值为列表
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
find = re.findall(pattern, string, re.I)
print(find)
print(type(find))

# 分割IP地址
pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str = '127.0.0.1 192.168.1.66 187.0.1.9'
match = re.findall(pattern, str)
for item in match:
    print(item[0])
'''
# 替换字符串：re.sub(pattern, repl, string, [count], [flags])，返回值为字符串
# pattern：表示模式字符串，正则表达式
# repl：表示要替换的字符串
# string：表示要被查找替换的原始字符串
# count：可选，表示模式匹配后替换的最大次数，默认值为0，表示替换所有
# flags：可选，标志位，用于控制匹配方式
'''
# 替换违禁字符
pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
about1 = '我是一名黑客，喜欢抓包，监听网络，想研究Trojan。'
about = '我爱你'
sub = re.sub(pattern, '**', about)
print(sub)
'''
# 分割字符串：re.split(pattern, string, [maxsplit], [flags])，其返回结果为列表
pattern = r'[?|&]'
url = 'http://www.baidu.com/login.jsp?username="liming"&pwd="123"'
result = re.split(pattern, url)
print(result)
