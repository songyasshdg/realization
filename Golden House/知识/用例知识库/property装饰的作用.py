#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
class pr(object):  # 加了装饰器
    def __init__(self):
        pass

    @property  # 缺点不能加参数
    def yy(self):
        return 1

    @property
    def ys(self):
        return 10


ol = pr()
print(ol.yy)  # 使用了property装饰器, 这里可以不用加小括号
print(ol.ys)  # 使用了property装饰器, 这里可以不用加小括号


class pr(object):  # 不加装饰器
    def __init__(self):
        pass

    def yy(self):
        return 1

    def ys(self):
        return 10


ol = pr()
print(ol.yy())  # 不使用property装饰器, 这里需要加括号
print(ol.ys())  # 不使用property装饰器, 这里需要加括号
