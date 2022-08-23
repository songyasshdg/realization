#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
# 定义
'''
集合：
    无序，没有索引
    不支持数据重复
'''
set1 = {1, 2, 3, 4, 1, "5"}
print(set1)  # {1, 2, 3, 4, '5'} 重复之会出现一个

# 集合特殊操作
# 去除指定的元素
print({1, 2, 3, 4, 5} - {1, 2})
# 找到指定元素相同的元素
print({1, 2, 3, 4, 5} & {1, 2})

# 合并去重
print(({1, 2, 3, 4, 5} | {3, 5, 6, 7}))

# 定义一个空的集合
print(type(set()))  # <class 'set'>
print(type({}))  # <class 'dict'>
