#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
class A:
    '''私有属性和方法只能在类内部使用'''
    __x = 1
    y = 2

    def __gai_y(self):
        self.y += 1

    def du_y(self):
        print('y的值为{}'.format(self.y))

    def test(self):
        self.__gai_y()
        print(self.__x)

# a=A()
# a.test()
# a.du_y()
# print(a.y)
##虽然是私有属性、方法，但是还是可以通过类名和方法(变量)名来访问的，不建议使用
# print(a._A__x)
#a._A__gai_y

class B(A):
    '''继承的类不能使用父类的私有属性和方法'''
    __b='b'
    bb='bb'
    def b1(self):
        print(self.__b)
        # print(A.__x) 会报错


b=B()
b.b1()
