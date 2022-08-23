#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
# 定义
str1 = '1jaskj'

# 切片操作         结果
'''
字符串[开始索引：结束索引：步长]
切取字符串为开始索引到结束索引-1内的字符串(取头不取尾)
步长不指定时步长为1 字符串[开始索引:结束索引]
'''
print(str1[0])  # 1
print(str1[-1])  # j
print(str1[1:3])  # ja
# 翻转
print(str1[::-1])  # jksaj1

a='a\a\a\a'
#原生字符串，不会被里面的转义所影响
b=r'a\a\a\a'
