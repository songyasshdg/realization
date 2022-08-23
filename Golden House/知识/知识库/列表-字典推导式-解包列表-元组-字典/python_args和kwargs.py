#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''
不能将**kwargs置于*args前，否则将产生错误；
“args kwargs ”是一个标准化规范 使用其他的名称也是可以的 *args 和 *没有区别 kwargs也是
最好使用标准规范
'''

'''传参查看参数'''

def a(b, *c):
    print(f'b={b}---c={c}')


a(1, (1, 2, 3, 4))  # b=1---c=((1, 2, 3, 4),)
a(1, 2, 3, 4, 5)  # b=1---c=(2, 3, 4, 5)
a({1:1}) #b={1: 1}---c=()


def b(b, **c):
    print(f'b={b}---c={c}')

b(1, d=1, c=1)  # b=1---c={'d': 1, 'c': 1}

'''使用'''

def lis(*args):
    print(f'args={args},类型为{type(args)}')


lis(1,2,3) #args=(1, 2, 3),类型为<class 'tuple'>
a=[1,3,'d']
b=(1,3,'d')
lis(a) #args=([1, 3, 'd'],),类型为<class 'tuple'>
lis(b) #args=((1, 3, 'd'),),类型为<class 'tuple'>

def dic(**kwargs):
    print(f'kwargs={kwargs},类型为{type(kwargs)}')
dic(d=1,c=2) #kwargs={'d': 1, 'c': 2},类型为<class 'dict'>
#这样写要报错的 dic({1:1,2:2})

