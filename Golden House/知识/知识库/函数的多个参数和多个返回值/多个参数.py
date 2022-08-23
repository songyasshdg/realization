#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''
默认参数:
它是如何工作的

名为 func 的函数有一个没有默认参数值的参数，后跟两个各自带有默认参数值的参数。

在第一次调用python函数时，func(3, 7)，参数 a 获得了值 3，参数 b 获得了值 7，而 c 获得了默认参数值 10。

在第二次调用函数时，func(25, c=24)，由于其所处的位置，变量 a 首先获得了值 25。然后，由于命名——即关键字参数——指定，变量 c 获得了值 24。变量 b 获得默认参数值 5。

在第三次调用函数时，func(c=50, a=100)，我们全部使用关键字参数来指定值。在这里要注意到，尽管 a 在 c 之前定义，但我们还是在变量 a 之前指定了变量 c。
'''


def sum(a, b=1):
    return a + b

print(sum(1))


def func(a, b=5, c=10):
    print(a, b, c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)

def t(a,*b,c=2):
    print(a)
    print(b)
    print(c)

t(1,2,1,c=5)
'''
结果
1
(2, 1)
5
'''
