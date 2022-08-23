#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
print(1 in [1, '2m'])  # True
print(1 not in [1, '2m'])  # False
# 这样只能判断字典的key 是不是存在
print('c' in {'c': 1})  # True
print(1 in {'c': 1})  # False
