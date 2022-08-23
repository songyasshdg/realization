#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''变量注解    更多详情参考https://www.dusaiphoto.com/article/164/  建议python3.9使用再去参考，现在先就用这些'''
age = 20
print(type(age))
#  <class 'int'>

age = '20'
print(type(age))
#  <class 'str'>


b:int =1
b='2'
#不运行这行代码时不会报错，但是会标记出来
print(b) # 结果是'2' 但是不会报错
# print(b+1) #但是这里就会报错了，在运行代码前看到直接的错误标记并修改可以提前发现问题

a: int = 3
b: float = 3.14
c: str = 'abc'
d: bool = False

'''函数注解 定义函数的返回类型'''
#1.普通参数
def st(s:str) -> str:
    return s+'字符串'
print(st('1'))

#2.对象参数
def hello(p: 'Person') -> str:
    return f'Hello, {p.name}' #f''和format()方法一样的写法
#为了避免类定义在方法定义之后，先用字符把类名包起来
class Person:
    def __init__(self, name: str):
        self.name = name
p=Person('kk')
print(hello(p))
