# 注释：
# 1.单行注释：
# 格式：# 说明文字
# 快捷键：ctrl+/
# 2.多行注释：
# 格式："""说明文字""" 或着 '''说明文字'''

# 输出语句
print('Hello Word!')

# 变量的定义
a = 10  # int类型
name = '小明'  # str类型
height = 1.80  # float类型
flag = True  # bool类型

# 查看变量类型
print(type(name))
print(type(a))
print(type(10.0))
'''运行结果
<class 'str'>
<class 'int'>
<class 'float'>
'''

# 命名规范
# 类名使用大驼峰
# 模块等使用小驼峰或者下划线连接

# 导入模块 
# import keyword

# 利用keyword模块查看关键字
# print(keyword.kwlist)

# 格式化输出
age = 10
print('今年我%d岁了' % age)

# 常用格式符号
'''
% s : 字符串(采用str()的显示)
% r : 字符串(采用repr()的显示)
% c : 单个字符
% b : 二进制整数
% d : 十进制整数
% i : 十进制整数
% o : 八进制整数
% x : 十六进制整数
% e : 指数(基底写为e)
% E : 指数(基底写为E)
% f : 浮点数
% F : 浮点数，与上相同
% g : 指数(e)或浮点数(根据显示长度)
% G : 指数(E)或浮点数(根据显示长度)
% % : 字符"%"
'''
# 例：
num = 98
print('我们班数据结构与算法课程的及格率为%d%%' % num)

# 多个变量输出
name = '小明'
age = 18
print('姓名：%s，年龄：%d' % (name, age))

# 换行输出
print('您好\n世界')

# 输入 input()函数
tel = input('请输入手机号：')
print(tel)

