#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""几次常规用法"""
for i in range(1, 4):  # 从1开始  1 2 3
    print(i)

for i in range(4):  # 从0开始 0 1 2 3
    print(i)

a = [1, 2, 3, 'll', '24']
for i in a:  # 遍历每个列表元素
    print(i)

b = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
for i in b.keys():  # 遍历字典键
    print(i)

for i in b.values():  # 遍历字典值
    print(i)

for k, v in b.items():  # 键值对一起遍历
    print(k, v)
