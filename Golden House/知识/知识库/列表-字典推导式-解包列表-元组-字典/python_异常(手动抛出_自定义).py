#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
a=[1,2,3]
#异常捕获处理
try:
    # print(1)
    print(a[4]) #索引异常
    # print(1 / 0) #被除数为0异常
except ZeroDivisionError:
    print('被除数为0异常')
    #可以打印出具体异常信息
except IndexError as e:
    print(f'索引异常。异常信息：{e}')
    #父类异常，可以接受所有异常，父类异常写在最后
except Exception:
    print('没有发现上述异常，未知异常')
else:
    print('没有异常')
finally:
    print('有无异常我都执行')

#手动抛出异常
x=2
if x>2:
    #这里可是使用所有的异常类型
    raise Exception('x不能大于2')

#自定义异常

class NameLengthError(Exception):
    '''当名字长度大于5位时抛出该异常'''
    # 自定义异常类型的初始化
    def __init__(self,length :int):
        self.length=length
    # 返回异常类对象的说明信息
    def __str__(self):
        if self.length>5:
            return f'姓名的长度最大为5位,您输入的位数为{self.length}位'
        return ''

length=3
try:
    raise NameLengthError(length)
except NameLengthError as e:
    print(e)
