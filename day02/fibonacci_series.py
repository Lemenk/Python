# Fibonacci series: 斐波那契数列
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b  # 计算方式为先计算等号右边表达式，然后同时赋值给左边
    '''等价于
    n=b
    m=a+b
    a=n
    b=m
    '''
# print函数的参数
'''
value：需要输出的值，可以是多个，用","分隔。 
sep：多个输出值之间的间隔，默认为一个空格。 
end：输出语句结束以后附加的字符串，默认是换行（'\n'）。 
file：输出的目标对象，可以是文件也可以是数据流，默认是“sys.stdout”。 
flush：flush值为True或者False，默认为False,表示是否立刻将输出语句输出到目标对象。
'''
# 示例：end参数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
