#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''要调用这个方法后才能使用这个函数里面的局部变量，感觉不好用'''
def text():
    global add
    add= "http://c.biancheng.net/java/"
    print("函数体内访问：",add)
text()
print('函数体外访问：',add)
