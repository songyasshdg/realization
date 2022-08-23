#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from math import pi


class G:
    '''@property 直接把方法的返回值当作一个属性值，存储在属性名为当前方法名的属性里面，可以通过对象.之间访问'''

    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return self.r ** 2 * pi


g = G(2)
print(g.area)


class Method:
    '''类方法可以之间类来调用，而实例方法需要用对象来调用'''
    a = 1

    @classmethod
    def test_cls(cls):
        print('类方法里使用变量a={}'.format(cls.a))

    def test_self(self):
        print('实例方法里面使用变量a={}'.format(self.a))

    @staticmethod
    def ha():
        '''静态方法里面无法使用self，也无法使用类里面的属性值和方法，只是一个普通的方法挂在这个类下面方便查找'''
        print('打印日志')


me = Method()
me.test_cls()
me.test_self()
Method.test_cls()
# Method.test_self() 会报错
Method.ha()
