#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
# # 定义
dict1 = {'key': 'value'}
d = dict(name='Bob', age=20, score=88)
print(dict1)

# 取值
print(dict1['key'])

# 增加
dict1['cc'] = 22
# 修改
dict1['cc'] = 33
# 删除
del dict1['cc']
# 清空字典的值
dict1.clear()
print(dict1)
# update方法  存在就修改，不存在则删除
dict1.update({1: 1, 2: 2})
dict1.update({1: 1.0, 3: 3})
print(dict1)
# pop方法：删除指定的键值对并返回值
print(dict1.pop(2))
print(dict1)
# 遍历键值对
dict2 = {1: 1, 2: 2}
for k, v in dict2.items():
    print(k, v)

if 'kk' not in d:
    print('kk不在字典d中')
    d.update({'kk': 99})
    if d.pop('kk') == 99:
        print('kk被新增了，但是又被我干掉了')
