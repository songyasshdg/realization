#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
"""
break是直接结束当前循环
continue是结束当前循环的剩余语句进行下一论的循环
continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分
"""

for i in 'py1thon':
    if i == '1':
        break
    print(i)

print('-------------------------------------')
for i in 'py1thon':
    if i == '1':
        continue
    print(i)

print('-------------------------------------')
# 冒泡排序 ：左右比较并互换位置
a = [2, 1, 4, 6, 2, 3, 5, 9, 7]
print(len(a))  # 9
for i in range(len(a) - 1):
    for j in range(len(a) - 1):
        print(j)
        # if a[j] >= a[j + 1]:
        #     # 互换之术
        #     a[j], a[j + 1] = a[j + 1], a[j]
        #     print(a)
        #     print(j)
