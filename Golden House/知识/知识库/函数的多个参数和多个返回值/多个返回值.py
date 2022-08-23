#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
def aa():
    a=1
    b=2
    #这种返回是返回一个元组 (1, 2)
    # return a,b
    #也可以用字典访问
    return {'a':a,'b':b}
a=aa()
print(type(a))

def bb():
    c=2
    d=4
    return c,d
'''还可以这样访问使用函数返回的2个参数'''
c,d=bb()
print(c,d)

