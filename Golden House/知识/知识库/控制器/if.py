#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''
非0和非空（null）值为true，0 或者 null为false。
'''
if 0:  # if false 不满足无法打印
    print('0为false')

if None:  # if false 不满足无法打印
    print('表达式为None')

if 1:  # if true 满足打印
    print('非0为true')

if '1':  # if true 满足打印
    print('表达式为非空')
a = 3

if a == 1:
    print('a=1')
elif a == 2:
    print('a=2')
else:
    print('a==0')
a = 2
print(a)
