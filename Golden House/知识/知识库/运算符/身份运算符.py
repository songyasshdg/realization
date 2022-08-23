#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''
总结：
    对象的三个特征 id value type
    只有三个特征都相等时 使用 is 的结果才为True
    而使用==时只需要value的结果就是True
'''

# 基本使用
print(1 is 1)  # True
print(1 is not 2)  # True
print('1' is 1)  # False
# ==和is区别
print(1 is 1.0)  # False
print(1 == 1.0)  # True
print(1 == True)  # True
print(1 is True)  # False
a = {1, 2, 3}
print(id(a))  # 2257202349000
b = {1, 3, 2}
print(id(b))  # 2257200217896
print(a == b)  # True
print(a is b)  # False

# 判断数据的类型
print(type(1) == int)  # True
print(isinstance(1, int))  # True
print(isinstance("2", str))  # True
print(isinstance(1, (int, str, float)))  # True
print(isinstance({1: 1}, (int, str, float)))  # False
