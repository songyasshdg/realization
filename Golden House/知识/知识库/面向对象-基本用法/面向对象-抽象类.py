#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
'''从实现角度来看，抽象类与普通类的不同之处在于：抽象类中有抽象方法，该类不能被实例化，只能被继承，且子类必须实现抽象方法'''
import abc  # 利用abc模块实现抽象类


class All_file(metaclass=abc.ABCMeta):
    all_type = 'file'

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass


class Txt(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('txt文本数据的读取方法')

    def write(self):
        print('txt文本数据的写入方法')


class Execl(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('execl文本数据的读取方法')

    def write(self):
        print('execl文本数据的写入方法')
