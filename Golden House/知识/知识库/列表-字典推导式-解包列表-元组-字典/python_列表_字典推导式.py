#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
import random
#基本推导
print([i for i in 'dadasd']) #['d', 'a', 'd', 'a', 's', 'd']
# 实现把a列表里面的int类型取出来组成一个新列表b
a = ['1', 2, 'kk', 4, 0]
b = [i for i in a if isinstance(i, int)]
print(b)  # [2, 4, 0]

d1 = {'one': 1, 'two': 2, 'three': 3, 1: 1}
d2 = {i for i in d1}
print(d2)  # {'one', 'three', 'two'}

# 实现把值大于1的键值对组成一个新的字典
d3 = {k: v for k, v in d1.items() if v > 1}
print(d3)  # {'two': 2, 'three': 3}

# 实现字典翻转
d4 = {v: k for k, v in d1.items()}
print(d4)  # {1: 1, 2: 'two', 3: 'three'} 重复的会被去重'one': 1 被 1:1 所取代

# 生成20个学生和学生成绩，找出大于92分的人
d5 = {'li{}'.format(i): random.randint(60, 100) for i in range(20)}
d6 = {k: v for k, v in d5.items() if v >= 90}
print(d6)

# 把学生的名字收集起来
d7 = [i for i in d6]
print(d7)

# 取1到100之间的大于60的偶数
d8 = [i for i in range(1, 101) if i % 2 == 0 and i>=60]
print(d8)
