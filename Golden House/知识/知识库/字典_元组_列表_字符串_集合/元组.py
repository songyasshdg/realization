#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
# 定义
tuple1 = (1, "2", "进阶")
print(tuple1)
# 嵌套
tuple2 = (1, "2", "进阶", (1, 2))
print(tuple2)

# 取值(细节)
tuple3 = ('c', 'a', 'd', 'g')
print(tuple3[1])  # 取索引为1的值，结果为字符串 'a'
print(tuple3[1:2])  # 取索引为1的值，结果为列表 ('a',)，会有个逗号
print(tuple3[1:3])  # 取索引为1和2的值，结果为列表 ('a', 'd')

# 定义只有一个元素的元组
print((1))  # 这是'1'
print((1,))  # 这是元组(1,)
'''神奇'''
a = {1: 1},
print(type(a))  # <class 'tuple'>  a也是元组

b = [1, 2],
print(type(b))  # <class 'tuple'>  b也是元组
