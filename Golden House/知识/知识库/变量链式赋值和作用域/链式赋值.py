#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com


d = 1, 2, 3
print(d)  # 元组(1, 2, 3)
'''a,b=[1,2,2] 需要一一对应，不管是1,2,3，[1,2,3]，(1,2,3)都需要一一对应'''

a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3
print(type(a))  # <class 'int'>

a, b, c = (1, 2, 3)
print(a, b, c)  # 1 2 3
print(type(a))  # <class 'int'>

a = b = c = 1  # 1 1 1
print(a, b, c)

c = 2
print(a, b, c)  # 1 1 2
