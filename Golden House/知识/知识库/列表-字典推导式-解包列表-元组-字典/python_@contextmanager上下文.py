#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
from contextlib import contextmanager


# 一个应用场景，给一个书名前后加上书名号

@contextmanager
def book_mark():
    print('《', end='')
    yield  # yield 后面不一定要返回结果，纯粹起一个中断作用
    print('》', end='')


with book_mark():
    print("年少不努力", end='')


# 打开文件，文件不存在打印出不存在的文件名
@contextmanager
def file_open(file_name):
    try:
        yield
    except FileNotFoundError as e:
        print(file_name)


file_name = 'data1.txt'
with file_open(file_name):
    open(file_name, mode='r')
