#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''lambda 匿名函数用法 add和add1 实现的是一样的功能'''
def add(x, y):
    return x+ y
print(add(3,4))


add1 = lambda x,y:x+y
print(add1(3,4))

#输入一个int，返回一个列表
ge=lambda a : [int(a),str(a)]
l=ge(1)
print(l) #[1, '1']
